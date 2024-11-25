from pyspark.sql import SparkSession

def get_spark_session(app_name="Network-Traffic-Pipeline"):
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.cassandra.connection.host", "cassandra") \
        .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.5.1") \
        .getOrCreate()
