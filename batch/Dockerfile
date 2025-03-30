ARG sparkpy_version
FROM apache/spark-py:${sparkpy_version}
ARG workdir
USER root
RUN mkdir -p ${workdir}
WORKDIR ${workdir}
COPY ./requirements.txt .
COPY ./.env .
ARG jdbc_postgres
RUN pip install --no-cache-dir -r requirements.txt && \
    wget --progress=dot:giga -P ./jars ${jdbc_postgres}
