# Temporary debug routes for Railway deployment troubleshooting
# Add these routes to your app1.py file temporarily to diagnose the API key issue

@app.route('/debug/env')
def debug_env():
    """Debug route to check environment variables in production"""
    import os
    
    # Check if we're in production
    is_production = os.environ.get('FLASK_ENV') == 'production'
    
    # Check API key availability (don't expose the actual key)
    gemini_key_set = bool(os.environ.get('GEMINI_API_KEY'))
    gemini_key_length = len(os.environ.get('GEMINI_API_KEY', ''))
    
    # Check other environment variables
    debug_info = {
        "environment": os.environ.get('FLASK_ENV', 'development'),
        "is_production": is_production,
        "gemini_api_key_set": gemini_key_set,
        "gemini_api_key_length": gemini_key_length,
        "database_url_set": bool(os.environ.get('DATABASE_URL')),
        "secret_key_set": bool(os.environ.get('SECRET_KEY')),
        "port": os.environ.get('PORT', 'not set'),
        "python_path": os.environ.get('PYTHONPATH', 'not set'),
    }
    
    return jsonify(debug_info)

@app.route('/debug/ai-test')
def debug_ai_test():
    """Debug route to test AI generation in production"""
    try:
        import os
        from api_utils import APIKeyManager, generate_quiz_questions
        
        # Initialize API key manager
        key_manager = APIKeyManager()
        
        # Check if keys are loaded
        keys_count = len(key_manager.data.get('keys', []))
        active_keys = sum(1 for key_id, status in key_manager.data.get('key_status', {}).items() 
                         if status.get('is_active', False))
        
        # Try to get an active key
        try:
            active_key = key_manager.get_active_key()
            key_available = True
            key_preview = active_key[:10] + "..." if active_key else "None"
        except Exception as e:
            active_key = None
            key_available = False
            key_preview = f"Error: {str(e)}"
        
        # Try to generate a simple question
        try:
            questions = generate_quiz_questions("Python", 1)
            generation_success = True
            question_count = len(questions)
            sample_question = questions[0] if questions else None
        except Exception as e:
            generation_success = False
            question_count = 0
            sample_question = f"Error: {str(e)}"
        
        debug_result = {
            "total_keys": keys_count,
            "active_keys": active_keys,
            "key_available": key_available,
            "key_preview": key_preview,
            "generation_success": generation_success,
            "question_count": question_count,
            "sample_question": sample_question,
            "environment_key_set": bool(os.environ.get('GEMINI_API_KEY')),
            "environment_key_length": len(os.environ.get('GEMINI_API_KEY', ''))
        }
        
        return jsonify(debug_result)
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "traceback": str(e.__traceback__) if hasattr(e, '__traceback__') else "No traceback"
        })
