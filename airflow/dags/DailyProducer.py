import yfinance as yf
from confluent_kafka import Producer
from airflow import DAG
from airflow.operators.python import PythonOperator
import pytz
from datetime import datetime, timedelta
import json

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


def get_stock_data(companies):
    stock_data = []
    for symbol, (sector, industry) in companies.items():
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            last_data = data.iloc[-1]
            date = str(last_data.name.date()) 
            stock_data.append({
                'date': date,
                'company': symbol,
                'sector': sector,
                'industry': industry,
                'open': last_data['Open'],
                'high': last_data['High'],
                'low': last_data['Low'],
                'close': last_data['Close'],
                'volume': last_data['Volume'],
                'adj_close': last_data['Close']})
    return stock_data

default_args = {'owner': 'DE Team','retries': 5,'retry_delay': timedelta(minutes=1)}


egypt_tz = pytz.timezone('Africa/Cairo')

dag = DAG('Daily_Producer', default_args=default_args, schedule = '@daily', start_date=egypt_tz.localize(datetime(2024, 9, 25)),catchup = True)

def to_kafka_topic():
    Topic = 'DailyStocks'
    producer = Producer({'bootstrap.servers': '10.0.0.10:9092,10.0.0.11:9092,10.0.0.12:9092','linger.ms': 600 , 'acks': 'all'})  

    latest_data_json = json.dumps(get_stock_data(companies))

    producer.produce(Topic , value=latest_data_json)

    producer.poll(1)
    producer.flush()

to_kafka = PythonOperator(task_id='DailyProducer' , python_callable=to_kafka_topic,dag=dag) 

to_kafka

