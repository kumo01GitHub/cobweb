import os
from string import Template

def exec(spark):
    url = Template("jdbc:postgresql://${host}:${port}/${database}")

    df = (
        spark.read.format("jdbc")
        .option(
            "url",
            url.substitute(
                host=os.environ["DATABASE_HOST"],
                port=os.environ["DATABASE_PORT"],
                database=os.environ["DATABASE_NAME"],
            ),
        )
        .option("dbtable", "django.auth_user")
        .option("user", os.environ["DATABASE_USER"])
        .option("password", os.environ["DATABASE_PASSWORD"])
        .option("driver", "org.postgresql.Driver")
        .load()
    )

    df.printSchema()
    df.show(20)
