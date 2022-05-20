from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True,
                                unique=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'username'
    #  USERNAME_FIELD = 'email'
    #   phone_no = models.CharField(max_length=10)
    #  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']



    def __str__(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username

"""
    def __str__(self):
        return "{}".format(self.email)
 """