#!/usr/bin/env python

"""
OOP Practice - Started 12/7/24

Library Catalog 
"""
__author__ = "A. Valentine"


class Book:
    def __init__(self,name,author,category,desc = None):
        self.name = name
        self.author = author
        self.category = category
        self.in_stock = True
        self.desc = desc

    def show(self):
        print("Book: ",self.name)
        print("Author: ",self.author)
        print("Category: ",self.category)
        if self.desc != None:
            print("Description: ",self.desc)

    def add_description(self,desc):
        self.desc = desc 


class Library:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book.name+" has been added to the library collection")

    def search_by_name(self,book_name):
        pass

    def search_by_author(self,author_name):
        pass

    ##Should be able to create a visual table with all of the books
    """
    This should be the display used to show books
    |--No.--|--Name--|---Author--|--Description--|
    """
    def show_books(self):
        cnt = 1
        for book in self.books:
            print(str(cnt)+". Book: " + book.name +" Author: "+ book.author +" Category: "+book.category)
            cnt+=1
    def checkout_book(self,book_name):
        pass

    def delete_book(self,book_name):
        pass


main_library = Library("Valentine Library","156 Technology Drive")
book1 = Book("MANIFEST","Gene Jones","Self-Help")
book2 = Book("Door Kit","Aaron Valentine","Home Maintenance")

main_library.add_book(book1)
main_library.add_book(book2)

main_library.show_books()


