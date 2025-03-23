import sys
from os.path import join, dirname
from dotenv import load_dotenv

from pyspark.sql import SparkSession

from sample import sample

def main():
    load_dotenv(verbose=True)
    dotenv_path = join(dirname(__file__), '../../.env')
    load_dotenv(dotenv_path)

    spark = SparkSession.builder.appName(sys.argv[1]).getOrCreate()
    print("run", spark.conf.get("spark.app.name"))

    if spark.conf.get("spark.app.name") == "sample":
        sample.exec(spark)
    else:
        raise ValueError("No such application: " + spark.conf.get("spark.app.name"))

if __name__ == "__main__":
    main()
