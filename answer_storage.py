#Answer Storage
#Jerry Luis
#Ellen Dee

import os
import datetime

class AnswerStorage:
    def __init__(self):
        self.answers = {}  # Store user answers, key=question ID and value=answer
        self.file_name = "answer_storage.txt"

    def save_answers(self):
        session_date = datetime.datetime.now().strftime("%Y-%m-%d")

        formatted_ans = []

        # Format answers in list
        for q_id, answer_data in self.answers.items():
            correctness = "correct" if answer_data["correct"] else "incorrect"
            formatted_ans.append(f"{q_id}: {answer_data['answer']}: {correctness}")

        # Save study session and include formatted_ans
        study_session = session_date + " : " + ", ".join(formatted_ans) + "\n"

        # Append on file the study session info
        with open(self.file_name, "a") as file:
            file.write(study_session)

    def retrieve_answers(self):
        review_session = input("Do you want to review previous study sessions? Type 'yes' or 'no.'")

        if review_session.lower() == "yes":
            # Check first if file exists
            if not os.path.exists(self.file_name):
                print("No study sessions available yet.")

            sessions = []  # List of all session dates available

            # Read through file containing sessions
            with open(self.file_name, "r") as file:
                for line in file:
                    session_date = line.split(":")[0]
                    sessions.append(session_date)

                print("Available sessions: ")
                print(sessions)

                # Ask what session to retrieve answers from
                session_choice = input("Please choose a session date: ")

                # Find session in file
                session_found = False
                with open(self.file_name, "r") as file:
                    for line in file:
                        if line.startswith(session_choice):
                            session_found = True
                            # Get study session info of session date chosen
                            session_info = line.split(":")[1].strip()

                            session_answers = {}
                            # Iterate through every question
                            for item in session_info.split(","):
                                q_id, answer, correctness = item.split(":")
                                session_answers[q_id] = {'answer': answer.strip(), 'correct': correctness.strip() == 'correct'}

                            print(f"Answers for session {session_choice}: {session_answers}")
                            return session_answers

                if not session_found:
                    print(f"Session {session_choice} not found.")
                    return None

        else:
            print("Got it. Choose from the main menu again.")
            return None