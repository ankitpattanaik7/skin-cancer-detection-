FROM python:3.11

USER root

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app"]