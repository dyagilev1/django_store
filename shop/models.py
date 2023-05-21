from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User




############ BRAND ############

class Brand(models.Model):
    brand = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    
    class Meta:        
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand




############ GENDER ############

class Gender(models.Model):
    gender = models.CharField(max_length=20, blank=True, null=True)
    code = models.SlugField(max_length=10,  blank=True, null=True)

    class Meta:        
        verbose_name = 'gender'
        verbose_name_plural = 'genders'

    def __str__(self):
        return self.gender



############ CATEGORY ############

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
    


############ PRODUCT ############

class Product(models.Model):

    VARIANTS = (
        ('None','None'),
        ('Size', 'Size')
    )

    SEASONS = (
        ('None', 'None'),
        ('Fall/Winter', 'Fall/Winter'),
        ('Hot Summer', 'Hot Summer'),
        ('Autumn/Winter', 'Autumn/Winter'),
        ('Spring/Summer', 'Spring/Summer'),
    )

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products',blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    season = models.CharField(max_length=20, choices=SEASONS, default='None')
    new_arrival = models.BooleanField(default=False)
    top_seller = models.BooleanField(default=False)


 
 
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"id": self.id, "slug": self.slug})
    


############ GALLERY FOR PRODUCT ############

class Gallery(models.Model):
    images = models.ImageField(upload_to='products/Gallery', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.product.name
    


############ PRODUCT SIZE ############

class Size(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name
    


############ PRODUCT VARIANT ############

class Variants(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    

############ RATING SYSTEM ############

RATING=(
    ('1','★☆☆☆☆'),
    ('2','★★☆☆☆'),
    ('3','★★★☆☆'),
    ('4','★★★★☆'),
    ('5','★★★★★'),
)


############ PRODUCT REVIEW ############
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField(max_length=300)
    rating = models.CharField(max_length=300, choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:        
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return self.product.name
    
    def get_rating(self):
        return self.rating
    



