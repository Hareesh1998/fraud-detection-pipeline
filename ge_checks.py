import great_expectations as ge
import pandas as pd

df = pd.read_parquet("/mnt/delta/bronze_transactions")
gdf = ge.from_pandas(df)

gdf.expect_column_values_to_not_be_null("transaction_id")
gdf.expect_column_values_to_be_between("amount", min_value=0, max_value=10000)

results = gdf.validate()
print(results)
