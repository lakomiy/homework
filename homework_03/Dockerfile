#docker build . -t homework_003 && docker run -p 8000:8000 homework_003
FROM python:3.9-buster

WORKDIR /var/app

RUN pip install poetry==1.1.11

COPY appp/pyproject.toml appp/poetry.lock ./

RUN poetry config virtualenvs.create false

RUN poetry install

COPY appp .

EXPOSE 8000

CMD uvicorn app:app --host=0.0.0.0
