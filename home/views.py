from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable' : 'vishwa',
        'variable_name' : 'Raj'
    }
    return render(request,'index.html', context)
    # return HttpResponse("welcome to home page vishwa in home app")

def about(request):
    return HttpResponse("welcome to about page")
