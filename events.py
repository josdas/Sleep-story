from note_record import Note
from note_storage import Storage
import datetime


class Events:
    """Class for callback from GUI."""

    def __init__(self, suffix='', other_data=None):
        self.suffix = suffix
        self.other_data = other_data

    def __call__(self, text, feeling):
        now = datetime.datetime.now()
        time = now.strftime('%H:%M')
        date = now.strftime('%d_%m_%Y')
        note = Note(text, feeling, time, self.other_data)
        storage = Storage({date: note})
        storage.save(name="data/" + date + self.suffix + '.txt')
