#Create a program that ask user for a question.
#It will also ask for 4 possible answer and the correct answer.
#Write the collected data to a text file.
#Ask another question until the user chose to exit

import time
import os
from colorama import init, Fore, Back, Style
init(autoreset=True)

#Function to clear console
def clear_console():     
    os.system("cls" if os.name == "nt" else "clear")

#Function to ask number of questions to add
def number_of_questions():  
    while True:
        try:
            num_questions = int(input(Fore.CYAN + "\nHow many questions do you wish to add: "))
            if num_questions <= 0:
                print(Fore.RED + "Enter another number")
                continue
            return num_questions
        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number")

#Function to ask for a single question and its options
def question_data(question_counter):
    print(Fore.CYAN + Style.BRIGHT + f"\nQuestion #{question_counter}")
    
    #Ask user for a question
    question = input(Fore.GREEN + "Enter your question: " + Style.RESET_ALL)
    
    #Ask user for choices
    print(Fore.GREEN + "\nEnter 4 choices")
    choice_a = input("a. ")
    choice_b = input("b. ")
    choice_c = input("c. ")
    choice_d = input("d. ")
    
    #Ask user for correct answer, must be in [a, b, c, d] 
    while True:
        correct_answer = input(Fore.GREEN + "\nEnter correct answer: " + Style.RESET_ALL)
        if correct_answer in ['a', 'b', 'c', 'd']:
            break
        else:
            print(Fore.RED + "Please enter a valid answer (a, b, c, d)")

    return question, choice_a, choice_b, choice_c, choice_d, correct_answer

#Function to save quiz data to file
def save_to_file(file, question_counter, question, choice_a, choice_b, choice_c, choice_d, correct_answer):
    file.write(f"\nQuestion #{question_counter}")
    file.write(f"\n{question}")
    file.write(f"\na. {choice_a}")
    file.write(f"\nb. {choice_b}")
    file.write(f"\nc. {choice_c}")
    file.write(f"\nd. {choice_d}")
    file.write(f"\nCorrect Answer: {correct_answer}\n")

#Function to view question data
def view_questions():
    try:
        with open("quiz_data.txt", "r") as file:
            content = file.read()
            if content:
                print(Fore.MAGENTA + Style.BRIGHT + "\n========== Questions ==========")
                print(content)
                print(Fore.MAGENTA + Style.BRIGHT + "\n===============================")
            else:
                print(Fore.RED + "No questions available.")
    except FileNotFoundError:
        print(Fore.RED + "No quiz data file found.")
        
#Function to delete question data
def delete_question():
    confirm = input(Fore.RED + "Are you sure you want to delete all questions? (y/n): ").lower()
    if confirm == 'y':
        with open('quiz_data.txt', 'w') as file:
            file.truncate(0)
        print(Fore.GREEN + "\nAll questions have been deleted.")
        time.sleep(2)
    else:
        print(Fore.YELLOW + "No questions to delete.")
        time.sleep(2)
                    
#Function to add questions
def add_questions():
    
    #Count how many questions already exists
    try:
        with open("quiz_data.txt", "r") as file:
            existing_data = file.read()
            question_counter = existing_data.count("Question #") + 1
    except FileNotFoundError:
        question_counter = 1
    
    #Open a file in append mode to save data
    file = open("quiz_data.txt", "a")
      
    while True:
        num_question = number_of_questions()
        
        #Loop through each question and save it
        for i in range(num_question):
            question, choice_a, choice_b, choice_c, choice_d, correct_answer = question_data(question_counter)
            save_to_file(file, question_counter, question, choice_a, choice_b, choice_c, choice_d, correct_answer) 
            question_counter += 1
        
        #Ask if the user wants to continue adding questions or not
        continue_input = input(Fore.YELLOW + "\nDo you wish to add more questions (y/n): ").strip().lower()
        if continue_input != 'y':
            print(Fore.GREEN + "Returning to main menu...")
            time.sleep(2)
            clear_console()
            break
                
    #Close File
    file.close()

#Quiz Option Function
def quiz_option():
    clear_console()
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n========== Quiz Maker ==========")
        print(Fore.GREEN + Style.BRIGHT + "1. " + Style.RESET_ALL + "Add Questions")
        print(Fore.GREEN + Style.BRIGHT + "2. " + Style.RESET_ALL + "View Questions")
        print(Fore.GREEN + Style.BRIGHT + "3. " + Style.RESET_ALL + "Delete Questions")
        print(Fore.GREEN + Style.BRIGHT + "4. " + Style.RESET_ALL + "Exit")
        print(Fore.CYAN + Style.BRIGHT + "================================")

        choice = int(input("Choose an option (1-4): "))
        
        if choice == 1:
            add_questions()
        elif choice == 2:
            view_questions()
        elif choice == 3:
            delete_question()
        elif choice == 4:
            print("Exiting program...")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")
            time.sleep(1)

#Function to create quiz file
def create_quiz():
    while True:
        quiz_name = input(Fore.GREEN + "\nEnter the name of your new quiz: ").strip()
        if os.path.exists(f"{quiz_name}.txt"):
            print(Fore.RED + "A quiz with this name already exists. Choose another name.")
        else:
            print(Fore.GREEN + f"Creating new quiz: {quiz_name}")
            quiz_option(quiz_name)
            break



#Main Function
def main_menu():
    clear_console()
    while True:
        # List existing quizzes
        quiz_files = [file for file in os.listdir() if file.endswith(".txt")]

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
            create_quiz()
        elif option == 2:
            edit_quiz()
        elif option == 3:
            delete_quiz()
        elif option == 4:
            print("Exiting program...")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "Invalid option. Please select a valid option.")
            time.sleep(1)

#Run program
if __name__ == "__main__":
    main_menu()