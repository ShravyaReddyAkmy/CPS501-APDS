# This program is to write the code for a book shop using the object-oriented programming.
# Written by: Shravya Reddy Akmy
# Date: 11/21/2021

import Shravya_Class

def book_shop(user_choice):
    if user_choice==1:
        book_title=input("\nPlease enter the book title: ")
        book_title=book_title.title()
        book_author=input("\nPlease enter the author name: ")
        book_author=book_author.title()
        book_publish=int(input("\nPlease enter the year of book publication: "))
        book_price=int(input("\nPlease enter the price of book: "))
        book_cover=input("\nPlease enter the cover type of book:\n's' for Softcover \n'h' for Hardcover\n")
        if book_cover=='s':
            book=Shravya_Class.Softcover(book_title,book_author,book_publish,book_price,"Softcover")
            print(book.book_write())
        elif book_cover=='h':
            book=Shravya_Class.Hardcover(book_title,book_author,book_publish,book_price,"Hardcover")
            print(book.book_write())
    elif user_choice==2:
        book_author=str(input("\nPlease enter the author name of the book: "))
        book_author=book_author.title()
        book=Shravya_Class.BookShop(" ",book_author," "," ")
        book.book_read()

def main():
    user_choice=int(input("\nBook shop menu: \n1 - Add a book \n2 - View a book \n3 - Exit \nEnter your choice:")) 
    if user_choice==3:
        print("\nThankyou! Exiting the code")
    else:
        book_shop(user_choice)
        input()
        main()
main()

#**************END OF THE CODE***************           
        