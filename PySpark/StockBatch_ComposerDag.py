from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocStartClusterOperator,
    DataprocSubmitJobOperator,
    DataprocStopClusterOperator,
)
from airflow.utils.dates import days_ago

# Define your default arguments
default_args = {
    'start_date': days_ago(1),
    'retries': 1,
}

# Create a DAG instance
with DAG(
    'automated_stock_batch_daily',
    default_args=default_args,
    # Set the schedule to run at 9:54 PM UTC
    schedule_interval='0 15 * * *',  # 3 PM UTC --> 6 PM EGY
    catchup=False,
) as dag:

    # Task to start the Dataproc cluster
    start_cluster = DataprocStartClusterOperator(
        task_id='start_dataproc_cluster',
        cluster_name='dataproc-cluster',  # Specify your cluster name here
        region='us-central1',
        gcp_conn_id='google_cloud_default',
    )

    # Task to submit the PySpark job
    job_config = {
        "reference": {"project_id": "realtimepiplineproject"},
        "placement": {
            "cluster_name": "dataproc-cluster"  # Specify the cluster name here
        },
        "pyspark_job": {
            "main_python_file_uri": "gs://my-temp-bucket-123456/AutomatedBatchStockCode.py",
            "jar_file_uris": [
                "gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.28.0.jar"
            ],
            "args": [],
        },
    }

    submit_job = DataprocSubmitJobOperator(
        task_id='submit_pyspark_job',
        job=job_config,
        region='us-central1',
        gcp_conn_id='google_cloud_default',
    )
    
    # Task to stop the Dataproc cluster
    stop_cluster = DataprocStopClusterOperator(
        task_id='stop_dataproc_cluster',
        cluster_name='dataproc-cluster',  # Specify your cluster name here
        region='us-central1',
        gcp_conn_id='google_cloud_default',
    )

    # Set task dependencies
    start_cluster >> submit_job >> stop_cluster
