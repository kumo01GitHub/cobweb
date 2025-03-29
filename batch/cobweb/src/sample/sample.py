import os

def exec(spark):
    jdbc = (
        spark.read.format("jdbc")
        .option("url", os.environ["SPARK_DATABASE_URL"])
        .option("dbtable", "django.auth_user")
        .option("user", os.environ["SPARK_DATABASE_USER"])
        .option("password", os.environ["SPARK_DATABASE_PASSWORD"])
        .option("driver", "org.postgresql.Driver")
        .load()
    )

    jdbc.printSchema()
    jdbc.show(20)
