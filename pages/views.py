from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Note

#FLAW5:
from django.contrib.auth.models import User



#FLAW2:
#FLAW2_FIX:
#from django.views.decorators.csrf import csrf_exempt

#FLAW3:
#FLAW3_FIX:
from django.db import connection

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
    #FLAW1:
    #note = get_object_or_404(Note, id=note_id)
    #FLAW1_FIX:
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    return render(request, "pages/view_note.html", {"note": note})

#FLAW2:
#FLAW2_FIX: Use Django's default CSRF protection and include a CSRF token in the form.
#@csrf_exempt
@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("/notes/")
    return render(request, "pages/delete_note.html", {"note": note})


@login_required
def search_notes(request):
    query = request.GET.get("q", "")

#FLAW3:
 #   results = []
 #   if query:
 #       sql = "SELECT * FROM pages_note WHERE owner_id = " + str(request.user.id) + " AND title LIKE '%" + query + "%'"
 #       with connection.cursor() as cursor:
 #           cursor.execute(sql)
 #           rows = cursor.fetchall()
 #
 #       for row in rows:
 #            results.append({
 #                "id": row[0],
 #                "owner_id": row[1],
 #                "title": row[2],
 #                "content": row[3],
 #                "created_at": row[4],
 #            })

    #FLAW3_FIX:
    results = Note.objects.filter(owner=request.user, title__icontains=query)

    return render(request, "pages/search.html", {
         "query": query,
         "results": results,
         })

#FLAW5:
@login_required
def debug_users(request):
    users = User.objects.all()
    return render(request, "pages/debug_users.html", {"users": users})

#FLAW4:
@login_required
def debug_error(request):
    return 1 / 0
    # FLAW 4 FIX:
