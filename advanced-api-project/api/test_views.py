from rest_framework import status
from django.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author
from .seriealizers import BookSerializer

class BookCreateTest(APITestCase):
    def test_create_book(self):
        user = User.objects.create(username="maud", password="mypassword")
        author = Author.objects.create(name="Chimmamanda Ngozie")
        book = Book.objects.create(
            title="Purple Hibiscus",
            author = author,
            publication_year = 2002
        )
        data = {
            'title': book.title,
            'author': book.author.pk,
            'publication_year': book.publication_year
        }
        response = self.client.post("books/create", data=data)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.status_code, 200)


    def test_update_book(self):
        user = User.objects.create(username="maud", password="mypassword")

        author = Author.objects.create(name="Chimmamanda Ngozie")

        book = Book.objects.create(
            title="Purple Hibiscus",
            author = author,
            publication_year = 2002
        )
        data = {
            'title': book.title,
            'author': book.author.pk,
            'publication_year': book.publication_year
        }
        self.client.login(username=user.username, password=self.user.password)
        response = self.client.put("books/update/<int:pk>", data={'title': 'Purple Hibiscus for Hommies'})
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_book(self):
        response = self.client.post('books/delete/<int:pk>')
        self.assertEqual(response.status_code, 200)
        

        #Verify Book Creation
        # self.assertEqual(Book.objects.count(), 1)
        # self.assertEqual(book.title, data['title'])
        # self.assertEqual(book.author.name, self.author.name)
        # self.assertEqual(book.publication_year, data['publication_year'])