from django.shortcuts import render, redirect

import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def page1(request):
    return render(request, 'ronaldo.html')

def page2(request):
    return render(request, 'gst.html')

def page3(request):
    return render(request, 'chess.html')


def page4(request):
    return render(request, 'zomato.html')

def page5(request):
    return render(request, 'trade.html')

def page6(request):
    return render(request, 'tai.html')

def page7(request):
    return render(request, 'whatsapp.html')

def page8(request):
    return render(request, 'cwg.html')

def page9(request):
    return render(request, 'tesla.html')
