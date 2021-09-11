from django.shortcuts import render
from .models import Choice, Question

def q(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question_id=question_id)
    context = {
        'question': question,
        'choices': choices,
        }
    return render(request, 'q.html', context)