from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "🎉 تم إنشاء الحساب بنجاح! تم تسجيل دخولك تلقائيًا.")
            return redirect('product_list')
        else:
            messages.error(request, "❌ يوجد خطأ في البيانات. الرجاء التأكد من الحقول.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
