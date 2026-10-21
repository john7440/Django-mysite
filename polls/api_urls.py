from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api_views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('questions/', api_views.QuestionListCreateAPIView.as_view(), name='api_questions'),
    path('questions/<int:pk>/vote/', api_views.VoteAPIView.as_view(), name='api_vote'),
]