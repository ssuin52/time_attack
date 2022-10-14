from concurrent.futures.process import _python_exit
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = 'User'
    phone = PhoneNumberField()
    address = models.CharField(max_length=256)
