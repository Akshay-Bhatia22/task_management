from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=100, null=False)
    mobile = models.BigIntegerField()
    gender = models.CharField(max_length=15, null=False)
    position = models.CharField(max_length=100, null=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
