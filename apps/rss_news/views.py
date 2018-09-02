from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.

def index(request):
    number = random.randrange(0, 1000)
    context = {
        'value' : 'Hello',
        'number' : str(number)
    }
    # return HttpResponse("Hello")
    return render(request, "myHTML.html", context)
