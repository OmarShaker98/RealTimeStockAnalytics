# Airflow DAGs

This directory contains the Directed Acyclic Graphs (DAGs) for the Apache Airflow project focused on stock data processing and real-time simulation.

## Contents

### DAGs
- **dailyproducer.py**: A DAG that runs daily to fetch stock data from Yahoo Finance for a set of predefined companies and produces messages to a Kafka topic named `DailyStocks`.
  
- **5minproducer.py**: A DAG that executes every minute to simulate the generation of real-time stock data by fetching it from a local Flask API and producing messages to a Kafka topic named `StocksData5M`.

### Requirements
- **requirements.txt**: A list of Python dependencies required to run the DAGs. Install them using:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration
Refer to the `/config` directory for necessary configuration files like `airflow.cfg` and web server configuration settings.

### Database
- **airflow.db**: SQLite database that stores the metadata for your Airflow installation, including task instances, DAG runs, and user information.

### Systemd Configuration
For automating the starting of the Airflow web server and scheduler using `systemd`, a dedicated folder named **systemd-configs** will be created outside of the main Airflow directory. This folder will contain all necessary configuration files and instructions on how to set up and manage these services.

You will find the following information in the `systemd-services` folder:
- Instructions to create and configure `systemd` service files for Airflow.
- How to enable and start the Airflow web server and scheduler automatically at boot.

## Setup Instructions
1. **Install Dependencies**:
    Ensure you have the required packages installed:
    ```bash
    pip install -r requirements.txt
    ```

2. **Configure Airflow**:
    Modify the `airflow.cfg` file in the `/config` directory to suit your deployment needs.

3. **Initialize Database**:
    Initialize the Airflow database:
    ```bash
    airflow db init
    ```

4. **Access the UI**:
    Open your web browser and navigate to `http://localhost:8080` to access the Airflow UI.

## Notes
- Ensure Kafka is up and running to allow the DAGs to produce messages successfully.
- The Flask API should also be running to serve data for the `5minproducer.py`.

## Authors
- DE Team
