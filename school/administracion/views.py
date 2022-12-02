from django.shortcuts import redirect, render
from .models import ClassRoom, Book
from django.views.generic import TemplateView, FormView, View
from .forms import ClassRoomForm
import urllib.request
import datetime
import json

class AdministracionView(TemplateView):
    template_name = "administracion/index.html"
    extra_context = {"classrooms": ClassRoom.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classrooms"] = ClassRoom.objects.all()
        return context

class ClassRoomCreate(FormView):
    model = ClassRoom
    template_name = "administracion/create.html"
    form_class = ClassRoomForm

    def form_valid(self, form):
        ClassRoom.objects.create(**form.cleaned_data)
        return redirect("index")


def deleteClassRoom(request, id):
    classroom = ClassRoom.objects.get(id=id)
    classroom.delete()
    return redirect("index")


class BookView(View):
    def get(self, request):
        response = urllib.request.urlopen("https://silabuzinc.github.io/books/books.json")
        books = json.loads(response.read())

        for book in books:
            del book["bookID"]
            del book["FIELD13"]
            book["authors"] = book["authors"][:100]  
            # m/d/y -> y-m-d
            format = book["publication_date"].split("/")
            if len(format) == 3:
                print(format[2], format[1], format[0])
                if int(format[1]) > 12:
                    format[1] = 12
                book["publication_date"] = datetime.date(int(format[2]), int(format[1]), int(format[0]))
            else:
                book["publication_date"] = datetime.date(2000, 1, 1)
            Book.objects.create(**book)

        return render(request, "book/index.html")

    