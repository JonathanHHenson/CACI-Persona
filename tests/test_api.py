import json
from persona_api.db.db_operations import add_person
from .data import PEOPLE


# def test_get_person(app, session):
#     for p in PEOPLE:
#         add_person(p, session)
#     expected_user = PEOPLE[0]
#
#     with app.test_client() as c:
#         response = c.get(f'/search/{expected_user["username"]}')
#     actual_person = json.loads(response.data)
#
#     assert actual_person['username'] == expected_user['username']
