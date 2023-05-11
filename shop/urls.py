from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index),

    path('search/', views.search_product, name='search_product'),

    path('product_list', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),


    ### FOOTER ###
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
    path('delivery', views.delivery, name='delivery'),
    path('faq', views.faq, name='faq'),
    path('payment', views.payment, name='payment'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('return_product', views.return_product, name='return_product'),
    
    
    ## add review
    path('ajax-add-review/<int:id>/', views.ajax_add_review, name='ajax-add-review'),

]