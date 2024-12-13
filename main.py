#This part is the Feature selection
from question_bank import QuestionBank
# from answer_storage import AnswerStorage
from performance_analysis import PerformanceAnalysis
from customization import Customization
import answer_storage as ans
import utils as u

def main():
    question_bank = QuestionBank()
    # answer_storage = AnswerStorage()
    performance_analyzer = PerformanceAnalysis()
    customization = Customization()
    exam_taken = False

    while True:
        u.clear_terminal()
        print("\nWelcome to the Exam Reviewer!")
        print("\nMain Menu:")
        print("1. Question Management")
        print("2. Take Exam")
        print("3. View Performance")
        print("4. Customize Settings")
        print("5. Review Previous Study Sessions")
        print("6. Exit\n")
        choice = input("Enter your choice: ")

        # run question_bank module when choice is 1
        if choice == "1":
            question_bank.question_management_menu()
                                
        elif choice == "2":
            results = question_bank.take_exam()
            
            #  ask the user if they want to save the results of their current review
            save_results = input('\nDo you want to save the results of this review? (y or n only): ')
            
            while True:
                if save_results.lower() == 'y':
                    ans.save_answers(question_bank.user_answers,u.answer_storage_file_path)
                    print(f'\nAnswers are now saved in {u.answer_storage_file_path} file.')
                    input('\nPress Enter to continue...')
                    break
                elif save_results.lower() == 'n':
                    print(f'\nAnswers will not be saved!')
                    input('\nPress Enter to continue...')
                    break
                else:
                    print(f'\nInvalid Input. Please Enter Y or N only')


            # performance_analyzer.correct_count = len([r for r in results if r['result'] == 'Correct'])
            # performance_analyzer.wrong_count = len([r for r in results if r['result'] == 'Incorrect'])
            # performance_analyzer.results = results
            # performance_analyzer.performance_summary()  # Show performance
            # exam_taken = True # Will be set to true after taking the exam          

        elif choice == "3":
            if exam_taken:
                performance_analyzer.performance_summary()
            else:
               print("\nYou need to take an exam first before viewing your performance!")
               input("Press Enter to return to the main menu...") 
        elif choice == "4":
            customization.customize_questions()
        elif choice == "5":
            answer_storage.retrieve_answers(u.answer_storage_file_path)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
