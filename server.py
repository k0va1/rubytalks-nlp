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

run(host='0.0.0.0', port=5000, debug=True)
