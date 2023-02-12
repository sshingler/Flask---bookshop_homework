import unittest
from models.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("Python", "Author1", "testing", "a book about tests", True)

    def test_book_has_title(self):
        expected = "Python"
        actual = self.book.title 
        self.assertEqual(expected, actual)

    def test_book_has_author(self): 
        expected = "Author1"
        actual = self.book.author 
        self.assertEqual(expected, actual)

    def test_book_availability(self):
        expected = True
        actual = self.book.available
        self.assertEqual(expected, actual
        )



