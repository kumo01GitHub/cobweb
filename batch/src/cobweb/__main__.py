"""Execute PySpark batch."""
import sys
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

from pyspark.sql import SparkSession

from cobweb.sample import sample_database, sample_helloworld

def main():
    """Execute provided app name batch."""
    load_dotenv(verbose=True)
    env_filename = '.env'
    if getenv('PROFILE', '') != '':
        env_filename = f".env.{getenv('PROFILE')}"
    dotenv_path = join(dirname(__file__), '../..', env_filename)
    load_dotenv(dotenv_path, override=True)

    spark = SparkSession.builder.appName(sys.argv[1]).getOrCreate()
    log4j = spark._jvm.org.apache.log4j # pylint: disable=protected-access
    logger = log4j.LogManager.getLogger(__name__)
    logger.info(f"run {spark.conf.get('spark.app.name')}")

    if spark.conf.get("spark.app.name") == "helloworld":
        sample_helloworld.run(spark)
    elif spark.conf.get("spark.app.name") == "database":
        sample_database.run(spark)
    else:
        raise ValueError(f"No such application: {spark.conf.get('spark.app.name')}")

if __name__ == "__main__":
    main()
