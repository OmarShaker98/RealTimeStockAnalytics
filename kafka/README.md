
# Kafka Cluster Configuration Guide

This README provides guidance on how to customize the configuration files for all Kafka nodes within your cluster. It also covers Metricbeat setup for collecting Kafka metrics and system metrics. To ensure the components work correctly within your environment, please update the IP address placeholders, log directory paths, and other configurations as described below.

## 1. Kafka Node Configuration

### IP Placeholder Customization

#### Current Configuration
In each Kafka node's configuration file (`server.properties`), the IP addresses for the broker and the advertised listeners are set as placeholders. You need to replace these placeholders with your desired IP addresses or hostnames.

```properties
# The address the socket server listens on.
listeners=PLAINTEXT://kafka-node:9092

# Listener name, hostname, and port the broker will advertise to clients.
advertised.listeners=PLAINTEXT://kafka-node:9092
```

#### Instructions for Customization
- **Replace `kafka-node` with the IP address or hostname of your server** where this Kafka broker is running.
- For example, if the server IP address is `192.168.1.10`, update the settings as follows:
  ```properties
  listeners=PLAINTEXT://192.168.1.10:9092
  advertised.listeners=PLAINTEXT://192.168.1.10:9092
  ```

### Log Directory Customization

#### Current Configuration
The log directory where Kafka stores data is defined as follows:

```properties
log.dirs=/yourpath/real-time-stock-market-analytics/kafka/kafka-node/logs
```

#### Instructions for Customization
- **Replace `/yourpath/real-time-stock-market-analytics/kafka/kafka-node/logs` with the actual directory path** where you want Kafka to store its log files.
- For example, if your desired log path is `/var/lib/kafka/logs`, update the setting as follows:
  ```properties
  log.dirs=/var/lib/kafka/logs
  ```

### Additional Recommendations
- **broker.id**: Ensure that each Kafka broker has a unique `broker.id` to avoid conflicts within the cluster.
- **Zookeeper Configuration**: Make sure the `zookeeper.connect` string is properly set to reflect your Zookeeper cluster's IP addresses.

## 2. Metricbeat Configuration

Metricbeat is used to collect metrics from Kafka brokers and system-level metrics from each node. Below are the details on how to set up Metricbeat to gather Kafka and system metrics.

### Kafka Module

The Kafka module configuration for Metricbeat should be customized for each node:

```yaml
- module: kafka
  metricsets:
    - partition
    - consumergroup
    - consumer
    - broker
  period: 5s
  hosts: ["your-kafka-node:9092"]  # Replace with your Kafka node's IP or hostname

  client_id: metricbeat-node
  retries: 3
  backoff: 250ms
```

#### Instructions for Customization
- **Replace `your-kafka-node` with the IP address or hostname** of the Kafka broker.
- Update `client_id` to reflect the name of the node (e.g., `metricbeat-node1`, `metricbeat-node2`).

### System Module

The System module for Metricbeat collects metrics related to CPU, memory, network, and processes:

```yaml
- module: system
  period: 5s
  metricsets:
    - cpu
    - load
    - memory
    - network
    - process
    - process_summary
    - core
  process.include_top_n:
    by_cpu: 5
    by_memory: 5
```

This setup helps monitor the overall health and performance of the Kafka nodes.

## 3. Kibana and Elasticsearch Customization

To visualize and analyze the metrics collected by Metricbeat, you will need to configure Kibana and Elasticsearch nodes. Customization includes specifying the Kibana and Elasticsearch hosts in your Metricbeat configuration.

### Customization Instructions
- **Kibana**: Update the `setup.kibana.host` setting in Metricbeat to point to your Kibana node.
- **Elasticsearch**: Ensure that the `output.elasticsearch.hosts` configuration in Metricbeat points to your Elasticsearch cluster nodes.

```yaml
setup.kibana:
  host: "your-kibana-node:5601"

output.elasticsearch:
  hosts: ["your-elasticsearch-node:9200"]
```

Replace `your-kibana-node` and `your-elasticsearch-node` with the appropriate IP addresses or hostnames of your Kibana and Elasticsearch servers.

## 4. Systemd Services

In the future, the `systemd-services` folder will provide detailed instructions on how to configure Kafka and Metricbeat to start automatically on system boot using systemd. Stay tuned for updates.

## License
This configuration setup is licensed under the Apache License, Version 2.0. You may not use this setup except in compliance with the License. For more details, please see the [Apache License](http://www.apache.org/licenses/LICENSE-2.0).

## Troubleshooting
If you encounter issues with your setup, please check the following:
- **Firewall Settings**: Ensure that all necessary ports (e.g., `9092` for Kafka, `5601` for Kibana, `9200` for Elasticsearch) are open and accessible.
- **Hostname Resolution**: If you are using hostnames, make sure that they resolve correctly to the IP addresses of your servers.

Feel free to reach out if you have any questions or need further assistance with configuring your Kafka and Metricbeat setup.
