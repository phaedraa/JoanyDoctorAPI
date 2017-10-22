from rest_framework import serializers
 
from comments.models import Comment
 
 
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    doctors = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='doctors:doctor-detail',
        read_only=True
    )
    password = serializers.CharField(write_only=True)


    def create(self, validated_data):
        comment = Comment(
            username=validated_data.get('username', None)
        )
        comment.set_password(validated_data.get('password', None))
        comment.save()

        # fetch all doctors in the user's location
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
        fields = ('url', 'id', 'username',
                  'password', 'first_name', 'last_name',
                  'email', 'doctors'
                  )
        extra_kwargs = {
            'url': {
                'view_name': 'comments:comment-detail',
            }
        }