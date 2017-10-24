from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comments/$', views.comment_list),
    url(r'^comments/(?P<pk>[0-9]+)$', views.comment_detail),
]
