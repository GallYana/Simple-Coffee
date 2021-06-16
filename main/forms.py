from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username, '', password)
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    user = forms.CharField()
    class Meta:
        model = UserProfile
        fields = ['user']

    def save(self, commit=True):
        user = self.cleaned_data['user']
        test = UserProfile(name=user)
        if commit:
            test.save()
        return test