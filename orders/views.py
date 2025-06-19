from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product

def create_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_detail')

    total_price = 0
    order_items = []

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_price += product.price * quantity
        order_items.append((product, quantity, product.price))

    # إنشاء الطلب
    order = Order.objects.create(user=request.user, total_price=total_price)

    # إنشاء العناصر داخل الطلب
    for product, quantity, price in order_items:
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price
        )

    # تفريغ السلة
    request.session['cart'] = {}

    return render(request, 'orders/order_success.html', {'order': order})
