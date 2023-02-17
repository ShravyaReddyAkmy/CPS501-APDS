# This program is to calculate area and perimeter/circumference of different geometric shapes based on user choice
# Written by: Shravya Reddy Akmy
# Date: 09/23/2021 

# Importing module which has methods to perform geometric operations
import shapes

# This function is to present menu of geometric shapes to be selected by user 
# User Input : Geometric shape selection
def user_menu():
    user_selection=int(input("\nPlease select a geometric shape : \n1.CIRCLE \n2.SQUARE \n3.RECTANGLE \n4.RHOMBUS \n5.EXIT\n"))
    return user_selection

# This function is to calculate area and perimeter of geometric shape based on user inputs
# User Inputs : Diemnsions based on geometric shape
# Returns : Area and Perimeter of the geometric shape selected
def geometric_calculation(choice):
    if (choice==1):
            print("\n\nUser selected the geometric shape CIRCLE \nFormulae used to calculate:\nArea= pi*(radius)^2, Circumference= 2*pi*radius")
            radius=int(input("\nGive a value for the radius of circle:"))
            result=shapes.circle(radius)
    elif (choice==2):
            print("\n\nUser selected the geometric shape SQUARE \nFormulae used to calculate:\nArea= side*side, Perimeter= 4*side")
            side=int(input("\nGive a value for the side of square:"))
            result=shapes.square(side)
    elif (choice==3):
            print("\n\nUser selected the geometric shape RECTANGLE \nFormulae used to calculate:\nArea= length*breadth, Perimeter= 2*(length+breadth)")
            length=int(input("\nGive a value for the length of rectangle:"))
            breadth=int(input("\nGive a value for the breadth of rectangle:"))
            result=shapes.rectangle(length,breadth)
    elif (choice==4):
            print("\n\nUser selected the geometric shape RHOMBUS \nFormulae used to calculate:\nArea= (diagonal1*diagonal2)/2, Perimeter= 4*side")
            diagonal1=int(input("\nGive a value for the diagonal1 of rhombus:"))
            diagonal2=int(input("\nGive a value for the diagonal2 of rhombus:"))
            side=int(input("\nGive a value for the side of rhombus:"))
            result=shapes.rhombus(diagonal1,diagonal2,side)
    return result
    
# This function is to display the results of area and perimeter to the user
def user_display(result):
    print("\n\nArea =",result[0],"sq.units \nPerimeter =",result[1],"units")
    print("Press 'ENTER' key to continue")

# Main function call
def main():
    choice=user_menu()
    if (choice<5):
        result=geometric_calculation(choice)
        user_display(result)
        input()
        main()
    else:
        print("\nExiting the program....\nThank you!\n")
main()

# ********************* END OF THE CODE *********************



        

