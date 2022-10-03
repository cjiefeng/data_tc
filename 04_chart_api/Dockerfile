FROM python:3.10.4-slim-buster

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt update && apt upgrade -y && apt-get install python3-tk -y
ADD . /app

CMD ["/bin/sh", "-c", "python3 plot_covid.py"]
