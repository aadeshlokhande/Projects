from django.urls import path, include
from .views import index,getAjaxList,addCategory, edit, delete

urlpatterns = [
    path('', index, name='categories'),
    path('add', addCategory, name='addCategories'),
    path('get_categories_ajax_list', getAjaxList, name='getAjaxList'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]

