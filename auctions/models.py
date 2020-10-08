from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta():
        verbose_name_plural = 'Categories'

    
    def __str__(self):
        return self.title


class Listing(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, blank=True, related_name="categories") 
    photo = models.CharField(max_length=200, blank=True, default="auctions/images/default_image.jpg")
    description = models.TextField()
    start_price = models.IntegerField()
    pub_date = models.DateTimeField('created', default=timezone.now())

    def __str__(self):
        return self.title

class Bid(models.Model):
    value = models.IntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return self.value


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Publication date')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text