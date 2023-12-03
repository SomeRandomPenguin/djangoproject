from django.shortcuts import render, get_object_or_404, redirect
from notes.models import Note
# from .models import Note
# from .forms import NoteForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required
# from django.db.models import queue


def note_list(request):
    notelist = Note.objects.all()
    return render(request, 'note/note_list.html',  {'note':notelist})
def note_detail(request, note_id): 
    noteid = get_object_or_404(Note, pk=note_id)
    return render(request, 'note/note_detail.html',{'note':noteid})
def create_note(request): 
    return render(request, 'note/create_note.html')

# Create your views here.