from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': 'this is sent'
    }
    return render(request, 'index.html', context)
   # return HttpResponse("welcome to home page")

def about(request):
    return render(request, 'about.html')
  #  return HttpResponse("welcome to about page")

def contact(request):
    return render(request, 'contact.html')
  #  return HttpResponse("welcome to contact page")

def Maidservices(request):
    return render(request, 'services.html')


