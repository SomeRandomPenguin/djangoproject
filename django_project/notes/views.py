from django.shortcuts import render
# from .models import Note
# from .forms import NoteForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required
# from django.db.models import queue

def note_list(request):
    return render(request, 'note/note_list.html')
def note_detail(request, note_id): 
    return render(request, 'note/note_detail.html')

# Create your views here.
