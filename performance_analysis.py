#Performance Analysis
#Aleli
#Diane Zevedy
#Maria Lourdes

'''
This module is responsible for displaying the results of the exam 

Functions in this module:
1. PerformanceAnalysis: this computes the results and displays in tabular format the answer per question

'''
import textwrap
import datetime

class PerformanceAnalysis:
    def __init__(self):
        self.correct_count = 0 
        self.wrong_count = 0
        
    def performance_summary(self,answers):
        self.results = [] 
         
        # count the number of correct and incorrect answers
        self.correct_count = len([answer for answer in answers if int(answer['is_answer_correct']) == 1])
        self.wrong_count = len([answer for answer in answers if int(answer['is_answer_correct']) == 0])
        review_date = datetime.datetime.fromtimestamp(int(answers[0]['session_id'])).strftime("%Y-%m-%d %I:%M %p")
        subject = ",".join(list(set([answer['subject'] for answer in answers])))
        
        # generate the list needed from the answer list to display data
        for answer in answers:
            self.results.append({
                'id': answer['id'],
                'question': answer['question'],  # Include the question text
                'user_answer': answer['user_answer'],  # Include the user's answer
                'correct_answer': answer['correct_answer'],  # Include the correct answer
                'result': 'Correct' if int(answer['is_answer_correct']) == 1 else 'Incorrect'                
            })
        
        #Shows a summary of the user's overall performance
        total_questions = len(answers) # Total number of questions
        
        #Calculate the percentage of correct answers
        if total_questions > 0:
            percentage = (self.correct_count/total_questions) * 100
        else:
            percentage = 0 #This is to prevent math error

        #Determine if pass or fail
        if percentage >= 60:
            status = "Pass"
        else:
            status = "Fail"

        
        print("\n==== Performance Summary ====")
        print(f'Review Date: {review_date}')
        print(f'Subject: {subject}')
        print(f"Total Questions: {total_questions}")
        print(f"Correct Answers: {self.correct_count}")
        print(f"Wrong Answers: {self.wrong_count}")
        print(f"Score Percentage: {percentage:.2f}% ({status})")

        #Detailed exam results in tabular format
        header = f"{'Question':<70} {'Your Answer':<18} {'Correct Answer':<18} {'Result':<15}"
        print("\nDetailed Exam Results:")
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        for i, res in enumerate(self.results, 1):
            # Wrap question text to fit within 60 characters per line
            wrapped_question = textwrap.wrap(res['question'], width=60)
            print(f"\n{i}. {wrapped_question[0]:<70}{res['user_answer']:<18}{res['correct_answer']:<18}{res['result']:<15}")
            # Print additional lines of the question, if wrapped
            for line in wrapped_question[1:]:
                print(f"   {line:<60}")
        
        # Wait for user input before returning to the main menu

# Create an instance of the PerformanceAnalysis class
performance_analyzer = PerformanceAnalysis() 


def main():
    performance_analysis = PerformanceAnalysis()


if __name__ == "__main__":
    main()