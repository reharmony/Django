from django.urls import path

from .views import *

app_name = 'cart'

urlpatterns = [
    path('', detail, name='detail'),
    path('add/<int:product_id>', add, name='product_add'),
]