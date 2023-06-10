from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('login',views.handlelogin,name='login'),
    path('signup',views.handlesignup,name='signup'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('search', views.search, name='search'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('change-quantity/<str:product_id>', views.change_quantity, name='change_quantity'),
    path('remove-from-cart/<str:product_id>', views.remove_from_cart, name='remove_from_cart'),  
    path('cart', views.cart_view, name='cart_view'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('<slug:slug>/', views.category_detail, name='category_detail'), 
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
    
]