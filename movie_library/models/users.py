from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
        FEMALE = 'Female'
        MALE = 'Male'
        OTHER = 'Others'
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth= models.DateField()
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.FEMALE, )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

