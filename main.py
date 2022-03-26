"""
main.py
Lab 3 task 6
Notebook realisation
"""


class Note:
    """
    Note class
    It is used to store data
    """

    def __init__(self, content, label, tags=None, is_pinned=False) -> None:
        from datetime import datetime
        self.content = content
        self.label = label
        self.tags = tags
        self.is_pinned = is_pinned
        self.created_at = datetime.now().strftime(f"%d_%m_%Y-%H:%M:%S:%f")
        self.modified_at = self.created_at

    def __str__(self) -> str:
        changed = ''
        if self.created_at != self.modified_at:
            changed = f';\nModified at: {self.modified_at}'
        adjusted_label = self.label.replace('\n', '\n             ')
        adjusted_content = self.content.replace('\n', '\n             ')
        txt = [
            '\nLabel:       ',
            ';\nContent:     ',
            ';\nTags:        ',
            ';\nIs Pinned:   ',
            ';\nCreated at:  '
        ]
        parts = [
            f'{txt[0]}{adjusted_label}{txt[1]}{adjusted_content}{txt[2]}',
            f'{self.tags}{txt[3]}{self.is_pinned}{txt[4]}{self.created_at}{changed}'
        ]
        return f'{parts[0]}{parts[1]}.'

    def __repr__(self) -> str:
        return f'Note({self.label}; {self.content})'

    def modify(self, new_content, new_label='', new_tags='', new_is_pinned=None):
        """
        Modify method
        Modifies current note
        """
        from datetime import datetime
        self.content = new_content
        if new_label != '':
            self.label = new_label
        if new_tags != '':
            self.tags = new_tags
        if new_is_pinned != None:
            self.is_pinned = new_is_pinned
        self.modified_at = datetime.now().strftime(f"%d_%m_%Y-%H:%M:%S:%f")


class NoteBook:
    """
    Notebook class
    Used to handle multiple Note objects
    """

    def __init__(self, label) -> None:
        from datetime import datetime
        self.label = label
        self.created_at = datetime.now().strftime(f"%d_%m_%Y-%H:%M:%S:%f")
        self.modified_at = self.created_at
        self.notes = {}

    def __str__(self) -> str:
        txt = [
            '\n           ===Notebook info===\n',
            '\nNotebook Label: ',
            ';\nCreated at:     ',
            ';\nModified at:    ',
        ]
        optional_txt = ''
        if self.created_at != self.modified_at:
            optional_txt = f'{txt[3]}{self.modified_at}'
        parts = [
            f'{txt[0]}{txt[1]}{self.label}{txt[2]}',
            f'{self.created_at}{optional_txt}'
        ]
        string_to_return = f'{parts[0]}{parts[1]}\n'
        return string_to_return

    def create_note(self, content, label, tags=None, is_pinned=False) -> int:
        """
        create_note method
        Creates a new note with unique id
        """
        from datetime import datetime
        note_id = int(datetime.now().strftime(f"%Y%m%d%H%M%S%f"))
        self.notes[note_id] = Note(content, label, tags, is_pinned)
        return note_id

    def edit_note(
            self, note_id, new_content, new_label='', new_tags='',
            new_is_pinned=None) -> None:
        """
        edit_note method
        Edits certain note
        """
        self.notes[note_id].modify(
            new_content, new_label, new_tags, new_is_pinned)
        from datetime import datetime
        self.modified_at = datetime.now().strftime(f"%d_%m_%Y-%H:%M:%S:%f")

    def delete_note(self, note_id) -> None:
        """
        delete_note method
        Deletes certain note
        """
        self.notes.pop(note_id)

    def get_note(self, note_id) -> str:
        """
        get_note method
        Returns certain note
        """
        ans = self.notes[note_id]
        ans = str(ans)
        return ans

    def get_notebook(self):
        """
        get_notebook method
        Returns notebook info and notes
        """
        string_to_return = self.__str__()
        string_to_return += '\n\n           ====Notes  info====\n'
        if len(self.notes.items()) != 0:
            for elem in self.notes.items():
                string_to_return += f'\nID:          {elem[0]}'
                string_to_return += str(elem[1])
                string_to_return += '\n'
        else:
            string_to_return += '\n  There are no notes in your notebook!\n'
        return string_to_return


def show_menu():
    """
    Function that prints menu
    """
    options = [
        '         Menu\n'
        '1. Display Notebook\n'
        '2. Show Info & Notes\n'
        '3. Show Certain Note\n'
        '4. Create Note\n'
        '5. Modify Note\n'
        '6. Delete Note\n'
        '7. Exit\n'
    ]
    print(''.join(options))


def get_info():
    """
    Function tha gathers user info (input)
    """
    content = input('Type your note here: ')
    label = input('Type your note\'s label here: ')
    tags = input('Input your tags here (separated by ";"): ')
    tags = [tags.split(';')]
    while 1:
        is_pinned = input('Pin your note(N/y)')
        if is_pinned == 'y' or is_pinned == 'Y':
            is_pinned = True
            break
        elif is_pinned == 'n' or is_pinned == 'N' or is_pinned == '':
            is_pinned = False
            break
        else:
            print('Try again')
    return content, label, tags, is_pinned


def get_note_id(my_notebook: NoteBook):
    """
    Function that gets user input and
    checks if it si a valid note id
    """
    note_id = None
    while 1:
        try:
            note_id = input('\nType in NoteID you want to access: ')
            if note_id == 'exit':
                note_id = None
                break
            note_id = int(note_id)
            if note_id not in my_notebook.notes.keys():
                print('Wrong id!')
                raise ValueError
            else:
                break
        except ValueError:
            print('Try again, please\nIf you want to exit type "exit"\n')
    return note_id


def main(my_notebook: NoteBook):
    """
    Main function
    """
    print('\n#  Notebook example\n')
    while 1:
        show_menu()
        menu_action = input('Choose one of the options listed: ')
        if menu_action == '1':
            print(my_notebook)
        elif menu_action == '2':
            print(my_notebook.get_notebook())
        elif menu_action == '3':
            if len(my_notebook.notes) != 0:
                note_id = get_note_id(my_notebook)
                print(my_notebook.get_note(note_id))
            else:
                print(
                    '\nThere are no notes in your notebook!\nPlease, create one first\n')
        elif menu_action == '4':
            user_info = get_info()
            my_notebook.create_note(
                user_info[0], user_info[1], user_info[2], user_info[3])
            print(my_notebook.notes)
        elif menu_action == '5':
            if len(my_notebook.notes) != 0:
                note_id = get_note_id(my_notebook)
                if note_id != None:
                    user_info = get_info()
                    my_notebook.edit_note(
                        note_id, user_info[0],
                        user_info[1],
                        user_info[2],
                        user_info[3])
                else:
                    print('Try again!')
            else:
                print(
                    '\nThere are no notes in your notebook!\nPlease, create one first\n')
        elif menu_action == '6':
            if len(my_notebook.notes) != 0:
                note_id = get_note_id(my_notebook)
                if note_id != None:
                    user_info = get_info()
                    my_notebook.delete_note(note_id)
                else:
                    print('Try again!')
            else:
                print(
                    '\nThere are no notes in your notebook!\nPlease, create one first\n')
        elif menu_action == '7':
            print('Exiting!')
            break
        else:
            print('try again')


def research():
    """
    Function for efficiency research
    """
    print('Testing started...')
    my_note = Note('Just a note', 'My first note', ['101', '123'], True)
    assert isinstance(str(my_note), str)
    assert my_note.content == 'Just a note'
    my_note.modify('Just changed my first note :^)',
                   '', '', False)
    assert my_note.content == 'Just changed my first note :^)'
    assert isinstance(my_note, Note)
    print('Note class tested.')

    my_notebook = NoteBook('First notebook')
    assert isinstance(my_notebook, NoteBook)
    my_notebook.create_note('Just a note in a first notebook',
                            'My note Lol', ['#436', '123'], True)
    my_notebook.create_note('Another note in a notebook',
                            'Nothing new', ['#436', '!CrAzY!'], False)
    my_notebook.create_note('One more note in a notebook',
                            'Empty ^_^', ['#436', 'Still- :)'], True)
    assert isinstance(my_notebook.notes, dict)
    note_keys = list(my_notebook.notes.keys())
    my_notebook.edit_note(
        note_keys[0],
        'Just changed my first note once more :^)', '', '', False)
    assert isinstance(my_notebook.get_note(note_keys[0]), str)

    assert isinstance(my_notebook.notes[note_keys[0]], Note)
    assert isinstance(my_notebook.notes[note_keys[1]], Note)
    assert isinstance(my_notebook.notes[note_keys[2]], Note)
    print('NoteBook class tested')
    print(dir(my_note))
    print('---')
    print(my_note.__dict__)
    print(my_note)
    print('---')
    print(dir(my_notebook))
    print('Finished!')


if __name__ == '__main__':
    research()
    my_notebook = NoteBook('My Notebook')
    main(my_notebook)
