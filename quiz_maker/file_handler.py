import time
import os
from colorama import init, Fore, Back, Style
init(autoreset=True)

class FileHandler:
    def __init__(self):
        self.folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'quizzez'))
        os.makedirs(self.folder, exist_ok=True)
        
    #Function to save quiz data to file
    def save_to_file(self, quiz_name, question_counter, question, choice_a, choice_b, choice_c, choice_d, correct_answer):
        file_path = os.path.join(self.folder, f"{quiz_name}.txt")
        with open(file_path, "a") as file:
            file.write(f"\nQuestion #{question_counter}")
            file.write(f"\n{question}")
            file.write(f"\na. {choice_a}")
            file.write(f"\nb. {choice_b}")
            file.write(f"\nc. {choice_c}")
            file.write(f"\nd. {choice_d}")
            file.write(f"\nCorrect Answer: {correct_answer}\n")

    #Function to view question data
    def view_questions(self, quiz_name):
        file_path = os.path.join(self.folder, f"{quiz_name}.txt")
        try:
            with open(file_path, "r") as file:
                content = file.read()
                if content:
                    print(Fore.MAGENTA + Style.BRIGHT + "\n========== Questions ==========")
                    print(content)
                    print(Fore.MAGENTA + Style.BRIGHT + "===============================")
                else:
                    print(Fore.RED + "No questions available.")
        except FileNotFoundError:
            print(Fore.RED + "No quiz data file found.")
            
    #Function to delete question data
    def delete_question(self, quiz_name):
        file_path = os.path.join(self.folder, f"{quiz_name}.txt")
        confirm = input(Fore.RED + "Are you sure you want to delete all questions? (y/n): ").lower()
        if confirm == 'y':
            with open(file_path, 'w') as file:
                file.truncate(0)
            print(Fore.GREEN + "\nAll questions have been deleted.")
            time.sleep(2)
        else:
            print(Fore.YELLOW + "No questions to delete.")
            time.sleep(2)