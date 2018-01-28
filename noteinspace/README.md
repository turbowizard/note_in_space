# Note In Space
**Simple-frame to manage your notes.**
storage powered by [tinydb](https://github.com/msiemens/tinydb)
## Installation
* clone or download
* `python setup.py install`
run tests with pytest:
* `pytest -q noteinspace_test.py`
## Usage
* `from noteinspace import NoteInSpace, Note`
* `nis = NoteInSpace(storage_file='PATH/FILE_NAME.json')`
* `some_note = Note(note_dict={'content': 'WOW'})`
* `nis.insert_note(some_note)`
* `nis.get_all_notes()`
## Docs
### Note()
init params: note_dict
* content - required
* space - optional / 'empty_space' by default
* source - optional / 'self' by default
* type - optional / 'text' by default
* created - system
* id - system
methods:
* dictify - returns instance params (vars(self))
### NoteInSpace()
init params: storage_file , required to init tinydb
methods:
def get_all_notes()
get_note_by_id(int_id)
insert_note(, note_object)
delete_note_by_id(, int_id)
get_all_spaces()
get_notes_in_space(str_space)
remove_space(str_space)
get_recent_notes(int_count)
get_last_note()