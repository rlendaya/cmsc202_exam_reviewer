#Customization Options
#Richmond
#Stella
#Roda

'''




'''

class Customization:
    def __init__(self):
        self.time_limit = None

    def customize_questions(self):
        while True:
            print("\nCustomization Menu:")
            print("1. Set Time Limit for Review Sessions")
            print("2. View Current Customization Settings")
            print("3. Return to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.set_time_limit()
            elif choice == "2":
                self.view_customizations()
            elif choice == "3":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def set_time_limit(self):
        try:
            time = int(input("Enter the time limit for review sessions (in minutes): "))
            if time > 0:
                self.time_limit = time
                print(f"Time limit set to {self.time_limit} minutes.")
            else:
                print("Time limit must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def view_customizations(self):
        print("\nCurrent Customization Settings:")
        print(f"Time Limit: {self.time_limit} minutes" if self.time_limit else "Time Limit: None")

    def get_time_limit(self):
        return self.time_limit
