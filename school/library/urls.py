from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name="index_book"),
    path('book/<id>', views.select_book, name="select_book")
]
