import os
from os.path import isdir, join
from pathlib import Path
import pytest

from persona_api.db import db as _db
from persona_api.app import create_app


TESTDIR = join(Path.home(), 'caci_persona')
TESTDB = 'test_project.db'
TESTDB_PATH = join(TESTDIR, TESTDB)
TEST_DATABASE_URI = f'sqlite:///{TESTDB_PATH}'


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    if not isdir(TESTDIR):
        os.mkdir(TESTDIR)

    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    }
    app = create_app(__name__, settings_override)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TESTDB_PATH)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = _db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
