from persona_api.db.db_operations import add_person, update_person
from .data import PEOPLE


def test_update_person_set_fields_none(session):
    example_person = PEOPLE[0]
    person = add_person(example_person, session)

    update_person(person, {}, session)

    assert (
        person.company is None
        and person.ssn is None
        and person.residence is None
        and person.blood_group is None
        and person.name is None
        and person.sex is None
        and person.address is None
        and person.mail is None
        and person.birthdate is None
        and person.current_location is None
        and len(person.website) == 0
    )


def test_update_person_set_fields(session):
    example_person = PEOPLE[0]
    person = add_person(example_person, session)
    sample_person = PEOPLE[1]

    update_person(person, sample_person, session)
    person_dict = person.to_dict()

    assert (
        person.company == sample_person['company']
        and person.ssn == sample_person['ssn']
        and person.residence == sample_person['residence']
        and person.blood_group == sample_person['blood_group']
        and person.name == sample_person['name']
        and person.sex == sample_person['sex']
        and person.address == sample_person['address']
        and person.mail == sample_person['mail']
        and person.birthdate == sample_person['birthdate']
        and person.current_location.latitude == sample_person['current_location'][0]
        and person.current_location.longitude == sample_person['current_location'][1]
        and person_dict['website'] == sample_person['website']
    )