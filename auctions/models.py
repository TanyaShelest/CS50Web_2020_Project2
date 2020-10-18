from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta():
        verbose_name_plural = 'Categories'

    
    def __str__(self):
        return self.title


class User(AbstractUser):
    def __str__(self):
        return self.username


class Listing(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='listings/', blank=True)
    description = models.TextField()
    current_price = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Listing)

    def __str__(self):
        return f"{self.user}\'s Watchlist" 


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()

    def __str__(self):
        return f"{self.text} about {self.listing}"


class Bid(models.Model):
    value = models.IntegerField(verbose_name='your bid')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{self.value} from {self.author}"