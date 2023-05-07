from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Gallery
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger 

from django.contrib.postgres.search import SearchVector


def index(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'shop/index.html', context={
        'category': category,
        'categories': categories,
        'products': products,
    })
    

def product_list(request, category_slug=None):



    category = None
    categories = Category.objects.all()


    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 9)    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    


    
    return render (request, 'shop/product/list.html', context={
        'category': category,
        'categories': categories,
        'products': products,
        'page': page,
    })


def product_detail(request, id, slug):
    category = None
    categories = Category.objects.all()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    
    images = Gallery.objects.filter(product=product)

    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', context={'product': product,
                                                        'cart_product_form': cart_product_form,
                                                                'category': category,
                                                                'categories': categories,
                                                                "images": images})


def search_product(request):
    category = None
    categories = Category.objects.all()

    query = request.GET.get("q")

    products = Product.objects.filter(name__icontains=query)
    return render(request, 'shop/product/search.html', context={'products': products,
                                                               'query': query,
                                                               'category': category,
                                                                'categories': categories,
                                                               })