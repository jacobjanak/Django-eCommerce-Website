from django.shortcuts import render, redirect

from .models import Item


def index(request):
    return render(request, 'ceramics/index.html', {'no_footer': True})

def work(request):
    return render(request, 'ceramics/work.html', {'active_link': 'work'})

def store(request):
    items = Item.objects.all()
    return render(request, 'ceramics/store.html', {'active_link': 'store', 'items': items})

def about(request):
    return render(request, 'ceramics/about.html', {'active_link': 'about'})

def events(request):
    return render(request, 'ceramics/events.html', {'active_link': 'events'})

def product(request):
    print(request.path)
    item_id = request.path.strip('store/item/')
    print(item_id)
    product = Item.objects.get(id=item_id)
    return render(request, 'ceramics/product.html', {'active_link': 'store', 'product': product})
