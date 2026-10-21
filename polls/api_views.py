from django.db.models import F
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Question
from .serializers import (QuestionPublicSerializer,QuestionDetailSerializer,QuestionCreateSerializer)


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return (Question.objects.filter(pub_date__lte=timezone.now())
                .prefetch_related('choice_set').order_by('-pub_date'))

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return QuestionCreateSerializer
        if self.request.user.is_authenticated:
            return QuestionDetailSerializer
        return QuestionPublicSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        return Response(QuestionDetailSerializer(question).data,status=status.HTTP_201_CREATED)

