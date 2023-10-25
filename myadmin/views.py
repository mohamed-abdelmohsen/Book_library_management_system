from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from book.models import Books
from django.views.generic import CreateView,ListView,DetailView
from .forms import CreateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from book.models import BorrowedBook
from django.contrib.auth.mixins import LoginRequiredMixin


    
    
    
class DeleteGenericView(DeleteView):
    model=Books
    template_name='myadmin/delete.html'
    
    success_url=reverse_lazy('book_list')
    


class CreateGenericView(CreateView):
    form_class=CreateForm
    template_name='myadmin/create_book.html'
    success_url=reverse_lazy('book_list')
    
    
    
    
class EditGenericView(LoginRequiredMixin,UpdateView):
    model=Books
    form_class=CreateForm
    template_name='myadmin/edit_book.html'
    success_url=reverse_lazy('book_list')
    

class All_users(ListView):
    model=User
    
    template_name='myadmin/all_users.html'
    queryset=User.objects.all()


# def get_all(request):
#     User=get_user_model()
#     users=User.objects.all()
#     return render(request,'admin/all_users.html',{'users':users})


class UsersDetailView(DetailView):
    model=User
    template_name = 'myadmin/user_details.html'
    
    
class Display(ListView):
    model=Books
    template_name='myadmin/display.html'
    queryset=Books.objects.all()
    
    
    
# def get_user(request,user_id):
#     try:
#         student=User.objects.get(id=user_id)
#         return render(request,'myadmin/get_user.html',{'student':student})
#     except:
#         return HttpResponse("does not exist")
    
    
    
    
# def get_user(request):
#     if request.method=='Post':
#         searched=request.POST['searched']
#         students=User.objects.get(id=searched)
#         return render(request,'myadmin/get_user.html',{'searched':searched,'students':students})
    
#     return render(request,'myadmin/get_user.html')



def search_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('search')
        try:
            user = User.objects.get(id=user_id)
            return redirect('user_details', pk=user.id)
        except User.DoesNotExist:
            error_message = "User not found."
            return render(request, 'error.html', {'error_message': error_message})
    else:
        return redirect('book_list')






class AllBorrowedBooks(ListView):
    model=BorrowedBook
    template_name='myadmin/borrowed_book_list.html'
    queryset=BorrowedBook.objects.all()
        
        