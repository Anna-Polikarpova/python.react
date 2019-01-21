from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('addtocard/<int:product_id>/', views.CartView.as_view(), name='addtocard'),
    path('products/create/', views.CreateProd.as_view(), name='create'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]