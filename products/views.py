from django.shortcuts import render, redirect
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
        print('📦 الملفات المرسلة:', request.FILES)  # لفحص الصور

        # لا نمرر request.FILES للفورم لأنه لا يحتوي على حقل صورة
        form = ProductForm(request.POST)

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
            messages.error(request, '⚠️ حدث خطأ أثناء إضافة المنتج. تحقق من الحقول.')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})
