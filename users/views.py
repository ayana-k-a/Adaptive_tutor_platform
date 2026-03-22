from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from profiles.models import LearnerProfile, TutorProfile
from bookings.models import SessionBooking


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            if user.role == 'learner':
                LearnerProfile.objects.create(user=user)
            else:
                TutorProfile.objects.create(user=user)

            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard_view(request):
    if request.user.role == 'learner':
        profile = LearnerProfile.objects.get(user=request.user)
        learner_bookings = SessionBooking.objects.filter(learner=request.user).order_by('-id')
        return render(request, 'users/learner_dashboard.html', {
            'profile': profile,
            'learner_bookings': learner_bookings
        })
    else:
        profile = TutorProfile.objects.get(user=request.user)
        bookings = SessionBooking.objects.filter(tutor=request.user).order_by('-id')
        return render(request, 'users/tutor_dashboard.html', {
            'profile': profile,
            'bookings': bookings
        })