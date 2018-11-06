from django.urls import path
from . import views



urlpatterns = [
    path('qq/authorization/', views.OAuthQQURLView.as_view()),
    path('qq/user/', views.OAuthQQUserView.as_view()),
]

