from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get("sort", None)
    if sorting == None:
        phones = Phone.objects.all()
    elif sorting == 'name':
        phones = sorted(Phone.objects.all(), key = lambda x: x.name)
    elif sorting == 'min_price':
        phones = sorted(Phone.objects.all(), key = lambda x: x.price)
    elif sorting == 'max_price':
        phones = sorted(Phone.objects.all(), key = lambda x: x.price, reverse = True)
    context = {'phones':phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    item = Phone.objects.get(slug=slug)
    context = {'phone':item}
    return render(request, template, context)
