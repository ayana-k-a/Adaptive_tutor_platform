from django.urls import path
from .views import match_tutors

urlpatterns = [
    path('results/', match_tutors, name='match_tutors'),
]