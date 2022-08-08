from django.shortcuts import render, HttpResponse

# Create your views here.
# print("hello!")

def say_hello(request):
    return HttpResponse("Hello!")
