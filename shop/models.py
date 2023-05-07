from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Brand(models.Model):
    brand = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    
    class Meta:        
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand

class Category(MPTTModel):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ('name',)

    class Meta:        
        unique_together = [['parent', 'slug']]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])
    

class Product(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"id": self.id, "slug": self.slug})
    
class Gallery(models.Model):
    images = models.ImageField(upload_to='products/Gallery', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.product.name