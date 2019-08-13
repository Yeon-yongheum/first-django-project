import random
import datetime

from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'pages/index.html')

def hello(request, name):
    context = {'name': name}
    return render(request, 'pages/hello.html', context)

def lotto(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1, 46), 6))
    # 변수를 딕셔너리에 담아서 (보통 context라고 부름)
    context = {'numbers': numbers}
    # render 할때 3번째 인자로 넘겨준다.
    # render 함수의 필수 인자 : request, template 파일 
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language 이다.
    return render(request, 'pages/lotto.html', context)

def dinner(request):
    menus = ['햄버거', '편도', '응급실떡볶이', '노운각', '피자', '치킨']
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'menus': menus,
        'users': [],
        'sentence': 'life is short, you need python + django!',
        'datetime_now': datetime.datetime.now(),
        'google_link': 'https://www.google/com'
    }
    return render(request, 'pages/dinner.html', context)

def cube(request, 숫자):
    context = {
        'result': 숫자**3,
        '숫자': 숫자,
        'numbers': [0,1,2],
        'students': {'ab': 'ab!!!', 'cd': 'cd!!!!!'},
    }
    return render(request, 'pages/cube.html', context)

def about(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/about.html', context)

def isitgwangbok(request):
    # context = {
    #     'datetime_now': str(datetime.date.today())
    # }
    # return render(request, 'pages/isitgwangbok.html',context)
    now = datetime.datetime.now()
    if now.month == 8 and now.day == 15:
        result = True
    else:
        result = False
        context = {
            'result': result
        }
    return render(request, 'pages/isitgwangbok.html', context)

def ping(request):
    return render(request, 'pages/ping.html')    

def pong(request):
    # 사용자가 넘겨주는 값 받아오기
    # print(request.GET)# QueryDict
    data = request.GET.get('data')
    context = {
        'data': data
    }
    return render(request, 'pages/pong.html', context)

def signup(request):
    return render(request, 'pages/signup.html')

def signup_result(request):
    name = request.POST.get('name')
    psw = request.POST.get('psw')
    psw_confirm = request.POST.get('psw_confirm')
    is_signup = True
    # yesorno = True
    # if psw == psw_confirm:
    #     result = f'{name}님 회원가입 되셨습니다.'
    # else:
    #     result = f'{name}님 비밀번호가 같지 않습니다.'
    #     yesorno = False
    # context = {
    #     'result': result,
    #     'yesorno': yesorno
    # }
    if psw == psw_confirm:
        is_signup = True
    else:
        is_signup = False
    
    context = {
        'is_signup': is_signup,
        'name': name
    }
    return render(request, 'pages/signup_result.html', context)