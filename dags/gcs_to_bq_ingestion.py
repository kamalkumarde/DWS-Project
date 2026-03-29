from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime, timedelta

with DAG(
    '1PB_GCS_to_BigQuery',
    schedule_interval='@hourly',
    start_date=datetime(2026, 3, 1),
    catchup=False
) as dag:

    load_data = GCSToBigQueryOperator(
        task_id='load_jsonl_to_bq',
        bucket='dws-lake-prod',
        source_objects=['raw/dt={{ ds_nodash }}/*.jsonl'],
        destination_project_dataset_table='dws-project.warehouse_raw.events',
        source_format='NEWLINE_DELIMITED_JSON',
        write_disposition='WRITE_APPEND',
        autodetect=True
    )