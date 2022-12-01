from django import forms

class ClassRoomForm(forms.Form):
  name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))
  start_time = forms.TimeField(widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))
