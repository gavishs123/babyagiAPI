from django.urls import path
from .views import PromptTextViews,Index

urlpatterns = [
    path('generate/', PromptTextViews.as_view()),
    path('index/',Index.as_view())
]