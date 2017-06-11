from django.shortcuts import render
from magazine.models import Products
def home(request):
    products = Products.objects.all()
    return render(request, 'magazine/home.html', {'products': products})
