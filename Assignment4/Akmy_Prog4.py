# This program is to perform arithmatic operations with single/double/triple digits based on user preferences .
# Written by: Shravya Reddy Akmy
# Date: 10/20/2021

import random #Python in-built module to generate random numbers
import akmy_support #User defined module to display print statements

#Function to present menu and ask user to make selection
def user_menu():
    choice=int(input("\nWhich arithmetic operation would you like to perform? \n1-Addition \n2-Substraction \n3-Multiplication \n4-Division \n5-Exit \nPlease enter your choice:"))
    return choice

#FUnction to generate random numbers based on user preferences
def rand_num_gen(no_of_digits):
    if no_of_digits==1:
        num1=int(random.random()*10)
        num2=int(random.random()*10)
    elif no_of_digits==2:
        num1=random.randint(10,99)
        num2=random.randint(10,99)
    elif no_of_digits==3:
        num1=random.randint(100,999)
        num2=random.randint(100,999)
    if num2>num1:
        temp_num=num1
        num1=num2
        num2=temp_num
    return num1,num2

#Function to calculte arithmetic operations on generated numbers
def arithmetic_cal(num1,num2):
    addition=num1+num2
    substraction=num1-num2
    multiplication=num1*num2
    if num2!=0:
        division=round(num1/num2,2)
    else:
        division='Not possible'
    return addition,substraction,multiplication,division

#Function to ask user to make calculations and display output based on responses
def user_cal(user_choice,digits,operations):
    trial_responses={}
    count_incorrect=0
    for oper in range(0,operations):
        count_correct=0
        print("\nPerforming the operation trial-",str(oper+1))
        num1,num2=rand_num_gen(digits)
        addition,substraction,multiplication,division=arithmetic_cal(num1,num2)
        print("Number-1 = "+str(num1),"   Number-2 = "+str(num2))
        if user_choice==1:
            user_add=int(input("\nPlease enter the addition of numbers:"))
            if user_add==addition:
                count_correct=count_correct+1
            else:
                count_incorrect=count_incorrect+1  
        elif user_choice==2:
            user_sub=int(input("\nPlease enter the substraction of numbers:"))
            if user_sub==substraction:
                count_correct=count_correct+1
            else:
                count_incorrect=count_incorrect+1
        elif user_choice==3:
            user_mult=int(input("\nPlease enter the multiplication of numbers:"))
            if user_mult==multiplication:
                count_correct=count_correct+1
            else:
                count_incorrect=count_incorrect+1
        elif user_choice==4:
            if num2==0:
                print("Divison by zero not allowed so, considering this operation as correct response")
                count_correct=count_correct+1
            else:
                user_div=float(input("\nPlease enter the division of numbers \n(give upto 4 decimals if applicable and for recurring decimals give upto 2 decimals with second decimal increased by 1):")) 
                user_div=round(user_div,2)
                if user_div==division:
                    count_correct=count_correct+1
                else:
                    count_incorrect=count_incorrect+1
        akmy_support.user_display(count_correct,count_incorrect,user_choice,addition,substraction,multiplication,division)
        trial_responses[oper]=[count_correct]
    return trial_responses,count_incorrect

#Main program        
def main():
    data_track=[] # List to keep track of arithmetic operation,no.of operations,correct responses,incorrect responses
    total_correct_responses=0 # Initiating variable to count total correct responses
    menu={'1':'Addition','2':'Substraction','3':'Multiplication','4':'Division'}
    user_choice=user_menu()
    if user_choice==5:
        print("\nThankyou ! Exiting the code\n")
    else:
        data_track.append(menu[str(user_choice)])
        no_of_digits=int(input("\nHow many digits operation would you like to perform? \n1-Single digit \n2-Double digits \n3-Triple didgit \nPlease select:"))
        no_of_operations=int(input("\nHow many times would you like to perform the arithmetic operation? Please enter a number greater than 0:"))
        data_track.append(no_of_operations)
        correct_responses,incorrect_responses=user_cal(user_choice,no_of_digits,no_of_operations)
        for response in correct_responses:
            total_correct_responses=total_correct_responses+correct_responses[response][0]
        data_track.append(total_correct_responses)
        data_track.append(incorrect_responses)       
        print("\nArithemetic operation =",data_track[0],"\nTotal no.of practices =",data_track[1],"\nTotal no.of Correct Responses =",data_track[2],"\nTotal no.of Incorrect Responses =",data_track[3])
        input()
        main()
input("\nHey there! Please enter your name:")
main()

#******************* END OF THE CODE ************************



        
