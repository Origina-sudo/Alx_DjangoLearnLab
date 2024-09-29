### Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected output: <Book: 1984>

### Retrieve

book = Book.objects.get(id=1)
print(book)
# Expected output: <Book: 1984>

### Update
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
# Expected output: <Book: Nineteen Eighty-Four>

###Delete
book = Book.objects.get(id=1)
book.delete()
books = Book.objects.all()
print(books)
# Expected output: <QuerySet []>
