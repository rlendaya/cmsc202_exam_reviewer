#This part is the Feature selection
from question_bank import QuestionBank
# from answer_storage import AnswerStorage
# from performance_analysis import PerformanceAnalysis
# from customization import Customization

def main():
    question_bank = QuestionBank()
    # answer_storage = AnswerStorage()
    # performance_analysis = PerformanceAnalysis(answer_storage)
    # customization = Customization(question_bank)

    while True:
        question_bank.clear_terminal()
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
            question_bank.take_exam()
            # question_bank.take_exam(answer_storage)
        # elif choice == "3":
        #     performance_analysis.display_performance()
        # elif choice == "4":
        #     customization.customize_questions()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
