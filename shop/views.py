from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Gallery,  Variants, Brand, Gender, ProductReview
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger 
from .forms import ProductReviewForm
from django.http import JsonResponse




 # Страница при открытии сайта
def index(request):
    category = None
    categories = Category.objects.all()

    gender = Gender.objects.all()
    genderID = request.GET.get('gender')

    products = Product.objects.filter(available=True)

    if genderID:
        products = Product.objects.filter(gender = genderID)
    else:
        Product.objects.all()

    return render(request, 'shop/index.html', context={
        'category': category,
        'categories': categories,
        'products': products,
        'gender': gender
    })
    




#Вывод товаров ||| фильтр по полу, бренду ||| пагинация
def product_list(request, category_slug=None):

    gender = Gender.objects.all()
    genderID = request.GET.get('gender') 

    brand = Brand.objects.all()
    brandID = request.GET.get('brand') 

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
        pass

    if genderID:
        products = Product.objects.filter(gender = genderID)
    elif brandID:
        products = Product.objects.filter(brand = brandID)
    else:
        Product.objects.all()

    cart_product_form = CartAddProductForm()

    return render (request, 'shop/product/list.html', context={
        'category': category,
        'cart_product_form': cart_product_form,
        'categories': categories,
        'products': products,
        'page': page,
        'brand': brand,
        'gender': gender,
    })





#Вывод деталей товара (опис, цена, размеры и т.д.)
def product_detail(request, id, slug):
    category = None
    categories = Category.objects.all()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    
    reviews = ProductReview.objects.filter(product=product)

    review_form = ProductReviewForm()

    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False

    images = Gallery.objects.filter(product=product)

    cart_product_form = CartAddProductForm()
    context = {'product': product,
                'cart_product_form': cart_product_form,
                'category': category,
                'categories': categories,
                'images': images, 
                'reviews': reviews, 
                'review_form': review_form, 
                'make_review': make_review, 
                }

    if product.variant != "None":
        if request.method == 'POST':
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id)
            sizes = Variants.objects.raw('SELECT * FROM  shop_variants  WHERE product_id=%s GROUP BY size_id', [id])
        else:
            variants = Variants.objects.filter(product_id=id)
            sizes = Variants.objects.raw('SELECT * FROM  shop_variants  WHERE product_id=%s GROUP BY size_id', [id])
            variant = Variants.objects.get(id=variants[0].id)

        context.update({'sizes': sizes,
                        'variant': variant,
                        })


    return render(request, 'shop/product/detail.html', context)

                                                               



#Поисковая система по сайту
def search_product(request):
    gender = Gender.objects.all()
    genderID = request.GET.get('gender') 

    brand = Brand.objects.all()
    brandID = request.GET.get('brand') 

    category = None
    categories = Category.objects.all()

    query = request.GET.get("Q")
    products = Product.objects.filter(name__icontains=query)

    if genderID:
        products = Product.objects.filter(gender = genderID)
    elif brandID:
        products = Product.objects.filter(brand = brandID)
    else:
        Product.objects.all() 
    

    return render(request, 'shop/product/search.html', context={'products': products,
                                                                'query': query,
                                                                'category': category,
                                                                'categories': categories,
                                                                'brand': brand,                                                            
                                                                'gender': gender,
                                                                })



def ajax_add_review(request, id):
    product = Product.objects.get(pk=id)
    user = request.user

    review = ProductReview.objects.create(
        user = user,
        product = product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    return JsonResponse({
        'bool': True,
        'context': context,
        })








############ DOWN ##############
def about_us(request):
    category = None
    categories = Category.objects.all()
    return render(request, "shop/info/about_us.html", context={'category': category,
                                                                'categories': categories,})

def contact(request):
    category = None
    categories = Category.objects.all()
    return render(request, "shop/info/contacts.html", context={'category': category,
                                                                'categories': categories,})

def delivery(request):
    category = None
    categories = Category.objects.all()
    return render(request, "shop/info/delivery.html", context={'category': category,
                                                                'categories': categories,})

def faq(request):
    category = None
    categories = Category.objects.all()
    return render(request, "shop/info/faq.html", context={'category': category,
                                                                'categories': categories,})

def payment(request):
    category = None
    categories = Category.objects.all()
    return render(request, "shop/info/payment.html", context={'category': category,
                                                                'categories': categories,})

def privacy_policy(request):
    category = None
    categories = Category.objects.all()
    return render(request, "shop/info/privacy_policy.html", context={'category': category,
                                                                'categories': categories,})

def return_product(request):
    category = None
    categories = Category.objects.all()
    return render(request, "shop/info/return_product.html", context={'category': category,
                                                                'categories': categories,})



