import os
from urllib.parse import quote_plus

PREFIX = 'PERSONA_API_DB'
ENV_SQLITE_PATH = f'{PREFIX}_SQLITE_PATH'
ENV_PROTOCOL = f'{PREFIX}_PROTOCOL'
ENV_HOST = f'{PREFIX}_HOST'
ENV_USERNAME = f'{PREFIX}_USERNAME'
ENV_PASSWORD = f'{PREFIX}_PASSWORD'
ENV_NAME = f'{PREFIX}_NAME'

ERROR_TEMPLATE = f'No %s set for Persona DB. Please set {ENV_SQLITE_PATH} if you wish to use a local DB.'

DB_SQLITE_PATH = os.environ.get(ENV_SQLITE_PATH)
DB_PROTOCOL = os.environ.get(ENV_PROTOCOL)
DB_HOST = os.environ.get(ENV_HOST)
DB_USERNAME = os.environ.get(ENV_USERNAME)
DB_PASSWORD = os.environ.get(ENV_PASSWORD)
DB_NAME = os.environ.get(ENV_NAME)

if DB_SQLITE_PATH:
    DB_URI = 'sqlite:///' + DB_SQLITE_PATH
else:
    if not DB_PROTOCOL:
        raise ValueError(ERROR_TEMPLATE % ENV_PROTOCOL)
    if not DB_HOST:
        raise ValueError(ERROR_TEMPLATE % ENV_HOST)
    if not DB_USERNAME:
        raise ValueError(ERROR_TEMPLATE % ENV_USERNAME)
    if not DB_PASSWORD:
        raise ValueError(ERROR_TEMPLATE % ENV_PASSWORD)
    if not DB_NAME:
        raise ValueError(ERROR_TEMPLATE % ENV_NAME)

    DB_PROTOCOL = quote_plus(DB_PROTOCOL)
    DB_USERNAME = quote_plus(DB_USERNAME)
    DB_PASSWORD = quote_plus(DB_PASSWORD)
    DB_NAME = quote_plus(DB_NAME)

    DB_URI = f'{DB_PROTOCOL}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
