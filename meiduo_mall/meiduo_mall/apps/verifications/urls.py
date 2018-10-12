from django.urls import path
from . import views

urlpatterns = [
    path('image_codes/<str:image_code_id>/', views.ImageCodeView.as_view()),
]
