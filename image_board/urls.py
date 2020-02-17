from django.urls import path 
from .views import ImageBoard

urlpatterns = [
    path('', ImageBoard.as_view(), name='image_board'), #class based view
]