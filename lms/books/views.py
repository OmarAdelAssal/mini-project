from django.shortcuts import render
from django.http import HttpResponse
from books.models import books
# Create your views here.

def index (request):
    all_book = books.get_all_books
    return render(request , 'books/index.html' , context={'books':all_book})
