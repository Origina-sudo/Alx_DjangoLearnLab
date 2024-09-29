from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
from .forms import ExampleForm
from django.db import transaction
from django.views.decorators.http import require_http_methods
from django.core.exceptions import PermissionDenied


# Create your views here.
@permission_required("bookshelf.can_view", raise_exception=True)
@require_http_methods(["GET"])
def book_list(request):
    books = Book.objects.all().order_by("title")
    return render(request, "bookshelf/book_list.html", {"books":books})

@permission_required("bookshelf.can_view", raise_exception=True)
@require_http_methods(["GET"])
def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "bookshelf/book-details.html", {"book":book})

@permission_required("bookshelf.can_create", raise_exception=True)
@require_http_methods(["POST"])
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                book = form.save(commit=False)
                book.created_by = request.user
                form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/edit-book.html", {"form":form})

@permission_required("bookshelf.can_edit", raise_exception=True)
@require_http_methods(["GET", "POST"])
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            with transaction.atomic():
                book = form.save(commit=False)
                book.updated_by = request.user
                form.save()
            return redirect("book_details", pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/edit-book.html", {"form":form})


@permission_required("bookshelf.can_delete", raise_exception=True)
@require_http_methods(["GET", "POST"])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        with transaction.atomic():
            book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/deleted_book.html", {"book":book})
