from flask import render_template, request, redirect
from app import app
from models.book import *
from models.book_list import *
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock')
def display_stock():
    return render_template('display_books.html', book_list = book_list)

@app.route('/stock/add')
def add_stock():
    return render_template('add_book.html')