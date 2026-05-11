from rest_framework import serializers
from book.models import Book
from borrowing.models import Borrowing
from book.serializers import BookSerializer
from borrowing.notifications import send_telegram_notification


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user",
        )
        read_only_fields = ("id", "borrow_date", "actual_return_date", "user")

    def validate(self, attrs):
        book = attrs["book"]
        if book.inventory == 0:
            raise serializers.ValidationError("This book is out of stock.")
        return attrs

    def create(self, validated_data):
        book = validated_data["book"]
        book.inventory -= 1
        book.save()
        return super().create(validated_data)

    def create(self, validated_data):
        book = validated_data["book"]
        book.inventory -= 1
        book.save()

        borrowing = super().create(validated_data)

        message = (
            f"🚀 <b>New Borrowing Created!</b>\n"
            f"📖 Book: {book.title}\n"
            f"👤 User: {borrowing.user.email}\n"
            f"📅 Return date: {borrowing.expected_return_date}"
        )
        send_telegram_notification(message)

        return borrowing


class BorrowingListSerializer(BorrowingSerializer):
    book = BookSerializer(read_only=True)
