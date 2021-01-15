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
from django.urls import path , include
from django.conf.urls.static import static
from Tshop import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),#this is django application so it is having admin in the starting 
    path('', include('store.urls')),#here we only registered the store urls like above django url so when we open django by admin it goes there 

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#we have to define the media url and media root in settings.py of default app 

#main url py
#so this is the main url py files where we include our store url to tell this our app that is store

