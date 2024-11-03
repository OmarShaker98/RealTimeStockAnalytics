from confluent_kafka import Producer
from airflow import DAG
from airflow.operators.python import PythonOperator
import pytz
from datetime import datetime, timedelta
import logging
import requests
import json

default_args = {
    'owner': 'DE Team',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

egypt_tz = pytz.timezone('Africa/Cairo')

dag = DAG('PROD', default_args=default_args, schedule='*/5 * * * *',start_date=egypt_tz.localize(datetime(2024,9,29,19,41)) , max_active_runs=1)

def from_api():
    Topic = 'StocksData5M'
    producer = Producer({'bootstrap.servers': '10.0.0.10:9092,10.0.0.11:9092,10.0.0.12:9092','linger.ms': 300 , 'acks': '1'})  

    api_url = 'http://localhost:5000/stock_data'

    #df = pd.read_json(api_url)
    #json_data = df.to_json(orient='records',lines=False)

    response=requests.get(api_url)
    jsonifed=response.json()

    producer.produce(Topic , value=json.dumps(jsonifed))

    producer.poll(1)
    producer.flush()


to_kafka = PythonOperator(
    task_id='Producer',
    python_callable=from_api,
    dag=dag
)

to_kafka
