#Performance Analysis
#Aleli
#Diane Zevedy
#Maria Lourdes

class PerformanceAnalysis:
    def __init__(self):
        self.correct_count = 0 
        self.wrong_count = 0
        self.results = [] 


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
        
# Create an instance of the PerformanceAnalysis class
performance_analyzer = PerformanceAnalysis() 

