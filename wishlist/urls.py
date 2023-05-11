from django.urls import path

from . import views

app_name = 'wishlist'

urlpatterns = [
    path('wishlist/', views.wishlist_view, name='wishlist_view'),

    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),

]