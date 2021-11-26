FROM python:3

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY database /app/database
COPY handlers /app/handlers
COPY templates /app/templates
COPY app.py /app/app.py
COPY schema.sql /app/schema.sql

RUN flask init-db

EXPOSE 5000

CMD [ "python3", "app.py" ]
                             