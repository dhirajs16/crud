from django.urls import path
from .views import *


urlpatterns = [
    path('', ListCreateAPIView.as_view(), name='ListCreateAPIView'), 
    path('<int:pk>/', RetriveUpdateDeleteAPIView.as_view(), name='RetriveUpdateDeleteAPIView'),
]