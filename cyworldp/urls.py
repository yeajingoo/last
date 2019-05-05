"""cyworldp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from cy import views, urls
from realcy import urls as realcy_urls
from products import urls as products_urls
from products.views import list



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="main"),
    path('cy/', include(urls)),
    path('realcy/', include(realcy_urls)),
    # path('create/', views.create, name="create"),
    path('list/', views.list, name="list"),
    path('products/', include('products.urls')),
]
