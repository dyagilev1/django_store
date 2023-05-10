from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index),
    path('wishlist/', views.wishlist_view, name='wishlist_view'),

    path('search/', views.search_product, name='search_product'),

    path('product_list', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    #Search
]