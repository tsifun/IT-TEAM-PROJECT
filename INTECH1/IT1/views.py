#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
         return render(request, 'IT1/home.html')
def about(request):
         return render(request, 'IT1/about.html')
def countries(request):
         return render(request, 'IT1/countries.html')


def africa(request):
         return render(request, 'IT1/africa.html')


def america(request):
    return render(request, 'IT1/america.html')
def europe(request):
    return render(request, 'IT1/europe.html')
def asia(request):
    return render(request, 'IT1/asia.html')
def australia(request):
    return render(request, 'IT1/australia.html')

# Create your views here.
