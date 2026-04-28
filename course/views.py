from django.shortcuts import render
from .models import Question, Choice, Submission


def submit(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        total = 0
        score = 0

        questions = Question.objects.all()

        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))
            if selected_choice_id:
                choice = Choice.objects.get(id=selected_choice_id)

                Submission.objects.create(
                    user_name=user_name,
                    question=question,
                    selected_choice=choice
                )

                total += 1
                if choice.is_correct:
                    score += 1

        context = {
            'score': score,
            'total': total
        }

        return render(request, 'course/result.html', context)


def show_exam_result(request):
    submissions = Submission.objects.all()

    total = submissions.count()
    correct = 0

    for sub in submissions:
        if sub.selected_choice.is_correct:
            correct += 1

    context = {
        'score': correct,
        'total': total
    }

    return render(request, 'course/result.html', context)
