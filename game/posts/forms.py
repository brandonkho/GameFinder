from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'sport', 'description', 'location', 'capacity', 'time')
        #widgets = {'author': forms.HiddenInput()}