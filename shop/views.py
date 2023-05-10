from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Gallery,  Variants, Brand, Gender, WishList
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger 





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


    return render (request, 'shop/product/list.html', context={
        'category': category,
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
    
    images = Gallery.objects.filter(product=product)

    cart_product_form = CartAddProductForm()
    context = {'product': product,
                'cart_product_form': cart_product_form,
                'category': category,
                'categories': categories,
                'images': images, }

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
                                                                'brand': brand,                                                               'gender': gender,
                                                                })


def wishlist_view(request):
    category = None
    categories = Category.objects.all()
    return render(request, "shop/product/wishlist.html", context={'category': category,
                                                                'categories': categories,})

# def WishList_view(request):
#     wishlist = WishList_model.objects.all()
#     context = {
#         "w":wishlist
#     }
#     return render(request, "shop/wishlist.html", context)



# def add_to_wishlist(request):
#     product_id = request.GET['id']
#     product = Product.objects.get(id=product_id)
    
#     context = {}

#     wishlist_count = wishlist_model.objects.filter(product=product, uses=request.user).count()
