from django.conf.urls import url, include
from users.models import User
from comments.models import Comment
from doctors.models import Doctor
from specialties.serializers import SpecialtySerializer
from rest_framework.decorators import list_route, detail_route

from rest_framework import serializers, viewsets, routers

import json
# Serializers define the API representation.

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CommentList(APIView):
    """
    List all comment, or create a new snippet.
    """
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        comment = Comment(
            text=request.get('text', ''),
            rating=request.get('rating', ''),
            doctor_id=request.get('doctor_id', ''),
            title=request.get('title', '')
        )
        #comment.set_password(request.get('password', None))
        comment.save()
        #comment.user = user
        #comment.save()
        serializer_context = {
            'request': request,
        }
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True, context=serializer_context)
        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'latitude', 'longitude')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'rating_avg', 'rating_total', 'latitude', 'longitude', 'specialty')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User.objects.filter(id=validated_data.get('id')).first()
        #if not user:
            #user = User(name='test', username='test6', email='blajsdf6', latitude='34.00', longitude='34234.00')
            #raise Exception('Bad Request. Must create a user first.')
            #user.save()

    
        comment = Comment(
            text=validated_data.get('text', ''),
            rating=validated_data.get('rating', ''),
            doctor_id=validated_data.get('doctor_id', ''),
            title=validated_data.get('title', '')
        )
        #comment.set_password(validated_data.get('password', None))
        comment.save()
        return comment
        #comment.user = user
        #comment.save()
        #serializer_context = {
        #    'request': validated_data,
        #}
        #doctors = Doctor.objects.all()
        #serializer = DoctorSerializer(doctors, many=True, context=serializer_context)
        #return serializer.data

    def read(self, validated_data):
    	#pass
    	id = validated_data.get('id')
    	if not id:
    		e = Exception('Comment ID is required')
    		return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Comment.objects.get(id=id)

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
        fields = ('title', 'text', 'rating', 'doctor_id', 'user')


# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#
#
#class CommentViewSet(viewsets.ModelViewSet):
#    queryset = Doctor.objects.all()
#    serializer_class = DoctorSerializer
#
#    @detail_route(methods=['post'])
#    def post(self, request, **kwargs):
#
#        self.queryset = Doctor.objects.all()
#        self.serializer_class = DoctorSerializer
#	    #serializer_context = {
#	    #    'request': request,
#	    #}
#	    #user = get_object_or_404(User, id=id)
#	
#	    #doctors = Doctor.objects.all()
#	    # CommentSerializer(serializer_context)
#        comment = Comment(
#            text=request.get('text', ''),
#            rating=request.get('rating', ''),
#            doctor_id=request.get('doctor_id', ''),
#            title=request.get('title', '')
#        )
#	    #comment.set_password(validated_data.get('password', None))
#        comment.save()
#        serializer = DoctorSerializer(self.queryset, many=True)#, context=serializer_context)
#        return Response(serializer.data, status=status.HTTP_200_OK)


#@api_view(['GET', 'POST'])
#def comment_list(request):
#    if request.method == 'POST':
#        comment = Comment(
#            text=request.get('text', ''),
#            rating=request.get('rating', ''),
#            doctor_id=request.get('doctor_id', ''),
#            title=request.get('title', '')
#        )
#        #comment.set_password(validated_data.get('password', None))
#        comment.save()
#        serializer_context = {
#            'request': request,
#        }
#        serializer = DoctorSerializer(self.queryset, many=True, context=serializer_context)
#        return Response(serializer.data, status=status.HTTP_200_OK)



# Routers provide a way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet, base_name='users')
#router.register(r'comments', CommentViewSet, base_name='comments')
#
#
## Wire up our API using automatic URL routing.
## Additionally, we include login URLs for the browsable API.
#urlpatterns = [
#    url(r'^', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#]


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^comments/$', CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)