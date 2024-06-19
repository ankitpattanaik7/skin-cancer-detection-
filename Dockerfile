FROM python:3.11

USER root

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

RUN ["ifconfig"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]