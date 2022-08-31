from django.urls import path, include
from rest_framework import routers
from rest_framework import mixins, viewsets
from api import views
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from rest_framework.decorators import action
app_name = 'api'
# router = routers.DefaultRouter()
router = routers.SimpleRouter()
# router.register(r'result', views.ResultList, basename='MyResult')
router.register(r'total', views.TestDetail)
router.register(r'questions', views.QuestionsList)
router.register(r'options', views.OptionsList)
router.register(r'tests', views.TestList)
router.register(r'answer', views.AnswerList)


urlpatterns = [
    path('', include(router.urls)),
    # path(r'^result/(?P<user_pk>\d+)/(?P<test_pk>\d+)/', views.ResultList.as_view({'get': 'list'}), name='result-list'),
    path('result/<int:user>/<int:test>/',views.result,name="result" ),
    path('chart/<int:user>/<int:test>/',views.chart,name="chart" ),
    # path('questions/', views.QuestionsList.as_view(), name='questionsview'),
    # path('questions/', views.QuestionsList.as_view(), name='questionsview'),
    # path('questions/<int:pk>', views.QuestionDetail.as_view(), name='questionsdetail'),
    # path('options/', views.OptionsList.as_view(), name='optionsview'),
    # path('options/<int:pk>', views.OptionsDetail.as_view(), name='optionsdetail'),
    # path('users/', views.UserList.as_view(), name='userview'),
    # path('users/<int:pk>', views.UserDetail.as_view(), name='userdetail'),
    # path('tests/', views.TestList.as_view(), name='testsview'),
    # path('total/', views.TestDetail.as_view(), name='totalview'),
    # path('answer/', views.AnswerList.as_view(), name='answerview'),
    # path('result/', views.ResultList.as_view, name='resultview'),
]

# urlpatterns += router.urls
