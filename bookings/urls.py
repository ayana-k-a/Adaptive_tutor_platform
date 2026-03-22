from django.urls import path
from .views import book_session, update_booking_status, give_feedback

urlpatterns = [
    path('book/<int:tutor_id>/', book_session, name='book_session'),
    path('update/<int:booking_id>/<str:action>/', update_booking_status, name='update_booking_status'),
    path('feedback/<int:booking_id>/', give_feedback, name='give_feedback'),
]