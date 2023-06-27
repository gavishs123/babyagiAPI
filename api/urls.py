from django.urls import path
from .views import PromptTextViews

urlpatterns = [
    path('generate/', PromptTextViews.as_view())
]