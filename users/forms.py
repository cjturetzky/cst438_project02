
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #required = true ===one option

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #required = true ===one option

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class RemoveUser(forms.ModelForm):
    def clean_old_password(self):
        password = self.cleaned_data.get('password', None)
        if not self.user.check_password(password):
            raise ValidationError('Invalid password')
    class Meta:
        model = User
        fields = ['password']