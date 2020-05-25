from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Product

# Create your views here.
# ? HOME View
class ProductListView(ListView):
    model = Product
    template_name = "store/home.html"
    context_object_name='products'
    ordering = ['-date_posted']

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
        'catagory',
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
        'catagory',
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