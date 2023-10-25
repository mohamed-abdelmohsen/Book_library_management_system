from django.urls import path
from . import views

urlpatterns=[
    path('<int:pk>/delete',views.DeleteGenericView.as_view(), name='delete'),
    path('create/',views.CreateGenericView.as_view(),name='create_product'),
    path('edit/<int:pk>',views.EditGenericView.as_view(),name='edit'),
    path('all_users/', views.All_users.as_view(), name='all_users'),
    # path('all/',views.get_all,name='get_all')
    path('users/<int:pk>/', views.UsersDetailView.as_view(), name='user_details'),
    path('display/', views.Display.as_view(), name='display'),
    path('search/', views.search_user, name='search_user'),
    path('allborrowed/',views.AllBorrowedBooks.as_view(),name='allborrowed')
]