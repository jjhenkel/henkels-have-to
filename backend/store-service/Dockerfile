FROM redis:6.0-buster

RUN apt-get update && \
  apt-get install -y python3 python3-pip && \ 
  pip3 install flask

WORKDIR /app

COPY app.py .

CMD [ "/app/app.py" ]

ENTRYPOINT [ "python3" ]
