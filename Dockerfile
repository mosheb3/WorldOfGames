FROM python:3.7-alpine
WORkDIR /app
COPY . /app
RUN pip install Flask
RUN pip install python-exchangeratesapi
# CMD runWebServer.sh > /dev/null 2>&1
CMD python MainGame.py