from django import forms
from listino.models import Note
# Adding form objects here for search, creation, and updating


class NoteForm(forms.ModelForm):
    # Keep this consistent. You don't want your model to be different from your forms.
    # This could cause weird issues
    # The forms.ModelForm is for convenience and less repeating of yourself.
    class Meta:
        model = Note
        fields = ['title', 'body']


# class NoteFormModel(forms.ModelForm):
#     class Meta:
#         model = Note
#         fields = ['title', 'description']
