#Create the Quiz program that read the output file of the Quiz Creator. 
#The user will answer the randomly selected question and check if the answer is correct.

# Import libraries
import os
import time
import random
from colorama import init, Style, Fore

# Initialize colorama
init(autoreset=True)

#Function to clear console
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

class QuizLoader:
    # Function to load quiz data
    def load_quiz_data(self, filename):
        clear_console()
        # Initialize an list to hold quiz data
        quiz_data = []
        try:
            # Open the file in read mode
            with open(filename, "r") as file:
                lines = [line.strip() for line in file if line.strip() != '']
                
                index = 0
                # Loop through the lines and extract each question set
                while index < len(lines):
                    # Extract question, choices, and correct answer
                    if lines[index].startswith("Question #"):
                        question_text = lines[index + 1]
                        choice_a = lines[index + 2][3:]
                        choice_b = lines[index + 3][3:]
                        choice_c = lines[index + 4][3:]
                        choice_d = lines[index + 5][3:]
                        correct_answer = lines[index + 6].split(": ")[1].lower()
                        
                        # Store the full question as a dictionary
                        quiz_data.append({
                            "question": question_text, 
                            "choices": {
                                "a": choice_a, 
                                "b": choice_b, 
                                "c": choice_c, 
                                "d": choice_d
                            },
                            "correct": correct_answer
                        })
                        
                        # Move index to the next question
                        index += 7
                        
                    else:       # Skip any unrelated lines
                        index += 1
                        
            # Return the list of questions
            return quiz_data
        
        except Exception as e:
            print(Fore.RED + f"Error loading file {e}")
            return []

class PlayQuiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        
    #Function to start quiz
    def start_quiz(self):
        # If the question list is empty, exit the Quiz
        if not self.questions:
            print(Fore.RED + "No questions available in the file.")
            time.sleep(2)
            return
        
        # Display welcome message
        print("\n========== Welcome to the Quiz! ==========")
        
        # Shuffle questions to ensure randomness
        random.shuffle(self.questions)
        
        # Loop through each question in the quiz
        for question_index, question_item in enumerate(self.questions, 1):
            # Display question and choices
            print(f"\nQuestion {question_index}: {question_item['question']}")
            for choice_key, choice_text in question_item['choices'].items():
                print(f"{choice_key}. {choice_text}")
                
            # Ask user for their answer and validate input
            while True:
                answer = input("\nYour Answer: ").lower()
                if answer in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print(Fore.RED + "\nInvalid answer. Try again.")
                    
            # Check if the user's answer is correct
            if answer == question_item["correct"]:
                print(Fore.GREEN + "Correct! 🎉")
                time.sleep(1)
                clear_console()
                self.score += 1
                
            # Show the correct answer if the user was wrong
            else:
                correct_choice = question_item["choices"][question_item["correct"]]
                print( Fore.RED + f"Wrong! ❌ The correct answer was '{question_item['correct']}': {correct_choice}")
                time.sleep(2)
                clear_console()
                
        # After the quiz, display the final score
        message = f"\n🎯 Quiz Completed! You scored {self.score} out of {len(self.questions)}.\n"
        for char in message:
            print(Fore.CYAN + char, end='', flush=True)
            time.sleep(0.05)

        input("\nPress Enter to return to main menu...")

class QuizPlayer:
    def __init__(self):
        self.loader = QuizLoader() 
    
    #Main Menu Function
    def main_menu(self):
        while True:
            clear_console()
            
            # List existing quizzes
            quiz_files = [file for file in os.listdir() if file.endswith(".txt")]

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
                    
                # If the file exists, load questions and start quiz
                if os.path.exists(filename):
                    questions = self.loader.load_quiz_data(filename)
                    game = PlayQuiz(questions)
                    game.start_quiz()    
                # If the file is not found, show error
                else:
                    print(Fore.RED + f"\nFile '{filename}' not found")
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

#Run the Program
if __name__ == "__main__":
    app = QuizPlayer()
    app.main_menu()