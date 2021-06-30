"""apirest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from os import name
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import exception_handler
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from rest_framework import permissions, exceptions
from api import views_orders, views_products


urlpatterns = [
    path('admin', admin.site.urls),
    path('token', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),

    #create producto and categories
    path('product/add', views_products.productCreate, name="create_product"),
    path('categorie/add', views_products.categorieCreate, name="create_categorie"),

    #create order and status for this
    path('status/add', views_orders.statusCreated, name="create_status"),
    path('order/add', views_orders.orderCreated, name="create_order")
]
