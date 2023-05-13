from .models import WishList
from django.contrib import messages

def wishlist(request):
    try:
        wishlist = WishList.objects.filter(user=request.user)
    except:
        wishlist = 0 

    return {'wishlist': wishlist}