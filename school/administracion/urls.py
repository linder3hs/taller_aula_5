from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdministracionView.as_view(), name="index"),
    path('create/', views.ClassRoomCreate.as_view(), name="create"),
    path('delete/<int:id>', views.deleteClassRoom, name="delete")
]
