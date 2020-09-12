FROM python:3.8-slim
EXPOSE 5000
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD ./ ./
# CMD gunicorn -b 0.0.0.0:5001 -w 9 --worker-class=gthread --worker-connections=1000 main:app
CMD python3 main.py 0.0.0.0:5000




