from django import forms
from book.models import Books

class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField(label='Book ID')

    def clean_book_id(self):
        book_id = self.cleaned_data['book_id']
        try:
            Books.objects.get(pk=book_id)
        except Books.DoesNotExist:
            raise forms.ValidationError("Invalid book ID")
        return book_id
