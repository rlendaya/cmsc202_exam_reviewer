'''
This is a shared module that will handle functions that may be shared across modules

Function:
1. clear_terminal: this clears the terminal to improve readability
2. unique_id: this creates a unique integer id using time since epoch
3. 

'''


import os
import time


# function that will clear the terminal based on user's operating system
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
# unique id creator based on time
def unique_id():
    intTime = int(time.time())
    
    return intTime

question_bank_file_path = os.path.join("data",'questionSamples.csv')
answer_storage_file_path = os.path.join("data",'answers.txt')