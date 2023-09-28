FROM python:3.8.1-slim

RUN apt-get update && apt-get install -y python python-pip

RUN pip install flask flask_jsonpify flask_restful flask_cors

COPY app.py /opt/

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
