from django import forms
from bookstore.models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'released_year', 'description', 'book_cover', 'author']
