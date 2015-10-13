from django import forms
# from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from lensview.models import Rater, Rating


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class RaterForm(forms.ModelForm):
    class Meta:
        model = Rater
        fields = ['gender', 'age', 'occupation', 'zipcode']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'review']
