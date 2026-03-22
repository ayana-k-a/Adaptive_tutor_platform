from django.db import models
from django.conf import settings

class LearnerProfile(models.Model):
    LEARNING_STYLE_CHOICES = (
        ('visual', 'Visual'),
        ('practical', 'Practical'),
        ('conceptual', 'Conceptual'),
        ('discussion', 'Discussion'),
    )

    MODE_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('both', 'Both'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    roll_number = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    department = models.CharField(max_length=100, blank=True)
    semester = models.PositiveIntegerField(null=True, blank=True)
    subject_needed = models.CharField(max_length=100, blank=True)
    preferred_mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='online')
    availability = models.CharField(max_length=200, blank=True)

    q1 = models.CharField(max_length=50, blank=True)
    q2 = models.CharField(max_length=50, blank=True)
    q3 = models.CharField(max_length=50, blank=True)

    learning_style = models.CharField(
        max_length=20,
        choices=LEARNING_STYLE_CHOICES,
        blank=True
    )

    def __str__(self):
        return self.full_name or self.user.username


class TutorProfile(models.Model):
    TEACHING_STYLE_CHOICES = (
        ('visual', 'Diagram Based'),
        ('practical', 'Problem Solving'),
        ('conceptual', 'Concept Explanation'),
        ('discussion', 'Interactive Discussion'),
    )

    MODE_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('both', 'Both'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    roll_number = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    department = models.CharField(max_length=100, blank=True)
    subjects = models.CharField(max_length=200, blank=True)
    teaching_style = models.CharField(max_length=20, choices=TEACHING_STYLE_CHOICES, blank=True)
    available_mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='online')
    availability = models.CharField(max_length=200, blank=True)
    max_students = models.PositiveIntegerField(default=1)
    tutor_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.full_name or self.user.username