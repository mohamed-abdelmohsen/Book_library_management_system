from django.urls import path
from . import views

# app_name='book'

urlpatterns=[
    # path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/',views.book_list,name='book_list'),
    path('books/tag/<slug:tag_slug>',views.book_list,name='book_list_by_tag'),
    # path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),

    


]