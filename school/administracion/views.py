from django.shortcuts import redirect
from .models import ClassRoom
from django.views.generic import TemplateView, FormView
from .forms import ClassRoomForm

class AdministracionView(TemplateView):
    template_name = "administracion/index.html"
    extra_context = {"classrooms": ClassRoom.objects.all()}


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
