from django.contrib import admin
from .models import WishList



class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')


admin.site.register(WishList, WishListAdmin)
