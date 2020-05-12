FROM python:3.7-alpine
COPY . /app
RUN pip install Flask
RUN pip install python-exchangeratesapi
CMD python MainGame.py