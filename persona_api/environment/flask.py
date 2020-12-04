import os

PREFIX = 'PERSONA_API'

SECRET_KEY = os.environ.get(f'{PREFIX}_SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = os.urandom(16)
