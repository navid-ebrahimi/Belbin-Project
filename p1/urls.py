from django.urls import path, include
from rest_framework import routers

from p1 import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

app_name = 'roshan'
urlpatterns = [
    path('start/', views.start),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_excel, name='upload'),
    # path('', include(router.urls)),

    path('result/<int:user>/<int:test>/', views.result.as_view(), name='result'),
]