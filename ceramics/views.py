from django.shortcuts import render, redirect


def index(request):
    return render(request, 'ceramics/index.html', {'no_footer': True})

def work(request):
    return render(request, 'ceramics/work.html', {'active_link': 'work'})

def store(request):
    return render(request, 'ceramics/store.html', {'active_link': 'store'})

def about(request):
    return render(request, 'ceramics/about.html', {'active_link': 'about'})

def events(request):
    return render(request, 'ceramics/events.html', {'active_link': 'events'})
