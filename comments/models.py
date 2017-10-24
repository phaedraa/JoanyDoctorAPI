# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User

 
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=False, null=False)
    doctor_id = models.CharField(default=None, max_length=100, blank=False, null=True)
    user = models.ManyToManyField(User, blank=True)
    is_active = models.BooleanField(default=True, blank=False, null=False)

    def update_doctor(self):
    	from doctors.models import Doctor
    	doctor = Doctor.objects.get(id=self.doctor_id)
    	doctor.update(self.rating)

    def save(self, *args, **kwargs):
    	super(Comment, self).save(*args, **kwargs)
    	self.update_doctor()

    def delete(self):
    	self.is_active = False
    	self.save()

    class Meta:
        ordering = ('created',)
