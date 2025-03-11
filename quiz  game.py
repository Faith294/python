# Simple Quiz Game
# Quiz questions as a dictionary
quiz_questions = {
    "1.Coding is performed at?": {
        "options": ["A) Back end", "B) Front end", "C) Both A and B", "D) None of the above"],
        "answer": "C"
        },
    "2.There are how many coding languages?": {
        "options": ["A) 1", "B) 2", "C) 3", "D)More than 3"],
        "answer": "D"
        },
    "3._______ is the process of finding errors and fixing them within a program.": {
        "options": ["A) Debugging", "B) Compiling", "C) Scanning", "D) None of above"],
        "answer": "A"
        },
    "4.In python can you make your own library?": {
        "options": ["A) yes", "B) no", "C)You can but with some restrictions", "D) Not sure"],
        "answer": "A"
        },
    "5.Which of the following is not a programming language?": {
         "options": ["A) C", "B) Python", "C) Unix", "D) Java"],
        "answer": "C"
    }
        
    }
# Initialize score
score = 0

# Loop through questions
for question, data in quiz_questions.items():
    print("\n" + question)
    for option in data["options"]:
        print(option)

    # Get user answer
    user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

    # Check answer
    if user_answer == data["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {data['answer']}.")

# Display final score
print(f"\n🎉 Quiz Over! You scored {score} out of {len(quiz_questions)}.")
