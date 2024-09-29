# Python Command
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
# Expected output: <Book: Nineteen Eighty-Four>