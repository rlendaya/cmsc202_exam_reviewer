'''
This is a shared module that will handle functions that may be shared across modules

Function:
1. clear_terminal: this clears the terminal to improve readability
2. unique_id: this creates a unique integer id using time since epoch
3. 

'''


import os
import time
import csv

# initialize file paths variables
question_bank_file_path = os.path.join("data",'questionSamples.csv')
answer_storage_file_path = os.path.join("data",'answers.csv')

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

# load file function
def load_file(filepath):
        try:
            with open(filepath, 'r', encoding='ISO-8859-1') as file:
                reader = csv.DictReader(file)
                row_data = [row for row in reader]
                headers = reader.fieldnames
                
                return row_data, headers
            
        except Exception as e:
            print(f"An error occurred while loading questions: {e}")
            
# function to save files
def save_file(file_path,data_to_be_saved,headers,write_mode,include_headers=True):
        try:
            with open(file_path, write_mode) as file:
                writer = csv.DictWriter(file, fieldnames=headers)     
                if include_headers == True:
                    writer.writeheader()
                writer.writerows(data_to_be_saved)
        
        except Exception as e:
              print(f"An error occurred while savings questions: {e}")
              
if __name__ == "__main__":
    clear_terminal()
    unique_id()
    save_file()
    load_file()
    