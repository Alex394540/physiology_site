from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('product_page/<int:pk>/', views.product_page, name='product_page')
    ]