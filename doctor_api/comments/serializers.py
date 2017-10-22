from rest_framework import serializers
 
from comments.models import Comment

DECIMAL_DEGREE_TO_MILES = 68.703
MAX_RADIUS = 20.0
DOCTOR_RECOMMEND_LIMIT = 10
 

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # doctors = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name='doctors:doctor-detail',
    #     read_only=True
    # )
    # password = serializers.CharField(write_only=True)


    def create(self, validated_data):
    	user = User.Objects.get(id=validated_data.get('id'))
    	if not user:
    		raise Exception('Bad Request. Must create a user first.')

        comment = Comment(
        	user=user,
            text=validated_data.get('text', ''),
            rating=validated_data.get('rating', ''),
            doctor_id=validated_data.get('doctor_id', ''),
            title=validated_data.get('title', '')
        )
        #comment.set_password(validated_data.get('password', None))
        comment.save()
        # Find doctors within 20 miles, ranked from highest to lowest ratings
        max_radius = MAX_RADIUS / DECIMAL_DEGREE_TO_MILES
        long_range = [float(user.longitude) - max_radius, loat(user.latitude) + max_radius]
        doctors = Doctor.objects.filter(
        	longitude_lte=long_range[1],
        	longitude_gte=long_range[0]
        ).order_by('-ranking_avg', '-rating_total')
        # filter such that latitude is within the MAX_RADIUS
        final_doctors = []
        total = 0
        for doctor in doctors:
        	if total > 10:
        		break
        	longt = float(doctor.longitude)
        	lat = float(doctor.latitude)
        	distance = sqrt(
        		(longt - float(user.longitude))**2 + (lat - float(user.latitude))**2)
        	if distnace <= max_radius:
        		final_doctors.append(doctor)
        		total += 1


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
        fields = ('title', 'text', 'rating', 'doctor_id')
        extra_kwargs = {
            'url': {
                'view_name': 'comments:comment-detail',
            }
        }