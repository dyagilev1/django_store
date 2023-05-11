from django.shortcuts import render
from django.views import generic
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def wishlist_view(request):
    wishlist = WishList.objects.all()
    context = {
        "w":wishlist
    }
    return render(request, "wishlist/wishlist.html")


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
        new_wishlist = WishList.objects.create(product=product,
                                               user=request.user)
        context = {
            "bool": True
        }
        return JsonResponse(context)

