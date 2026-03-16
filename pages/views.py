from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Note


def home(request):
    return render(request, "pages/home.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/notes/")
    else:
        form = UserCreationForm()

    return render(request, "pages/register.html", {"form": form})


@login_required
def notes(request):
    user_notes = Note.objects.filter(owner=request.user)
    return render(request, "pages/notes.html", {"notes": user_notes})


@login_required
def add_note(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        Note.objects.create(owner=request.user, title=title, content=content)
        return redirect("/notes/")

    return render(request, "pages/add_note.html")


@login_required
def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    return render(request, "pages/view_note.html", {"note": note})