from django.urls import path, include
from .views import (
    ProductListApiView,
    RecommendAPIView,
)

urlpatterns = [
    path('api', ProductListApiView.as_view()),
    path('recommend/<int:id>', RecommendAPIView.as_view()),
]
