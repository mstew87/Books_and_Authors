from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
  name = models.CharField(max_length=255)
  books = models.ManyToManyField(Book, related_name="authors")
  notes = models.TextField(default="Note")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
