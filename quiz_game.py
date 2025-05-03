#Create the Quiz program that read the output file of the Quiz Creator. 
#The user will answer the randomly selected question and check if the answer is correct.

# Import libraries
import os
import time
import random
from colorama import init, Style, Fore

# Function to load quiz data
def load_quiz_data(filename):
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
                            choice_a, 
                            choice_b, 
                            choice_c, 
                            choice_d
                        }
                        "correct": correct_answer
                    })
                    
                    # Move index to the next question
                    i += 7
                    
                else:       # Skip any unrelated lines
                    i += 1
                    
        # Return the list of questions
        return quiz_data
    
    except Exception as e:
        print(f"Error loading file {e}")
        return []

#Function to start quiz
    # If the question list is empty, exit the Quiz
    # Display welcome message
    # Shuffle questions to ensure randomness
    # Initialize score
    # Loop through each question in the quiz
        # Display question and choices
        # Ask user for their answer and validate input
        # Check if the user's answer is correct
        # Show the correct answer if the user was wrong
    # After the quiz, display the final score

#Main Menu Function
def main_menu():
    while True:
        # Display the menu options
        print("\n========= QUIZ PLAYER =========")
        print("1." + " Start Quiz")
        print("2." + " Exit")
        print("===============================")
        
        # Get user input for their menu choice
        choice = input("\nEnter your choice: ").strip()
        
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
                print(f"\nFile '{filename}' not found")
                time.sleep(2)
                
        # If user chooses to exit
        elif choice == 2:
            print("\nGoodbye! 👋")
            time.sleep(1)
            break
        
        # If user enters invalid option
        else:
            print("Invalid choice. Please enter 1 or 2.")
            time.sleep(1)

#Run the Program
if __name__ == "__main__":
    main_menu()