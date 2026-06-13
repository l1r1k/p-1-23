from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from catalogue.models import Clothe
from orders.models import Order, PosOrder
from basket.basket import Basket
from .forms import OrderForm

@login_required
def order_show(request):
    context = {
        'form_order': OrderForm
    }
    return render(request, 'order_form.html', context)

@login_required
def order_confirm(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('catalogue')
    
    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(
            user = request.user,
            comment = form.cleaned_data['comment'],
            delivery_address = form.cleaned_data['delivery_address'],
            delivery_type=form.cleaned_data['delivery_type']
        )

        for item in basket:
            pos_order = PosOrder.objects.create(
                clothe=item['product'],
                count=item['count'],
                order=order
            )

        basket.clear()
    return redirect('basket_detail')