from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register/',views.createUser,name="register"),
    path('verify/',views.verifyUser,name="verify"),
    path('login/',views.login_function,name="login"),
    path('success/',views.success,name="success"),
    path('logout/',views.logout_function,name='logout')
]
