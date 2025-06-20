from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm
import cloudinary.uploader


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            image_file = request.FILES.get('image')
            if image_file:
                result = cloudinary.uploader.upload(image_file, folder='products/')
                product.image = result.get('secure_url')
            product.save()
            messages.success(request, '✅ تم إضافة المنتج بنجاح.')
            return redirect('product_list')
        else:
            messages.error(request, '⚠️ تحقق من الحقول.')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            image_file = request.FILES.get('image')
            if image_file:
                result = cloudinary.uploader.upload(image_file, folder='products/')
                product.image = result.get('secure_url')
            product.save()
            messages.success(request, '✅ تم تعديل المنتج بنجاح.')
            return redirect('product_list')
        else:
            messages.error(request, '⚠️ تحقق من الحقول.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, '🗑️ تم حذف المنتج.')
    return redirect('product_list')
