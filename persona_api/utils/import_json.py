import click
import ijson
from persona_api.db.db_operations import import_person_from_json
from os.path import isfile
from flask.cli import with_appcontext


@click.command('import-json')
@click.argument('filepath')
@with_appcontext
def import_json(filepath, progress_period=1000):
    """Imports all people from a json file

    :param filepath: The json file to load people from
    :param progress_period: The number of records to process between progress updates
    """
    if not isfile(filepath):
        click.echo(f'File "{filepath}" does not exist')
        return

    inserted_count = 0
    updated_count = 0
    period_count = 0
    with open(filepath, 'rb') as fs:
        person_stream = ijson.items(fs, 'item')
        for person_item in person_stream:
            if 'username' not in person_item:
                click.echo('Person missing username.. skipping..')
                continue
            operation = import_person_from_json(person_item)
            if operation == 'insert':
                inserted_count += 1
            else:
                updated_count += 1
            period_count += 1
            if period_count == progress_period:
                click.echo(f'Inserted {inserted_count} people, and updated {updated_count} people..')
                period_count = 0

    click.echo('Import complete!')


def register_command(app):
    """Registers the import_json cli command

    :param app: The flask app to register the command to
    """
    app.cli.add_command(import_json)
