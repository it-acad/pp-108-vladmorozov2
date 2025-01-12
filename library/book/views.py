from .models import Book
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q


def show_all_books(request):
    filter_string = request.GET.get("filter_string")
    print("Filter string:", filter_string)

    # If no filter string is provided, get all books
    if not filter_string:
        books = Book.get_all()
    else:
        # Filter books based on name, description, or related authors' fields
        books = Book.objects.filter(
            Q(name__icontains=filter_string)  # Book name filter
            | Q(description__icontains=filter_string)  # Book description filter
            | Q(authors__name__icontains=filter_string)  # Author's first name filter
            | Q(authors__surname__icontains=filter_string)  # Author's surname filter
        ).distinct()  # Ensure distinct books (to avoid duplicates when multiple authors match)

    template = loader.get_template("book/show_all_books.html")
    context = {"books": books}
    return HttpResponse(template.render(context, request))


def book_details(request, book_id):
    print("book details asdasdsadsadasd")
    template = loader.get_template("book/book_detail.html")
    book = Book.get_by_id(book_id=book_id)
    authors = book.authors.all()
    context = {"book": book, "authors": authors}

    return HttpResponse(template.render(context, request))
