from django.forms import ModelForm
from .models import Listing, Comment


class ListingForm(ModelForm):
    
    class Meta:     
        model = Listing
        fields = ['title', 'category', 'description', 'photo', 'start_price']

        
class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_text']    