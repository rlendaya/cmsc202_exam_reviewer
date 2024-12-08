#Question Bank
#Reynald
#Mark Lester
#Jade Carl

#Question bank Pseudocode (lets align with flowchart)
#1. Review Questions
#2. Display Questions and answers
#3. 

#1. Take Exam
#2. Output Questions ID, Subject, Type, Question
#3. select answers 1-4 (multiple choice)
#4. select 1 or 2 (T or F)
#5. calculate score
#6. End

'''
This question bank module will handle the following:

1. Manage questions
    - view question
    - edit question
    - delete question
    - add question
    
2. Conduct review
    - get review specifications from user
        - user select topic
        - user select question type
        - user input number of desired questions
    - display the questions
    - gather answer from user
    - check answer for correctness
    - 

'''

#Comment: Team please check our question_bank feature. I need help in aligning this with our current flowchart. Feel free to adjust.

import csv

# os module for interoperability of file path with different OS
import os

class QuestionBank:
    # function to handle file path and initialize variable for question list
    def __init__(self, file_path):
        self.file_path = file_path
        self.questions = []

    # function to handle loading of questions from file and filtering based on the chosen topics and question type
    
    def load_questions(self): #load question from csv file
        try:
            with open(self.file_path, 'r', encoding='ISO-8859-1') as file:
                reader = csv.DictReader(file)
                self.questions = [row for row in reader]
            # print(f"Loaded {len(self.questions)} questions successfully.")
        except Exception as e:
            print(f"An error occurred while loading questions: {e}")

    # function to handle viewing of all questions
    def view_question(self):
        number_of_questions = len(self.questions)
        print(f'There are {number_of_questions} questions in total!\n') 
        # below will print header
        print(f'{'Question Id':^15}{'Question Type':^20}{'Question':165}{'Answer':^10}\n')
        for questions in self.questions:
            print(f'{questions['id']:^15}{questions['type']:^20}{questions['question']:165}{questions['correct_answer']:^10}')


    
    def review_questions(self):
        
        if not self.questions:
            print("No questions available to review.")
            return
        
        print("\nReviewing Questions:\n")
        for question in self.questions:
            print(f"ID: {question['id']}, Subject: {question['subject']}, Type: {question['type']}")
            print(f"Question: {question['question']}")
            for i in range(1, 5):
                print(f"{i}. {question.get(f'answer_choice_{i}', '')}")
            print(f"Correct Answer: {question['correct_answer']}\n")

    def take_exam(self):
        if not self.questions:
            print("No questions available for the exam. Please load the questions properly.")
            return
        
        print("\nStarting the exam...\n")
        score = 0
        
        for question in self.questions:
            print(f"Question ID: {question['id']}")
            print(f"Subject: {question['subject']}")
            print(f"Type: {question['type']}")
            print(f"Question: {question['question']}")
            
            # Show answer choices for multiple choice questions
            if question['type'].lower() == 'multiplechoice':
                for i in range(1, 5):
                    print(f"{i}. {question[f'answer_choice_{i}']}")
                
                # Handle correct answer being a letter or number for multiple choice questions
                correct_answer = question["correct_answer"]
                try:
                    # Try to convert the correct answer to an integer
                    correct_index = int(correct_answer) - 1  # Convert to 0-based index
                except ValueError:
                    # If it's not a number, treat it as a letter corresponding to the answer choices
                    choices = [question[f'answer_choice_{i}'] for i in range(1, 5)]
                    correct_index = choices.index(correct_answer)  # Find the correct answer index
                
                # Get the user's response
                while True:
                    try:
                        user_answer = int(input("Enter your answer (1-4): ")) - 1
                        if 0 <= user_answer <= 3:
                            break
                        else:
                            print("Please enter a number between 1 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 4.")
            
            # True/False Handler
            elif question['type'].lower() == 'true/false':
                correct_answer = question['correct_answer']
                print("1. True")
                print("2. False")
                
                # Convert correct answer to an index based on 'True' or 'False'
                correct_index = 0 if correct_answer.upper() == 'T' else 1
                
                # Get the user's response for true/false question
                while True:
                    try:
                        user_answer = int(input("Enter your answer (1 for True, 2 for False): ")) - 1
                        if user_answer == 0 or user_answer == 1:
                            break
                        else:
                            print("Please enter 1 for True or 2 for False.")
                    except ValueError:
                        print("Invalid input. Please enter 1 for True or 2 for False.")
            
            # Check Answer
            if user_answer == correct_index:
                score += 1
        
        print(f"\nYour score: {score}/{len(self.questions)}")


#function to get user input on review question filters and other options
# Process flow based on defined flowchart in the user journey
# 
# Step 1: Select Question Option
#       1.1 Questions Management
#       1.2 Start Review
# Step 1.1 Question Management Option
#       1.1.1 View All Questions
#       1.1.2 Edit Question
#       1.1.3 Delete Question 
#       1.1.4 Add Question 
# 
# 
# 
# 
# 

def main():
    file_path = os.path.join("data",'questionSamples.csv') #linking to the data folder
    question_bank = QuestionBank(file_path)
    
    question_bank.load_questions()

    while True:
        print("""

Select number of chosen option below:

(1) Question Management
(2) Start Review

""")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print('You are now in the Question Management. You can view, edit, delete, and add questions here.')
            print('''

Select options from below: 
(1) View All Questions
(2) Edit Question
(3) Delete Question
(4) Add Question


''')
            # if questionManagementchoice == '1':
            question_bank.view_question()
            
        
        
        
        
        # if choice == '1':
        #     question_bank.review_questions()
        # elif choice == '2':
        #     question_bank.take_exam()
        # elif choice == '3':
        #     print("Exiting...")
        #     break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
