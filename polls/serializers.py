from django.db import transaction
from django.utils import timezone
from rest_framework import serializers
from .models import Question, Choice


class ChoicePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']

#----------------------------------------------------------
class ChoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']

#--------------------------------------------------------------
class QuestionPublicSerializer(serializers.ModelSerializer):
    choices = ChoicePublicSerializer(source='choice_set', many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']

#---------------------------------------------------------
class QuestionDetailSerializer(QuestionPublicSerializer):
    choices = ChoiceDetailSerializer(source='choice_set', many=True, read_only=True)

#-----------------------------------------------------------
class QuestionCreateSerializer(serializers.ModelSerializer):
    choices = serializers.ListField( child=serializers.CharField(max_length=200), min_length=2, write_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'choices']

    @transaction.atomic
    def create(self, validated_data):
        choices = validated_data.pop('choices')
        question = Question.objects.create(pub_date=timezone.now(), author=self.context['request'].user, **validated_data,)
        Choice.objects.bulk_create([Choice(question=question, choice_text=t) for t in choices])
        return question