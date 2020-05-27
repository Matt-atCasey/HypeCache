from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import *

# Create your views here.
# ? HOME View
class ProductListView(ListView):
    model = Product
    template_name = "store/home.html"
    context_object_name='products'
    ordering = ['-date_posted']

# ? CART View
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, confirmed=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}

    context={'items':items,'order':order}
    return render(request,'store/cart.html',context)



# ? Filter Products by Category
class FilterListView(ListView): 
    model = Product 
    template_name = "store/home.html" 
    context_object_name='products' 
    ordering = ['-date_posted']

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs.get('category'))


# ? Individual Post View
class ProductDetailView(DetailView):
    model = Product


#? Create Store Post for staff only
class ProductCreateView(CreateView):
    model = Product
    fields=[
        'name',
        'image',
        'condition',
        'brand',
        'category',
        'description',
        'size',
        'colour',
        'price',
        'in_stock',
        'for_sale'
    ]

    #? Update Posts
class ProductUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
    ):
    model = Product
    fields=[
        'name',
        'image',
        'condition',
        'brand',
        'category',
        'description',
        'size',
        'colour',
        'price',
        'in_stock',
        'for_sale'
    ]
    
    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False

# ? Delete Post View
class ProductDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
    ):
    model = Product
    success_url='/'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False