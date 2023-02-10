from flask import render_template, request, redirect
from app import app
from models.book import *
from models.book_list import book_list, add_new_book, delete_book

@app.route('/')
def index():
    return render_template('index.html', book_list = book_list)

@app.route('/stock')
def display_stock():
    return render_template('display_books.html', book_list = book_list)

@app.route('/stock/<display_stock>')
def book_detail(display_stock):
    chosen_book = book_list [int(display_stock)]
    return render_template ('single_book.html', book = chosen_book, book_list = book_list)

@app.route('/stock/add')
def new_book():
    return render_template('add_book.html')

@app.route('/stock', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    description = request.form['description']
    price = request.form['price']
    new_book = Book (title, author, genre, description, price)
    add_new_book(new_book)
    return redirect("/stock")

@app.route('/stock/delete/', methods =['POST'])
def delete():
    index_to_delete = int(request.form["delete"])
    delete_book(index_to_delete)
    return redirect("/stock")


