# rubytalks-nlp-api

API for Natural Language Processing

## Build

`docker build --tag rubytalks-nlp-api .`

## Run

`docker run --name nlp-api -p 5000:5000 rubytalks-nlp-api`

## Usage

```bash
curl -G 'http://localhost:5000/items' --data-urlencode "q=Alex Koval is a professional"

# response

{"text": "Alex Koval is a professional", "ents": [{"start": 0, "end": 10, "label": "PERSON"}], "sents": [{"start": 0, "end": 28}], "tokens": [{"id": 0, "start": 0, "end": 4, "pos": "PROPN", "tag": "NNP", "dep": "compound", "head": 1}, {"id": 1, "start": 5, "end": 10, "pos": "PROPN", "tag": "NNP", "dep": "nsubj", "head": 2}, {"id": 2, "start": 11, "end": 13, "pos": "AUX", "tag": "VBZ", "dep": "ROOT", "head": 2}, {"id": 3, "start": 14, "end": 15, "pos": "DET", "tag": "DT", "dep": "det", "head": 4}, {"id": 4, "start": 16, "end": 28, "pos": "ADJ", "tag": "JJ", "dep": "attr", "head": 2}]}
```
