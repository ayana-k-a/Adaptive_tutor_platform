from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import SessionBooking
from profiles.models import LearnerProfile
from django.shortcuts import render
from .models import SessionBooking, Feedback
from .forms import FeedbackForm

User = get_user_model()


@login_required
def book_session(request, tutor_id):
    if request.method == "POST" and request.user.role == "learner":
        tutor = get_object_or_404(User, id=tutor_id, role="tutor")
        learner_profile = get_object_or_404(LearnerProfile, user=request.user)

        SessionBooking.objects.create(
            learner=request.user,
            tutor=tutor,
            subject=learner_profile.subject_needed,
            date="2026-03-25",
            time="17:00",
            status="pending"
        )

    return redirect("dashboard")


@login_required
def update_booking_status(request, booking_id, action):
    booking = get_object_or_404(SessionBooking, id=booking_id)

    if request.method == "POST" and request.user == booking.tutor:
        if action == "accepted":
            booking.status = "accepted"
        elif action == "rejected":
            booking.status = "rejected"
        booking.save()

    return redirect("dashboard")
@login_required
def give_feedback(request, booking_id):
    booking = get_object_or_404(SessionBooking, id=booking_id, learner=request.user)

    if booking.status != "accepted":
        return redirect("dashboard")

    if hasattr(booking, 'feedback'):
        return redirect("dashboard")

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.booking = booking
            feedback.learner = request.user
            feedback.tutor = booking.tutor
            feedback.save()
            return redirect("dashboard")
    else:
        form = FeedbackForm()

    return render(request, "bookings/give_feedback.html", {
        "form": form,
        "booking": booking
    })