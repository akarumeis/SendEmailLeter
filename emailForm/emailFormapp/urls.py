from django.urls import path
from emailFormapp.views import *
urlpatterns = [
    path('', create_leter, name='create_leter'),
]