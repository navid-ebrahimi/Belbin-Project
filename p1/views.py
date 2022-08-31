from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views import View

from django.views.generic import DetailView
from tablib import Dataset
from django.shortcuts import get_object_or_404
from .resources import *
from .models import *

from django.shortcuts import render

# Create your views here.
def start(request):
    return HttpResponse('start')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return HttpResponse('Log In Successfully')

    else:
        form = AuthenticationForm()
    return render(request,'p1/login.html', {'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponse('SignUp Successfully')
    else:
        form = UserCreationForm()

    return render(request,'p1/signup.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponse('Log Out Successfully')



def upload_excel(request):
    if request.method == 'POST':
        question_resource = QuestionResource()
        dataset = Dataset()
        new_question = request.FILES['myfile']

        if not new_question.name.endswith('xlsx'):
            messages.info(request,'Error')
            return render(request,upload_excel)

        import_data = dataset.load(new_question.read(),format='xlsx')
        for data in import_data:
            if (data[0] != None):
                print(data[0])
                value = Questions.objects.create(
                    Question_Text= data[0],
                    Test= Test.objects.filter(title=data[10]).first(),
                )
                value.save()

                for i in range(1,10):
                    value = Options(
                        Option_Text= data[i],
                        Question= Questions.objects.filter(Question_Text=data[0]).first(),
                    )
                    value.save()

    return render(request,'p1/uploadexcel.html')

#------------------------------------------------------------------------------------------------

class result(View):
    def get(self, request, user, test):
        res = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        set = Answers.objects.filter(user=user).filter(Option__Question__Test=test)
        for i in range(set.count()):
            res[set[i].Option.id%9] += set[i].number
        print(res)

            