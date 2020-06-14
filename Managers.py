
#By default Django adds a Manager with the name objects to every Django model class
#If you want to use objects as a field name or if you want to use a name other than 
#objects for the Manager you can rename it on a per-model basis. TO rename the 
#Manager for a given class, define attribute of type models.Manager()

from django.db import models

class Person(models.Model):
  ...
  people=models.Manager()

#Using this example model, Person.people.all() instead of Person.objects.all()  

#Modifying a manager's initial QuerySet
class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author='Ronald')

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    objects=models.Manager()#The default manager
    book_objects=BookManager()#The custom manager
    
#With this sample model, Book.objects.all() will return all books in the database, but Book.
#book_objects.all() will only return the ones written by Roald Dahl.
#
