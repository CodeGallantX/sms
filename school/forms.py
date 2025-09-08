from django import forms
from .models import Result
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import uuid # Import uuid for generating unique usernames

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'subject', 'score', 'grade']

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        # Remove UserCreationForm.Meta.fields to exclude default username
        fields = ('full_name', 'email', 'password', 'password2') # Explicitly list fields needed

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name'].split(' ', 1)[0]
        user.last_name = self.cleaned_data['full_name'].split(' ', 1)[-1] if ' ' in self.cleaned_data['full_name'] else ''
        # Auto-generate username from email or a UUID if email is too long/not unique enough for username field
        # For simplicity, let's use email as username, but ensure it's unique
        # Django's User model username field has max_length=150
        username_base = self.cleaned_data['email'].split('@')[0]
        username = username_base
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{username_base}{counter}"
            counter += 1
        user.username = username # Set the auto-generated username

        if commit:
            user.save()
        return user
