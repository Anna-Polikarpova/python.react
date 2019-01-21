from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.AccountRegistrationView.as_view(), name='account_registration'),
    path('get/<str:username>/', views.get_profile, name='get'),
    path('edit/', views.update_profile, name='edit')
]