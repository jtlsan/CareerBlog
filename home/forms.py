from django import forms
from home.models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'sub_category', 'content']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']