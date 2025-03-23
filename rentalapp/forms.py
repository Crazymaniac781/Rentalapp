from django import forms
from .models import RentalHome

class RentalHomeForm(forms.ModelForm):
    class Meta:
        model = RentalHome
        fields = ['title', 'description', 'price', 'location', 'bedrooms', 'bathrooms', 'available']

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']
