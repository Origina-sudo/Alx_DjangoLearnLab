from rest_framework import serializers
from .models import Book, Author
import datetime

class AuthorSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Author
        filds = ['name']


Evans = Author(name='Evans Torddey')

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(f'Publication year cannot be in the future. Current year: {current_year}')
        return value


ghotam = Book(title="Ghotham City", publication_year='2020', author=Evans)
