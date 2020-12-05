from . import db
from .model import Person, Location, Website
from sqlalchemy.orm import Session


def import_person_from_json(person_item: dict):
    """Imports person either by updating an existing record or by inserting a new record

    :param person_item: A dictionary object that represents a person
    :returns: 'update' if person record updated else 'insert'
    """
    existing_person = get_person(person_item['username'])
    if existing_person:
        update_person(existing_person, person_item)
        return 'update'
    else:
        add_person(person_item)
        return 'insert'


def update_person(person: Person, person_item: dict, session: Session = db.session):
    """Updates a person record

    :param person: The person record to update
    :param person_item: The data to update the person with
    :param session: The current database session
    """
    person.company = person_item.get('company')
    person.ssn = person_item.get('ssn')
    person.residence = person_item.get('residence')
    person.blood_group = person_item.get('blood_group')
    person.name = person_item.get('name')
    person.sex = person_item.get('sex')
    person.address = person_item.get('address')
    person.mail = person_item.get('mail')
    person.birthdate = person_item.get('birthdate')

    current_location = person_item.get('current_location')
    if person.current_location and current_location:
        # If current location is defined in both new and old data, update existing record
        person.current_location.latitude = current_location[0]
        person.current_location.longitude = current_location[1]
    elif current_location:
        # If old current location is not defined and the new current location is, then create a new location record.
        location = Location(
            username=person.username,
            latitude=current_location[0],
            longitude=current_location[1]
        )
        session.add(location)
    elif person.current_location:
        # If new current location is not specified, delete the current location record.
        person.current_location = None

    new_websites = set(new_websites if (new_websites := person_item.get('website')) else [])
    old_websites = set()
    if person.website:
        # Remove old websites that aren't included in the new website list
        for old_website in person.website:
            if old_website.url not in new_websites:
                session.delete(old_website)
            else:
                # Updates the old_websites set with urls that are kept
                old_websites.add(old_website.url)

        # Add the new websites that aren't already in the old websites list
        for new_url in new_websites:
            if new_url not in old_websites:
                website = Website(
                    username=person.username,
                    url=new_url
                )
                session.add(website)

    session.add(person)
    session.commit()


def add_person(person_item: dict, session: Session = db.session):
    """Inserts a person record

    :param person_item: The data to construct the person record with
    :param session: The current database session
    :returns: The new person record
    """
    username = person_item['username']
    person = Person(
        username=username,
        company=person_item.get('company'),
        ssn=person_item.get('ssn'),
        residence=person_item.get('residence'),
        blood_group=person_item.get('blood_group'),
        name=person_item.get('name'),
        sex=person_item.get('sex'),
        address=person_item.get('address'),
        mail=person_item.get('mail'),
        birthdate=person_item.get('birthdate')
    )
    session.add(person)

    current_location = person_item.get('current_location')
    if current_location:
        location = Location(
            username=username,
            latitude=current_location[0],
            longitude=current_location[1]
        )
        session.add(location)

    if 'website' in person_item:
        for url in set(person_item['website']):
            website = Website(username=username, url=url)
            session.add(website)

    session.commit()
    return person


def get_person(username: str, session: Session = db.session):
    """Obtains the person record with the specified username

    :param username: The username of the person to obtain
    :param session: The current database session
    :return: A Person record or None
    """
    if not session:
        session = db.session
    return session.query(Person).filter_by(username=username).one_or_none()


def get_people(top: int, skip: int, session: Session = db.session):
    """Returns a list of all person records (paginated)

    :param top: The number of records to return
    :param skip: The number of records to skip
    :param session: The current database session
    :return: An iterable of Person records
    """
    if not session:
        session = db.session
    return session.query(Person).limit(top).offset(skip).all()


def delete_person(person: Person, session: Session = None):
    """Deletes a person record

    :param person: The person record to delete
    :param session: The current database session
    """
    if not session:
        session = db.session
    session.delete(person)
    session.commit()
