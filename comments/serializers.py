from .models import Comment
from rest_framework import serializers, viewsets, routers

class CommentSerializer(serializers.ModelSerializer):

    #def __init__(self, data):
    def create(self, validated_data):
        comment = Comment(
            text=validated_data.get('text', ''),
            rating=validated_data.get('rating', ''),
            doctor_id=validated_data.get('doctor_id', ''),
            title=validated_data.get('title', '')
        )
        comment.save()
        return comment


    def update(self, instance, validated_data):
    	for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance


    class Meta:
        model = Comment
        fields = ('id', 'title', 'text', 'rating', 'doctor_id', 'user')

