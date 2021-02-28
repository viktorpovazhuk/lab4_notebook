# Used sources: Python 3 Object-oriented Programming Second Edition , Dusty Phillips, 2015

"""Module with menu functions"""

import sys

from my_notebook import Notebook


class Menu:
    """Display a menu and respond to choices when run.

    Attributes:
        notebook (my_notebook.Notebook): Created notebook
        choices (dict): Menu choices
    """

    def __init__(self):
        """Initialize menu with associated notebook"""

        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        """Print menu instruction for user"""

        print(
            """
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
"""
        )

    def run(self):
        """Display the menu and respond to choices."""

        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        """Print notes in console"""

        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        """Search for notes and print them"""

        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        """Add note in notebook"""

        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """Change note's values"""

        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """Exit the app"""

        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
