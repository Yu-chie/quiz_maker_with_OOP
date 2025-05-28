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