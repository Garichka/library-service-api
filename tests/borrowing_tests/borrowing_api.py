from rest_framework import status

from book.models import Book


def test_cannot_borrow_out_of_stock_book(self):
    book = Book.objects.create(title="No Stock", author="A", inventory=0, daily_fee=1)
    payload = {"book": book.id, "expected_return_date": "2026-12-31"}
    res = self.client.post("/api/borrowing/borrowings/", payload)
    self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
