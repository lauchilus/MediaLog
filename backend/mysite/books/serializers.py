from rest_framework import serializers

from books.models import Book, UserBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","open_library_id","title","author","publish_date","cover_url"]

class UserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = ["id", "user_id","book"]