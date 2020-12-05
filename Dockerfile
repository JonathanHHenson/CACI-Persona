FROM python:3.9
RUN mkdir -p /etc/caci

RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /tmp/caci_persona
RUN pip install /tmp/caci_persona

RUN unzip /tmp/caci_persona/fake_profiles.zip && \
    rm /tmp/caci_persona/fake_profiles.zip

ENV FLASK_APP=persona_api.app
ENV PERSONA_API_DB_SQLITE_PATH=/etc/caci/persona.sqlite
CMD flask run initdb
CMD flask run import-json /tmp/caci_persona/fake_profiles.json
CMD flask run --host=0.0.0.0