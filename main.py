#This part is the Feature selection
from question_bank import QuestionBank
from answer_storage import AnswerStorage
from performance_analysis import PerformanceAnalysis
from customization import Customization

def main():
    question_bank = QuestionBank()
    answer_storage = AnswerStorage()
    performance_analysis = PerformanceAnalysis(answer_storage)
    customization = Customization(question_bank)

    while True:
        print("\nWelcome to the Exam Reviewer!")
        print("\nMain Menu:")
        print("1. Review Questions")
        print("2. Take Exam")
        print("3. View Performance")
        print("4. Customize Settings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            question_bank.review_questions()
        elif choice == "2":
            question_bank.take_exam(answer_storage)
        elif choice == "3":
            performance_analysis.display_performance()
        elif choice == "4":
            customization.customize_questions()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
