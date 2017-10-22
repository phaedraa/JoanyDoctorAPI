from rest_framework import serializers
 
from specialty.models import Specialty
 

class SpecialtySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Specialty
        fields = ('name')
