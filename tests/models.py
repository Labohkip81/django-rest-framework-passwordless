from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(regex=r'^\+254\d{1,9}$',
                                 message="Mobile number must be entered in the format:"
                                         " '+254712345678'. Up to 13 digits allowed.")

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    email_verified = models.BooleanField(default=False)

    mobile = models.CharField(max_length=17, unique=True, blank=True, null=True)
    mobile_verified = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'tests'
