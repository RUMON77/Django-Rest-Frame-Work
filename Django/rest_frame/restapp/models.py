from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    authorname = models.CharField(max_length=200)
    email = models.EmailField(max_length=20)
    date = models.DateTimeField()

    def __str__(self):
          return self.title
