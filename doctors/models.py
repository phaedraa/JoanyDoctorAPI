from __future__ import unicode_literals

from django.db import models
from users.models import User
from specialties.models import Specialty


class Doctor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(default='', max_length=100, blank=False, null=False)
    rating_avg = models.FloatField(blank=False, null=True)
    rating_total = models.IntegerField(default=0, blank=False, null=False)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    specialty = models.ForeignKey(Specialty, related_name='specialties', on_delete=models.CASCADE, null=False)
    users = models.ManyToManyField(User)

    def update(self, rating):
    	if not self.rating_total or not self.rating_avg:
    		self.rating_avg = float(rating)
    		self.rating_total = 1
    		self.save()
    		return
    	sum_ratings = float(self.rating_total) * self.rating_avg + float(rating)
    	self.rating_total += 1
    	self.rating_avg = sum_ratings / self.rating_total
    	self.save()

    class Meta:
        ordering = ('created',)
