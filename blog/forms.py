from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Post Title'}),
            'content': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 5, 'placeholder': 'Write your content here...'}),
            'image': forms.FileInput(attrs={'class': 'w-full p-2 border rounded', 'accept': 'image/jpeg,image/png'}),
            'category': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 20 or len(title) > 200:
            raise forms.ValidationError('Title must be between 20 and 200 characters.')
        return title

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 5 * 1024 * 1024:
            raise forms.ValidationError('Image file size must be less than 5MB.')
        return image