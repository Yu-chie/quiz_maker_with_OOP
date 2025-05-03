#Create the Quiz program that read the output file of the Quiz Creator. 
#The user will answer the randomly selected question and check if the answer is correct.

# Import libraries

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
    # Display the menu options
    # Get user input for their menu choice
    # If user chooses to start the quiz
        # Ask for filename and ensure it ends with ".txt"
        # If the file exists, load questions and start quiz
        # If the file is not found, show error
    # If user chooses to exit
    # If user enters invalid option

#Run the Program