from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("register/", views.register),
    path("notes/", views.notes),
    path("notes/add/", views.add_note),
    path("notes/<int:note_id>/", views.view_note),
]