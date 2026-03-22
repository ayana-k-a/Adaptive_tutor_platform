from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LearnerProfile, TutorProfile
from .forms import LearnerProfileForm, TutorProfileForm

def detect_learning_style(profile):
    scores = {
        'visual': 0,
        'practical': 0,
        'conceptual': 0,
        'discussion': 0,
    }

    if profile.q1:
        scores[profile.q1] += 1
    if profile.q2:
        scores[profile.q2] += 1
    if profile.q3:
        scores[profile.q3] += 1

    best_style = max(scores, key=scores.get)
    return best_style

@login_required
def edit_profile(request):
    if request.user.role == 'learner':
        profile = LearnerProfile.objects.get(user=request.user)

        if request.method == 'POST':
            form = LearnerProfileForm(request.POST, instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.learning_style = detect_learning_style(profile)
                profile.save()
                return redirect('dashboard')
        else:
            form = LearnerProfileForm(instance=profile)

        return render(request, 'profiles/edit_learner_profile.html', {'form': form})

    else:
        profile = TutorProfile.objects.get(user=request.user)

        if request.method == 'POST':
            form = TutorProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = TutorProfileForm(instance=profile)

        return render(request, 'profiles/edit_tutor_profile.html', {'form': form})