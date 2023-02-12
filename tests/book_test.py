import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def SetUp(self):
        self.book = Book ("Python for Beginners", "Tim Wapling", "Education", "A book about the Python programming language, written for beginners. Learn everything you need to know!", True)

    # def test_book_has_title (self):
    #     self.assertEqual("Python for Beginners", self.book.title)