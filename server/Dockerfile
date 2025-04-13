ARG python_version=latest
FROM python:${python_version}
ENV PYTHONUNBUFFERED=1
RUN mkdir /code/
WORKDIR /code/
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./.env /code/
COPY ./src/ /code/src/
RUN python3 src/manage.py collectstatic && \
    python3 src/manage.py migrate
RUN python3 src/manage.py createsuperuser --noinput; exit 0
ENV PYTHONPATH=/code/src/
