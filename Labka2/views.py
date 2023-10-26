from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Labka2.models import Book


# Create your views here.


def page_menu(request):
    return render(request, 'Labka2/base2.html')


def book_search1(request, nameOfBooks):
    context = {'nameOfBooks': nameOfBooks}
    return render(request, 'Labka2/seach-Result.html', context)


def book_search2(request):
    nameOfBooks = request.GET.get('q')
    context = {'nameOfBooks': nameOfBooks}
    return render(request, 'Labka2/seach-Result.html', context)



# ////////////////////////////////////////////////////////////////


def average_rating(rating_list):
    if not rating_list:
        return 0
    return round(sum(rating_list) / len(rating_list))


def get_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'uLabka2/seach-Result.html', context)


def get_books_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "Joo": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "Joo": None
        }
    return render(request, "Labka2/seach-Result.html", context)

# def book_list(request):
#     books = Book.objects.all()
#     book_list = []
#     for book in books:
#         Joo = book.review_set.all()
#         if Joo:
#             book_rating = average_rating([review.rating for review in Joo])
#             number_of_reviews = len(Joo)
#         else:
#            book_rating = None
#            number_of_reviews = 0
#         book_list.append({'book': book,'book_rating': book_rating,'number_of_reviews': number_of_reviews})
#         context = {'book_list': book_list}
#         return render(request, 'Joo/books_list.html', context)