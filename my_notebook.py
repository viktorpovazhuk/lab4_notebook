# Used sources: Python 3 Object-oriented Programming Second Edition , Dusty Phillips, 2015

"""Module to represent notebook"""

import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """Represent note in notebook. Match against a filter string,
    can add, store and modify tags.

    Attributes:
        memo (str): Memo saved in note
        tags (str): Labels to search among notes
        creation_date (datetime.date): Date of creation
        id (int): Id of note
    """

    def __init__(self, memo: str, tags: str = ""):
        """Initialize a new note with memo and optional space-separated
        tags. Automatically set the note's creation date and a unique id."""

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter: str) -> bool:
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags.

        >>> n1 = Note("hello first", "sun icecrean beach")
        >>> n1.match("sun")
        True
        """

        return filter in self.memo or filter in self.tags


class Notebook:
    """Represent a collection of notes that can be tagged,
    modified, and searched.

    Attributes:
        notes (list): List of notes in notebook
    """

    def __init__(self):
        """Initialize a notebook with an empty list."""

        self.notes = []

    def new_note(self, memo: str, tags: str = ''):
        """Create a new note and add it to the list.

        >>> nb1 = Notebook()
        >>> nb1.new_note("test note", "sun beach")
        >>> nb1.notes[0].memo == "test note"
        True
        """

        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id: int):
        """Locate the note with the given id."""

        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id: int, memo: str):
        """Find the note with the given id and change its
        memo to the given value.

        >>> nb2 = Notebook()
        >>> nb2.new_note("test note", "sun beach")
        >>> nb2.notes[0].id = 1
        >>> nb2.modify_memo(1, "another note")
        >>> print(len(nb2.search("another note")))
        1
        """

        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id: int, tags: str):
        """Find the note with the given id and change its
        tags to the given value.

        >>> nb1 = Notebook()
        >>> nb1.new_note("test note", "sun beach")
        >>> nb1.notes[0].id = 1
        >>> nb1.modify_tags(1, "nothing")
        >>> print(len(nb1.search("nothing")))
        1
        """

        self._find_note(note_id).tags = tags

    def search(self, filter: str):
        """Find all notes that match the given filter
        string.

        >>> nb1 = Notebook()
        >>> nb1.new_note("test note", "sun beach")
        >>> nb1.notes[0].id = 1
        >>> (nb1.search("test no")[0].tags == "sun beach" and \
        nb1.search("test no")[0].memo == "test note")
        True
        """

        return [note for note in self.notes if
                note.match(filter)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
