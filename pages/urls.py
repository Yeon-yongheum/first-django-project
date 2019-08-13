from django.urls import path
from . import views

# 1. url 설정
# pages app의 views.py 파일 불러오기
urlpatterns = [
    # path(url, 해당하는 views의 함수)
    #url의 특정 값을 변수처럼 활용
    path('', views.index),
    path('hello/<str:name>/', views.hello),
    path('lotto/', views.lotto),
    path('dinner/', views.dinner),
    path('cube/<int:숫자>/', views.cube),
    path('about/<str:name>/<int:age>/',views.about),
    path('isitgwangbok/',views.isitgwangbok),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('signup/', views.signup),
    path('signup_result/', views.signup_result),
]