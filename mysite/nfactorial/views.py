from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello, nfactorial school!")

def add(request, first, second):
    return HttpResponse(first + second)

def upper(request, text):
    return HttpResponse(text.upper())

def palindrome(request, word):
    if (word == word[::-1]):
        return HttpResponse("True")
    else:
        return HttpResponse("False")
    
def calculator(request, first, operation, second):
    if (operation == "add"):
        return HttpResponse(first + second)
    elif (operation == "sub"):
        return HttpResponse(first - second)
    elif (operation == "mult"):
        return HttpResponse(first * second)
    else:
        return HttpResponse(first // second)