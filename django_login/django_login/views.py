from django.shortcuts import render


def first(request):
    return render(request,'first_page.html')

def login(request):
    return render(request,'login.html')

def get_home(request):
    return render(request,'home.html')