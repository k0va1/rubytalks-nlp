from bottle import route, run, response, request
from json import dumps
import spacy

nlp = spacy.load("en_core_web_sm")

@route('/items')
def items():
    query = request.params.q

    doc = nlp(query)

    response.content_type = 'application/json'
    return doc.to_json()

@route('/people')
def people():
    query = request.params.q

    doc = nlp(query)

    people = dict({'people': list(map(lambda p: p.text, filter(lambda e: e.label_ == 'PERSON', doc.ents)))})

    response.content_type = 'application/json'
    return dumps(people)

run(host='0.0.0.0', port=5000, debug=True)
