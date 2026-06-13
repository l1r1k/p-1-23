from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from catalogue.models import Clothe
from .basket import Basket
from .forms import BasketAddClotheForm

# Create your views here.
def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket_detail.html', context={'basket': basket})

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Clothe, pk=product_id)
    form = BasketAddClotheForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload']
        )
    return redirect('basket_detail')

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Clothe, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')