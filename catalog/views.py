from django.shortcuts import render
from .models import*
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import RenewBookForm

def index(request):
    num_books = Book.objects.all().count()
    num_copies = BookInstance.objects.all().count()
    #Available book (status = 'a')
    num_available_book = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count()
    books = Book.objects.filter(title__icontains = 'code')
    book_list = []
    for book in books:
        book_list.append(book)
    num_visits = request.session.get('num_visits',1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books' : num_books,
        'num_books_instance' : num_copies,
        'num_available_book': num_available_book,
        'num_authors' : num_authors,
        'book_list': book_list,
        'num_visits' : num_visits,
    }
    return render(request, 'index.html', context = context)
class BookListView(generic.ListView):
    model = Book
    context_object_name = "my_book_list" #defaul la book_list
    template_name = 'catalog/my_book_list.html' #neu co file my_book_list.html thi no chay file day
    #default theo django thi chay file book_list.html
    paginate_by = 2
    def get_queryset(self):
        return Book.objects.all()[:3]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test_content"] = "test_get_content"
        return context 

class BookDetailView(generic.DetailView):
    model = Book
    #default context_object_name is book
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
class AuthorDetailView(generic.DetailView):
    model = Author
class LoanedBooksbyUserListView(LoginRequiredMixin ,generic.ListView):
    model = BookInstance
    context_object_name = 'loaned_books'
    template_name = 'catalog/bookinstance_list_borrowed_by_user.html'
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(borrowed = self.request.user).filter(status__exact = 'o').order_by('due_back')

# def renew_book_librarian(request, pk):
#     book_instance = get_object_or_404(BookInstance, pk=pk)

