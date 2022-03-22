from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Вы уверены?')

    class Meta:
        model = Post
        fields = ['author', 'category', 'publication', 'heading', 'text', 'rating', 'check_box']