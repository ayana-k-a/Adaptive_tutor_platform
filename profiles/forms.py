from django import forms
from .models import LearnerProfile, TutorProfile

class LearnerProfileForm(forms.ModelForm):
    class Meta:
        model = LearnerProfile
        fields = [
            'full_name',
            'roll_number',
            'phone',
            'department',
            'semester',
            'subject_needed',
            'preferred_mode',
            'availability',
            'q1',
            'q2',
            'q3',
        ]
        widgets = {
            'q1': forms.Select(choices=[
                ('visual', 'I prefer diagrams'),
                ('conceptual', 'I prefer explanations'),
            ]),
            'q2': forms.Select(choices=[
                ('practical', 'I learn by solving problems'),
                ('conceptual', 'I learn through theory'),
            ]),
            'q3': forms.Select(choices=[
                ('visual', 'Step-by-step examples'),
                ('discussion', 'Discussion/interactive learning'),
            ]),
        }


class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = [
            'full_name',
            'roll_number',
            'phone',
            'department',
            'subjects',
            'teaching_style',
            'available_mode',
            'availability',
            'max_students',
        ]