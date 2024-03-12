# In blog/forms.py

from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text_content', 'voice_content']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user','content']
