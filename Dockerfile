FROM python:3

RUN pip3 install --upgrade pip
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

RUN curl -o redis.tar.gz "http://download.redis.io/releases/redis-4.0.2.tar.gz" && \
    mkdir redis_tmp/ && \
    tar xzf redis.tar.gz -C redis_tmp && \
    # Rename temporary directory
    mv redis_tmp/* redis && \
    # Install Redis
    cd redis && \
    make && \
    make install && \
    # Remove source files
    cd .. && \
    rm -rf redis && \
    redis-server -v

COPY app.py /app/app.py
COPY templates /app/templates

EXPOSE 8000
EXPOSE 6379

CMD [ "python3", "app.py" ]