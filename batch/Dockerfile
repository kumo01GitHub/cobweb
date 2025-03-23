FROM apache/spark-py:latest
ADD ./requirements.txt .
RUN pip install -r requirements.txt && \
    wget -P ./jars https://jdbc.postgresql.org/download/postgresql-42.7.3.jar
ADD ./cobweb/bin/exec.sh ./cobweb/bin/exec.sh
