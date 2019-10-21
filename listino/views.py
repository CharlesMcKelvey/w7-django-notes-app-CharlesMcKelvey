from django.shortcuts import render
from listino.data import NOTES
# Create your views here.


def home_page(request):
    """
    This is your landing page for your app
    """
    return render(request, 'listino/home_page.html', {
        'lists': NOTES,
    })


def note_details(request, id):
    """
    This will bring back the specific note details
    Given the id for the note 
    """
    note = NOTES[id]
    return render(request, 'listino/note_details.html', {
        'note': note,
    })