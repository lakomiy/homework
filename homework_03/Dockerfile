#docker run -p 8000:8000 homework
FROM python:3.9-buster
WORKDIR /var/app
RUN pip install poetry==1.1.11
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install
COPY app.py .

CMD uvicorn app:app --host=0.0.0.0
