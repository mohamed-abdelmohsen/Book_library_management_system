from django.urls import path
from . import views
urlpatterns=[
    # path('books/<int:book_id>/borrow/', views.BorrowBookView.as_view(), name='borrow_book'),
    path('books/<int:book_id>/borrow/', views.borrow, name='borrow_book'),
    path('borrowed-books/', views.dashboard, name='borrowed_books'),
    path('borrowed-books/return/<int:borrowed_book_id>', views.return_book, name='return_book'),
    path('about_us/',views.about_us,name='about_us'),
    path('contact_us/',views.contact_us,name='contact_us'),
]