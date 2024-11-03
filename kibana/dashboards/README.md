
# Dashboard Documentation

This folder contains Kibana dashboard files for visualizing various real-time insights into Kafka and system performance. The dashboards are provided in `.ndjson` format for easy import into Kibana.

## Dashboards Included

### 1. Real-Time Kafka Insights

- **File:** `Real-Time Kafka Insights.ndjson`
- **Description:** This dashboard provides detailed visualizations and metrics on Kafka performance and activity, including:
  - **Topic & Consumer Offsets:** Monitoring the offsets of different Kafka topics.
  - **Consumer Group Lag:** Analyzing lag per consumer group.
  - **Kafka Metrics:** Key metrics on Kafka brokers and partitions.
  - **Consumer Partition Reassignments:** Visualization of partition movements and reassignments.
  - **Kafka Brokers Overview:** Insights into broker status and health.

#### Usage
To use the `Real-Time Kafka Insights` dashboard:
1. Import the `.ndjson` file into Kibana using the **Saved Objects** import feature.
2. Navigate to **Dashboard** in Kibana to view real-time Kafka metrics.

### 2. Real-Time System Insights

- **File:** `Real-Time System Insights.ndjson`
- **Description:** This dashboard visualizes real-time system metrics for host monitoring. Key metrics include:
  - **CPU and Memory Usage:** Detailed views of CPU load and memory consumption.
  - **Network Performance:** Insights into network traffic and connection stability.
  - **Process Monitoring:** Lists of top resource-consuming processes.
  - **System Health Overview:** General health indicators for the monitored system.

#### Usage
To use the `Real-Time System Insights` dashboard:
1. Import the `.ndjson` file into Kibana using the **Saved Objects** import feature.
2. Navigate to **Dashboard** in Kibana to monitor system health and performance in real-time.

## Importing Dashboards into Kibana

1. Go to **Kibana UI** > **Management** > **Saved Objects**.
2. Click on the **Import** button.
3. Select the `.ndjson` file you want to import (`Real-Time Kafka Insights.ndjson` or `Real-Time System Insights.ndjson`).
4. Follow the prompts to complete the import process.

## Additional Notes

- These dashboards are designed to integrate with Metricbeat and other data sources that feed real-time metrics into Elasticsearch.
- Ensure that the appropriate indices are configured in Kibana to match the data provided by Metricbeat and your Kafka setup.

## Troubleshooting

- If the dashboards do not display correctly, verify that the required data is available in your Elasticsearch indices.
- Check your Kibana version compatibility with the `.ndjson` files provided.
