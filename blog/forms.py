# forms.py
from django import forms
from .models import Post, Review

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class ReviewForm(forms.ModelForm):
    """
    ReviewForm is a ModelForm for creating and updating Review instances.

    Attributes:
        Meta (class): A nested class that defines metadata for the form.
            model (Review): The model that the form is based on.
            fields (list): The list of fields to include in the form.
    """
    class Meta:
        model = Review
        fields = ['content', 'rating']
