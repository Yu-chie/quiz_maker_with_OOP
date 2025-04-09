#Create a program that ask user for a question.
#It will also ask for 4 possible answer and the correct answer.
#Write the collected data to a text file.
#Ask another question until the user chose to exit

#Function to ask number of questions to add
def number_of_questions():
    while True:
        try:
            num_questions = int(input("How many questions do you wish to add: "))
            if num_questions <= 0:
                print("Enter another number")
                continue
            return num_questions
        except ValueError:
            print("Invalid input. Enter a number")

#Function to ask for a single question and its options
def question_data(question_counter):
    print(f"\nQuestion #{question_counter}")
    
    #Ask user for a question
    question = input("Enter your question: ")
    
    #Ask user for choices
    print("\nEnter 4 choices")
    choice_a = input("a. ")
    choice_b = input("b. ")
    choice_c = input("c. ")
    choice_d = input("d. ")
    
    #Ask user for correct answer, must be in [a, b, c, d] 
    while True:
        correct_answer = input("\nEnter correct answer: ")
        if correct_answer in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Please enter a valid answer (a, b, c, d)")

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
                print("\n===== Questions =====")
                print(content)
            else:
                print("No questions available.")
    except FileNotFoundError:
        print("No quiz data file found.")
        
#Function to delete question data
def delete_question():
    confirm = input("Are you sure you want to delete all questions? (y/n): ").lower()
    if confirm == 'y':
        with open('quiz_data.txt', 'w') as file:
            file.truncate(0)
        print("\nAll questions have been deleted.")
    else:
        print("No questions to delete.")
                    
#Function to add questions
def add_questions():
        
    #Open a file in append mode to save data
    file = open("quiz_data.txt", "a")
    
    question_counter = 1
    
    while True:
        num_question = number_of_questions()
        
        #Loop through each question and save it
        for i in range(num_question):
            question, choice_a, choice_b, choice_c, choice_d, correct_answer = question_data(question_counter)
            save_to_file(file, question_counter, question, choice_a, choice_b, choice_c, choice_d, correct_answer) 
            question_counter += 1
        
        #Ask if the user wants to continue adding questions or not
        continue_input = input("\nDo you wish to add more questions (y/n): ").strip().lower()
        if continue_input != 'y':
            print("Returning to main menu...")
            break
                
    #Close File
    file.close()

#Main menu Function
def main_menu():
    while True:
        print("\n===== Quiz Maker =====")
        print("1. Add Questions")
        print("2. View Questions")
        print("3. Delete a Question")
        print("4. Exit")

        choice = int(input("Choose an option (1-4): "))
        
        if choice == 1:
            add_questions()
        elif choice == 2:
            view_questions()
        elif choice == 3:
            delete_question()
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

#Run program
if __name__ == "__main__":
    main_menu()