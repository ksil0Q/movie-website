from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Collecting client data from comment form"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
