from django.shortcuts import render, redirect
from listino.data import NOTES
from listino.models import Note
from listino.forms import NoteForm

# Need a better linter, that is why Note is underlined


def notes_list(request):
    """
    This is your landing page for your app
    """
    # .order_by.all() gives you back the information based upon the order that is stated in
    notes = Note.objects.all()
    return render(request, 'listino/notes_list.html', {
        'notes': notes,
    })


def note_details(request, pk):
    """
    This will bring back the specific note details
    Given the id for the note 
    """
    # Using PK = PK finds the info that is the same as the information
    # Using PK as this is a regular convention in Django
    note = Note.objects.get(pk=pk)
    items = note.items
    # Added in from PM class
    # note_item_form = NoteItemForm()
    # items = note.items
    # items = note.items.order_by('order')
    return render(request, 'listino/note_details.html', {
        'note': note,
        'items': items,
    })


def create_note(request):
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            # Reason being, we want to have it to where
            note = note_form.save()
            # note.title = form.cleaned_data['title']
            # note.description = form.cleaned_data['description']
            # OR note = Note(**form.cleaned_data)

            # note = form.save()
            # This is for the ModelForm which makes it easier
            # You would only need to save the form and then save it
            # Doesn't work for when you have multiple pieces you need to validate
            # note.save()
            return redirect(to='/')
    else:
        note_form = NoteForm()
    return render(request, 'listino/create_note.html', {"form": form})
