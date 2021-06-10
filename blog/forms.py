from django import forms
from .models import Post


# Form: Need to definefields
# ModelForm: Fileds is defined by related Model automatically.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'text', 'author', 'published_date')
        # UX: User unlike to write author(=user) name and publish_date.
        fields = ('title', 'text',)