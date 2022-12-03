from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
"""
Por defecto django tiene un form con los siguientes campos
username
email
password1 
password2

En el formulario tener una seccion para confirmar que ambos password sean iguales
Ahora si queremos aumentar mas campos al registro
podemos hacer un customform y heredar UserCreationForm
"""

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        """ Vamos a indicar que este formualario pertenece a un modelo """
        model = User
        """ Podemos definir que campos seran los que mistremos usando el atributo fields """
        fields = ("username", "first_name", "last_name", "email",  "password1", "password2")

    """ Vamos a sobreescribir el metodo save """
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        # aumentar el email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
