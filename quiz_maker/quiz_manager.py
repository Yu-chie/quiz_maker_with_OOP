import time
import os
from utility import clear_console
from file_handler import FileHandler
from quiz_data import QuizData
from colorama import init, Fore, Back, Style
init(autoreset=True)

class QuizManager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.quiz_data = QuizData(self.file_handler)
        
    #Function to create quiz file
    def create_quiz(self):
        while True:
            quiz_name = input(Fore.GREEN + "\nEnter the name of your new quiz: ").strip()
            file_path = os.path.join("quizzes", f"{quiz_name}.txt")
            if os.path.exists(file_path):
                print(Fore.RED + "A quiz with this name already exists. Choose another name.")
            else:
                print(Fore.GREEN + f"Creating new quiz: {quiz_name}")
                self.quiz_option(quiz_name)
                break
            
    # Function to edit an existing quiz
    def edit_quiz(self):
        quiz_name = input(Fore.GREEN + "\nEnter the name of the quiz to edit: ").strip()
        file_path = os.path.join("quizzes", f"{quiz_name}.txt")
        if os.path.exists(file_path):
            self.quiz_option(quiz_name)
        else:
            print(Fore.RED + f"No quiz found with the name {quiz_name}.")
            time.sleep(2)

    # Function to delete an existing quiz
    def delete_quiz(self):
        quiz_name = input(Fore.GREEN + "\nEnter the name of the quiz to delete: ").strip()
        file_path = os.path.join("quizzes", f"{quiz_name}.txt")
        if os.path.exists(file_path):
            os.remove(file_path)
            print(Fore.GREEN + f"Quiz {quiz_name} has been deleted.")
            time.sleep(2)
        else:
            print(Fore.RED + f"No quiz found with the name {quiz_name}.")    
    
    #Quiz Option Function
    def quiz_option(self, quiz_name):
        clear_console()
        while True:
            print(Fore.CYAN + Style.BRIGHT + f"\n========== Quiz Option for {quiz_name} ==========")
            print(Fore.GREEN + Style.BRIGHT + "1. " + Style.RESET_ALL + "Add Questions")
            print(Fore.GREEN + Style.BRIGHT + "2. " + Style.RESET_ALL + "View Questions")
            print(Fore.GREEN + Style.BRIGHT + "3. " + Style.RESET_ALL + "Delete Questions")
            print(Fore.GREEN + Style.BRIGHT + "4. " + Style.RESET_ALL + "Exit")
            print(Fore.CYAN + Style.BRIGHT + "================================")

            try:
                choice = int(input("Enter choice (1-4): "))
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
                time.sleep(1)
                continue
            
            if choice == 1:
                self.quiz_data.add_questions(quiz_name)
            elif choice == 2:
                self.file_handler.view_questions(quiz_name)
            elif choice == 3:
                self.file_handler.delete_question(quiz_name)
            elif choice == 4:
                print("Going back...")
                time.sleep(1)
                break
            else:
                print(Fore.RED + "Invalid choice. Please select a valid option.")
                time.sleep(1)

    #Main Function
    def main_menu(self):
        clear_console()
        while True:
            # List existing quizzes
            quiz_folder = "quizzes"
            if not os.path.exists(quiz_folder):
                os.makedirs(quiz_folder)
            quiz_files = [file for file in os.listdir(quiz_folder) if file.endswith(".txt")]

            print(Fore.MAGENTA + Style.BRIGHT + "\n======= Existing Quizzes =======")
            if quiz_files:
                for quiz in quiz_files:
                    print(Fore.YELLOW + f"- {quiz[:-4]}")
            else:
                print(Fore.RED + "No quizzes found.")
            print(Fore.MAGENTA + Style.BRIGHT + "===============================")

            print(Fore.CYAN + Style.BRIGHT + "\n========== Quiz Maker ==========")
            print(Fore.GREEN + Style.BRIGHT + "1. " + Style.RESET_ALL + "Create Quiz")
            print(Fore.GREEN + Style.BRIGHT + "2. " + Style.RESET_ALL + "Edit Quiz")
            print(Fore.GREEN + Style.BRIGHT + "3. " + Style.RESET_ALL + "Delete Quiz")
            print(Fore.GREEN + Style.BRIGHT + "4. " + Style.RESET_ALL + "Exit")
            print(Fore.CYAN + Style.BRIGHT + "================================")

            try:
                option = int(input("Choose an option (1-4): "))
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
                time.sleep(1)
                continue
            
            if option == 1:
                self.create_quiz()
            elif option == 2:
                self.edit_quiz()
            elif option == 3:
                self.delete_quiz()
            elif option == 4:
                print("Exiting program...")
                time.sleep(1)
                break
            else:
                print(Fore.RED + "Invalid option. Please select a valid option.")
                time.sleep(1)