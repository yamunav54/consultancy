from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import  Http404


# Create your views here.
from polls.models import Question


def oldindex(request):
    qlists = Question.objects.order_by('-pub_date')[:]
    result = ','
    for q in qlists:
        print(q.qtext)
        result = result.join([q.qtext])

    return HttpResponse(qlists)


def index(request):
    qlists = Question.objects.order_by('-pub_date')[:]
    context = {'qlist':qlists}
    return render(request,'polls/index.html',context)
    # return HttpResponse(qlists)


    # return render(request,'polls/index.html');

def detail(request, question_id):

    quest = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':quest})


def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected = question.choice_set.get(pk=request.POST['choice'])
    except:
        print("Choice is not set")

        selected.votes +=1
        selected.save()

    return HttpResponseRedirect(reverse('results', args=(question_id,)))


