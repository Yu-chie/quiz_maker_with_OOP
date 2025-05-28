import time
from colorama import init, Fore, Back, Style
init(autoreset=True)
from utility import clear_console

class QuizData:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        
    #Function to ask number of questions to add
    def number_of_questions(self):  
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
    def input_question_data(self, question_counter):
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

    #Function to add questions
    def add_questions(self, quiz_name):
        
        #Count how many questions already exists
        try:
            file_path = os.path.join("quizzes", f"{quiz_name}.txt")
            with open(file_path, "r") as file:
                existing_data = file.read()
                question_counter = existing_data.count("Question #") + 1
        except FileNotFoundError:
            question_counter = 1
        
        while True:
            num_question = self.number_of_questions()
            
            #Loop through each question and save it
            for i in range(num_question):
                question, choice_a, choice_b, choice_c, choice_d, correct_answer = self.input_question_data(question_counter)
                self.file_handler.save_to_file(quiz_name, question_counter, question, choice_a, choice_b, choice_c, choice_d, correct_answer)
                question_counter += 1
            
            #Ask if the user wants to continue adding questions or not
            continue_input = input(Fore.YELLOW + "\nDo you wish to add more questions (y/n): ").strip().lower()
            if continue_input != 'y':
                print(Fore.GREEN + "Returning to quiz options...")
                time.sleep(2)
                clear_console()
                break