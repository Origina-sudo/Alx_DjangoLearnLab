from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import User

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')


class UserAdmin(CustomUserAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
