import os
from pathlib import Path
from django.contrib.messages import constants as messages
from dotenv import load_dotenv
import cloudinary

# تحميل متغيرات البيئة
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

# المسار الأساسي
BASE_DIR = Path(__file__).resolve().parent.parent

# مفاتيح الأمان
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'accounts',
    'products',
    'orders',
    'cart',
    'wishlist',
    'reviews',
    'checkout',
    'dashboard',
    'settingsapp',
    'notifications',

    # مكتبات خارجية
    'cloudinary',
    'cloudinary_storage',
    'widget_tweaks',
]

# الوسيطات
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# الراوتر
ROOT_URLCONF = 'ecomstore.urls'

# القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'ecomstore.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'asia/riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'

# معرف الحقول التلقائي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# نموذج المستخدم
AUTH_USER_MODEL = 'accounts.CustomUser'

# إعادة التوجيه
LOGIN_REDIRECT_URL = 'product_list'
LOGOUT_REDIRECT_URL = 'login'

# رسائل التنبيه
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# إعدادات Cloudinary من .env
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

# التخزين الافتراضي للصور
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


