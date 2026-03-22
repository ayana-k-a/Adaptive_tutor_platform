from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profiles.models import LearnerProfile, TutorProfile

def calculate_match_score(learner, tutor):
    score = 0

    # subject match
    tutor_subjects = [s.strip().lower() for s in tutor.subjects.split(',') if s.strip()]
    learner_subject = learner.subject_needed.strip().lower()

    if learner_subject in tutor_subjects:
        score += 40

    # learning style ↔ teaching style
    if learner.learning_style and learner.learning_style == tutor.teaching_style:
        score += 30

    # mode match
    if learner.preferred_mode == tutor.available_mode:
        score += 15
    elif tutor.available_mode == 'both' or learner.preferred_mode == 'both':
        score += 10

    # simple availability overlap check
    if learner.availability and tutor.availability:
        learner_times = learner.availability.lower()
        tutor_times = tutor.availability.lower()
        if learner_times in tutor_times or tutor_times in learner_times:
            score += 15

    return score

@login_required
def match_tutors(request):
    if request.user.role != 'learner':
        return render(request, 'matching/not_allowed.html')

    learner = LearnerProfile.objects.get(user=request.user)
    tutors = TutorProfile.objects.all()

    matched_tutors = []
    for tutor in tutors:
        score = calculate_match_score(learner, tutor)
        if score > 0:
            matched_tutors.append({
                'tutor': tutor,
                'score': score
            })

    matched_tutors = sorted(matched_tutors, key=lambda x: x['score'], reverse=True)

    return render(request, 'matching/match_results.html', {
        'learner': learner,
        'matched_tutors': matched_tutors
    })