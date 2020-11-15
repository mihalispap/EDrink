from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django_registration.views import RegistrationView

from edrink.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'avatar')


class CustomRegistration(RegistrationView):
    def register(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # TODO: do something if exists
            avatar = form.cleaned_data.get('avatar')
            user = form.save()
            user.is_staff = True
            user.save()
        else:
            pass  # TODO: do something here


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', ]
