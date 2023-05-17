from .models import Product
from django.db.models import Min, Max

def shop(request):

    min_max_price = Product.objects.aggregate(Min('price'), Max('price'))

    return {
        'min_max_price': min_max_price
    }