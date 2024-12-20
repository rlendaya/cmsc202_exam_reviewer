#Question Bank
#Reynald
#Mark Lester
#Jade Carl``

'''
Functions in this module:

Menu function
1. question_management_menu: this function shows the main menu for the question management functions

Helper functions
2. load_data_to_lists: loads the data to the question list
3. get_index_of_questions :gets the index of the question to assist the edit question function

functions below are part of the question management and are self-explanatory on what they do. All functions interact with files.
4. view_questions
5. add_question
6. edit question
7. delete question

functions below are related to the review proper
8. review_questions_filtered: this function is to customize the exam by allowing the user to select the subject, question type, and number of questions
9. take_exam: this function will handle the exam/review proper

'''

import random
import utils
import textwrap

class QuestionBank:
    # function to handle file path and initialize variable for question list and question ids
    def __init__(self):
        self.questions = []
        self.headers = []
        self.question_ids = []

    def load_data_to_lists(self):
        # load the questions from the file into the questions list. Results return is a tuple and first index is the list of questions
        self.questions = utils.load_file(utils.question_bank_file_path)[0]
        # load the headers from the file into the headers list. Results return is a tuple and first index is the list of questions
        self.headers = utils.load_file(utils.question_bank_file_path)[1]
        # load the unique question ids into the question_ids list
        self.question_ids = [questions['id'] for questions in self.questions]
          
    # function to get the index of question from the self.questions list for easier manipulation in deleting and editing.
    def get_index_of_question(self,id):
        # use list comprehension to get the dictionary to edit for the edit question function
        self.dict_to_edit = [question for question in self.questions if question['id'] == id][0]
        
        # get the index of the question to edit from the self.questions list
        self.index_of_question = self.questions.index(self.dict_to_edit)
    
    # function to handle viewing of all questions
    def view_question(self,output_code):
        if not self.questions:
            print("No questions available to review.")

        number_of_questions = len(self.questions)
        utils.clear_terminal()
        print(f'\nThere are {number_of_questions} questions in total!\n') 
        
        # initialize variables for header alignment
        no_width = 5
        subject_width = 10
        type_width = 20
        question_width = 70
        
        # print all the questions. There are types of output identified by an output code:
        # Code '1': Will print a sequential number to distinguish each question for readability
        # Code '2': will print the question_id which may not be sequential and is used to identify the question for other processing
        if output_code == '1':
           
            
            # print question headers
            header = (f'{"No":<{no_width}}{"Subject":<{subject_width}}{"Question Type":<{type_width}}{"Question":<{question_width}}')
            print('-'*len(header))
            print(header)
            print('-'*len(header))
            # counter variable for numbering of question on print. This is different from the unique question id
            count = 0
            # loop through the self.questions list and then print.
            for question in self.questions:
                count += 1
                formatted_question = textwrap.wrap(question['question'],70)
                print(f'{count:<{no_width}}{question["subject"]:<{subject_width}}{question["type"]:<{type_width}}{formatted_question[0]:<{question_width}}')
                for line in formatted_question[1:]:
                    print(f'{" "*35}{line}')
    
        else:
            # print question headers
            header = (f'{"Id":<{no_width}}{"Subject":<{subject_width}}{"Question Type":<{type_width}}{"Question":<{question_width}}')
            print('-'*len(header))
            print(header)
            print('-'*len(header))
            for question in self.questions:
                formatted_question = textwrap.wrap(question['question'],70)
                print(f'{question["id"]:<{no_width}}{question["subject"]:<{subject_width}}{question["type"]:<{type_width}}{formatted_question[0]:<{question_width}}')
                for line in formatted_question[1:]:
                    print(f'{" "*35}{line}')

    # function to add questions to the question bank
    def add_question(self):
        utils.clear_terminal()
        print('You can now add questions.\n')
        
        # initialize dictionary for the new question
        new_question = {'id':'','subject':'','type':'','question':'','answer_choice_1':'','answer_choice_2':'','answer_choice_3':'','answer_choice_4':'','correct_answer':''}
        
        # generate unique id for the new question. Max of 100 questions only
        while True:
            new_question_id = random.randint(1,100)
            if str(new_question_id) not in self.question_ids:
                new_question['id'] = new_question_id
                break
            
        # ask user to input values of the other keys in the question dictionary
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
        add_new_question_to_file = input('\nDo you wish to permanently add this question to the question bank? (y or n only): ')
        
        # if user confirms, append to current question list and save to file. Otherwise, advice user that question is not saved
        if add_new_question_to_file.lower() == 'y':
            self.questions.append(new_question)
            utils.save_file(utils.question_bank_file_path,self.questions,self.headers,'w')
            print(f'Changes are now saved to file {utils.question_bank_file_path}')
            # reload question from file to ensure initialized list variables are updated
            self.load_data_to_lists()
        else:
            print('\nQuestion will not be saved to file. Thank you.')
    
    
    # function to delete questions from the question bank
    def delete_question(self):
        utils.clear_terminal()
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
                confirm_delete = input('\nAre you sure you want to delete the question above? (y or n only) ')              
                if confirm_delete.lower() == 'y':
                    del self.questions[self.index_of_question]
                    utils.save_file(utils.question_bank_file_path,self.questions,self.headers,'w')
                    print(f'\nChanges are now saved to file {utils.question_bank_file_path}')
                    self.load_data_to_lists()
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
        utils.clear_terminal()
        
        # run the view question again to show all the questions
        self.view_question('2')
        
        # ask user for the id of the question they want to edit
        while True:
            question_to_edit = input('\nEnter Question Id of the question you want to edit. Press \'x\' to exit: ')
            
            if question_to_edit.lower() == 'x':
                break
            else:
                try: 
                    # call the get_index_of_question function
                    self.get_index_of_question(question_to_edit)
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
                                    
                                    if new_value != '':
                                        if key != 'correct_answer':
                                            self.dict_to_edit[key] = new_value
                                            break
                                        elif key == 'correct_answer' and new_value.lower() in ['t','f']:
                                            self.dict_to_edit[key] = new_value.upper()
                                            break
                                        else:
                                            print('\nWrong Input. Enter t or f only')
                                    else:
                                        print(f'\n{key} cannot be blank. Input a value.\n')
                        
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
                                    if new_value != '':
                                        if key != 'correct_answer':
                                            self.dict_to_edit[key] = new_value
                                            break
                                        elif key == 'correct_answer' and new_value in ['1','2','3','4']:
                                            self.dict_to_edit[key] = new_value
                                            break
                                        else:
                                            print('\nWrong Input. Enter 1 - 4 only')
                                    else:
                                        print(f'\n{key} cannot be blank. Input a value.\n')
                        
                        print('Here are the new values.\n')
                        for key,value in self.dict_to_edit.items():
                            print(f'{key}: {value}')
                    
                    # loop to confirm with user if they want to save the changes in the file
                    while True:
                        save_new_values_to_dict = input('\nDo you with to save these new values? ( y|n only ) ')
                        if save_new_values_to_dict.lower() == 'y':
                            self.questions[self.index_of_question] = self.dict_to_edit
                            utils.save_file(utils.question_bank_file_path,self.questions,self.headers,'w')
                            print(f'\nChanges are now saved to {utils.question_bank_file_path}')
                            self.load_data_to_lists()
                            break
                        elif save_new_values_to_dict == 'n':
                            print('Changes are not saved.')
                            break
                        else:
                            print('Wrong input. Enter y or n only.')
                
                    break      
                                    
                except Exception as e:
                    print(f'\nInvalid Input. Enter the correct question ID...')
                
                
                
                
    
    # function to handle menu options for question management
    def question_management_menu(self):
        
        # load data to the different lists
        self.load_data_to_lists()
    
        utils.clear_terminal()
        
        while True:
            utils.clear_terminal()
            print('You are now in the Question Management Menu. You can view, edit, delete, and add questions here.')
            questionManagementchoice = input('''
Select options from below: 
(1) View All Questions
(2) Edit Question
(3) Delete Question
(4) Add Question
(5) Back to Main Menu

: ''')
            if questionManagementchoice == '1':
                utils.clear_terminal()
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
                print('\nInvalid Option.') 
                input('\nPress Enter to input again...')
                    
                    
    
    # functions below are for the exam proper
  
    # This will be the exam proper user journey
    # 1. Ask user for the exam filters
    #     - topic
    #     - question type
    #     - number of desired questions
    # 2. Take exam
    # 3. Record output and correct answers
    # 4. Display final score and store results in a dictionary
    
    # function to filter the questions based on user feedback
    def review_questions_filtered(self):
        utils.clear_terminal()
        
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
         
        print('\nWelcome to the exam reviewer!')
        print('\nLet\'s setup some of the review settings before we start.')
        input('\nPress Enter to continue... ')
        
       
            
        
        # loop to get user input to choose subjects
        while True:
            utils.clear_terminal()
             # filter user input for available subjects and question type
            print('Filter questions by topic. Only the subjects below are available:\n')
            # display the available subject selection
            for key,value in self.subjects_available.items():
                print(f'({key}) {value}')
            
            subject_response = input('\nEnter (number) of preferred topic. ')
            # if user input is not in the available option, ask for another
            try:
                if int(subject_response) in self.subjects_available:
                    subject_chosen = self.subjects_available[int(subject_response)]
                    break
            except:
                print('\nInvalid Input. Select from the available options only.\nPress Enter to continue...')
                input()
                
        # loop to get user input to choose question type
        while True:
            utils.clear_terminal()
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
                print('\nInvalid Input. Select from the available options only.\nPress Enter to continue...')
                input()
            
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
        
        # initialize the list to store user_answers and details per answer for this session
        self.user_answers = []
        self.user_answers_details_per_question = {}
        
        # load the questions in the list
        self.load_data_to_lists()
        
        # call the review questions filtering function
        self.review_questions_filtered()
        input('\nFilters have been applied. Press Enter to start the exam reviewer..\n')
        utils.clear_terminal()
        
        # create a unique session id for this exam using the utils module
        session_id = utils.unique_id()
        
        print("\nStarting the exam...\n")
        score = 0
        question_count = 0
        is_answer_correct = 0
        results = []
        
        # Show the questions
        for question in self.filtered_question_list:
            utils.clear_terminal()
            question_count += 1
            print(f"No: {question_count}")
            print(f"Subject: {question['subject']}")
            print(f"Type: {question['type']}\n")
            print(f"Question: {question['question']}\n")
               
            # Show answer choices for multiple choice questions
            if question['type'].lower() == 'multiplechoice':
                for i in range(1, 5):
                    print(f"{i}. {question[f'answer_choice_{i}']}")
                     
                # Get the user's response
                while True:
                    try:
                        user_answer = int(input(f"\nEnter your answer (1-4): "))
                        if 1 <= user_answer <= 4:
                            if user_answer == int(question['correct_answer']):
                                score += 1
                                is_answer_correct = 1
                                print(f'\nGood job! You got the correct answer.')
                                input('\nPress Enter to continue...')
                                break
                            else:
                                is_answer_correct = 0
                                print(f'\nYour answer is wrong. Correct answer is {question["correct_answer"]}')
                                input('\nPress Enter to continue...')
                                break
                        else:
                            print("\nInvalid input. Please enter a number between 1 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 4.")
            
            # True/False Handler
            elif question['type'].lower() == 'true/false':
                
                # Get the user's response for true/false question
                while True:
                    try:
                        # get user input for the correct answer
                        user_answer = input("Enter your answer (T for true, F for false): ").capitalize()
                        # check if user's answer is within allowable values
                        if user_answer.lower() in ['t','f']:
                        # Check Answer
                            if user_answer.capitalize() == question["correct_answer"]:
                                score += 1
                                is_answer_correct = 1
                                print(f'\nGood job! You got the correct answer.')
                                input('\nPress Enter to continue...')
                                break
                            else:
                                is_answer_correct = 0
                                print(f'\nYour answer is wrong. Correct answer is {question["correct_answer"]}')
                                input('\nPress Enter to continue...')
                                break
                        else:
                            print("Invalid input. Please enter T or F only!")
                            
                    except ValueError:
                        print("Invalid input. Please enter T or F only!")

            # store the user's answers to a dictionary
            self.user_answers_details_per_question = {
                
                'session_id' : session_id,
                'id' : question['id'],
                'subject' : question['subject'],
                'type' : question['type'],
                'correct_answer' : question['correct_answer'],
                'user_answer' : user_answer,
                'question' : question['question'],
                'is_answer_correct' : is_answer_correct
            }
            
            # append the dictionary of this question to a list of exam answers.
            self.user_answers.append(self.user_answers_details_per_question)
            
        print(f"\nYour score: {score}/{len(self.filtered_question_list)}")
        input(f'\nPress Enter to continue...')
        return results

def main():
    
    question_bank = QuestionBank()
    
if __name__ == "__main__":
    main()
