import os
import pytest
import noteinspace as nis


def test_note_init_params():
    with pytest.raises(KeyError):
        nis.Note(invalid_param={})


@pytest.mark.parametrize('note, expected', [
    ({}, KeyError),
    ([], TypeError),
    ({'content': ''}, ValueError),
    ({'content': 'wow', 'invalid_key': ''}, KeyError),
])
def test_note_init(note, expected):
    with pytest.raises(expected):
        nis.Note(note_dict=note)


@pytest.mark.parametrize('note, content, space, source, type', [
    ({'content': 'wow'}, 'wow', 'empty_space', 'self', 'text'),
    ({'content': 'wow', 'space': 'test', 'source': 'test', 'type': 'test'}, 'wow', 'test', 'test', 'test')
])
def test_note_self_params(note, content, space, source, type):
    test_note = nis.Note(note_dict=note)
    assert test_note.content == content
    assert test_note.space == space
    assert test_note.source == source
    assert test_note.type == type


storage_file = 'nis_test.json'
try:
    os.remove(storage_file)
except OSError:
    pass


@pytest.fixture
def test_nis():
    return nis.NoteInSpace(storage_file=storage_file)


def test_nis_note_actions(test_nis):
    some_note = nis.Note(note_dict={'content': 'wow'})
    new_note_id = test_nis.insert_note(some_note)
    returned_note = test_nis.get_note_by_id(new_note_id)
    assert new_note_id == returned_note['id']
    assert len(test_nis.get_all_notes()) == 1
    test_nis.delete_note_by_id(new_note_id)
    assert len(test_nis.get_all_notes()) == 0


def test_nis_space_actions(test_nis):
    some_note1 = nis.Note(note_dict={'content': 'wow1', 'space': 'test_space_1'})
    some_note2 = nis.Note(note_dict={'content': 'wow2', 'space': 'test_space_2'})
    test_nis.insert_note(some_note1)
    test_nis.insert_note(some_note2)
    assert test_nis.get_all_spaces() == ['test_space_1', 'test_space_2']
    notes_space_1 = test_nis.get_notes_in_space('test_space_1')
    assert len(notes_space_1) == 1
    assert notes_space_1[0]['content'] == 'wow1'
    test_nis.remove_space('test_space_1')
    assert len(test_nis.get_notes_in_space('test_space_1')) == 0
    assert len(test_nis.get_all_spaces()) == 1
    test_nis.remove_space('test_space_2')
    assert len(test_nis.get_notes_in_space('test_space_2')) == 0
    assert len(test_nis.get_all_spaces()) == 0


def test_nis_other_actions(test_nis):
    some_note1 = nis.Note(note_dict={'content': 'wow1'})
    some_note2 = nis.Note(note_dict={'content': 'wow2'})
    test_nis.insert_note(some_note1)
    test_nis.insert_note(some_note2)
    last = test_nis.get_last_note()
    assert len(last) == 1
    assert last[0]['content'] == 'wow2'
    some_note3 = nis.Note(note_dict={'content': 'wow3'})
    test_nis.insert_note(some_note3)
    last2 = test_nis.get_recent_notes(2)
    assert len(last2) == 2
    assert last2[0]['content'] == 'wow2'
    assert last2[1]['content'] == 'wow3'
    test_nis.clear_notes()
    assert len(test_nis.get_all_notes()) == 0


