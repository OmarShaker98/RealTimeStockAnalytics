from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_date, when, explode, year, month, dayofmonth, date_format
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, ArrayType, IntegerType
#import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

import os
import subprocess
import sys

# Check if yfinance is installed; if not, install it
try:
    import yfinance as yf
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yfinance'])

# Google Cloud Storage bucket path for streaming output
gcs_bucket_name = "my-temp-bucket-123456"



# Define the companies and sectors/industries
companies = {
    'AAPL': ['Technology', 'Consumer Electronics'],
    'MSFT': ['Technology', 'Software'],
    'GOOGL': ['Communication Services', 'Internet Content'],
    'NVDA': ['Technology', 'Semiconductors'],
    'BRK-B': ['Financial Services', 'Insurance'],
    'MA': ['Financial Services', 'Credit Services'],
    'V': ['Financial Services', 'Credit Services'],
    'INTC': ['Technology', 'Semiconductors'],
    'CSCO': ['Technology', 'Communication Equipment'],
    'JPM': ['Financial Services', 'Banking'],
    'CRM': ['Technology', 'Software'],
    'BA': ['Industrials', 'Aerospace & Defense'],
    'CAT': ['Industrials', 'Construction Machinery'],
    'CVX': ['Energy', 'Oil & Gas'],
    'HON': ['Industrials', 'Conglomerates'],
    'IBM': ['Technology', 'IT Services'],
    'GS': ['Financial Services', 'Capital Markets'],
    'TRV': ['Financial Services', 'Insurance'],
    'XOM': ['Energy', 'Oil & Gas'],
    'COP': ['Energy', 'Oil & Gas'],
    'PSX': ['Energy', 'Refining & Marketing'],
    'EOG': ['Energy', 'Oil & Gas Exploration & Production']
}


# Create a Spark session
spark = SparkSession.builder.appName("StockData").getOrCreate()

# Define BigQuery table
project_id = "realtimepiplineproject"
dataset_id = "Stock_Pipline"
table_id = "Years"

# Define start and end dates
start_date = datetime.now().date()  # Get today's date
end_date = start_date  # End date is the same as start date for one day of data

all_data = []

for ticker, details in companies.items():
    stock_df = yf.download(ticker, start=start_date, end=end_date + timedelta(days=1), interval='1d')
    
    if not stock_df.empty:
        stock_df['Sector'] = details[0]
        stock_df['Industry'] = details[1]
        stock_df.reset_index(inplace=True)
        stock_df['Company'] = ticker
        
        # Append DataFrame to list
        all_data.append(spark.createDataFrame(stock_df))

# Union all DataFrames and sort
final_df = all_data[0]
for df in all_data[1:]:
    final_df = final_df.union(df)

final_df = final_df.orderBy('Date')
final_df = final_df.withColumnRenamed("Adj Close", "Adj_Close")

final_df = final_df.withColumn("Date", to_date(col("Date"), "yyyy-MM-dd"))
final_df = final_df.withColumn('Price_Range', col('High') - col('Low'))
final_df = final_df.withColumn("Daily_Return", (col("Close") - col("Open")) / col("Open") * 100)
final_df = final_df.withColumn("Price_Category", when(col("Close") < 100, "Low").when(col("Close").between(100, 200), "Medium").otherwise("High"))
final_df = final_df.withColumn("Volatility_percentage", ((col("High") - col("Low")) / col("Close")) * 100)
final_df = final_df.withColumn("Year", year(col("Date"))) \
    .withColumn("Month", month(col("Date"))) \
    .withColumn("Day", dayofmonth(col("Date"))) \
    .withColumn("Weekday", date_format(col("Date"), "E"))


final_df.write \
    .format("bigquery") \
    .option("table", f"{project_id}.{dataset_id}.{table_id}") \
    .option("temporaryGcsBucket", gcs_bucket_name) \
    .mode("append") \
    .save()

# Stop the Spark session
spark.stop()