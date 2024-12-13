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


# removed OOP for now for fine tuning, please feel free to convert if needed
#class AnswerStorage:
    #def __init__(self):
        #self.answers = {}  # Store user answers, key=question ID and value=answer
        #self.file_name = "answer_storage.txt"

#     (question['id'], question['question'], question['correct_answer'], user_answer)


import os
import utils as u

''''
def save_answers expected input: a list of dictionaries with the following info: 
[
{session_id:'session_id', question_id: 'question_id, subject: 'subject', type: 'type', correct_answer: correct_answer, user_answer: 'user_answer', question: 'question text'
]

sample:
[{'session_id': 1734082085, 'id': '13', 'subject': 'cmsc 206', 'type': 'multiplechoice', 'correct_answer': '3', 'user_answer': 3, 'question': 'It uniquely identifies each entity in the entity set'}, 
{'session_id': 1734082385, 'id': '12', 'subject': 'cmsc 206', 'type': 'multiplechoice', 'correct_answer': '3', 'user_answer': 3, 'question': 'It is the number of vertices in a graph.'}, 
{'session_id': 1734082185, 'id': '19', 'subject': 'cmsc 206', 'type': 'multiplechoice', 'correct_answer': '3', 'user_answer': 4, 'question': 'It is the number of edges in a graph.'}]

'''

answer_storage_file_path = u.answer_storage_file_path


def save_answers(answer_storage_file_path):
    current_session_id = None

    # Open the file where answer data will be stored
    with open(answer_storage_file_path, 'a') as file: 

        # Parse and format answers in answer_data list
        for dictionary in file:
            keys = list(dictionary.keys())

            session_id = dictionary[keys[0]]
            question_id = dictionary[keys[1]]
            subject = dictionary[keys[2]]
            question_text = dictionary[keys[6]]
            user_answer = dictionary[keys[5]]
            correct_answer = dictionary[keys[4]]
            is_correct = (str(user_answer).lower() == str(correct_answer).lower()) # Checks correctness of user answer

            # Ends the session and starts session if new session available
            if session_id != current_session_id:
                if current_session_id is not None:
                    file.write("######### End of Session #########\n\n\n") # End of session

                # Header as the session date
                file.write(f"Session ID: {session_id}\n")
                file.write("========================\n")
                current_session_id = session_id

            # Write question details in file
            file.write(f"Question ID: {question_id}\n")            
            file.write(f"Subject: {subject}\n")
            file.write(f"Question: {question_text}\n")
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write(f"User Answer: {user_answer}\n")
            file.write(f"Is Correct: {is_correct}\n\n") # create an empty line in between questions
        
        # End session
        file.write("######### End of Session #########\n\n\n")


    '''
    Session ID: 1734082085
    =========================
    Question ID: 8
    Subject: CMSC 202
    Question: What is 2+2?
    Correct Answer: 4
    User Answer: 4
    Is Correct: True

    Question ID: 3
    Subject: CMSC 201
    Question: Is a set unordered?
    Correct Answer: True
    User Answer: False
    Is Correct: False

    ######### End of Session #########

    
    Session Date: 1734082086
    ========================
    Question ID: 1
    Subject: CMSC 202
    Question: "What is 2+6?"
    Correct Answer: 4
    User Answer: 4
    Is Correct: False

    ######### End of Session #########
    '''





def retrieve_answers(answer_storage_file_path):
        
    review_session = input("Do you want to review previous study sessions? Type 'yes' or 'no'\n")

    if review_session.lower() == "yes":
        # Check first if file exists
        if not os.path.exists(answer_storage_file_path):
            print("No study sessions available yet.")
            return # Return to main menu

        sessions = []  # List of all sessions available

        # Read through file containing sessions
        with open(answer_storage_file_path, "r") as file:
            lines = file.readlines()

            # Get available sessions
            for line in lines:
                line = line.strip() # Remove leading/trailing spaces
                if line.startswith("Session ID:"):
                    session_id = line.split(": ")[1]
                    sessions.append(session_id)
        
        # Check that file has session/s
        if not sessions:
            print("No study sessions available yet.")
            return # Return to main menu
        

        # Ask user to choose study session from list:
        try:
            print("\nSelect a session number to view questions and answers, or 0 to go back to main menu")
            # Show available sessions
            print("Available Study Sessions: \n")
            print("0. Go back to Main Menu")
            for idx, session in enumerate(sessions):
                print(f"{idx + 1}. Session: {session}")
            
            choice = int(input("\nNumber: "))
            print("")
            if choice == 0:
                return # Return to Main Menu
            elif 1 <= choice <= len(sessions):
                current_session = sessions[choice - 1]

                # Display data of chosen session
                session_found = False
                for line in lines:
                    line = line.strip()
                    if line.startswith(f"Session ID: {current_session}"):
                        session_found = True # Flags session beginning
                    if session_found:
                        print(line) # Print subsequent lines of the chosen session
                    if line == "#### End of Session ####":
                        session_found = False # Reset flag
                        break # Stop loop
            
            else:
                print("Invalid input. Please input a valid session number.")
        
        except ValueError:
            print("Invalid input. Please input a number.")
    
    else:
        print()
        print("Great. We'll return to the main menu.") # Handles if the user chooses 'no'

        



####################### TEST RUN #########################

def test_main_menu():
    while True:
        print("\nMAIN MENU")
        print("1. View Previous Sessions")
        print("5. Exit\n")

        choice = input("Please choose a number from the main menu: ")
        print("")


        if choice == "1":
            retrieve_answers(file_path)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Incorrect input. Please choose agaian.")



# test_answer_data1 = [{'session_id': 1734082085, 'id': '13', 'subject': 'cmsc 206', 'type': 'multiplechoice', 'correct_answer': '3', 'user_answer': 3, 'question': 'It uniquely identifies each entity in the entity set'}, 
# {'session_id': 1734082085, 'id': '12', 'subject': 'cmsc 206', 'type': 'multiplechoice', 'correct_answer': '3', 'user_answer': 3, 'question': 'It is the number of vertices in a graph.'}, 
# {'session_id': 1734082085, 'id': '19', 'subject': 'cmsc 206', 'type': 'multiplechoice', 'correct_answer': '3', 'user_answer': 4, 'question': 'It is the number of edges in a graph.'}]

# test_answer_data2 = [{'session_id': 1734082086, 'id': '14', 'subject': 'cmsc 203', 'type': 'multiplechoice', 'correct_answer': '3', 'user_answer': 3, 'question': 'It uniquely identifies each entity in the entity set'}, 
# {'session_id': 1734082086, 'id': '13', 'subject': 'cmsc 201', 'type': 'T/F', 'correct_answer': 't', 'user_answer': 'F', 'question': 'Order is the number of vertices in a graph.'}, 
# {'session_id': 1734082086, 'id': '20', 'subject': 'cmsc 202', 'type': 'multiplechoice', 'correct_answer': '3', 'user_answer': 4, 'question': 'It is the number of edges in a graph.'}]

# save_answers(test_answer_data1) # creates answers.txt file that saves the answers 

# save_answers(test_answer_data2)

# test_main_menu()


if __name__ == "__main__":
    test_main_menu()
    retrieve_answers()
    save_answers()
