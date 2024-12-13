#This part is the Feature selection
from question_bank import QuestionBank
# from answer_storage import AnswerStorage
from performance_analysis import PerformanceAnalysis
from customization import Customization
import utils

def main():
    question_bank = QuestionBank()
    # answer_storage = AnswerStorage()
    performance_analyzer = PerformanceAnalysis()
    customization = Customization()
    exam_taken = False

    while True:
        utils.clear_terminal()
        print("\nWelcome to the Exam Reviewer!")
        print("\nMain Menu:")
        print("1. Question Management")
        print("2. Take Exam")
        print("3. View Performance")
        print("4. Customize Settings")
        print("5. Exit\n")
        choice = input("Enter your choice: ")

        # run the question_bank module load_question function
        question_bank.load_questions()
        # run question_bank module when choice is 1
        if choice == "1":
            # run the question management function
            question_bank.question_management_menu()
        elif choice == "2":
            results = question_bank.take_exam() 
            performance_analyzer.correct_count = len([r for r in results if r['result'] == 'Correct'])
            performance_analyzer.wrong_count = len([r for r in results if r['result'] == 'Incorrect'])
            performance_analyzer.results = results
            performance_analyzer.performance_summary()  # Show performance
            exam_taken = True # Will be set to true after taking the exam          
        elif choice == "3":
            if exam_taken:
                performance_analyzer.performance_summary()
            else:
               print("\nYou need to take an exam first before viewing your performance!")
               input("Press Enter to return to the main menu...") 
        elif choice == "4":
            customization.customize_questions()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
