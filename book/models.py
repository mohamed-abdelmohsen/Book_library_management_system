from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from taggit.managers import TaggableManager
from django.urls import reverse



def in_three_days():
    return timezone.now() + timedelta(days=3)

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,null=True)
    is_available = models.BooleanField(default=True)
    image=models.ImageField(upload_to='book/images',null=True)
    tags=TaggableManager()
    
    def __str__(self) :
        return self.title
    



class BorrowedBook(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='hh')
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=in_three_days,null=True, blank=True)
    STATUS_CHOICES = (
        ('B', 'Borrowed'),
        ('R', 'Returned'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='B')
    
    
