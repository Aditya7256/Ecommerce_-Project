from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
              password1 = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Password'}))
              password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Conform_Password'}))
              email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
              class Meta:
                model = User
                fields = ['username', 'email', 'password1', 'password2']
                labels = {'username':'Username', 'email':'Email', 'password1':'Password1', 
                        'password2':'Password2'}
                widgets = {
                        'username':forms.TextInput(attrs={'placeholder': 'Username'}),
                        'password1':forms.TextInput(attrs={'placeholder': 'Password'}),
                        }