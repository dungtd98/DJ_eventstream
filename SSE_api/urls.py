from django.urls import path
from .views import QuestionApiView
urlpatterns = [
    path('question/', QuestionApiView.as_view(), name='question-view')
]