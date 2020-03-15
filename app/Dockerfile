FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /app


