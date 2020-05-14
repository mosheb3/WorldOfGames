FROM python:3
# FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip install python-exchangeratesapi
RUN pip install selenium

CMD ["python3", "MainGame.py"]