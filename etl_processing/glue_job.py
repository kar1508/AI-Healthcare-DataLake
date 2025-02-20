import sys
import boto3
import pyspark
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

# Initialize Spark and Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# S3 bucket and Redshift details
S3_INPUT_PATH = "s3://healthcare-data-lake/raw-data/"
S3_OUTPUT_PATH = "s3://healthcare-data-lake/processed-data/"
REDSHIFT_TABLE = "healthcare_anomalies"
REDSHIFT_CONNECTION = "redshift-healthcare-cluster"

# Read data from S3
input_dynamic_frame = glueContext.create_dynamic_frame.from_options(
    format_options={"json": {}},
    connection_type="s3",
    connection_options={"paths": [S3_INPUT_PATH]},
    format="json"
)

# Data Transformation: Filter anomalous records
def filter_anomalies(rec):
    return rec["heart_rate"] > 110 or rec["oxygen_level"] < 90

filtered_df = input_dynamic_frame.toDF().filter(filter_anomalies)
filtered_dynamic_frame = DynamicFrame.fromDF(filtered_df, glueContext, "filtered_dynamic_frame")

# Write transformed data to S3
glueContext.write_dynamic_frame.from_options(
    frame=filtered_dynamic_frame,
    connection_type="s3",
    connection_options={"path": S3_OUTPUT_PATH},
    format="json"
)

# Write transformed data to Redshift
glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=filtered_dynamic_frame,
    catalog_connection=REDSHIFT_CONNECTION,
    connection_options={"dbtable": REDSHIFT_TABLE, "database": "dev"},
    transformation_ctx="write_to_redshift"
)

print("ETL Job Completed Successfully!")
