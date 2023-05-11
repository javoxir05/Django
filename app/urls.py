from django.urls import path
from . import views
from .views import Home, Contact, About, Blog, Properties, Agents, ProductDetail, search, logout, login, register

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('properties/', Properties.as_view(), name='properties'),
    path('agents/', Agents.as_view(), name='agents'),
    path('blog/', Blog.as_view(), name='blog'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('productdetail/', ProductDetail.as_view(), name='productdetail'),
    path('search/', search, name='search'),
    # path('product-detail/<int:pk>', ProductDetail.as_view(), name='product_detail')
]
