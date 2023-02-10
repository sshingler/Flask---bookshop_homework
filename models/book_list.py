from models.book import *
import datetime

book_1 = Book("Python for Beginners", "Tim Wapling", "Education", "A book about the Python programming language, written for beginners. Learn everything you need to know!", True)
book_2 = Book("HTML & CSS for Beginners", "Barry Rodgers", "Education", "A book about HTML and CSS, written for beginners. Learn everything you need to know!", True)
book_3 = Book("JavaScript for Beginners", "Mary Hollow", "Education", "A book about the JavaScript programming language, written for beginners. Learn everything you need to know!", True)

book_list = [book_1, book_2, book_3]

def add_new_book(book):
    book_list.append(book)

def delete_book(index):
    book_list.pop(index)




