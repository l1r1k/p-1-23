from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.basket_detail, name='basket_detail'),
    path('add/<int:product_id>/', view=views.basket_add, name='basket_add'),
    path('remove/<int:product_id>/', view=views.basket_remove, name='basket_remove'),
    path('clear/', view=views.basket_clear, name='basket_clear'),
]