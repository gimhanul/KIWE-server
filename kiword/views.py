from django.shortcuts import redirect, render
from .models import Choice, Question, KeywordRelated, Keyword, Usermemory, Each
from datetime import date 
from django.http import JsonResponse
import json

def q(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question_id=question_id)
    context = {
        'question': question,
        'choices': choices,
    }

    if request.method == 'POST':
        if request.POST.get('oncedata') == '1' or request.POST.get('oncedata') == '3':
            question_id = question_id+2
        else:
            question_id=question_id+1
        if question_id>=4:
            return redirect('/keyword')
        return redirect('/q/%s' %question_id)

    return render(request, 'q.html', context)
    

    
class Rank():
    def __init__(self, score, keyword_str):
        self.score = score
        self.keyword_str = keyword_str

    def __repr__(self):
        return repr((self.score, self.keyword_str))


def kiword(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['dt']=='k':
            one = data['one']
            two = data['two']
            three = data['three']
            if one != 2:
                two=-1
            today = date.today()
            birth = request.user.birth
            birth = (today.year - birth.year + 1)//10
            keywords = KeywordRelated.objects.filter(question='10', choice=birth).values('keyword')
            recomm = []

            for i in keywords:
                score = 0
                if (KeywordRelated.objects.filter(keyword_id=i['keyword'], question='2', choice=two)).exists():
                    score += 1
                if (KeywordRelated.objects.filter(keyword_id=i['keyword'], question='3', choice=three)).exists():
                    score += 1
                words = Rank(score, Keyword.objects.filter(id=i['keyword']).values('keyword')[0]['keyword'])
                recomm.append(words)

            recomm = sorted(recomm, key=lambda rank : rank.score, reverse=True)
            recomm = [i.keyword_str for i in recomm]

            usermemory = Usermemory.objects.create(user = request.user)
            usermemory.save()

            return JsonResponse({'recomm':recomm}, safe=False)

            
        elif data['dt'] == 'time' or data['dt'] == 'end':
            usermemory = Usermemory.objects.filter(user=request.user).latest('id')
            each = Each.objects.create(memory_id=usermemory, keyword = data['keyword'], time = float(data['while']))
            each.save()

            if data['dt'] == 'end':
                usermemory.longestt = data['longestt']
                usermemory.longestk = data['longestk']
                usermemory.shortestt = data['shortestt']
                usermemory.shortestk = data['shotestk']
                usermemory.save()
                


    return render(request, 'keyword.html')

def memories(request):
    usermemory = Usermemory.objects.filter(user=request.user)
    usermemory = reversed(usermemory)

    context = {
        'usermemory': usermemory,
    }
    return render(request, 'memories.html', context)
    

def memory(request, usermemory_id):
    words = []
    each = Each.objects.filter(memory_id=usermemory_id)
    for i in each:
        temp = (i.keyword, i.time)
        words.append(temp)

    context = {
        'id': usermemory_id
    }
    
    return render(request, 'memory.html', context)

#def word_cloud(usermemory_id):