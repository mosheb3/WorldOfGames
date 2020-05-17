FROM python:3
# FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip3 install python-exchangeratesapi
RUN pip3 install selenium
RUN pip3 install --upgrade setuptools

CMD ["python3", "MainGame.py"]
