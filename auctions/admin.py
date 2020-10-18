from django.contrib import admin

from .models import Category, Bid, Listing, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Category, CategoryAdmin)


class BidAdmin(admin.ModelAdmin):
    list_display = ['listing', 'author', 'value']
admin.site.register(Bid, BidAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['listing', 'pub_date', 'author', 'text']
admin.site.register(Comment, CommentAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'current_price', 'pub_date', 'author', 'active']
admin.site.register(Listing, ListingAdmin)