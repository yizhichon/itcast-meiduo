from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('categories/<category_id>/hotskus/', views.HotSKUListView.as_view()),
    path('categories/<category_id>/skus/', views.SKUListView.as_view()),
]
router = DefaultRouter()
router.register('skus/search', views.SKUSearchViewSet, base_name='skus_search')
urlpatterns += router.urls