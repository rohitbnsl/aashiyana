"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    
    path('',views.index, name= 'home'),
    path('index',views.index, name= 'home'),
    path('aboutus',views.aboutus, name= 'aboutus'),
    path('services',views.services, name= 'services'),
    path('contact',views.contact, name= 'contact'),
    path('buy',views.buy, name='buy'),
    path('insertcontact/',views.insertcontact),
    path('blog/',views.blogview),
    path('blogsdetail/<int:id>',views.blogsdetail),
    path('shop',views.shop, ),
    path('shopdetail/<int:id>',views.shopdetail),
    path('faq/',views.faqview),
    path('signup/',views.signupview),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('sell/',views.sell),
    path('insertsell/',views.insertsell),
    path('buy/',views.buyview),
    path('rent/',views.rentview),
    
]

