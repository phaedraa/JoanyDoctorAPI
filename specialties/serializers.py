from rest_framework import serializers
 
from specialties.models import Specialty
 

class SpecialtySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Specialty
        fields = ('name')
