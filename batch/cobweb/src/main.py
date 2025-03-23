import sys

from pyspark.sql import SparkSession

from sample import sample

def main():
    spark = SparkSession.builder.appName(sys.argv[1]).getOrCreate()
    print("run", spark.conf.get("spark.app.name"))

    if spark.conf.get("spark.app.name") == "sample":
        sample.exec(spark)
    else:
        raise ValueError("No such application: " + spark.conf.get("spark.app.name"))

if __name__ == "__main__":
    main()
