"""doctor_api URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
 
from doctor_api import views
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Doctor Comment API', description='RESTful API for Dcotor Ratings')),
    url(r'^$', views.api_root),
    url(r'^', include('comments.urls', namespace='comments')),
]