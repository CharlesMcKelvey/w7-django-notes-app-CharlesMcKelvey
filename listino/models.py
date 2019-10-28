from django.db import models

# Create your models here.


class Note(models.Model):
    # CharField means a stored value as a string, given a length maximum
    title = models.CharField(max_length=100)
    # null being True allows it to be empty and blank is allowed to be blank
    # Seems redundant cause it is
    body = models.TextField(
        blank=True, null=True, help_text='Any information is okay to be given here.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def item_count(self):
        return self.items.count()


class NoteItem(models.Model):
    class Meta:
        ordering = ['order']

    body = models.CharField(max_length=255)
    # CASCADE allows so that when the Note is deleted, then all items associated are too.
    note = models.ForeignKey(
        to=Note, on_delete=models.CASCADE, related_name='items')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
