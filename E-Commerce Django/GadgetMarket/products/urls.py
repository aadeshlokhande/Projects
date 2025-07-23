from django.urls import path, include
from .views import index, addProduct,editProduct,deleteProduct


urlpatterns = [
    path('', index,name='products'),
    path('add/', addProduct,name='add_products'),
    path('edit/<int:id>/', editProduct,name='edit_products'),
    path('delete/<int:id>/', deleteProduct,name='delete_products'),
]
