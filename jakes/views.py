from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm  
from .models import Product
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View (NO template, as requested)
def logout_view(request):
    logout(request)
    return redirect('login')

def product(request):
    products = Product.objects.all().order_by('id')  # or any stable field
    paginator = Paginator(products, 20)
  # Show 20 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"product.html",{'page_obj': page_obj})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'jakes/product_detail.html', {'product': product})



@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'jakes/product_create.html', {'form': form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.created_by != request.user:
        return redirect('product_detail', pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'jakes/product_edit.html', {'form': form})

# Delete view
@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.created_by != request.user:
        return redirect('product_detail', pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product')

    return render(request, 'jakes/product_confirm_delete.html', {'product': product})
