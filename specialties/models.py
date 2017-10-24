from __future__ import unicode_literals
from django.db import models

 
class Specialty(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    class Meta:
        ordering = ('created',)
