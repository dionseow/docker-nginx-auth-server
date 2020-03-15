FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /app


