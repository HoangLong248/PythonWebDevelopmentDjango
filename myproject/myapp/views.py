from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "name" : "Long Tran",
        "age": 23,
        "nationality": "Viet Nam"
    }
    return render(request, 'index.html', context)