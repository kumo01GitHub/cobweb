ARG python_version
FROM python:${python_version}
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./.env /code/
COPY ./cobweb/ /code/cobweb/
COPY ./manage.py /code/
RUN python3 manage.py collectstatic && \
    python3 manage.py migrate
RUN python3 manage.py createsuperuser --noinput; exit 0
