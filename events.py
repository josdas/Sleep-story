from note_record import Note
from note_storage import Storage
import datetime


class Events:
    """Class for callback from GUI."""

    def __init__(self, weather=''):
        now = datetime.datetime.now()
        self.date = now.strftime("%d_%m_%Y")
        self.weather = weather

    def __call__(self, text, feeling):
        note = Note(text, feeling, self.weather)
        storage = Storage({self.date: note})
        storage.save(name="data/" + self.date + '.txt')
