from rest_framework import serializers
from .models import Book

#This BookSerializer serializes all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


#This custom validation ensures publication_year is not in the future.
    def validate_publication_year(self, value):
        current_year = date.today().current_year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value
        
#This serializes all author fields while nested Bookserializer serialize related books  
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']