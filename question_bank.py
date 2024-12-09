#Question Bank
#Reynald
#Mark Lester
#Jade Carl

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
'''

#Comment: Team please check our question_bank feature. I need help in aligning this with our current flowchart. Feel free to adjust.

import csv
import random

# os module for interoperability of file path with different OS
import os

class QuestionBank:
    # function to handle file path and initialize variable for question list
    def __init__(self, file_path):
        self.file_path = file_path
        self.questions = []
        self.headers = []
        self.question_ids = []

    # this function will handle cross-platform clearing of terminal for readability
    def clear_terminal(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # function to handle loading of questions from file
    def load_questions(self): #load question from csv file
        try:
            with open(self.file_path, 'r', encoding='ISO-8859-1') as file:
                reader = csv.DictReader(file)
                self.questions = [row for row in reader]
                self.headers = reader.fieldnames
                self.question_ids = [question['id'] for question in self.questions]
            # print(f"Loaded {len(self.questions)} questions successfully.")
        except Exception as e:
            print(f"An error occurred while loading questions: {e}")


    # function to handle saving of question to file
    def save_questions(self):
        try:
            with open(self.file_path, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)     
                writer.writeheader()
                writer.writerows(self.questions)
        
        except Exception as e:
              print(f"An error occurred while savings questions: {e}")
                
    # function to get the index of question from the self.questions list for easier manipulation in deleting and editing.
    def get_index_of_question(self,id):
        # use list comprehension to get the dictionary to edit
        self.dict_to_edit = [question for question in self.questions if question['id'] == id][0]
        
        # get the index of the question to edit from the self.questions list
        self.index_of_question = self.questions.index(self.dict_to_edit)
    
    # function to handle viewing of all questions
    def view_question(self,output_code):
        if not self.questions:
            print("No questions available to review.")

        number_of_questions = len(self.questions)
        print(f'There are {number_of_questions} questions in total!\n') 
        
        # below will print header
        
        # print all the questions
        if output_code == '1':
            print(f'{'No':^3}{'Subject':^10}{'Question Type':^20}{'Question':<165}\n')
            count = 0
            for questions in self.questions:
                count += 1
                print(f'{count:^3}{questions['subject']:^10}{questions['type']:^20}{questions['question']:<165}')
        else:
            print(f'{'Id':^3}{'Subject':^10}{'Question Type':^20}{'Question':<165}\n')
            count = 0
            for questions in self.questions:
                count += 1
                print(f'{questions['id']:^3}{questions['subject']:^10}{questions['type']:^20}{questions['question']:<165}')
        
    # function to add questions to the question bank
    def add_question(self):
        print('You can now add questions.\n')
        
        # initialize dictionary for the new question
        new_question = {'id':'','subject':'','type':'','question':'','answer_choice_1':'','answer_choice_2':'','answer_choice_3':'','answer_choice_4':'','correct_answer':''}
        
        # generate unique id for the new question
        while True:
            new_question_id = random.randint(1,99)
            if new_question_id not in self.question_ids:
                new_question['id'] = new_question_id
                break
            
        # ask user for the values of the other keys in the question dictionary
        new_question['subject'] = input('Enter subject: ')
        
        # get question type but restrict the values to just true/false or multiple choice
        while True:
            question_type = input('\nSelect (number) of question type below.\n(1) true/false\n(2) multiple choice\n: ')
            if question_type == '1':
                new_question['type'] = 'true/false'
                break
            elif question_type == '2':
                new_question['type'] = 'multiplechoice'
                break
            else:
                print('\nWrong input. Enter only the options provided.')
            
        # ask user to enter question
        new_question['question'] = input('Enter question: ')
        
        # ask user to enter choices if multiple choice
        if question_type == '2':
            new_question['answer_choice_1'] = input('\nEnter answer_choice_1: ')
            new_question['answer_choice_2'] = input('Enter answer_choice_2: ')
            new_question['answer_choice_3'] = input('Enter answer_choice_3: ')
            new_question['answer_choice_4'] = input('Enter answer_choice_4: ')
        
        # ask user to enter the correct answer. Limit input depending on the type of question
        if question_type == '1':
            while True:
                correct_answer = input('\nEnter correct answer (T/F only): ')
                if correct_answer in ['T','F','t','f']:
                    new_question['correct_answer'] = correct_answer
                    break
                else:
                    print('\nWrong input. Enter T or F only.')
        else:
            while True:
                correct_answer = input('\nEnter correct_answer. Enter 1 - 4 only : ')
                if correct_answer in ['1','2','3','4']:
                    new_question['correct_answer'] = correct_answer
                    break
                else:
                    print('\nWrong input. Enter 1 - 4 only.')
        
        # show user summary of the new question for review
        print('Here is the new question:')
        for key,value in new_question.items():
            if question_type == '1':
                if 'answer_choice' not in key:
                    print(f'{key}: {value}')
            else:
                print(f'{key}: {value}')
        
        # ask the user if they want they question to be saved
        add_new_question_to_file = input('\nDo you wish to permanently add this question to the question bank? (Y/N)')
        
        # if user confirms, append to current question list and save to file
        if add_new_question_to_file.lower() == 'y':
            self.questions.append(new_question)
            self.save_questions()
            print(f'Changes are now saved to file {self.file_path}')
            self.load_questions()
        else:
            print('\nData will not be saved. Thank you.')
    
    
    # function to delete questions from the question bank
    def delete_question(self):
        self.clear_terminal()
        print('You can now delete questions.')
        
        # show the list of all questions with code 2
        self.view_question('2')
        
        # loop to ask user to enter id of question they want to delete
        while True:
            id_to_delete = input('\nEnter Id of question to delete. Press \'x\' to exit: ')
            # conditional statement to check if id is found
            if id_to_delete in self.question_ids:
                self.get_index_of_question(id_to_delete)
                print()
                for key, value in self.questions[self.index_of_question].items():
                    print(f'{key}: {value}')
                confirm_delete = input('\nAre you sure you want to delete the question above? (y|n) ')
                
                if confirm_delete.lower() == 'y':
                    del self.questions[self.index_of_question]
                    self.save_questions()
                    print(f'Changes are now saved to file {self.file_path}')
                    self.load_questions()
                    break
                elif confirm_delete.lower() == 'n':
                    print('Question is not deleted.')
                    break
            elif id_to_delete == 'x':
                break
            else: 
                print('That Id does not exist. Input another Id.')
            
        
        
        
                
                
            
        
    ''' Still a work in progress'''
    # function to handle editing of questions
    def edit_question(self):
        self.clear_terminal()
        
        # run the view question again to show all the questions
        self.view_question()
        
        # ask user for the id of the question they want to edit
        question_to_edit = input('\nEnter Question Id of the question you want to edit: ')
        dict_to_edit, index_of_question = self.get_index_of_question(question_to_edit)
        
        
        print('You can now edit questions here. Only editable fields will be shown.\n')
        
        # Ask user for the new values
        # conditional statement for the values to be edited based on type of question
        if self.questions[index_of_question]['type'] == 'true/false':
            for key,value in dict_to_edit.items():
                if 'answer_choice' not in key and key.lower() != 'id':
                    print(f'\n{key}: {value}')
                    
                    if key == 'type':
                        print('\nOnly the values below are allowed! Enter (number) of chosen value.')
                        print('(1) true/false')
                        print('(2) multiplechoice')
                        
                        chosenValue = input('\n: ')
                        if chosenValue == '1':
                            new_value = 'true/false'
                        elif chosenValue == '2':
                            new_value = 'multiplechoice'
                            print('\nQuestion type has changed from true/false to multiplechoice. Enter choices below:')
                            answer_choice_1 = input('answer_choice_1: ')
                            self.questions[index_of_question]['answer_choice_1'] = answer_choice_1
                            answer_choice_2 = input('answer_choice_2: ')
                            self.questions[index_of_question]['answer_choice_2'] = answer_choice_2
                            answer_choice_3 = input('answer_choice_3: ')
                            self.questions[index_of_question]['answer_choice_3'] = answer_choice_3
                            answer_choice_4 = input('answer_choice_4: ')
                            self.questions[index_of_question]['answer_choice_4'] = answer_choice_4
                        
                        else:
                            print('Wrong Input. Skipping changes in this field')
                    
                    elif key == 'correct_answer':
                        chosenValue = input('\nOnly \'T\' or \'F\' are allowed: ')
                        
                        if chosenValue.lower() == 't' or chosenValue.lower() == 'f':
                            new_value = chosenValue
                        else:
                            print('Wrong Input!')
                        
                    else:
                        new_value = input('Enter new value (press Enter to skip): ')
                    
                    if new_value != '':
                        self.questions[index_of_question][key] = new_value
                
            print(self.questions[index_of_question])
                        
        else:
            for k,v in dict_to_edit.items():
                if 'answer_choice' not in k:
                    print(k,v)
        
        
      
        
        
        
        
        


    
    # function below is superseded by the view question function
        # def review_questions(self):
            
        #     if not self.questions:
        #         print("No questions available to review.")
        #         return
            
        #     print("\nReviewing Questions:\n")
        #     for question in self.questions:
        #         print(f"ID: {question['id']}, Subject: {question['subject']}, Type: {question['type']}")
        #         print(f"Question: {question['question']}")
        #         for i in range(1, 5):
        #             print(f"{i}. {question.get(f'answer_choice_{i}', '')}")
        #         print(f"Correct Answer: {question['correct_answer']}\n")

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

def main():
    file_path = os.path.join("data",'questionSamples.csv') #linking to the data folder
    question_bank = QuestionBank(file_path)
    
    # load the questions
    question_bank.load_questions()

    while True:
        question_bank.clear_terminal()
        print("""This is the Main Menu

Select number of chosen option below:

(1) Question Management
(2) Start Review
(3) Exit Program
""")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            question_bank.clear_terminal()
            print('You are now in the Question Management Menu. You can view, edit, delete, and add questions here.')
            
            while True:
                question_bank.clear_terminal()
                questionManagementchoice = input('''
Select options from below: 
(1) View All Questions
(2) Edit Question
(3) Delete Question
(4) Add Question
(5) Back to Main Menu

: ''')
                if questionManagementchoice == '1':
                    question_bank.clear_terminal()
                    question_bank.view_question('1')
                    input('\nPress Enter to go back to the previous menu')
                elif questionManagementchoice == '2':
                    question_bank.edit_question()
                    input()
                elif questionManagementchoice == '3':
                    question_bank.delete_question()
                    input('\nPress Enter to go back to the previous menu')
                elif questionManagementchoice == '4':
                    question_bank.add_question()
                    input('\nPress Enter to go back to the previous menu')
                elif questionManagementchoice == '5':
                    break
                else:
                    print('Invalid Option. ')
            
        
        
        
        

        elif choice == '2':
            question_bank.take_exam()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
