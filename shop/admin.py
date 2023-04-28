
from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Category, Product
from django_mptt_admin.admin import DjangoMpttAdmin


class CategoryMPTTModelAdmin(DjangoMpttAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Category, CategoryMPTTModelAdmin)
