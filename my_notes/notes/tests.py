from django.test import TestCase
from .models import Note, Tag


class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Note.objects.create(title='Address')
        note = Note.objects.create(content='tomato, bread')
        tag = note.tags.create(label='shop')
        tag.save()

    def test_note_title(self):
        note = Note.objects.get(id=1)
        self.assertEquals(note.title, 'Address')

    def test_note_content(self):
        note = Note.objects.get(id=2)
        self.assertEquals(note.content, 'tomato, bread')

    def test_tag_label(self):
        note = Note.objects.get(id=2)
        tag = Tag.objects.get(id=1)
        self.assertEqual(note.tags.get(pk=tag.pk), tag)

    def test_remove_note(self):
        note = Note.objects.get(id=2)
        note.delete()
        self.assertEqual(Note.objects.count(), 1)

    def test_add_tag(self):
        note = Note.objects.get(id=2)
        note.tags.create(label="food")
        self.assertEqual(note.tags.count(), 2)
