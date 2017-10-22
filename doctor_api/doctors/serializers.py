from rest_framework import serializers
 
from doctors.models import Doctor
from specialty.models import Specialty
 

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
	specialty = SpecialtySerializer(source='specialty_set', many=True)

    class Meta:
        model = Doctor
        fields = ('name', 'specialty', 'rating_avg', 'rating_total',
        	'latitude', 'longitude', 'created')
