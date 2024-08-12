from django.db import models


# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)


class Books(models.Model):
    imeges = models.ImageField()
    name = models.CharField(max_length=100, unique=True)
    date = models.CharField(max_length=10)
    date_published = models.DateField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    filename = models.FileField()


class Review(models.Model):
    rating = models.CharField(max_length=10)
    text = models.CharField(max_length=1000)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
