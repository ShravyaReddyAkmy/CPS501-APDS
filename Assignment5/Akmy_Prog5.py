# """This program is to perform arithmatic operations with single/double/triple digits 
# based on user preferences and present a report file of final results."""
# Written by: Shravya Reddy Akmy
# Date: 11/10/2021

import akmy_support
import random 
from os.path import exists 
from datetime import datetime 

# Multidimensional list containing data of all mathematical operations and responses
output=[[],[],[],[]] 
output[0]=['Addition',0,0,0]
output[1]=['Substraction',0,0,0]
output[2]=['Multiplication',0,0,0]
output[3]=['Division',0,0,0]

#Function to present menu and ask user to make selection
def user_menu():
    choice=int(input("\n1 - Addition \n2 - Substraction \n3 - Multiplication \n4 - Division \n5 - Write a report file \n6 - View a report file \n7 - Exit \nPlease enter your choice:"))
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

# Function to calculte arithmetic operations on generated numbers
def arithmetic_cal(num1,num2):
    addition=num1+num2
    substraction=num1-num2
    multiplication=num1*num2
    if num2!=0:
        division=round(num1/num2,2)
    else:
        division='Not possible'
    return addition,substraction,multiplication,division

# Function to ask user to make calculations and display output based on responses
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
                user_div=float(input("\nPlease enter the division of numbers \n(give upto 4 decimals if applicable and \nfor recurring decimals give upto 2 decimals with second decimal increased by 1):")) 
                user_div=round(user_div,2)
                if user_div==division:
                    count_correct=count_correct+1
                else:
                    count_incorrect=count_incorrect+1
        akmy_support.user_display(count_correct,count_incorrect,user_choice,addition,substraction,multiplication,division)
        trial_responses[oper]=[count_correct]
    return trial_responses,count_incorrect

# Function to display output report to user
def user_output(user_choice,data_track):
    for i in range(len(output)):
        i=user_choice-1
        for j in range(1,len(output[i])):
            output[i][j]=data_track[j]
        if user_choice==1:
            output[0]=output[i]
        elif user_choice==2:
            output[1]=output[i]
        elif user_choice==3:
            output[2]=output[i]
        elif user_choice==4:
            output[3]=output[i]
        return output

# Function to write the output report to a file and stamp it with current date and time.
def create_report(filename):
    current_time_date=datetime.now()
    print("\nReport of user performance of arithmetic operations \nDate: {0}   Time : {1}".format(current_time_date.strftime("%m/%d/%Y"),current_time_date.strftime("%H:%M:%S")),file=filename)
    for i in range(len(output)):
        print("\nArithemetic operation =",output[i][0],"\nTotal no.of practices =",output[i][1],"\nTotal no.of Correct Responses =",output[i][2],"\nTotal no.of Incorrect Responses =",output[i][3],file=filename)
    print("\n**********************************************************",file=filename)

# Main program    
def main():
    data_track=[] # List to keep track of no.of operations,correct responses,incorrect responses
    total_correct_responses=0 # Initiating variable to count total correct responses
    filename=name+'.txt' # Final report creating in the name of user
    menu={'1':'Addition','2':'Substraction','3':'Multiplication','4':'Division'}
    user_choice=user_menu()
    if user_choice==7:
        print("\nThankyou ! Exiting the code\n")
    else:
     if user_choice==5:
        print("\nHey ! The final report file is saved after your name:",filename)
        file_exists = exists(filename)
        if file_exists==False:
            with open(filename,mode='w') as report:
                create_report(report)
        elif file_exists==True:
            file_choice=input("\nFile already exists.Enter:\n'a' to append report \n'w' to create new report\n")
            if file_choice=='a':
                with open(filename,mode='a') as report:
                    create_report(report)
            elif file_choice=='w':
                with open(filename,mode='w') as report:
                    create_report(report)
     elif user_choice==6:
        file_exists = exists(filename)
        if file_exists==True:
            file_read=open(filename,'r')
            content=file_read.read()
            print(content)
            file_read.close()
        elif file_exists==False:
            print("\nYou have not practiced any operations yet and no file exist.")
     else:
        data_track.append(menu[str(user_choice)])
        no_of_digits=int(input("\n1 - Single digit \n2 - Double digits \n3 - Triple didgit \nPlease select how many digits operation:"))
        no_of_operations=int(input("\nPlease enter how many times you like to perform the operation:"))
        data_track.append(no_of_operations)
        correct_responses,incorrect_responses=user_cal(user_choice,no_of_digits,no_of_operations)
        for response in correct_responses:
            total_correct_responses=total_correct_responses+correct_responses[response][0]
        data_track.append(total_correct_responses)
        data_track.append(incorrect_responses)   
        user_output(user_choice,data_track)    
     input()
     main()
name=input("\nHey there! Please enter your name:")
print("\nHi",name.upper(),".This program gives you an opportunity to practice different math operations")  
main()

#******************* END OF THE CODE ************************
