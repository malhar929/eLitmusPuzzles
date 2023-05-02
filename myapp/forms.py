from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
# from django_mysql.models import ListCharField
import datetime


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ('username', 'email', 'password1', 'password2')
        # fields = ('first_name', 'last_name', 'username', 'email',  'password1', 'password2')
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


# ###################### LOGIN

class Plogin(models.Model):
    USERNAME = models.CharField(max_length=20)
    PASSWORD = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.USERNAME
