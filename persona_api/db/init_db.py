import click
from . import db
from flask.cli import with_appcontext


@click.command('initdb')
@with_appcontext
def init_db():
    """Reconstructs all the database tables"""
    db.drop_all()
    db.create_all()
    click.echo('Initialized the database.')


def register_command(app):
    """Registers the init_db cli command

    :param app: The flask app to register the command to
    """
    app.cli.add_command(init_db)
