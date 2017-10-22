from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from comments import views
 
urlpatterns = [
    url(r'^comments/$', views.CommentsList.as_view(), name='comments-list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentsDetail.as_view(), name='comments-detail'),
]