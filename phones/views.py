from django.shortcuts import render, redirect
from .models import Phone

# Create your views here.

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sortType = request.GET.get('sort', 'name')
    if sortType == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sortType == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    elif sortType == 'min_price':
        phones = Phone.objects.all().order_by('price')
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)