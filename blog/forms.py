from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # title = 'title'
        # text = 'text'
        fields = ['title', 'text', 'published_date', 'author']
        # field_classes = {'title', forms.CharField}
        widgets = {
            'title': forms.Textarea(attrs={'class':'post_title', 'cols': 5, 'rows': 1}),
            'text': forms.Textarea()
            # 'published_date': )
        }