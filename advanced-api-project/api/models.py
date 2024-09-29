from django.db import models

# Create your models here.

#This model creates the Author table in our database
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

'''This model creates the Book table in our database, with author serving 
a foreign key linking to the Author model. '''
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




