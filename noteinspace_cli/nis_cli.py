from noteinspace import Note, NoteInSpace
import click

sf = 'test.json'
nis = NoteInSpace(storage_file=sf)


def note_format(note):
    click.echo('*Note  {}, [{}]'.format(note['id'], note['space']))
    click.echo('    {}'.format(note['content']))
    click.echo('meta: (source: {} ,type: {}, created:{})'.format(note['source'], note['type'], note['created']))
    click.echo('-' * 24)


@click.group()
def cli():
    """Note In Space cli.
    """

@cli.command()
@click.option('--content', prompt='Note content')
@click.option('--space', '-s', type=unicode)
def note(content, space):
    """create fresh note"""
    nd = {'content': content}
    if space:
        nd['space'] = space
    nis.insert_note(Note(note_dict=nd))


@cli.command('get_all')
def get_all_notes():
    """get all notes"""
    res = nis.get_all_notes()
    for note in res:
        note_format(note)


@cli.command('get_note')
@click.argument('note_id', type=int)
def get_note_by_id(note_id):
    note_format(nis.get_note_by_id(note_id))


@cli.command('del_note')
@click.argument('note_id', type=int)
def del_note_by_id(note_id):
    click.echo('Removing note {}'.format(note_id))
    nis.delete_note_by_id(note_id)


@cli.command()
def spaces():
    for space in nis.get_all_spaces():
        click.echo(space)


@cli.command('in_space')
@click.argument('space_name', type=str)
def get_notes_in_space(space_name):
    click.echo('** Notes in {}'.format(space_name))
    for note in nis.get_notes_in_space(space_name):
        note_format(note)


@cli.command('del_space')
@click.argument('space_name', type=str)
def get_notes_in_space(space_name):
    click.echo('Deleting notes in {}'.format(space_name))
    nis.remove_space(space_name)


@cli.command('recent')
@click.argument('count', type=int)
def get_recent(count):
    for note in nis.get_recent_notes(count):
        note_format(note)


@cli.command('last')
def get_last_note():
    note_format(nis.get_last_note()[0])


@cli.command('wipe')
def remove_all_notes():
    if click.confirm('Are you sure?'):
        nis.clear_notes()

if __name__ == '__main__':
    cli()
