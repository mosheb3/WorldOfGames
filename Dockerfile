FROM python:3

WORKDIR /app

COPY . /app

RUN python3 -m pip install --upgrade pip
RUN pip3 install python-exchangeratesapi
RUN pip3 install selenium
RUN pip3 install --upgrade setuptools

RUN chmod 744 *.py *.sh

CMD ["python3", "/app/MainGame.py"]
