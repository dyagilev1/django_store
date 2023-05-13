from .models import WishList
from django.contrib import messages

def wishlist(request):
    try:
        wishlist = WishList.objects.filter(user=request.user)
    except:
        messages.warning(request, "You need to login before")
        wishlist = 0 

    return {'wishlist': wishlist}