from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    x = 12
    y = 2
    return render(request, 'hello.html', {'name': 'Suvendu'})