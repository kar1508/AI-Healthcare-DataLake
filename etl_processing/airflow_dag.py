from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator

# Define default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'healthcare_data_pipeline',
    default_args=default_args,
    description='Orchestrate Healthcare Data Processing using Glue and S3',
    schedule_interval='@hourly',
    catchup=False,
)

# Task to trigger AWS Glue Job
glue_task = AwsGlueJobOperator(
    task_id='run_glue_job',
    job_name='HealthcareGlueJob',
    aws_conn_id='aws_default',
    script_location='s3://healthcare-data-lake/scripts/glue_job.py',
    s3_bucket='healthcare-data-lake',
    iam_role_name='AWSGlueServiceRole',
    dag=dag,
)

# Task to check S3 bucket after Glue Job
check_s3 = BashOperator(
    task_id='check_s3_output',
    bash_command='aws s3 ls s3://healthcare-data-lake/processed-data/',
    dag=dag,
)

glue_task >> check_s3
