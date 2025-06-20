from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'available']
        labels = {
            'category': 'الفئة',
            'name': 'اسم المنتج',
            'description': 'الوصف',
            'price': 'السعر',
            'available': 'متاح؟'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'name': forms.TextInput(attrs={'placeholder': 'مثال: ساعة ذكية'}),
            'price': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
        }
