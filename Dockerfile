FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 "app:create_app()"

