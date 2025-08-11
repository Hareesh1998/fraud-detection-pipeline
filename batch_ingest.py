from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BatchIngestion").getOrCreate()

# Load CSV from Azure Blob Storage
df = spark.read.csv("wasbs://data@<your-storage-account>.blob.core.windows.net/transactions/*.csv", header=True, inferSchema=True)

# Write to Bronze Delta table
df.write.format("delta").mode("append").save("/mnt/delta/bronze_transactions")
