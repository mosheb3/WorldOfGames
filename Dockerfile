FROM python:3
# FROM python:3.7-alpine
WORKDIR /app
COPY . /app
VOLUME . /app
RUN pip install Flask
RUN pip install python-exchangeratesapi
# CMD runWebServer.sh > /dev/null 2>&1
CMD python3 MainGame.py
