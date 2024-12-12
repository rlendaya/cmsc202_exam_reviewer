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

import csv
import random

# os module for interoperability of file path with different OS
import os

class QuestionBank:
    # function to handle file path and initialize variable for question list and question ids
    def __init__(self):
        self.file_path = os.path.join("data",'questionSamples.csv') #linking to the data folder
        self.questions = []
        self.headers = []
        self.question_ids = []
        self.user_answers = {}

    # function to handle cross-platform clearing of terminal for readability
    def clear_terminal(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    # function to handle loading of questions from file
    def load_questions(self):
        
        try:
            with open(self.file_path, 'r', encoding='ISO-8859-1') as file:
                reader = csv.DictReader(file)
                self.questions = [row for row in reader]
                self.headers = reader.fieldnames
                self.question_ids = [question['id'] for question in self.questions]
        except Exception as e:
            print(f"An error occurred while loading questions: {e}")

    # function to handle saving of questions to file
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
        self.clear_terminal()
        print(f'There are {number_of_questions} questions in total!\n') 
        
        # print all the questions. There are types of output identified by an output code:
        # Code '1': Will print a sequential number to distinguish each question for readability
        # Code '2': will print the question_id which may not be sequential and is used to identify the question for other processing
        if output_code == '1':
            # print question headers
            print(f'{"No":^3}{"Subject":^10}{"Question Type":^20}{"Question":<165}\n')
            # counter variable for numbering of question on print. This is different from the unique question id
            count = 0
            # loop through the self.questions list and then print.
            for questions in self.questions:
                count += 1
                print(f'{count:^3}{questions["subject"]:^10}{questions["type"]:^20}{questions["question"]:<165}')
        else:
            # print question headers
            print(f'{"Id":^3}{"Subject":^10}{"Question Type":^20}{"Question":<165}\n')
            for questions in self.questions:
                print(f'{questions["id"]:^3}{questions["subject"]:^10}{questions["type"]:^20}{questions["question"]:<165}')

 
    # function to add questions to the question bank
    def add_question(self):
        self.clear_terminal()
        print('You can now add questions.\n')
        
        # initialize dictionary for the new question
        new_question = {'id':'','subject':'','type':'','question':'','answer_choice_1':'','answer_choice_2':'','answer_choice_3':'','answer_choice_4':'','correct_answer':''}
        
        # generate unique id for the new question. Max of 100 questions only
        while True:
            new_question_id = random.randint(1,100)
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
        new_question['question'] = input('\nEnter question: ')
        
        # ask user to enter choices if question type is multiple choice
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
                    new_question['correct_answer'] = correct_answer.upper()
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
        print('\nHere is the new question:')
        # loop through the dictionary of the new question. Remove multiple choice inputs true/false type of question
        for key,value in new_question.items():
            if question_type == '1':
                if 'answer_choice' not in key:
                    print(f'{key}: {value}')
            else:
                print(f'{key}: {value}')
        
        # ask the user if they want they question to be saved
        add_new_question_to_file = input('\nDo you wish to permanently add this question to the question bank? (y/n): ')
        
        # if user confirms, append to current question list and save to file. Otherwise, advice user that question is not saved
        if add_new_question_to_file.lower() == 'y':
            self.questions.append(new_question)
            self.save_questions()
            print(f'Changes are now saved to file {self.file_path}')
            # reload question from file to ensure initialized list variables are updated
            self.load_questions()
        else:
            print('\nQuestion will not be saved to file. Thank you.')
    
    
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
                
                # confirm with user if they want to proceed with deletion of question
                confirm_delete = input('\nAre you sure you want to delete the question above? (y|n) ')              
                if confirm_delete.lower() == 'y':
                    del self.questions[self.index_of_question]
                    self.save_questions()
                    print(f'\nChanges are now saved to file {self.file_path}')
                    self.load_questions()
                    break
                elif confirm_delete.lower() == 'n':
                    print('\nQuestion is not deleted.')
                    break
            # exit the question delete module when user enters 'x'
            elif id_to_delete == 'x':
                break
            # error message when question id is not found in the question_ids list
            else: 
                print('\nThat Question Id does not exist. Input another Id.')


    # function to handle editing of questions
    def edit_question(self):
        self.clear_terminal()
        
        # run the view question again to show all the questions
        self.view_question('2')
        
        # ask user for the id of the question they want to edit
        while True:
            try: 
                question_to_edit = input('\nEnter Question Id of the question you want to edit: ')
        
                # call the get_index_of_question function
                self.get_index_of_question(question_to_edit)
                break
            
            except Exception as e:
                print('\nInvalid Input. Enter the correct question ID...')
                
        
        print('\nYou can now edit questions here. Only editable fields will be shown.\n')
        
        # Ask user for the new values. Below is the conditional statement for the values to be edited based on type of question
        # These are the only allowable values to be edited. Any field outside of these should be recreated as another question
        # For question type: true/false:
        # 1. Subject
        # 2. Question
        # 3. correct answer
        # 
        # For question type: multiple choice 
        # 1. Subject
        # 2. Question
        # 3. answer_choices 1 - 4
        # 4. correct_answer

        # if question type is t/f, only show the subject, question, and correct answer
        if self.questions[self.index_of_question]['type'] == 'true/false':
            for key,value in self.dict_to_edit.items():
                if 'answer_choice' not in key and key.lower() != 'id' and key.lower() != 'type':
                    print(f'\nCurrent value:\n{key}: {value}')
                    
                    # if current key is correct answer, limit input to just t and f
                    while True:
                        new_value = input(f'Enter new value for {key}: ')
                        if key != 'correct_answer':
                            self.dict_to_edit[key] = new_value
                            break
                        elif key == 'correct_answer' and new_value.lower() in ['t','f']:
                            self.dict_to_edit[key] = new_value.upper()
                            break
                        else:
                            print('\nWrong Input. Enter t or f only')
            
            print('Here are the new values.\n')
            for key,value in self.dict_to_edit.items():
                if 'answer_choice' not in key and key.lower() != 'id' and key.lower() != 'type':
                    print(f'{key}: {value}')
        
        # if question type is multiple choice, show edit ability for answer choice
        else:
            for key,value in self.dict_to_edit.items():
                if key.lower() != 'id' and key.lower() != 'type':
                    print(f'\nCurrent value:\n{key}: {value}')
                    
                    # if key is correct answer, limit input to just 1 - 4
                    while True:
                        new_value = input(f'Enter new value for {key}: ')
                        if key != 'correct_answer':
                            self.dict_to_edit[key] = new_value
                            break
                        elif key == 'correct_answer' and new_value in ['1','2','3','4']:
                            self.dict_to_edit[key] = new_value
                            break
                        else:
                            print('\nWrong Input. Enter 1 - 4 only')
            
            print('Here are the new values.\n')
            for key,value in self.dict_to_edit.items():
                print(f'{key}: {value}')
        
        while True:
            save_new_values_to_dict = input('\nDo you with to save these new values? ( y|n only ) ')
            if save_new_values_to_dict.lower() == 'y':
                self.questions[self.index_of_question] = self.dict_to_edit
                self.save_questions()
                print(f'Changes are now saved to {self.file_path}')
                self.load_questions()
                break
            elif save_new_values_to_dict == 'n':
                print('Changes are not saved.')
                break
            else:
                print('Wrong input. Enter y or n only.')
    
    # function to handle menu options for question management
    def question_management_menu(self):
            self.clear_terminal()
            print('You are now in the Question Management Menu. You can view, edit, delete, and add questions here.')
            
            while True:
                self.clear_terminal()
                questionManagementchoice = input('''
Select options from below: 
(1) View All Questions
(2) Edit Question
(3) Delete Question
(4) Add Question
(5) Back to Main Menu

: ''')
                if questionManagementchoice == '1':
                    self.clear_terminal
                    self.view_question('1')
                    input('\nPress Enter to go back to the previous menu')
                elif questionManagementchoice == '2':
                    self.edit_question()
                    input('\nPress Enter to go back to the previous menu')
                elif questionManagementchoice == '3':
                    self.delete_question()
                    input('\nPress Enter to go back to the previous menu')
                elif questionManagementchoice == '4':
                    self.add_question()
                    input('\nPress Enter to go back to the previous menu')
                elif questionManagementchoice == '5':
                    break
                else:
                    print('Invalid Option. ')  
                    
    
    # functions below are for the exam proper
    '''
    This will be the exam proper user journey
    1. Ask user for the exam filters
        - topic
        - question type
        - number of desired questions
    2. Take exam
    3. Record output and correct answers
    4. Display final score and store results in a dictionary
    '''

    # function to filter the questions based on user feedback
    def review_questions_filtered(self):
        self.clear_terminal()
        
        # initialize dictionary and other variables to be used for filtering 
        self.subjects_available = {}
        
        
         # store the unique subjects from the question bank to a dictionary
        subject_number = 0
        for question in self.questions:
            if question['subject'] not in self.subjects_available.values():
                subject_number += 1
                self.subjects_available[subject_number] = question['subject']
        
        # add the 'all' option as another key in the dictionary
        subject_number+=1
        self.subjects_available[subject_number] = 'All Subjects'
         
        
        print('\nWelcome to the mock exam!')
        print('\nLet\'s setup some of the review settings before we start.\n ')
        
        # filter user input for available subjects and question type
        print('Filter questions by topic. Only the subjects below are available:\n')
        # display the available subject selection
        for key,value in self.subjects_available.items():
            print(f'({key}) {value}')
            
        
        # loop to get user input to choose subjects
        while True:
            subject_response = input('\nEnter (number) of preferred topic. ')
            # if user input is not in the available option, ask for another
            try:
                if int(subject_response) in self.subjects_available:
                    subject_chosen = self.subjects_available[int(subject_response)]
                    break
            except:
                print('\nInvalid Input. Select from the available options only.')
                
        # loop to get user input to choose question type
        while True:
            self.clear_terminal()
            question_response = input('\nSelect Preferred Question Type\n(1) True or False\n(2) Multiple Choice\n(3) All Question Types\n\nEnter (number) of preferred question type: ')
            if question_response in ['1','2','3']:
                if question_response == '1':
                    question_type = 'true/false'
                
                elif question_response == '2':
                    question_type = 'multiplechoice'
                
                else:
                    question_type = 'All Question Types'
                    
                break
            
            else:
                print('\nInvalid Input. Select from the available options only.')
            
        # get the initial list of questions based on user input for 2 filters. these filters will be applied sequentially. 
        # After application of these filters, apply question count filter
        
        if subject_chosen != 'All Subjects':
            self.filtered_question_list = [question for question in self.questions if question['subject'] == subject_chosen]
        else:
            self.filtered_question_list = [question for question in self.questions]
            
        if question_type != 'All Question Types':
            self.filtered_question_list = [question for question in self.filtered_question_list if question['type'] == question_type]
        else:
            self.filtered_question_list = [question for question in self.filtered_question_list]
        
        # filter for the users preferred number of question
        max_question_count = len(self.filtered_question_list)
        while True:
            # user input must not exceed the max question available and should be >0
            try:
                question_count = input(f'\nHow many questions do you want to answer? Max of {max_question_count} question/s only: ')
                # if the inputted question count is same as max question then keep the question list as is. Otherwise randomly select from the question ids
                if int(question_count) == int(max_question_count):
                    break
                
                # condition to randomize questions based on id 
                elif int(question_count) > 0 and int(question_count) < max_question_count:
                    self.filtered_question_list_ids = [question_list['id'] for question_list in self.filtered_question_list]
                    
                    # select question_ids randomly from the list
                    self.filtered_question_list_ids = random.sample(self.filtered_question_list_ids, int(question_count))
                    self.filtered_question_list = [question for question in self.filtered_question_list if question['id'] in self.filtered_question_list_ids]
                    break
                
                else:
                    print(f'\nInvalid Input. Select from 1 to {max_question_count} question/s only!!!!')
                    
            except Exception as e:
                print(f'\nInvalid Input. Select from 1 to {max_question_count} question/s only. {e}')
        

    # function to conduct the exam review
    def take_exam(self):
        # call the review questions filtering function
        self.review_questions_filtered()
        input('\nFilters have been applied. Press Enter to start the exam reviewer..\n')
        self.clear_terminal()
        
        print("\nStarting the exam...\n")
        score = 0
        question_count = 0
        
        # Show the questions
        for question in self.filtered_question_list:
            self.clear_terminal()
            question_count += 1
            print(f"No: {question_count}")
            print(f"Subject: {question['subject']}")
            print(f"Type: {question['type']}\n")
            print(f"Question: {question['question']}\n")
            
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
                
                # Get the user's response for true/false question
                while True:
                    try:
                        
                        user_answer = input("Enter your answer (T for true, F for false): ")
                        
                        # check if user's answer is within allowable values
                        if user_answer.lower() in ['t','f']:
                        # Check Answer
                            if user_answer.capitalize() == question['correct_answer']:
                                score += 1
                                print(f'\nGood job! You got the correct answer.')
                                input('\nPress Enter to continue...')
                                break
                            else:
                                print(f'\nYour answer is wrong. Correct answer is {question['correct_answer']}')
                                input('\nPress Enter to continue...')
                                break
                        else:
                            print("Invalid input. Please enter T or F only!")
                    except ValueError:
                        print("Invalid input. Please enter T or F only!")
        
            
        print(f"\nYour score: {score}/{len(self.filtered_question_list)}")
        input(f'\nPress Enter to continue...')


def main():
    
    question_bank = QuestionBank()
    
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
            question_bank.question_management_menu()
        elif choice == '2':
            question_bank.take_exam()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
