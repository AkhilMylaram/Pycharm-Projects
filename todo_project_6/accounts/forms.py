from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pyexpat import model


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']