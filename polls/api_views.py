from django.db.models import F
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, Choice
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

#--------------------------
class VoteAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk, pub_date__lte=timezone.now())
        try:
            choice_id = int(request.data.get('choice'))
        except (TypeError, ValueError):
            return Response({'detail': 'Champ requis'}, status=status.HTTP_400_BAD_REQUEST)

        updated = Choice.objects.filter(pk=choice_id, question=question).update(votes=F('votes') +1)

        if not updated:
            return Response({'detail': 'Choix invalide pour ce sondage'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Vote enregistré!'})