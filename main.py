'''
This is the main module for the program that connects all the other modules

'''

#This part is the Feature selection
from question_bank import QuestionBank
from performance_analysis import PerformanceAnalysis
import answer_storage as ans
import utils as u

def main():
    question_bank = QuestionBank()
    performance_analyzer = PerformanceAnalysis()

    while True:
        # display selection menu
        u.clear_terminal()
        print("\nWelcome to the Exam Reviewer!")
        print("\nMain Menu:")
        print("(1) Question Management")
        print("(2) Take Exam")
        print("(3) View Historical Performance")
        print("(4) Exit\n")
        choice = input("Enter (number) of your choice: ")

        # run question_bank module when choice is 1
        if choice == "1":
            question_bank.question_management_menu()
                                
        elif choice == "2":
            # results = question_bank.take_exam()
            question_bank.take_exam()
            
            # clears the screen for readability
            u.clear_terminal()
            
            # call the performance analyzer for better display of results
            performance_analyzer.performance_summary(question_bank.user_answers)
            
            #  ask the user if they want to save the results of their current review
            save_results = input('\nDo you want to save the results of this review? (y or n only): ')
            
            # process user input on saving of results
            while True:
                if save_results.lower() == 'y':
                    ans.save_answers(question_bank.user_answers)
                    print(f'\nAnswers are now saved in {u.answer_storage_file_path} file.')
                    input('\nPress Enter to continue...')
                    break
                elif save_results.lower() == 'n':
                    print(f'\nAnswers will not be saved!')
                    input('\nPress Enter to continue...')
                    break
                else:
                    print(f'\nInvalid Input. Please Enter Y or N only')

        elif choice == "3":
            u.clear_terminal()
            # import the retrieve answers function from the answer storage module
            results = ans.retrieve_answers(u.answer_storage_file_path)
            
            # clear terminal for readability and then display the results
            u.clear_terminal()
            performance_analyzer.performance_summary(results)
            
            input("\nPress Enter to return to the main menu...") 
            
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
            input()

if __name__ == "__main__":
    main()
