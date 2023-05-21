
from django.contrib import admin

from .models import Category, Product, Brand, Gallery, Size, Variants, Gender, ProductReview
from django_mptt_admin.admin import DjangoMpttAdmin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

from django_mptt_admin.admin import DjangoMpttAdmin
class CategoryMPTTModelAdmin(DjangoMpttAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


class ProductResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Product



class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class ProductVariantInline(admin.TabularInline):
    model = Variants
    extra = 1
    show_change_link = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'gender', 'slug', 'price', 'available', 'created', 'updated',)
    list_filter = ('available', 'created', 'updated', 'category', 'gender')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GalleryInline, ProductVariantInline]



class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand', 'slug',)
    prepopulated_fields = {'slug': ('brand',)}


class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender', 'code',)
    prepopulated_fields = {'code': ('gender',)}


class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    prepopulated_fields = {'code': ('name',)}



class VariantsAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'size',)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review', 'rating')


admin.site.register(Category, CategoryMPTTModelAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Variants, VariantsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)





         #IMPORT EXPORT DB
          
# class ProductAdmin(ImportExportActionModelAdmin):
#     resource_class = ProductResource
#     list_display = [field.name for field in Product._meta.fields if field.name != "id"]



# admin.site.register(Product, ImportExportActionModelAdmin)

