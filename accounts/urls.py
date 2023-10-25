from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import  views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/',views.profile,name='profile'),
    path('update_profile/<int:pk>',views.ProfileUpdateView.as_view(),name='update_profile'),
    path('register/',views.register,name='register'),
    path('admin/change_password/', auth_views.PasswordChangeView.as_view(template_name='admin/change_password.html'),
         name='admin_change_password'),

    
    
]


