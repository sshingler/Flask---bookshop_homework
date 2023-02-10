from flask import render_template, request, redirect
from app import app
from models.book import *
from models.book_list import book_list

@app.route('/')
def index():
    return render_template('index.html', book_list = book_list)

@app.route('/stock')
def display_stock():
    return render_template('display_books.html', book_list = book_list)

@app.route('/stock/<display_stock>')
def book_detail(display_stock):
    chosen_book = book_list [int(display_stock)]
    return render_template ('single_book.html', book = chosen_book)

@app.route('/stock/add')
def add_stock():
    return render_template('add_book.html')