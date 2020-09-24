FROM redis:6.0-buster

RUN apt-get update && \
  apt-get install -y python3 python3-pip && \ 
  pip3 install flask redis

WORKDIR /app

COPY app.py .

CMD [ "-c", "redis-server --daemonize yes && FLASK_APP=/app/app.py flask run --host 0.0.0.0 --port 80" ]

ENTRYPOINT [ "bash" ]
