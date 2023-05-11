from django.contrib import auth
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.timezone import activate

# from .forms import UsersCreationForm, ProductForm
from .models import *
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

# from apps.forms import UsersCreationForm, ProductForm
# from apps.models import User



class Home(View):
    template_name = "index.html"
    context = {}

    def get(self, request):
        products = Product.objects.all().order_by('id')
        self.context['products'] = products
        return render(request, self.template_name, context=self.context)


class Properties(View):
    template_name = 'properties.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)


class Agents(View):
    template_name = 'agents.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)


class Blog(View):
    template_name = 'blog.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)


class About(LoginRequiredMixin, View):
    template_name = 'about.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)


class Contact(View):
    template_name = 'contact.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        full_name = request.POST.get('full_name', None)
        email = request.POST.get('email', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)

        msg = f"""
            From: {full_name}
            Email: {email}
            Message: {message}
        """

        send_mail(
            subject=subject,
            message=msg,
            from_email=email,
            recipient_list=['rahmetruslanov6797@gmail.com'],
            fail_silently=True
        )

        msg = Message.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )
        msg.save()

        return redirect('/contact')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password, first_name=name, last_name=surname)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


class ProductDetail(View):
    template_name = 'single.html'
    context = {}

    def get(self, request, pk):
        if not (request.user.is_authenticated and UserProductView.objects.filter(Q(product_id=pk),
                                                                                 Q(user=request.user)).exists()):
            user_product_view = UserProductView.objects.create(
                product_id=pk,
                user=request.user
            )
            user_product_view.save()
        product = Product.objects.get(pk=pk)
        self.context['product'] = product
        return render(request, self.template_name, context=self.context)

    def post(self, request, pk):
        update_or_delete = request.POST.get('update_or_delete', None)

        if update_or_delete == 'update':
            address = request.POST.get('address', None)
            price = request.POST.get('price', None)
            image1 = request.POST.get('image1', None)
            image2 = request.POST.get('image2', None)
            image3 = request.POST.get('image3', None)
            image4 = request.POST.get('image4', None)
            image5 = request.POST.get('image5', None)
            description = request.POST.get('description', None)
            sale_rent = request.POST.get('sale_rent', None)

            product = Product.objects.get(pk=pk)

            if address:
                product.address = address
            if price:
                product.price = price
            if image1:
                product.image1 = image1
            if image2:
                product.image2 = image2
            if image3:
                product.image3 = image3
            if image4:
                product.image4 = image4
            if image5:
                product.image5 = image5
            if description:
                product.description = description
            if sale_rent:
                product.sale_rent = sale_rent
            product.save()

            return redirect(f'/product-detail/{pk}')
        else:
            Product.objects.get(pk=pk).delete()
            return redirect('/')

def set_language(request, LANGUAGE_SESSION_KEY=None):
    if request.method == 'POST':
        language = request.POST.get('language', None)
        if language:
            request.session[LANGUAGE_SESSION_KEY] = language
            activate(language)
        return redirect(request.META.get('HTTP_REFERER', reverse('home')))


def search(request):
    query = request.GET.get('serarch')
    indexting = Product.objects.filter(name_icontains=query)
    return render(request, 'index.html', {'indexting': indexting})
