FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN pip install -r ./requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo_app.wsgi:application"]
