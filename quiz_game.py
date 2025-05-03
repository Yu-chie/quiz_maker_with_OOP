#Create the Quiz program that read the output file of the Quiz Creator. 
#The user will answer the randomly selected question and check if the answer is correct.

# Import libraries
import os
import time
import random
from colorama import init, Style, Fore

# Function to load quiz data
    # Initialize an list to hold quiz data
    # Open the file in read mode
    # Loop through the lines and extract each question set
        # Extract question, choices, and correct answer
        # Store the full question as a dictionary
    # Move index to the next question
    # Skip any unrelated lines
    # Return the list of questions

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