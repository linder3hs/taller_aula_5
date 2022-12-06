from django.urls import path
# django tiene un tempalte preparado para le login
# Es decir no provee de la clase LoginView para poder mostrar el formalario de inicio de session
from django.contrib.auth.views import LoginView, logout_then_login
from .views import RegisterView, test_celery

# Segun el documento de django la url correact para que funcion debe ser accounts/login/
urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_then_login, name='logout'),
    path('test/', test_celery, name="test_celery")
]

"""
LoginView
va a buscar al archivo registration/login
template_name = "registration/login.html"
Esta clase recibe 2 cosas username y password
Dentro de la clase va a verificar que el username y password
ingresados sea correctos 

Para que este funcione hay que seguir ciertas reglas
1: La url se debe llamar: accounts/login/
2: El template de login debe estar en la carpeta registration/login.html
"""
