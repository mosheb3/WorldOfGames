FROM python:3
# FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip install Flask
RUN pip install python-exchangeratesapi

EXPOSE 8081

CMD ["python3", "webServer.py"]
CMD ["python3", "MainGame.py"]
