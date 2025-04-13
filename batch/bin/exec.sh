$SPARK_HOME/bin/spark-submit --driver-class-path ./jars/postgresql-42.7.3.jar --jars ./jars/postgresql-42.7.3.jar --master spark://master:7077 ./src/cobweb/__main__.py "$@"
