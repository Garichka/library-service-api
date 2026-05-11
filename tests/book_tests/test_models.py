from django.test import TestCase
from book.models import Book


class ModelTests(TestCase):
    def test_book_str(self):
        book = Book.objects.create(
            title="Clean Code", author="Robert Martin", inventory=1, daily_fee=1.0
        )
        self.assertEqual(str(book), "Clean Code by Robert Martin")
