from django.shortcuts import render, redirect
from .models import Course, Enrollment, Question, Choice, Submission


def submit(request, course_id):
    course = Course.objects.get(id=course_id)
    enrollment = Enrollment.objects.first()

    submission = Submission.objects.create(
        enrollment=enrollment
    )

    for question in course.question_set.all():
        selected_choice_id = request.POST.get(str(question.id))
        if selected_choice_id:
            choice = Choice.objects.get(id=selected_choice_id)
            submission.choice_set.add(choice)

    return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):
    course = Course.objects.get(id=course_id)
    submission = Submission.objects.get(id=submission_id)

    total_score = 0
    possible_score = 0

    for question in course.question_set.all():
        possible_score += 1
        if question.is_get_score(submission):
            total_score += 1

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score
    }

    return render(request, 'course/exam_result_bootstrap.html', context)
