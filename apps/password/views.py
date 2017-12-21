# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
import random
def index(request):
    response = "Hello, I am your first request!"
    chars = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXVYZ!@#$%^&*'
    length = input('password length?')
    length = int(length)
    numberOfPasswords = input('Number of passwords?')
    numberOfPasswords = int(numberOfPasswords)

    for p in range(numberOfPasswords):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(password)
    return HttpResponse(response)