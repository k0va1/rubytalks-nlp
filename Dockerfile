FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN spacy download en_core_web_sm

EXPOSE 5000

CMD [ "python", "./server.py" ]
