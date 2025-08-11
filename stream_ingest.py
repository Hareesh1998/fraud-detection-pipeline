from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StreamingIngestion").getOrCreate()

# Read from Azure Event Hubs
connectionString = "Endpoint=sb://<namespace>.servicebus.windows.net/...;SharedAccessKeyName=...;SharedAccessKey=..."
ehConf = {
    'eventhubs.connectionString': connectionString
}

df_stream = spark.readStream.format("eventhubs").options(**ehConf).load()

# Parse transaction JSON
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("amount", DoubleType()),
    StructField("merchant", StringType()),
    StructField("timestamp", StringType()),
    StructField("customer_id", StringType())
])

df_parsed = df_stream.select(from_json(col("body").cast("string"), schema).alias("data")).select("data.*")

# Write to Bronze Delta
df_parsed.writeStream.format("delta").outputMode("append").option("checkpointLocation", "/mnt/checkpoints/transactions").start("/mnt/delta/bronze_transactions")
