from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,unique=True,blank=False,null=False)
    email = models.EmailField(max_length=100,unique=True,null=False,blank=False)


class Note(models.Model):
    account = models.ForeignKey(to=Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100,blank=False,null=False)


class Point(models.Model):
    matter = models.CharField(max_length=500,null=False,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    note = models.ForeignKey(to=Note,on_delete=models.CASCADE)