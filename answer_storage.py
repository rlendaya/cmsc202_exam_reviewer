#Answer Storage
#Jerry Luis
#Ellen Dee


'''
MODULE INFO

save_answer:
-called when taking the test proper, when user agrees to save answers
-takes a list of dictionaries from question_bank.py and reformats it
-adds session date
-adds and saves the new format to a file


retrieve_answers:
-called when chosen from the main menu
-asks the user if they want to review previous study sessions; returns to main menu if 'no'
-if no answer file found, no previous session available; print message and return to main menu
-lists the sessions available and ask the user to pick
-displays the questions, answers and correct answers from the chosen session

'''



import os
import datetime

# Reverting to functions for now while fine tuning code
#class AnswerStorage:
    #def __init__(self):
        #self.answers = {}  # Store user answers, key=question ID and value=answer
        #self.file_name = "answer_storage.txt"



def save_answers(answer_data): # Expected input: a list of tuples with the following info: (question['id'], question['question'], question['correct_answer'], user_answer) 
    session_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Open the file where answer data will be stored
    with open('answers.txt', 'a') as file:
        # Header as the session date
        file.write(f"Session Date: {session_date}\n")
        file.write(" ========================\n")

    # Format answers in answer_data list
    for answer in answer_data:
        question_id = answer[0]
        question_text = answer[1]
        user_answer = answer[2]
        correct_answer = answer[3]
        is_correct = (user_answer == correct_answer) # Checks correctness of user answer

        # Write question details in file
        file.write(f"Question ID: {question_id}\n")
        file.write(f"Question: {question_text}\n")
        file.write(f"Correct Answer: {correct_answer}\n")
        file.write(f"User Answer: {user_answer}\n")
        file.write(f"Is Correct: {is_correct}\n\n") # create an empty line in between questions
    
    # End session
    file.write("==== End of Session ====\n\n")


'''
Session Date: 2024-12-25
=========================
Question ID: 8
Question: What is 2+2?
Correct Answer: 4
User Answer: 4
Is Correct: True

Question ID: 3
Question: Is a set unordered?
Correct Answer: True
User Answer: False
Is Correct: False

==== End of Session ====

Session Date: 2024-12-26
========================
Question ID: 1
Question: "What is 2+6?"
Correct Answer: 4
User Answer: 4
Is Correct: False

==== End of Session ====
'''


def retrieve_answers(filename):
    review_session = input("Do you want to review previous study sessions? Type 'yes' or 'no.'")

    if review_session.lower() == "yes":
        # Check first if file exists
        if not os.path.exists(filename):
            print("No study sessions available yet.")
            return # Return to main menu

        sessions = []  # List of all session dates available

        # Read through file containing sessions
        with open(filename, "r") as file:
            lines = file.readlines()

            # Get available session dates
            for line in lines:
                line = line.strip() # Remove leading/trailing spaces
                if line.startswith("Session Date:"):
                    session_date = line.split(": ")[1]
                    sessions.append(session_date)
        
        # Check that file has session/s
        if not sessions:
            print("No study sessions available yet.")
            return # Return to main menu

        # Show available sessions
        print("Available Study Sessions:")
        for idx, session in enumerate(sessions):
            print(f"{idx + 1}. Session: {session}")

        # Ask user to choose study session from list:
        try:
            choice = int(input("\nSelect a session number to view questions and answers, or 0 to go back to main menu"))
            if choice == 0:
                return # Return to Main Menu
            elif 1 <= choice <= len(sessions):
                current_session = sessions[choice - 1]

                # Display data of chosen session
                session_found = False
                for line in lines:
                    line = line.strip()
                    if line.startswith(f"Session Date: {current_session}"):
                        session_found = True # Flags session beginning
                    if session_found:
                        print(line) # Print subsequent lines of the chosen session
                    if line == "==== End of Session ====":
                        session_found = False # Reset flag
                        print(f"\n{line}\n")
                        break # Stop loop
            
            else:
                print("Invalid input. Please input a valid session number.")
        
        except ValueError:
            print("Invalid input. Please input a number.")
    
    else:
        print("Great. We'll return to the main menu.") # Handles if the user chooses 'no'

    