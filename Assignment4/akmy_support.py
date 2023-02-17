# Program to create methods to output print statements based on user calculations
# Module: akmy_support Method: user_display
# Written by: Shravya Reddy Akmy

# Function to display output print statements based on user calculations
def user_display(count_correct,count_incorrect,user_choice,addition,substraction,multiplication,division):
    if count_correct>0:
        print("\nExcellent! Your answer is correct")
    else:
        if count_incorrect==1:
            print("\nOops! Your answer is wrong.Please try again..")
        else:
            if user_choice==1:
                print("\nSorry! Wrong again.The correct answer =",addition)
            elif user_choice==2:
                print("\nSorry! Wrong again.The correct answer =",substraction)
            elif user_choice==3:
                print("\nSorry! Wrong again.The correct answer =",multiplication)
            elif user_choice==4:
                print("\nSorry! Wrong again.The correct answer =",division)
