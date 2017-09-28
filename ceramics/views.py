from django.shortcuts import render, redirect


def index(request):
    return render(request, 'ceramics/index.html')

def work(request):
    return render(request, 'ceramics/work.html')

def store(request):
    return render(request, 'ceramics/store.html')

def about(request):
    return render(request, 'ceramics/about.html')

def events(request):
    return render(request, 'ceramics/events.html')
