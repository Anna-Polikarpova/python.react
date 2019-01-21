from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [

    path('<int:id>/', views.detail, name='detail'),
    path('', views.list, name='listView')

]
