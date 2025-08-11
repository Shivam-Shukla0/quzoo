#!/usr/bin/env python3
"""
Test script for AI Quiz Generator
Run this to test if the AI functionality is working properly
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from api_utils import generate_quiz_questions

def test_ai_generation():
    print("Testing AI Quiz Generation...")
    print("=" * 50)
    
    try:
        # Test with a simple topic
        topic = "Python Programming Basics"
        num_questions = 3
        
        print(f"Generating {num_questions} questions on topic: {topic}")
        questions = generate_quiz_questions(topic, num_questions)
        
        if questions:
            print(f"✅ Successfully generated {len(questions)} questions!")
            print("\nGenerated Questions:")
            print("-" * 30)
            
            for i, q in enumerate(questions, 1):
                print(f"\nQ{i}: {q['question_text']}")
                print("Options:")
                for j, option in enumerate(q['options'], 1):
                    marker = "✓" if option == q['correct_answer'] else " "
                    print(f"  {marker} {j}. {option}")
                print(f"Correct Answer: {q['correct_answer']}")
                
        else:
            print("❌ No questions were generated")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_ai_generation()
