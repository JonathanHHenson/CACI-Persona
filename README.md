# Persona API
The Persona API is a fake RESTful API that delivers made up data on a few endpoints. The data sits within a zip file and needs to be decompressed only on deployment. A crucial task is to find a way to do that in an elegant manner.

# Setup
## Basic Steps
1. Install python 3.9 and pipenv
2. Run `pipenv install` to install dependencies
3. Change `PERSONA_API_DB_SQLITE_PATH` in `.env` to where you would like the DB to be initialized
4. Run `pipenv run initdb` to initialize the database
5. Run `pipenv run import-json <json-file>` replacing `<json-file>` with the path to the json data to import
6. Run `pipenv run server` to start the flask server on port 5000

## Environment Variables
**PERSONA_API_SECRET_KEY** - To set the secret key for flask sessions

**PERSONA_API_DB_SQLITE_PATH** - To set the location of a local SQLITE database

**PERSONA_API_DB_PROTOCOL** - To configure the driver protocol for an external database (e.g. `sqlite` for a sqlite database)

**PERSONA_API_DB_HOST** - To configure the hostname for an external database

**PERSONA_API_DB_NAME** - To configure the name of an external database

**PERSONA_API_DB_USERNAME** - To configure the username to connect to an eternal database

**PERSONA_API_DB_PASSWORD** - To configure the password to connect to an eternal database
