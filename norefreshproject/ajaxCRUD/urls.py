from django.urls import path,include
from .views import book_list ,book_create, book_update, book_delete

app_name = "ajaxCRUD"
urlpatterns = [
    path('',book_list, name = 'book_list'),
    path('create/',book_create, name = 'book_create'),
    path('<pk>/update/', book_update, name='book_update'),
    path('<pk>/delete/', book_delete, name='book_delete'),
]