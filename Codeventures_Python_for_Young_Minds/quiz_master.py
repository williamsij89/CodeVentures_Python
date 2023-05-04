quiz_data = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Which planet is closest to the sun?", "answer": "Mercury"},
    {"question": "What is the largest mammal?", "answer": "Blue whale"},
    {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"}
]
def quiz():
    score = 0

    for question_data in quiz_data:
        print(question_data["question"])
        user_answer = input("> ").lower()

        if user_answer == question_data["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question_data["answer"])

    print("Your final score is:", score)
