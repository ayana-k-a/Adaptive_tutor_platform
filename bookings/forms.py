from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }