from .models import Doctor
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = (
        	'first_name', 'last_name', 'rating_avg',
        	'rating_total', 'latitude', 'longitude', 'specialty')
