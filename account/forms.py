from django import forms
from django.core.mail import send_mail

from .models import User

def send_welcome_email(email):
    message = f'Спасибо за регистрацию на нашем сайте PyShop 14'
    send_mail(
        'Welcome to KG',
        message,
        'admin@gmail.com',
        [email],
        fail_silently=False
    )

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name', 'image')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This user already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('password do not match')
        return data

    def save(self):
        print(self.cleaned_data)
        user = User.objects.create_user(**self.cleaned_data)
        return user