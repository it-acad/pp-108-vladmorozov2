from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import Author
from utils.permissions import is_admin


@user_passes_test(is_admin)
def list_authors(request):
    authors = Author.get_all()
    return render(request, "authors/list_authors.html", {"authors": authors})


@user_passes_test(is_admin)
def create_author(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        patronymic = request.POST.get("patronymic")

        if name and surname and patronymic:
            Author.create(name=name, surname=surname, patronymic=patronymic)
            return redirect("list_authors")
        else:
            return render(
                request,
                "authors/create_author.html",
                {"error": "All fields are required."},
            )

    return render(request, "authors/create_author.html")


@user_passes_test(is_admin)
def create_author(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        patronymic = request.POST.get("patronymic")

        if name and surname and patronymic:
            Author.create(name=name, surname=surname, patronymic=patronymic)
            return redirect("list_authors")
        else:
            return render(
                request,
                "authors/create_author.html",
                {"error": "All fields are required."},
            )

    return render(request, "authors/create_author.html")


from django.http import HttpResponse


@user_passes_test(is_admin)
def delete_author(request, author_id):
    author = Author.get_by_id(author_id)

    if not author:
        return HttpResponse("Author not found.", status=404)

    if author.books.exists():
        return HttpResponse(
            "Cannot delete. This author is attached to one or more books.", status=400
        )

    Author.delete_by_id(author_id)

    return redirect("list_authors")
