# Python Command
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
books = Book.objects.all()
print(books)
# Expected output: <QuerySet []>