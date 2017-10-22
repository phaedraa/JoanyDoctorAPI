# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User

 
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey('users.User', related_name='doctors', on_delete=models.CASCADE, null=False)
    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=False, null=False)
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ('created',)
