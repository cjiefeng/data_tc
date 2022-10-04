FROM python:3.10.4-slim-buster

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app

CMD ["/bin/sh", "-c", "python3 ml.py"]
