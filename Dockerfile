FROM python:3.8

COPY ./requirements.txt /requirements.txt

WORKDIR .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "uvicorn" ]

CMD [ "main:app", "--host", "0.0.0.0", "--port", "8000" ]