import json
import os
from datetime import datetime
import google.generativeai as genai
import random

class APIKeyManager:
    def __init__(self, keys_file='api_keys.json'):
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Make the path relative to the script directory
        self.keys_file = os.path.join(script_dir, keys_file)
        self.load_keys()
    
    def load_keys(self):
        """Load API keys from the JSON file or environment variables"""
        # Try to load from environment variable first (for production)
        env_api_key = os.environ.get('GEMINI_API_KEY')
        
        if env_api_key and env_api_key.strip():
            # If environment variable is set, use it
            self.data = {
                "keys": [env_api_key.strip()],
                "key_status": {
                    env_api_key.strip(): {
                        "is_active": True,
                        "usage_count": 0,
                        "last_used": None
                    }
                }
            }
            return
        
        # Fallback to JSON file (for development)
        if os.path.exists(self.keys_file):
            with open(self.keys_file, 'r') as f:
                self.data = json.load(f)
        else:
            # Create default structure if file doesn't exist
            self.data = {"keys": [], "key_status": {}}
    
    def save_keys(self):
        """Save API keys to the JSON file (only in development mode)"""
        # Don't save if using environment variable (production mode)
        if os.environ.get('GEMINI_API_KEY'):
            return
        
        # Only save if we have the JSON file available (development mode)
        try:
            with open(self.keys_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except (IOError, OSError):
            # If we can't write to file (e.g., in production), just skip
            pass
    
    def get_active_key(self):
        """Get an active API key with lowest usage count"""
        keys = self.data.get('keys', [])
        key_status = self.data.get('key_status', {})
        
        # Find active keys or activate all if none are active
        active_keys = []
        for key in keys:
            status = key_status.get(key, {})
            if status.get('is_active', True):  # Default to True if not specified
                active_keys.append(key)
        
        if not active_keys:
            # If no active keys, activate all keys
            for key in keys:
                if key not in key_status:
                    key_status[key] = {}
                key_status[key]['is_active'] = True
            active_keys = keys.copy()
            self.save_keys()
        
        if not active_keys:
            return None
        
        # Sort by usage count (ascending) and return the least used key
        active_keys.sort(key=lambda k: key_status.get(k, {}).get('usage_count', 0))
        return active_keys[0]
    
    def mark_key_used(self, api_key):
        """Mark an API key as used and update usage statistics"""
        if api_key not in self.data.get('key_status', {}):
            self.data['key_status'][api_key] = {}
        
        self.data['key_status'][api_key]['last_used'] = datetime.now().isoformat()
        self.data['key_status'][api_key]['usage_count'] = self.data['key_status'][api_key].get('usage_count', 0) + 1
        self.save_keys()
    
    def mark_key_inactive(self, api_key, reason="quota_exceeded"):
        """Mark an API key as inactive due to quota issues"""
        if api_key not in self.data.get('key_status', {}):
            self.data['key_status'][api_key] = {}
        
        self.data['key_status'][api_key]['is_active'] = False
        self.data['key_status'][api_key]['deactivated_at'] = datetime.now().isoformat()
        self.data['key_status'][api_key]['deactivation_reason'] = reason
        self.save_keys()
    
    def reactivate_all_keys(self):
        """Reactivate all keys (useful for daily quota reset)"""
        for key in self.data.get('keys', []):
            if key not in self.data.get('key_status', {}):
                self.data['key_status'][key] = {}
            self.data['key_status'][key]['is_active'] = True
        self.save_keys()

def generate_quiz_questions(topic, num_questions=5, max_retries=3):
    """Generate quiz questions using AI with API key rotation"""
    key_manager = APIKeyManager()
    
    prompt = f"""Create a JSON array of {num_questions} multiple-choice quiz questions on the topic of '{topic}'.
    Each question object must have this exact format:
    {{
        "question_text": "The question text here",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "correct_answer": "The correct option text from above"
    }}
    
    IMPORTANT RULES:
    - Return ONLY a JSON array, no additional text or code blocks
    - Each question must have exactly 4 options
    - The correct_answer must exactly match one of the options
    - Avoid using code snippets with backticks in question text
    - Use simple, clear language
    - Make questions educational and challenging
    """
    
    for attempt in range(max_retries):
        try:
            api_key = key_manager.get_active_key()
            if not api_key:
                raise Exception("No active API keys available")
            
            # Configure the API with the current key
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            response = model.generate_content(prompt)
            key_manager.mark_key_used(api_key)
            
            # Clean the response to extract JSON
            response_text = response.text.strip()
            
            # Remove any markdown code blocks
            import re
            
            # First, try to extract from code blocks
            json_match = re.search(r'```(?:json)?\s*(.*?)\s*```', response_text, re.DOTALL)
            if json_match:
                json_text = json_match.group(1).strip()
            else:
                json_text = response_text
            
            # Remove any remaining markdown formatting
            json_text = re.sub(r'^```.*?$', '', json_text, flags=re.MULTILINE)
            json_text = json_text.strip()
            
            # If it starts and ends with array brackets, it's likely the JSON we want
            if json_text.startswith('[') and json_text.endswith(']'):
                pass  # Good format
            elif json_text.startswith('{') and json_text.endswith('}'):
                # Might be wrapped in an object
                pass
            else:
                # Try to find JSON array in the text
                array_match = re.search(r'\[.*\]', json_text, re.DOTALL)
                if array_match:
                    json_text = array_match.group(0)
            
            print(f"Attempt {attempt + 1} - Cleaned JSON text (first 200 chars):")
            print(json_text[:200] + "..." if len(json_text) > 200 else json_text)
            
            # Parse the JSON
            questions_list = json.loads(json_text)
            
            # Validate the structure
            if isinstance(questions_list, dict) and 'questions' in questions_list:
                questions_list = questions_list['questions']
            
            if not isinstance(questions_list, list):
                raise ValueError("Expected a list of questions")
            
            # Validate each question
            validated_questions = []
            for i, question in enumerate(questions_list):
                if not isinstance(question, dict):
                    continue
                
                if 'question_text' not in question or 'options' not in question or 'correct_answer' not in question:
                    continue
                
                options = question['options']
                if isinstance(options, dict):
                    options = list(options.values())
                
                if len(options) != 4:
                    continue
                
                # Clean up question text (remove problematic characters)
                question_text = question['question_text'].replace('```', '').replace('\n```', '').strip()
                
                # Ensure correct_answer matches one of the options
                correct_answer = question['correct_answer']
                if correct_answer not in options:
                    # Try to find the closest match
                    for option in options:
                        if option.lower().strip() == correct_answer.lower().strip():
                            correct_answer = option
                            break
                    else:
                        # If no match found, skip this question
                        continue
                
                validated_questions.append({
                    'question_text': question_text,
                    'options': options,
                    'correct_answer': correct_answer
                })
            
            if len(validated_questions) >= min(3, int(num_questions) // 2):  # At least half or 3 questions
                return validated_questions
            else:
                raise ValueError(f"Only {len(validated_questions)} valid questions generated, expected {num_questions}")
                
        except json.JSONDecodeError as e:
            print(f"JSON parsing error on attempt {attempt + 1}: {e}")
            print(f"Response text: {response_text[:500]}...")
            
        except Exception as e:
            error_msg = str(e).lower()
            print(f"Error on attempt {attempt + 1}: {e}")
            
            # Check for quota-related errors
            if any(keyword in error_msg for keyword in ['quota', 'limit', '429', 'rate limit']):
                if api_key:
                    key_manager.mark_key_inactive(api_key, "quota_exceeded")
                    print(f"Marked API key as inactive due to quota: {api_key[:10]}...")
                
            if attempt == max_retries - 1:
                raise e
    
    raise Exception(f"Failed to generate questions after {max_retries} attempts")
