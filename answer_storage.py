#Answer Storage
#Jerry Luis
#Ellen Dee

'''
Functions in this module:
1. save_answers: this function saves the answers from the current session to the answer storage file
2. retrieve answers: this function retrieves the dictionary of the session based on the users input
'''

import utils as u
import datetime

def save_answers(answers): 
    
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

# function to retrieve the answers from the answer_storage.csv this returns a list of answers based on the users selected review session
def retrieve_answers(answer_storage_file_path):
    
    # read the saved answers from the csv file (answer.csv)
    answers = u.load_file(u.answer_storage_file_path)[0]
    
    # initalize the dictionary where the filtered values will be stored
    session_list = []
    session_id = []
    session_count = 0
    exam_type = []
    subjects = []
        
    # show user all the unique review sessions
    for answer in answers:        
        if answer['session_id'] not in session_id:
            session_count += 1
            current_session_id = answer['session_id']
            exam_type = ",".join(list(set([answer['type'] for answer in answers if answer['session_id'] == current_session_id])))
            subjects = ",".join(list(set([answer['subject'] for answer in answers if answer['session_id'] == current_session_id])))
            number_of_items = len([answer['subject'] for answer in answers if answer['session_id'] == current_session_id])
            session = {
                'session_number': session_count
                ,'session_id' : answer['session_id']
                ,'session_date': datetime.datetime.fromtimestamp(int(answer['session_id'])).strftime("%Y-%m-%d %I:%M %p")
                ,'subject': subjects
                ,'type': exam_type
                ,'number_of_items':number_of_items
            }
            session_id.append(answer['session_id'])
            session_list.append(session)
    
    # printout all the session ids and ask user to choose from the session ids 
    header = f'{"Session Number":^17}{"Session Id":<15}{"Session Date":<25}{"Subject":<30}{"Exam Type":<30}{"Number of Items":^15}'
    print('-'*len(header))
    print(header)
    print('-'*len(header))
    for session in session_list:
        print(f'')
    
    # print the data from the chosen session id
    while True:
        choose_session = input(f'\nSelect session number that you want to view: ')
        try:
            
            # this will be the return variable
            results = []
            
            # determine session id from the choose session variable
            session_id_selected = session_list[int(choose_session)-1]['session_id']
            for answer in answers:
                if answer['session_id'] == session_id_selected:
                    results.append(answer)

            return results
            
        except Exception as e:
            print(f'Invalid Input. Please Enter from the available session numbers only.')


if __name__ == "__main__":
    retrieve_answers(u.answer_storage_file_path)
    save_answers(u.answer_storage_file_path)
