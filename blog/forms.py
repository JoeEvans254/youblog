from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'space-y-2'}),
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'content': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 6}),
            'image': forms.FileInput(attrs={'class': 'w-full p-2 border rounded'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 4, 'placeholder': 'Add a comment...'}),
        }