from django.urls import path
from . import views

urlpatterns = [
    path('iamge_codes/<int:image_code_id>/', views.ImageCodeView.as_view()),
]
