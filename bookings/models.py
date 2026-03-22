from django.db import models
from django.conf import settings

class SessionBooking(models.Model):
    learner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='learner_sessions')
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tutor_sessions')
    subject = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.learner} → {self.tutor} ({self.status})"
class Feedback(models.Model):
    booking = models.OneToOneField(SessionBooking, on_delete=models.CASCADE, related_name='feedback')
    learner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedback_given')
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedback_received')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Feedback by {self.learner} for {self.tutor}"