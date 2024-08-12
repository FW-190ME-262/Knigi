from django.db.models import Avg
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Books, Authors, Review

from .forms import UserForm


# Create your views here.


def home(request):
    books = Books.objects.all()
    authors = Authors.objects.all()

    # Создаем словарь, где ключ - это книга, а значение - средний рейтинг
    book_ratings = {}
    for book in books:
        avg_rating = Review.objects.filter(books=book).aggregate(Avg('rating'))['rating__avg']
        book_ratings[book.id] = avg_rating

    return render(request, 'home.html', {
        'books': books,
        'authors': authors,
        'book_ratings': book_ratings,
    })


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})



