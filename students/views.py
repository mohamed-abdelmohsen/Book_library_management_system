from django.shortcuts import render, get_object_or_404, redirect
from book.models import BorrowedBook, Books
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import BorrowBookForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.
# class BorrowBookView(LoginRequiredMixin, FormView):
#     template_name = 'students/borrow_book.html'
#     form_class = BorrowBookForm

#     def form_valid(self, form):
#         book = get_object_or_404(Books, pk=form.cleaned_data['book_id'])

#         if not book.is_available:
#             return render(self.request, 'students/book_not_available.html', {'book': book})

#         borrowed_book = BorrowedBook(user=self.request.user, book=book)
#         borrowed_book.save()
#         book.is_available = False
#         book.save()
#         return redirect('book_list')
    
@login_required
def borrow(request,book_id):
    book=Books.objects.get(id=book_id)

    if request.method=="POST":
        borrowed_book = BorrowedBook(user=request.user, book=book)
        borrowed_book.save()
        book.is_available = False
        book.save()
        
        return redirect('book_list')
    return render(request, 'students/borrow_book.html',{'book':book})

            
    

    

@login_required
def dashboard(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'students/dashboard.html', {'borrowed_books': borrowed_books})


@login_required
def return_book(request, borrowed_book_id):
    borrowed_book = get_object_or_404(BorrowedBook, id=borrowed_book_id, user=request.user,status='B')
    if request.method == 'POST':
        borrowed_book.return_date = timezone.now()
        borrowed_book.save()
        borrowed_book.delete()
        
        book=borrowed_book.book
        book.is_available = True
        book.save()
        
        return redirect('borrowed_books')
    return render(request, 'students/return_book.html', {'borrowed_book': borrowed_book})







def about_us(request):
    return render(request,'students/about_us.html')

def contact_us(request):
    return render(request,'students/contact_us.html')