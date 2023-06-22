from django.urls import path
from .views import article_list , article_details

urlpatterns = [
    path('articles/', article_list.as_view()),
    path('articles/<int:id>/', article_details.as_view()),
]
