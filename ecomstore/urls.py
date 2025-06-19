from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # تسجيل الدخول والخروج
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # تسجيل حساب جديد (من accounts/urls.py)
    path('accounts/', include('accounts.urls')),

    # التطبيقات الأخرى
    path('', include('products.urls')),          # الصفحة الرئيسية: المنتجات
    path('products/', include('products.urls')), # المنتجات
    path('cart/', include('cart.urls')),         # السلة
    path('orders/', include('orders.urls')),     # الطلبات
]

# عرض ملفات الصور والوسائط في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
