import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'services/index.html')

def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    string = request.GET.get('string')
    font = request.GET.get('font')
    
    url = 'http://artii.herokuapp.com/make?text='
    url += string
    url += '&font='+font
    response = requests.get(url)
    context = {
        'result': response.text,
    }
    return render(request, 'services/artii_result.html', context)