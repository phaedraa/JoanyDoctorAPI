from __future__ import unicode_literals

from django.db import models
from users.models import User
from specialties.models import Specialty


class Doctor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    rating_avg = models.FloatField(blank=False, null=False)
    rating_total = models.IntegerField(default=0, blank=False, null=False)
    latitude = models.CharField(max_length=100, unique=True, blank=False, null=False)
    longitude = models.CharField(max_length=100, unique=True, blank=False, null=False)
    specialty = models.ForeignKey(Specialty, related_name='specialties', on_delete=models.CASCADE, null=False)
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ('created',)
