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
