from django.forms import ModelForm
from .models import Listing, Comment, Bid


class ListingForm(ModelForm):
    
    class Meta:     
        model = Listing
        fields = ['title', 'category', 'description', 'image', 'current_price']

        
class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']    


class BidForm(ModelForm):

    class Meta:
        model = Bid
        fields = ['value']