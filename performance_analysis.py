#Performance Analysis
#Aleli
#Diane Zevedy
#Maria Lourdes

class PerformanceAnalysis:
    def __init__(self):
        self.correct_count = 0 
        self.wrong_count = 0
        self.results = [] 

    def ask_question(self, question_data):
        #Displays a question, gets the user's answer and check if it's correct
        question = question_data['question']
        correct_answer = question_data['answer']

        #Display the question
        print(f"\nQuestion: {question}") 

        #Ask the user for their answer
        user_answer = input("Your answer: ").strip()  # Strip removes the extra spaces

        #Check if the answer provided is correct
        if user_answer.lower() == correct_answer.lower(): #lower is used so the answers will be in the same lettercase
            print("Correct!")
            self.correct_count += 1
            result = "Correct"
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")
            self.wrong_count += 1
            result = "Incorrect"

        #Save the results for the summary
        self.results.append({
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "result": result 
        })

    def performance_summary(self):
        #Shows a summary of the user's overall performance
        total_questions = len(self.results) # Total nyumber of questions
        
        #Calculate the percentage of correct answers
        if total_questions > 0:
            percentage = (self.correct_count/total_questions) * 100
        else:
            percentage = 0 #This is to prevent math error

        #Determine if pass or fail
        if percentage >= 70:
            status = "Pass"
        else:
            status = "Fail"

        
        print("\n==== Performance Summary ====")
        print(f"Total Questions: {total_questions}")
        print(f"Correct Answers: {self.correct_count}")
        print(f"Wrong Answers: {self.wrong_count}")
        print(f"Score Percentage: {percentage:.2f}% ({status})")

        #Detailed exam results in tabular format
        print("\nDetailed Exam Results:")
        print("-" * 110)
        print(f"{'Question':<60} {'Your Answer':<18} {'Correct Answer':<18} {'Result':<15}")
        print("-" * 110)
        for i, res in enumerate(self.results, 1):
            print(f"{i}.{res['question']:<60}{res['user_answer']:<18}{res['correct_answer']:<18}{res['result']:<15}")
        
        # Show detailed results for each question answered
        print("\nDetailed Results:")
        for i, res in enumerate(self.results, 1):
            print(f"{i}.{res['question']}")
            print(f"    Your Answer: {res['user_answer']} | Correct Answer: {res['correct_answer']} |Result: {res['result']}")

#Sample run
questions = [
    {"question": "What is the powerhouse of the cell?", "answer": "Mitochondria"},
    {"question": "What is 1 + 1?", "answer": "4"},
    {"question": "Who is our national hero?", "answer": "Jose Rizal"}
]

# Create an instance of the PerformanceAnalysis class
performance_analyzer = PerformanceAnalysis() 

for q in questions:
    performance_analyzer.ask_question(q)

performance_analyzer.performance_summary()
