from django.shortcuts import render 
from .models import Product 
from math import ceil 

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = [] # empty list 
    catprods = Product.objects.values('category', 'id') # access all category and id in catprods variable
    cats = {item['category'] for item in catprods} # Using set comprehension remove duplicate categories.
    for cat in cats: # iterating one by one category 
        prod = Product.objects.filter(category=cat) # using filter to add product in category which is similar.
        n = len(prod)  # length of products
        nSlides = n // 4 + ceil((n / 4) - (n // 4))  # 
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    #fetch the products using the Id
    product=Product.objects.filter(id=myid)

    return render(request, 'shop/productView.html', {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')

