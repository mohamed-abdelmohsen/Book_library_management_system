from django.shortcuts import render, get_object_or_404, redirect
from .models import  Books
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from taggit.models import Tag
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import ListView, DetailView
from django.db.models import Count






# class BookListView( ListView):
#     model = Books
#     template_name = 'book/book_list.html'
#     context_object_name = 'books'
#     queryset = Books.objects.filter(is_available=True)
#     paginate_by=8
    


def book_list(request,tag_slug=None):
    book_list=Books.objects.filter(is_available=True)
    tag=None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        book_list = book_list.filter(tags__in=[tag])
    paginator=Paginator(book_list,8)
    page_number = request.GET.get('page', 1)
    try:    
        books=paginator.page(page_number)
    except EmptyPage :
        books =paginator.page(paginator.num_pages)
        
    except PageNotAnInteger:
        books=paginator.page(1)
        
    return render(request,'book/book_list.html',{'books':books,'tag':tag})


# class BookDetailView(DetailView):
#     model = Books
#     template_name = 'book/book_detail.html'
#     context_object_name = 'book'
    
def book_detail(request,book_id):
    book=get_object_or_404(Books,id=book_id)
    
    book_tags_ids = book.tags.values_list('id', flat=True)
    similar_books = Books.objects.filter(tags__in=book_tags_ids).exclude(id=book.id)
    similar_books = similar_books.annotate(same_tags=Count('tags'))[:4]

    
    return render(request,'book/book_detail.html',{'book':book,'similar_books':similar_books})
    
    








