from flask import Flask, request, jsonify, abort
from noteinspace import Note, NoteInSpace

sf = '<PATH/FILE>.json'
nis_app = Flask(__name__)
nis = NoteInSpace(storage_file=sf)


headers = {'Content-Type': 'application/json', }


# APIs ------------------------------------------


@nis_app.route('/api/notes', methods=['GET'])
def get_notes():
    ''' retrive all notes'''
    return jsonify(nis.get_all_notes())


@nis_app.route('/api/notes', methods=['POST'])
def save_note():
    ''' create new note '''
    rs = request.json
    print rs
    try:
        stored_note = nis.insert_note(Note(note_dict=rs))
        return jsonify(stored_note), 201
    except:
        abort(400)


@nis_app.route('/api/notes/<int:note_id>', methods=['GET'])
def get_note_by_id(note_id):
    ''' retrive note by id'''
    return jsonify(nis.get_note_by_id(note_id))


@nis_app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def remove_note_by_id(note_id):
    ''' remove note by id'''
    return jsonify(nis.delete_note_by_id(note_id))


@nis_app.route('/api/notes/recent/<int:recent_count>', methods=['GET'])
def get_recent(recent_count):
    ''' retrive recent by int'''
    return jsonify(nis.get_recent_notes(recent_count))


@nis_app.route('/api/spaces', methods=['GET'])
def get_spaces():
    ''' retrive all spaces'''
    return jsonify(nis.get_all_spaces())


@nis_app.route('/api/spaces/<string:space>', methods=['GET'])
def get_notes_in_space(space):
    ''' retrive all notes in space'''
    return jsonify(nis.get_notes_in_space(space))


if __name__ == '__main__':
    nis_app.run(port=5007)