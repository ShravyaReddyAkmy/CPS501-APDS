# This program is to write the code for a class using the object-oriented programming.
# Written by: Shravya Reddy Akmy
# Date: 11/21/2021

class BookShop:
    """Class BookShop is to write a book to or read a book from a file"""
    def __init__(self,title,author,publishedyear,price):
        self.title=title
        self.author=author
        self.publish=publishedyear
        self.price=price
    
    def book_read(self):
        with open("BookShop.txt",'r') as file:
            found=0
            L = [line.split() for line in file]
            for i in range(len(L)):
                for item in L[i]:
                    if item ==self.author+",":
                        found=found+1
                        b=" ".join(L[i])
                        b=b.split(",")
                        r=f'The book is found.\nTitle:{b[0]} \nAuthor:{b[1]} \nPublished in year:{b[2]} \nPrice:{b[3]} \nBook Cover:{b[4]}\n'
                        print(r)                
            if found==0:
                        r=f'There is no book by author {self.author}\n'
                        print(r)
            
    def book_write(self,cover="softCover"):
        with open("BookShop.txt",'a') as file:
            file.write(f'{self.title}, {self.author}, {self.publish}, {self.price}, {cover}\n')
        return f'Book "{self.title}" is added to the file BookShop.txt'

class Softcover(BookShop):
    def __init__(self,title,author,publishedyear,price,cover):
        super().__init__(title,author,publishedyear,price)
        self.cover=cover
    def book_write(self):
        return super().book_write(self.cover)

class Hardcover(BookShop):
    def __init__(self,title,author,publishedyear,price,cover):
        super().__init__(title,author,publishedyear,price)
        self.cover=cover
    def book_write(self):
        return super().book_write(self.cover)
