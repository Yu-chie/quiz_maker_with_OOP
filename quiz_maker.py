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

    #Ask user for a question

    #Ask user for choices
    
    #Ask user for correct answer, must be in [a, b, c, d] 

#Function to save quiz data to file

#Main Function
def main():
    print("===== Quiz Maker =====")
    
    #Open a file in append mode to save data
    file = open("quiz_data.txt", "a")
    
        #Loop through each question and save it
                
        #Ask if the user wants to continue adding questions or not

    #Close File
    file.close()
#Run program
if __name__ == "__main__":
    main()