from django.urls import path
from .views import *
urlpatterns = [
    path('search/<str:infl>' , search_inf , name='search')
]