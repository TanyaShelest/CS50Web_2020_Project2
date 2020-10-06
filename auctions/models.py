from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    title = models.CharField(max_length=200)


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_price = models.IntegerField()
    category = models.ManyToManyField(Category) 


class Bid(models.Model):
    value = models.IntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Publication date')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment_text = models.TextField()