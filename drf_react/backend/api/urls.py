from django.urls import path
from .views import LCApiView
urlpatterns = [
    path('', LCApiView.as_view(), name='listCreate'), 
]