
from django.contrib import admin

from .models import Category, Product, Brand, Gallery
from django_mptt_admin.admin import DjangoMpttAdmin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class CategoryMPTTModelAdmin(DjangoMpttAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


class ProductResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Product


# class ProductAdmin(ImportExportActionModelAdmin):
#     resource_class = ProductResource
#     list_display = [field.name for field in Product._meta.fields if field.name != "id"]



# admin.site.register(Product, ImportExportActionModelAdmin)
admin.site.register(Category, CategoryMPTTModelAdmin)




class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'slug', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GalleryInline,]



class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand', 'slug',)
    prepopulated_fields = {'slug': ('brand',)}
admin.site.register(Brand, BrandAdmin)


