from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login_page'),
    path('registration/', views.register_user, name='registration_page'),
    path('logout/', views.logout_user, name='logout_page'),
]