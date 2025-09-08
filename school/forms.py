from django import forms
from .models import Result
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'subject', 'score', 'grade']

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('full_name', 'email',)

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
        if commit:
            user.save()
        return user
