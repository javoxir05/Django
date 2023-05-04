from django.urls import path
from .views import Home, Contact, About, Login, Blog, Properties, Agents, ProductDetail


urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('properties/', Properties.as_view(), name='properties'),
    path('agents/', Agents.as_view(), name='agents'),
    path('blog/', Blog.as_view(), name='blog'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('login/', Login.as_view(), name='login'),
    path('productdetail/', ProductDetail.as_view(), name='productdetail'),
    # path('product-detail/<int:pk>', ProductDetail.as_view(), name='product_detail')
]
