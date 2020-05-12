FROM python:3.7-alpine
COPY . /app
RUN pip install Flask
RUN pip install python-exchangeratesapi
CMD /app/runWebServer.sh > /dev/null 2>&1
CMD python /app/MainGame.py