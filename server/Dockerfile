FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./.env /code/
ADD ./cobweb/ /code/cobweb/
ADD ./manage.py /code/
RUN python3 manage.py collectstatic && \
    python3 manage.py migrate && \
    python3 manage.py createsuperuser --noinput
