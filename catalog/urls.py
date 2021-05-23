from django.urls import include, path, re_path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('books/',views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/',views.LoanedBooksbyUserListView.as_view(), name='my-borrowed')
]
# urlpatterns += [
#     path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
# ]
