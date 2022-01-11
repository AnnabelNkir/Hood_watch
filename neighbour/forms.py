from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Neighbour,Business,Post
from django.forms.boundfield import BoundField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pro_photo','email','neighbourhood','bio')


class NeighbourForm(forms.ModelForm):
    class Meta:
        model = Neighbour
        fields = ('name','image','location','occupants','police_dept','health_dept')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude =  []
        fields = ['name','description','email','neighbourhood']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =  ['user','neighbourhood']
        fields = ['post']