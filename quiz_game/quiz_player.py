import os
import time
from colorama import init, Fore, Style
from quiz_loader import QuizLoader
from play_quiz import PlayQuiz
from utility import clear_console

# Initialize colorama
init(autoreset=True)

class QuizPlayer:
    def __init__(self):
        self.loader = QuizLoader() 
        self.quiz_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'quizzes')
    
    #Main Menu Function
    def main_menu(self):
        while True:
            clear_console()
            
            # List existing quizzes in folder
            quiz_files = [file for file in os.listdir(self.quiz_folder) if file.endswith(".txt")]

            print(Fore.MAGENTA + Style.BRIGHT + "\n======= Existing Quizzes =======")
            if quiz_files:
                for quiz in quiz_files:
                    print(Fore.YELLOW + f"- {quiz[:-4]}")
            else:
                print(Fore.RED + "No quizzes found.")
            print(Fore.MAGENTA + Style.BRIGHT + "===============================")
            
            # Display the menu options
            print(Fore.CYAN + Style.BRIGHT + "\n========= QUIZ PLAYER =========")
            print(Fore.GREEN + Style.BRIGHT +"1." + Style.RESET_ALL + " Start Quiz")
            print(Fore.GREEN + Style.BRIGHT +"2." + Style.RESET_ALL + " Exit")
            print(Fore.CYAN + Style.BRIGHT + "===============================")
            
            # Get user input for their menu choice
            try:
                choice = int(input("Enter your choice: ").strip())
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number (1 or 2).")
                time.sleep(1)
                continue
            
            # If user chooses to start the quiz
            if choice == 1:
                # Ask for filename and ensure it ends with ".txt"
                filename = input("\nEnter quiz filename: ").strip()
                if not filename.endswith(".txt"):
                    filename += ".txt"
                
                full_path = os.path.join(self.quiz_folder, filename)
                
                # If the file exists, load questions and start quiz
                if os.path.exists(full_path):
                    questions = self.loader.load_quiz_data(full_path)
                    game = PlayQuiz(questions)
                    game.start_quiz()   
                # If the file is not found, show error
                else:
                    print(Fore.RED + f"\nFile '{filename}' not found in quiz folder")
                    time.sleep(2)
                    
            # If user chooses to exit
            elif choice == 2:
                print(Fore.GREEN + "\nGoodbye! 👋")
                time.sleep(1)
                break
            
            # If user enters invalid option
            else:
                print(Fore.RED + "Invalid choice. Please enter 1 or 2.")
                time.sleep(1)