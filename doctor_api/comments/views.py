# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from comments.models import Comment
from rest_framework import generics
from rest_framework.response import Response
#from rest_framework.reverse import reverse
 
from comments.serializers import CommentSerializer
 
 
class CommentsList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
 
 
class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
 
    def get_queryset(self):
        return Comment.objects.all().filter(username=self.request.user)