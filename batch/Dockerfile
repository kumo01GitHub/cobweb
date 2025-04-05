ARG sparkpy_version
FROM apache/spark-py:${sparkpy_version}
ARG workdir
USER root
RUN mkdir -p ${workdir}
WORKDIR ${workdir}
COPY ./requirements.txt .
COPY ./.env .
ARG jdbc_postgres
ARG python_version
RUN apt-get -y update && \
    apt-get -y --no-install-recommends install python${python_version} && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt && \
    wget --progress=dot:giga -P ./jars ${jdbc_postgres}
ENV PYTHONPATH ${workdir}
