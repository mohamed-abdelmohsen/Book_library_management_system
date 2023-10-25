from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .forms import User_Form 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.


def profile(request):
    return  render(request,'registration/profile.html')

  
  
def register(request):
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = User_Form()
    return render(request, 'registration/register.html', {'form': form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User 
    template_name = 'registration/update_profile.html' 
    fields = ['first_name', 'last_name','username', 'email']
    success_url=reverse_lazy('profile')


    
   
    

        
    