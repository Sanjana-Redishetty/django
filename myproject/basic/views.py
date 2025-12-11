from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def sample(request):
    return HttpResponse("hello")
def sample1(request):
    return HttpResponse("welcome to django")