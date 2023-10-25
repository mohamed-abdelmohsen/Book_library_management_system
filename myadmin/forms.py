from django import forms
from book.models import Books




class CreateForm(forms.ModelForm):
    
    class Meta:
        model=Books
        fields='__all__'
        