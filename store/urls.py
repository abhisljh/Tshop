"""Tshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import home ,cart, login, orders, signup, signout, show_product , add_to_cart#these are all the function defined in views.py

urlpatterns = [
    path('', home , name='homepage'),
    path('cart/', cart),
    path('orders/', orders),
    path('login/', login),
    path('signup/', signup),
    path('logout/', signout),
    path('product/<str:slug>', show_product),
    path('addtocart/<str:slug>/<str:size>', add_to_cart) #we are abou to get slug and size

]
