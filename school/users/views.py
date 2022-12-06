from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import NewUserForm
from .tasks import sumar
from django.views.generic import CreateView

class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self, form):
      form.save()
      return redirect('login')


def test_celery(request):
    for i in range(1, 50):
        sumar.delay(i + 2, i + 3)

    return HttpResponse("Usando celery")
