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

        self.col_headers = {
            'NUM':7 ,
            'TITLE':25,
            'AUTHOR':25,
            'CATEGORY':25
         }

    def add_book(self, book):
        self.books.append(book)
        print(book.name+" has been added to the library collection")

    def search_by_name(self,book_name):
        pass

    def search_by_author(self,author_name):
        pass

    ##SHOULD BE ABLE TO SHOW STOCKING STATUS WITH TABLE (e.g IN STOCK, CHECKED OUT, AVAILABLE XYZ)
    def show_books(self):
        cnt = 1
        self.print_spacers(cols=self.col_headers)
        self.print_header()
        self.print_spacers(cols=self.col_headers)

        for book in self.books:
            print("|"+str(cnt).center(self.col_headers['NUM'])+"|" + book.name.center(self.col_headers['TITLE'],) +"|"+ book.author.center(self.col_headers['AUTHOR']) +"|"+book.category.center(self.col_headers["CATEGORY"])+"|")
            cnt+=1
        self.print_spacers(cols = self.col_headers)

    def checkout_book(self,book_name):
        pass

    def delete_book(self,book_name):
        pass

    ##Formatting methods - Could potentially create own class for this (ACSII Table)
    """IF you decide to go this route then header function or table class should be able
       to take columns names and columns widths as input to create table
   """
    def print_header(self):
        print("|{}|{}|{}|{}|".format("NO.".center(self.col_headers['NUM']),
                                     "TITLE".center(self.col_headers['TITLE']),
                                     "AUTHOR".center(self.col_headers["AUTHOR"]),
                                     "CATEGORY".center(self.col_headers["CATEGORY"])))

    def print_spacers(self,cols=None):
        if cols == None:
            col_sum = sum(self.col_headers.values()) + len(self.col_headers)-1
            print("+{}+".format("-"*col_sum))
        else:
            spacer_str = "+"
            for val in sorted(cols.values()):
                spacer_str = spacer_str+("-"*val)+"+"
            print(spacer_str)

    def print_footer(self):
        col_sum = sum(self.col_headers.values()) + len(self.col_headers)+1
        print("+"+"-"*col_sum+"+")

main_library = Library("Valentine Library","156 Technology Drive")
book1 = Book("MANIFEST","Gene Jones","Self-Help")
book2 = Book("Door Kit","Aaron Valentine","Home Maintenance")

main_library.add_book(book1)
main_library.add_book(book2)

main_library.show_books()
