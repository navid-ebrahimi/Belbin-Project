import requests
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from api.serializers import *
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import viewsets
from braces.views import JSONResponseMixin
from django.http import JsonResponse, HttpResponse, FileResponse, Http404
import matplotlib.pyplot as plt
from fpdf import FPDF
import pandas as pd
from pandas import DataFrame
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from matplotlib.backends.backend_pdf import PdfPages
import io
from prettytable import PrettyTable




# Create your views here.
class TestList(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestsSerializer


class AnswerList(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class TestDetail(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = getTestSerializer

class QuestionsList(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class QuestionDetail(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class OptionsList(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class OptionsDetail(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def result_dictionary(user, test):
    res = {'IMP': 0, 'CO': 0, 'SH': 0, 'PL': 0,
           'RI': 0, 'ME': 0, 'TW': 0, 'CF': 0
           }

    lists = [['RI', 'TW', 'PL', 'CO', 'CF', 'SH', 'IMP', 'ME'], ['IMP', 'CO', 'RI', 'ME', 'SH', 'TW', 'PL', 'CF'],
             ['CO', 'CF', 'SH', 'PL', 'TW', 'RI', 'ME', 'IMP'], ['TW', 'SH', 'ME', 'IMP', 'PL', 'CF', 'RI', 'CO'],
             ['ME', 'IMP', 'TW', 'SH', 'RI', 'CO', 'CF', 'PL'], ['PL', 'TW', 'CO', 'CF', 'ME', 'IMP', 'SH', 'RI'],
             ['SH', 'ME', 'CF', 'RI', 'IMP', 'PL', 'CO', 'TW']]
    set = Answers.objects.filter(user=user).filter(Option__Question__Test=test)
    for i in range(set.count()):
        x = (set[i].Option.id) % 8
        if (x != 0):
            res[lists[set[i].Option.Question.id - 1][x - 1]] += set[i].number
        else:
            res[lists[set[i].Option.Question.id - 1][7]] += set[i].number

    return res

def result(request, user, test):
    dic = result_dictionary(user,test)
    return JsonResponse(dic,safe=False)


def grade(score):
    if (score < 30):
        return "Low"
    elif(score >= 30 and score < 50):
        return "Middle"
    else:
        return "High"

def chart(request, user, test):
    dic = result_dictionary(user, test)
    keys_list = list(dic.keys())
    values_list = list(dic.values())
    data = {'keys_list' : keys_list,
            'values_list' : values_list}

    plt.figure()
    df = pd.DataFrame(data, columns=["keys_list", "values_list"])
    df.plot(x="keys_list", y="values_list",color='blue', marker='o', grid=True)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, dpi=200)

    pdf = FPDF()
    pdf.add_page()
    pdf.image(img_buf, w=pdf.epw)
    pdf.add_page()

    ################################### table
    data = []
    for i in range(len(keys_list)):
        data.append((f"{keys_list[i]}", f"{values_list[i]}", grade(values_list[i]), "Saint-Mahturin-sur-Loire"))
    data = tuple(data)

    pdf.set_font("Times", size=10)
    line_height = pdf.font_size * 3
    column_width = pdf.epw / 4
    pdf.ln(6*line_height)
    for row in data:
        for datum in row:
            pdf.multi_cell(column_width, line_height, datum, border=1,
                           new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.ln(line_height)
    ###################################
    data = {'CF': 3,
            'IMP': 0}
    plt.figure()
    df = pd.DataFrame(data, columns=["CF", "IMP"])
    df.plot(x="CF", y="IMP",color='blue', marker='o', grid=True, polar=True)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, dpi=200)








    ###################################
    pdf.output('Charts.pdf')
    img_buf.close()
    try:
        return FileResponse(open('Charts.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()