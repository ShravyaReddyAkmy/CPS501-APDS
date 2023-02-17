# This Program is to generate two random numbers and perform arithmetic operations based on user preferences
# Written by: Shravya Reddy Akmy
# Date: 09/13/2021

#importing python library "random"
import random

#Defining all functions
#Function to present menu and ask user to make selection
def menu():
    menu.user_selection=int(input("\n\nPlease make a selection from menu by giving option number: \n1 Addition \n2 Substraction \n3 Exit\n"))
    print("User selected:",menu.user_selection)
    return menu.user_selection

#Function to generate random numbers and perform arithmetic operations
def rand_num_add_sub():   
    
#Generating two random numbers 'num1' and 'num2' using in-built module 'random'
    rand_num_add_sub.num1=int(random.random()*10)
    print("Random number 'num1' is:",rand_num_add_sub.num1)
    rand_num_add_sub.num2=int(random.random()*10)
    print("Random number 'num2' is:",rand_num_add_sub.num2)
    
#Performing addition on generated numbers
    rand_num_add_sub.addition=rand_num_add_sub.num1+rand_num_add_sub.num2
    
#Performing substraction on generated numbers
    if (rand_num_add_sub.num2>rand_num_add_sub.num1):
            temp_num=rand_num_add_sub.num1
            rand_num_add_sub.num1=rand_num_add_sub.num2
            rand_num_add_sub.num2=temp_num
    rand_num_add_sub.substraction=rand_num_add_sub.num1-rand_num_add_sub.num2
    
    return rand_num_add_sub.num1,rand_num_add_sub.num2,rand_num_add_sub.addition,rand_num_add_sub.substraction

#Main program
user_name = input("\nHi there! Please enter your name:")
user_name=user_name.upper()
menu()
while (menu.user_selection<3):
    rand_num_add_sub()
    if (menu.user_selection==1):
        addition_by_user=int(input("\n\nPlease enter the sum of numbers 'num1' and 'num2':"))
        if addition_by_user==rand_num_add_sub.addition:
            print("\n\nBravo!",user_name,"The sum is correct.\nPlease press 'ENTER' key to continue...")
        else:
            print("\n\nOops!",user_name,".Your answer is incorrect.The correct sum is:",rand_num_add_sub.addition, "\nPlease press 'ENTER' key to continue...")
    elif (menu.user_selection==2):
        if (rand_num_add_sub.num1==rand_num_add_sub.num2):
            print("\n\nBoth numbers 'num1' and 'num2' are the same and the difference of numbers is 0.\nPlease press 'ENTER' key to continue...")
        else:
            substraction_by_user=int(input("\n\nPlease enter the difference of numbers 'num1' and 'num2':"))
            if substraction_by_user==rand_num_add_sub.substraction:
                print("\n\nBravo!",user_name,".The differnce is correct.\nPlease press 'ENTER' key to continue...")
            else:
                print("\n\nOops!",user_name,".Your answer is incorrect. \nThe correct difference is:",rand_num_add_sub.substraction, "\nPlease press 'ENTER' key to continue...")
    input()
    menu()
    
print("\n\nExiting the program")

# **************** END OF THE CODE*********************
    

    
    