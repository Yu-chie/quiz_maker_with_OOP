import os
from colorama import Fore
from utility import clear_console

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