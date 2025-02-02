# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Users(models.Model):

    #__Users_FIELDS__
    imię = models.CharField(max_length=255, null=True, blank=True)
    nazwisko = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    nip = models.IntegerField(null=True, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Category(models.Model):

    #__Category_FIELDS__
    id = models.ForeignKey(Users, on_delete=models.CASCADE)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Product(models.Model):

    #__Product_FIELDS__
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Auth(models.Model):

    #__Auth_FIELDS__
    login = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    #__Auth_FIELDS__END

    class Meta:
        verbose_name        = _("Auth")
        verbose_name_plural = _("Auth")


class Trasnsactios(models.Model):

    #__Trasnsactios_FIELDS__
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    trancaction_id = models.IntegerField(null=True, blank=True)

    #__Trasnsactios_FIELDS__END

    class Meta:
        verbose_name        = _("Trasnsactios")
        verbose_name_plural = _("Trasnsactios")



#__MODELS__END
