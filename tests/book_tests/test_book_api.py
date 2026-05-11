from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from book.models import Book
from book.serializers import BookSerializer

class PublicBookApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Book.objects.create(title="Book 1", author="Author 1", inventory=5, daily_fee=1.0)

    def test_auth_not_required(self):
        res = self.client.get("/api/library/books/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

class PrivateBookApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="admin@test.com", password="password123", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_book(self):
        payload = {
            "title": "New Book",
            "author": "Author",
            "cover": "HARD",
            "inventory": 10,
            "daily_fee": "2.50"
        }
        res = self.client.post("/api/library/books/", payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
