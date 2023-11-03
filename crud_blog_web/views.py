from django.http import HttpResponse
from django.template import loader
from .models import Article
from django.shortcuts import render
from .models import Product


def index(request):
    article = Article.objects.order_by('title')
    template = loader.get_template('index.html')
    context = {
        'article': article,
    }
    return HttpResponse(template.render(context, request))

def product_list(request):
    # Pobierz parametry zapytania z request.GET
    category = request.GET.get('category')
    max_price = request.GET.get('max_price')
    in_stock = request.GET.get('in_stock')

    # Początkowy queryset
    products = Product.objects.all()

    # Filtruj według kategorii, jeśli parametr 'category' jest obecny
    if category is not None:
        products = products.filter(category__name=category)

    # Filtruj według maksymalnej ceny, jeśli parametr 'max_price' jest obecny
    if max_price is not None:
        products = products.filter(price__lte=max_price)

    # Filtruj, aby pokazać tylko te produkty, które są dostępne
    if in_stock == '1':
        products = products.filter(in_stock=True)

    # Zwróć przefiltrowane produkty do szablonu
    return render(request, 'index.html', {'products': products})


def myNextPage(request):
    return HttpResponse("<b>To jest moja następna strona!</b>")
def home(request):
    latest_products = Product.objects.all()[:5]
    return render(request, 'home.html', {'latest_products': latest_products})