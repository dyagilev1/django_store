from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm




@require_POST
def cart_add(request, product_id):
    """Add Product to Cart View"""

    cart = Cart(request)    
    product = get_object_or_404(Product, id=product_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, quantity=cd['quantity'], override_quantity=cd['override'])
        messages.success(request, "Товар було успішно додано до вашого кошика.")
    return redirect('cart:cart_detail')




@require_POST
def cart_remove(request, product_id):
    """Remove Priduct from the Cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, "Товар було успішно видалено з вашого кошика.")
    return redirect('cart:cart_detail')




def cart_detail(request):
    """Cart View"""
    category = None
    categories = Category.objects.all()
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True,
        })
    return render(request, 'cart/detail.html', context={'cart': cart,
                                                        'category': category,
                                                        'categories': categories,})



