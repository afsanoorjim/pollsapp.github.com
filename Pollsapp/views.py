
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import*
from django.contrib import messages 

def home(request):
    question = Question.objects.all()
    context = {
        'question':question,
    }
    return render(request, 'home.html', context)

def create(request):
    if request.method == 'POST':
        question = request.POST['poll']
        data = Question(question = question)
        data.save()
        messages.success(request, 'Question Added')
        return redirect(home)
    else:
        context = {
            'message':messages.error(request, 'Error')
        }
        
        return render(request, 'home.html')
    

def addopt(request):
    if request.method == 'POST':
        question_id = request.POST['selected-question']
        choice = request.POST['option']
        selected_question = Question.objects.get(id=question_id)
        selected_question.choices.create(choice=choice)
        selected_question.save()
        messages.success(request, 'Choice added')
        return redirect(home)
        


def vote(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    context = {
        'question':question,
        'options':options
    }
    return render(request, 'vote.html', context)

def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    context = {
        'question':question,
        'options':options,
    }
    if request.method == 'POST':
        selectedOpt = request.POST['selected-option']
        selected_option = options.get(id=selectedOpt)
        selected_option.vote+=1
        selected_option.save()
        return render(request, 'result.html', context)

