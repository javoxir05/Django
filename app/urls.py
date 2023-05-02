from django.urls import path
from .views import Home, Contact, About, Login, Blog, ProductDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('blog/', Blog.as_view(), name='blog'),
    path('contact/', Contact.as_view(), name='contact'),
    path('login/', Login.as_view(), name='login'),
    # path('product-detail/<int:pk>', ProductDetail.as_view(), name='product_detail')
]
