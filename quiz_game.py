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

# Function to load quiz data
def load_quiz_data(filename):
    clear_console()
    # Initialize an list to hold quiz data
    quiz_data = []
    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip() != '']
            
            i = 0
            # Loop through the lines and extract each question set
            while i < len(lines):
                # Extract question, choices, and correct answer
                if lines[i].startswith("Question #"):
                    question_text = lines[i + 1]
                    choice_a = lines[i + 2][3:]
                    choice_b = lines[i + 3][3:]
                    choice_c = lines[i + 4][3:]
                    choice_d = lines[i + 5][3:]
                    correct_answer = lines[i + 6].split(": ")[1].lower()
                    
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
                    i += 7
                    
                else:       # Skip any unrelated lines
                    i += 1
                    
        # Return the list of questions
        return quiz_data
    
    except Exception as e:
        print(Fore.RED + f"Error loading file {e}")
        return []

#Function to start quiz
def start_quiz(questions):
    # If the question list is empty, exit the Quiz
    if not questions:
        print(Fore.RED + "No questions available in the file.")
        time.sleep(2)
        return
    
    # Display welcome message
    print("\n========== Welcome to the Quiz! ==========")
    # Shuffle questions to ensure randomness
    random.shuffle(questions)
    
    # Initialize score
    score = 0
    
    # Loop through each question in the quiz
    for idx, q in enumerate(questions, 1):
        # Display question and choices
        print(f"\nQuestion {idx}: {q['question']}")
        for key, choice in q['choices'].items():
            print(f"{key}. {choice}")
            
        # Ask user for their answer and validate input
        while True:
            answer = input("\nYour Answer: ").lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print(Fore.RED + "\nInvalid answer. Try again.")
                
        # Check if the user's answer is correct
        if answer == q["correct"]:
            print(Fore.GREEN + "Correct! 🎉")
            time.sleep(1)
            clear_console()
            score += 1
            
        # Show the correct answer if the user was wrong
        else:
            correct_choice = q["choices"][q["correct"]]
            print(Fore.RED + f"Wrong! ❌ The correct answer was '{q["correct"]}': {correct_choice}")
            time.sleep(2)
            clear_console()
            
    # After the quiz, display the final score
    print(f"\n🎯 Quiz Completed! You scored {score} out of {len(questions)}.\n")
    input("Press Enter to return to main menu...")

#Main Menu Function
def main_menu():
    while True:
        clear_console()
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
                questions = load_quiz_data(filename)
                start_quiz(questions)
                
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
    main_menu()