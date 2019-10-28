from django.shortcuts import render, redirect, get_object_or_404
from listino.data import NOTES
from listino.models import Note
from listino.forms import NoteForm
# Gives ability to have updated time using timezone.now
from django.utils import timezone

# Need a better linter, that is why Note is underlined


def notes_list(request):
    """
    This is your landing page for your app
    """
    notes = Note.objects.all()
    return render(request, 'listino/notes_list.html', {
        'notes': notes,
    })


def note_details(request, pk):
    """
    This will bring back the specific note details
    Given the id for the note 
    """
    note = Note.objects.get(pk=pk)
    return render(request, 'listino/note_details.html', {
        'note': note,
    })


def create_note(request):
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save()
            return redirect(to='/')
    else:
        note_form = NoteForm()
    return render(request, 'listino/create_note.html', {"form": note_form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note_form = NoteForm(request.POST, instance=note)
        if note_form.is_valid():
            note.updated_at = timezone.now()
            note.save()
            return redirect('note_details', pk=pk)
    else:
        note_form = NoteForm()
        note_form['title'].initial = note.title
        note_form['body'].initial = note.body
    return render(request, 'listino/edit_note.html', {
        'form': note_form
    })


def delete_note(request, pk):
    Note.objects.get(id=pk).delete()
    return redirect('/')
