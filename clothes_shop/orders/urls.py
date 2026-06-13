from django.urls import path
from . import views

urlpatterns = [
    path('confirm/', view=views.order_confirm, name='order_confirm'),
    path('create/', view=views.order_show, name='order_open'),
]