from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.get_cart, name='cart'),
    path('add-to-cart/<int:item_id>/<str:item_type>/', views.add_to_cart, name='add_to_cart'),
]
