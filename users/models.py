from __future__ import unicode_literals

from django.db import models

 	
class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    email = models.CharField(max_length=100, unique=True, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)

    class Meta:
        ordering = ('created',)
