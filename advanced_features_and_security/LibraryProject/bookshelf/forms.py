from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "isbn"]
        widget = {
            "published_date": forms.DateInput(attrs={"type":"date"}),
        }

class ExampleForm(forms.Form):
    # Add some fields to your form
    name = forms.CharField(max_length=100)
    email = forms.EmailField()