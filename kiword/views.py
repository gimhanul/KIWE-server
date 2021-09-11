from django.shortcuts import render
from .models import Question

def q(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'q.html', context)
