from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.contrib import messages


def wishlist_view(request):

    category = None
    categories = Category.objects.all()

    if  request.user.is_authenticated:
        wishlist = WishList.objects.filter(user=request.user)
    else:
        wishlist = WishList.objects.filter()

    context = {
        "w":wishlist,
        'category': category,
        'categories': categories,
    }
    return render(request, "wishlist/wishlist.html", context)


def add_to_wishlist(request):
    product_id = request.GET['id']
    product = Product.objects.get(id=product_id)

    context = {}

    wishlist_count = WishList.objects.filter(product=product, user=request.user).count()
    if wishlist_count > 0:
        context = {
            "bool": True
        }
    else:
        new_wishlist = WishList.objects.create(
            user=request.user,
            product=product,
        )
        
        context = {
            "bool": True,
            
        }
    return JsonResponse(context)


def remove_wishlist(request):
    pid = request.GET['id']
    wishlist = WishList.objects.filter(user=request.user)
    wishlist_d = WishList.objects.get(id=pid)
    delete_product = wishlist_d.delete()

    context = {
        "bool": True,
        "w":wishlist
    }
    wishlist_json = serializers.serialize('json', wishlist)
    t = render_to_string("wishlist/wishlist-list.html", context)
    return JsonResponse({"data": t, "w":wishlist_json})
