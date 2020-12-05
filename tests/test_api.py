import json
from persona_api.db.db_operations import add_person, get_people
from .data import PEOPLE


def test_get_person_200(client, session):
    for p in PEOPLE:
        add_person(p, session=session)
    expected_person = PEOPLE[0]

    response = client.get(f'/search/{expected_person["username"]}')
    actual_person = json.loads(response.data)

    assert response.status_code == 200 and actual_person['username'] == expected_person['username']


def test_get_person_404(client, session):
    for p in PEOPLE:
        add_person(p, session=session)

    response = client.get('/search/thisusernamedoesntexist')
    message = json.loads(response.data)

    assert response.status_code == 404 and len(message.keys()) == 1 and 'message' in message


def test_get_people_200(client, session):
    for p in PEOPLE:
        add_person(p, session=session)
    expected_people = PEOPLE

    response = client.get('/people')
    actual_people = json.loads(response.data)

    assert response.status_code == 200 and actual_people == expected_people


def test_delete_person_204(client, session):
    for p in PEOPLE:
        add_person(p, session=session)
    person_to_delete = PEOPLE[0]
    expected_people = PEOPLE[1:]

    response = client.delete(f'/people/{person_to_delete["username"]}')
    actual_people = get_people(50, 0, session=session)

    assert response.status_code == 204 and response.data == '' and actual_people == expected_people


def test_delete_person_404(client, session):
    for p in PEOPLE:
        add_person(p, session=session)
    expected_people = PEOPLE

    response = client.delete('/people/thisusernamedoesntexist')
    message = json.loads(response.data)
    actual_people = get_people(50, 0, session=session)

    assert (
        response.status_code == 404
        and len(message.keys()) == 1
        and 'message' in message
        and actual_people == expected_people
    )
