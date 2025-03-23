FROM apache/spark-py:latest
USER root
ADD ./requirements.txt .
ADD ./.env .
RUN pip install -r requirements.txt && \
    wget -P ./jars https://jdbc.postgresql.org/download/postgresql-42.7.3.jar
