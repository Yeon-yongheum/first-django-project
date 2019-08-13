from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'num/index.html')

def push(request):
    return render(request,'num/push.html')

def pull(request):
    num = request.GET.get('num')
    context = {
        'num': num
    }
    return render(request,'num/pull.html', context)