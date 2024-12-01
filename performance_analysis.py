#Performance Analysis
#Aleli
#Diane Zevedy
#Maria Lourdes


correct_count = 0 #Tracks how many questions the user answered correctly
wrong_count = 0 #Tracks how many questions the user answered wrong
results = [] #Stores a list of dictionaries (question details, user's answer, if the answer is correct)

def ask_question(question_data):
    #Displays a question, gets the user's answer and check if it's correct
    global correct_count, wrong_count, results

    question = question_data['question']
    correct_answer = question_data['answer']

    #Display the question
    print(f"\nQuestion: {question}") 

    #Ask the user for their answer
    user_answer = input("Your answer: ").strip()  #Strip removes the extra spaces

    #Check if the answer provided is correct
    if user_answer.lower() == correct_answer.lower(): #lower is used so the answers will be in the same lettercase
        print("Correct!")
        correct_count += 1
        result = "Correct"
    else:
        print(f"Incorrect! The correct answer is: {correct_answer}")
        wrong_count += 1
        result = "Incorrect"

    #Save the results for the summary
    results.append({
        "question": question,
        "user_answer": user_answer,
        "correct_answer": correct_answer,
        "result": result 
    })

def performance_summary():
    #Shows a summary of the user's overall performance
    total_questions = len(results) # Total nyumber of questions
    
    #Calculate the percentage of correct answers
    if total_questions > 0:
        percentage = (correct_count/total_questions) * 100
    else:
        percentage = 0 #This is to prevent math error

    #Print the summary
    print("\n==== Performance Summary ====")
    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {correct_count}")
    print(f"Wrong Answers: {wrong_count}")
    print(f"Score Percentage: {percentage:.2f}%")

    # Show detailed results for each question answered
    print("\nDetailed Results:")
    for i, res in enumerate(results, 1):
        print(f"{i}.{res['question']}")
        print(f"    Your Answer: {res['user_answer']} | Correct Answer: {res['correct_answer']} |Result: {res['result']}")
    

#Sample run
questions = [
    {"question": "What is the powerhouse of the cell?", "answer": "Mitochondria"},
    {"question": "What is 1 + 1?", "answer": "4"},
    {"question": "Who is our national hero?", "answer": "Jose Rizal"}
]

for q in questions:
    ask_question(q)

performance_summary()
