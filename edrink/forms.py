from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_registration.views import RegistrationView

from edrink.models import Participant


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)

    name = forms.CharField(max_length=256, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'avatar')


class CustomRegistration(RegistrationView):
    def register(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # TODO: do something if exists
            name = form.cleaned_data.get('name')
            avatar = form.cleaned_data.get('avatar')
            user = form.save()
            user.is_staff = True
            user.save()
            participant = Participant(user=user, name=name, avatar=avatar)
            participant.save()
        else:
            pass  # TODO: do something here
