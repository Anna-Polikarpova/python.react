from django import forms
from django.forms import ModelForm
from .models import Review, Product
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']

class ProdForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'image', 'description', 'price', 'stock']