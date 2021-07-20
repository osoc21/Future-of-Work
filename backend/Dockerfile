FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_RUN_PORT=4000
ENV FLASK_DEBUG=1

EXPOSE 4000

COPY src .

CMD python ./app.py
