#Answer Storage
#Jerry Luis
#Ellen Dee

'''
save_answer:
-called when taking the test proper, when user agrees to save answers
-takes a list of dictionaries from question_bank.py and reformats it
-adds and saves the new format to a file


retrieve_answers:
-called when chosen from the main menu
-asks the user if they want to review previous study sessions; returns to main menu if 'no'
-if no answer file found, no previous session available; print message and return to main menu
-lists the sessions available and ask the user to pick
-displays the questions, answers and correct answers from the chosen session

'''

import os
import utils as u
import datetime
import textwrap

def save_answers(answers): 
    
    print(answers)
    # get the headers from the first dictionary in the list
    headers = answers[0].keys()
    
    # check if file already has a header
    existing_headers = u.load_file(u.answer_storage_file_path)[1]
    
    # if no header, include header in the append
    if not existing_headers:
        u.save_file(u.answer_storage_file_path,answers,headers,'a')
    
    # exclude header in append if it already exists
    else:   
        u.save_file(u.answer_storage_file_path,answers,headers,'a',False)


def retrieve_answers(answer_storage_file_path):
    
    # read the saved answers from the csv file (answer.csv)
    answers = u.load_file(u.answer_storage_file_path)[0]
    headers = u.load_file(u.answer_storage_file_path)[1]
    
    # initalize the dictionary where the filtered values will be stored
    session_list = []
    session_id = []
    session_count = 0
    
        
    # show user all the unique review sessions
    for answer in answers:        
        if answer['session_id'] not in session_id:
            session_count += 1
            session = {
                'session_number': session_count
                ,'session_id' : answer['session_id']
                ,'session_date': datetime.datetime.fromtimestamp(int(answer['session_id'])).strftime("%Y-%m-%d %I:%M %p")
                ,'subject': answer['subject']
                ,'type': answer['type']         
            }
            session_id.append(answer['session_id'])
            session_list.append(session)

    # printout all the session ids and ask user to choose from the session ids 
    print(f'\n{'Session Number':^17}{'Session Id':<15}{'Session Date':<25}{'Subject':<15}{'Type':<15}')
    for session in session_list:
        print(f'{session['session_number']:<17}{session['session_id']:<15}{session['session_date']:<25}{session['subject']:<15}{session['type']:<15}')
          
    # print the data from the chosen session id
    while True:
        session_number =[int(session['session_number']) for session in session_list]
        choose_session = input(f'\nSelect session number that you want to view: ')
        try:
            
            # initialize variable for text alignment
            session_id_selected = session_list[int(choose_session)-1]['session_id']
            
            # initialize variables for textwrapping
            no_width = 5
            subject_width = 10
            question_width = 70
            answer_width = 15
            count = 0
            
            u.clear_terminal()
            print(f'\n{'No.':<{no_width}}{'Subject':<{subject_width}}{'Question':<{question_width}}{'Your Answer':^{answer_width}}{'Correct answer':^{answer_width}}{'Result':^{answer_width}}')
            
            # loop to print the results from the previous exams
            for answer in answers:
                # check if session id is in the list
                if answer['session_id'] == session_id_selected:
                    count+=1

                    # check for correctness of answer
                    if answer['user_answer'] == answer['correct_answer']:
                        is_answer_correct = 'Correct'
                    else:
                        is_answer_correct = 'Incorrect'
                    
                    # wrap the questions that are too long to be displayes
                    formatted_question_text = textwrap.wrap(answer['question'],70,subsequent_indent=' '*(subject_width+no_width))
                    
                    # compute the needed space to add for consistent table formatting.
                    spaces_to_add = question_width-len(formatted_question_text[0])
                    
                    # enter the first line text
                    print(f'\n{count:<{no_width}}{answer['subject']:<{subject_width}}{formatted_question_text[0]+' '*spaces_to_add}{answer['user_answer']:^{answer_width}}{answer['correct_answer']:^{answer_width}}{is_answer_correct:^{answer_width}}')
                    # enter the succeeding lines that are over the wrap limit
                    for line in range(1,len(formatted_question_text)):
                        print(f'{formatted_question_text[line]}')
                
            input('\nPress Enter to continue...')
            break

        except Exception as e:
            print(f'Invalid Input. Please Enter from the available session numbers only. {e}')

if __name__ == "__main__":
    retrieve_answers(u.answer_storage_file_path)
    save_answers(u.answer_storage_file_path)
