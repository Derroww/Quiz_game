import json
import random
import time

def load_quiz_data(filename="questions.json"):       # Loads quiz questions from an external JSON file with error handling.
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please ensure 'questions.json' is in the same directory.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON formatting.")
        exit(1)

def get_feedback(score, total):                    # Generates feedback based on the user's score percentage.
    percentage = (score / total) * 100
    if percentage >= 80:
        return "Excellent! You nailed it!"
    elif percentage >= 50:
        return "Good job! Solid effort."
    else:
        return "Try Again! Keep practicing to improve your score."

def run_quiz():                                  # Load data dynamically from JSON file
    quiz_data = load_quiz_data("questions.json")
    
    print("=" * 45)
    print("        WELCOME TO THE CLI QUIZ GAME!        ")
    print("=" * 45)
    
    
    print("\nPlease choose a quiz category:")   # Allow user to choose a category
    for key, cat in quiz_data.items():
        print(f"[{key}] {cat['name']}")
    
    choice = input("\nEnter category number: ").strip()
    if choice not in quiz_data:
        print("Invalid choice. Defaulting to category 1.")
        choice = "1"
    
    selected_category = quiz_data[choice]
    questions = selected_category["questions"]
    
    
    random.shuffle(questions)             # Shuffle question order
    
    score = 0
    total_questions = len(questions)
    
    print(f"\nStarting '{selected_category['name']}' Quiz! ({total_questions} Questions)\n")
    print("-" * 45)
    
    
    for i, q in enumerate(questions, 1):                # Loop through questions
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['choices']:
            print(f"  {option}")
            
        start_time = time.time()
        
        
        while True:                                     # Input validation with try/except
            try:
                user_answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
                if not user_answer:
                    raise ValueError("Input cannot be empty.")
                if user_answer not in ['A', 'B', 'C', 'D']:
                    raise ValueError("Invalid choice. Please enter A, B, C, or D.")
                break
            except ValueError as e:
                print(f"error {e}")
        
        end_time = time.time()
        print(f"Answered in {end_time - start_time:.1f} seconds.")
        
        
        if user_answer == q['correct']:                 # Compare answer
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['correct']}.")
            
        print("-" * 45)
        
    
    print("\n" + "=" * 45)                             # Results & Feedback
    print("                 QUIZ RESULTS                ")
    print("=" * 45)
    print(f"Category : {selected_category['name']}")
    print(f"Score    : {score} out of {total_questions} ({(score/total_questions)*100:.1f}%)")
    print(f"Feedback : {get_feedback(score, total_questions)}")
    print("=" * 45)

if __name__ == "__main__":
    run_quiz()