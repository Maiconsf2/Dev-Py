from pyspark.sql import SparkSession
from time import sleep

spark = SparkSession.builder.appName("Projeto Python").getOrCreate()

juros = spark.read.json("hdfs://namenode:8020/user/maicon/data/juros_selic/juros_selic.json")
juros.collect()
juros.write.parquet("hdfs://namenode:8020/user/maicon/projeto_python", mode="overwrite")

sleep(100)

spark.stop()