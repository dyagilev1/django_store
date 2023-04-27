# from django.contrib import admin
# from .models import Category, SubCategory, Product

# # Register your models here.


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug',)
#     prepopulated_fields = {'slug': ('name',)}

# # @admin.register(SubCategory)
# # class SubCategoryAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'slug', 'category')
# #     prepopulated_fields = {'slug': ('name',)}
# #     category = {'category': ('category',)}





from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product


class CategoryMPTTModelAdmin(MPTTModelAdmin):
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
