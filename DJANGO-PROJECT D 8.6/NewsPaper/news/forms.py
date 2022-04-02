from django.forms import ModelForm, BooleanField
from .models import Post
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from allauth.account.forms import SignupForm


class PostForm(ModelForm):
    check_box = BooleanField(label='Вы уверены?')

    class Meta:
        model = Post
        fields = ['author', 'category', 'publication', 'heading', 'text', 'rating', 'check_box']


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Surname')

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2"
                  )


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user