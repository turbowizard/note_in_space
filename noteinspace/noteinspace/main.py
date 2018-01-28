from datetime import datetime as dt
from abc import ABCMeta, abstractmethod
try:
    from tinydb import TinyDB, where
except ImportError:
    raise ImportError('Failed importing tinydb, try pip install tinydb')


class Note:
    '''note object'''

    note_keys = ['content', 'space', 'source', 'type']

    def __init__(self, **kwargs):
        if 'note_dict' not in kwargs:
            raise KeyError('note_dict expected')
        note_dict = kwargs['note_dict']
        if type(note_dict) is not dict:
            raise TypeError('Note init argument is not dict')
        if 'content' not in note_dict:
            raise KeyError('content is required')
        if len(note_dict['content']) == 0:
            raise ValueError('content cannot be empty')
        # init defaults
        self.source = 'self'
        self.space = 'empty_space'
        self.type = 'text'
        self.created = str(dt.now())
        self.id = None
        for key in note_dict:
            if key in self.note_keys:
                setattr(self, key, note_dict[key])
            else:
                raise KeyError('key {} is not allowed'.format(key))

    def dictify(self):
        return vars(self)


class AbstractNIS(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_notes(self): pass

    @abstractmethod
    def get_note_by_id(self, int_id): pass

    @abstractmethod
    def insert_note(self, note_object): pass

    @abstractmethod
    def delete_note_by_id(self, int_id): pass

    @abstractmethod
    def get_all_spaces(self): pass

    @abstractmethod
    def get_notes_in_space(self, str_space): pass

    @abstractmethod
    def remove_space(self, str_space): pass

    @abstractmethod
    def get_recent_notes(self, int_count): pass

    @abstractmethod
    def get_last_note(self): pass


class NoteInSpace(AbstractNIS):
    '''note controller over tinydb'''

    def __init__(self, **kwargs):
        if 'storage_file' not in kwargs:
            raise KeyError('storage is not defined')
        self.storage = TinyDB(kwargs['storage_file'])

    def get_all_notes(self):
        return self.storage.all()

    def get_note_by_id(self, int_id):
        if not isinstance(int_id, int):
            raise TypeError('int expected, got {}'.format(type(int_id)))
        return self.storage.get(doc_id=int_id)

    def insert_note(self, note_object):
        if not isinstance(note_object, Note):
            raise TypeError('object type is not Note')
        iid = self.storage.insert({})
        note_object.id = iid
        if not note_object.id:
            raise AttributeError('failed to asign ID')
        self.storage.update(note_object.dictify(), doc_ids=[iid])
        # return note_object
        return iid

    def delete_note_by_id(self, int_id):
        return self.storage.remove(where('id') == int_id)

    def get_all_spaces(self):
        result = []
        for note in self.get_all_notes():
            if note['space'] not in result:
                result.append(note['space'])
        return result

    def get_notes_in_space(self, str_space):
        result = []
        for note in self.get_all_notes():
            if note['space'] == str_space:
                result.append(note)
        return result

    def remove_space(self, str_space):
        return self.storage.remove(where('space') == str_space)

    def get_recent_notes(self, int_count):
        return self.get_all_notes()[-int_count:]

    def get_last_note(self):
        return self.get_recent_notes(1)

    def clear_notes(self):
        self.storage.purge_tables()
