from django import forms
from Blog.models import BlogPostModel

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ['title', 'author', 'content']
