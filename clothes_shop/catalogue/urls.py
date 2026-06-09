from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('catalogue/', views.ClothesListView.as_view(), name='catalogue'),
    path('catalogue/clothe/create', views.ClothesCreateView.as_view(), name='clothes_create'),
    path('catalogue/clothe/<int:pk>/', views.ClothesDetailView.as_view(), name='clothes_detail'),
    path('catalogue/clothe/<int:pk>/update/', views.ClothesUpdateView.as_view(), name='clothes_update'),
    path('catalogue/clothe/<int:pk>/delete/', views.ClothesDeleteView.as_view(), name='clothes_delete'),
]