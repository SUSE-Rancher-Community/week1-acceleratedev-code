FROM redis:6.2

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-pip

WORKDIR /app

RUN mkdir -p /app/redis/

COPY 6379.conf /app/redis/6379.conf

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /app/app.py
COPY templates /app/templates

COPY start.sh /app/start.sh
RUN chmod 755 start.sh

EXPOSE 8000

ENTRYPOINT [ "/app/start.sh" ]