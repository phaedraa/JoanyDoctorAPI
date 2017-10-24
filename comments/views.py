from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Comment
from .serializers import CommentSerializer
from doctors.models import Doctor
from users.models import User
from rest_framework.decorators import list_route
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework.response import Response


DECIMAL_DEGREE_TO_MILES = 68.703
MAX_RADIUS = 20.0
DOCTOR_RECOMMEND_LIMIT = 10


def extract_doctor_info(doctor):
    try:
    	specialty = doctor.specialty.name
    except Exception:
    	specialty = ''

    return {
    	'first_name': doctor.first_name,
    	'last_name': doctor.last_name,
    	'rating_avg': doctor.rating_avg,
    	'rating_total': doctor.rating_total,
    	'latitude': doctor.latitude,
    	'longitude': doctor.longitude,
    	'specialty': specialty
    }


def get_distance(user, doctor):
    return (
    	(doctor.longitude - user.longitude)**2 +\
    	(doctor.latitude - user.latitude)**2
    ) ** 0.5
    


def fetch_nearby_doctors_ranked(user):
    max_radius = MAX_RADIUS / DECIMAL_DEGREE_TO_MILES
    doctors = Doctor.objects.filter(
    	longitude__lte=user.longitude + max_radius,
    	longitude__gte=user.longitude - max_radius,
    ).order_by('-rating_avg', '-rating_total')
    # filter such that latitude is within the MAX_RADIUS
    final_doctors = []
    total = 0
    for doctor in doctors:
    	if total > DOCTOR_RECOMMEND_LIMIT:
    		break
    	if get_distance(user, doctor) <= max_radius:
    		final_doctors.append(extract_doctor_info(doctor))
    		total += 1
    return final_doctors


@api_view(['GET', 'POST'])
def comment_list(request):
    """ List all Comments or Create Comment """
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
    	username = request.POST.get('username', '')
    	if not username:
    		return Response(
    			{'Error': 'username required'},
    			status=status.HTTP_400_BAD_REQUEST
    		)
    	user = User.objects.get(username=username)
    	if not user:
    		return Response(
    			{'Error': 'Required existing user to comment.'},
    			status=status.HTTP_400_BAD_REQUEST
    		)
    	comment = Comment(
    	    text=request.POST.get('text', ''),
    	    rating=request.POST.get('rating', ''),
    	    doctor_id=request.POST.get('doctor_id', ''),
    	    title=request.POST.get('title', '')
    	 )
    	comment.save()
        return Response({'nearby_doctors': fetch_nearby_doctors_ranked(user)})


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    """
    Retrieve, update or delete a comment.
    """
    try:
        comment = Comment.objects.get(pk=pk)
    except comment.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, request.data, partial=True)#json.loads(request.body))#.PUT.get('latitude'))
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
    	if comment.is_active:
        	comment.delete()
        	data = {
        		'Success': 'Comment {} successfully marked inactive'.format(pk),
        	}
        else:
        	data = {
        		'Invalid': 'Comment {} already marked inactive'.format(pk),
        	}

        return Response(data)

