# Elasticsearch Configuration Overview

This README provides an overview of the Elasticsearch configuration for setting up a multi-node cluster. It includes instructions for customizing the configuration, such as specifying the paths for data and logs, configuring the cluster and node settings, and setting up security options.

## Table of Contents
- [Cluster Setup](#cluster-setup)
- [Node Configuration](#node-configuration)
- [Paths for Data and Logs](#paths-for-data-and-logs)
- [Memory Settings](#memory-settings)
- [Network Settings](#network-settings)
- [Discovery and Cluster Formation](#discovery-and-cluster-formation)
- [Security Settings](#security-settings)
- [Customization Guidelines](#customization-guidelines)
- [Additional Resources](#additional-resources)

## Cluster Setup
- **Cluster Name**: The cluster name is set to `kafka-metrics-cluster`. It is recommended to keep this name to ensure consistency when managing multiple clusters.
  ```yaml
  cluster.name: kafka-metrics-cluster
  ```

## Node Configuration
- **Node Name**: Use descriptive names for each node in your cluster to help identify them easily. For example:
  ```yaml
  node.name: <elastic-search-node-name>
  ```
  Replace `<your-elastic-search-node-name>` with a unique identifier for each node.

## Paths for Data and Logs
- **Data Path**: The path where Elasticsearch stores data. This should be customized for each node in the cluster. For example:
  ```yaml
  path.data: /path/to/your/data-directory # EX: /var/lib/elasticsearch/data
              
  ```
- **Log Path**: The path for storing Elasticsearch log files. This should also be customized for each node:
  ```yaml
  path.logs: /path/to/your/log-directory # EX: /var/lib/elasticsearch/logs
  ```

> **Note**: Replace `/path/to/your/data-directory` and `/path/to/your/log-directory` with the actual paths on your system where you want to store the data and logs.

## Memory Settings
- **Heap Size**: Configure the JVM heap size to about half of the available system memory to ensure optimal performance.
- **Memory Lock**: To prevent memory swapping, set the following:
  ```yaml
  bootstrap.memory_lock: true
  ```

## Network Settings
- **Network Host**: Configure the network addresses for each node. This will make the node accessible over the network:
  ```yaml
  network.host: ["<your-elasticsearch-node-ip>", "localhost"]
  ```
  Replace `<your-elasticsearch-node-ip>` with the actual IP address of your Elasticsearch node.

## Discovery and Cluster Formation
- **Seed Hosts**: Specify the initial list of hosts to help Elasticsearch discover other nodes in the cluster:
  ```yaml
  discovery.seed_hosts: ["<elasticsearch-node-ip-1>", "<elasticsearch-node-ip-2>"]
  ```
  Replace `<elasticsearch-node-ip-1>` and `<elasticsearch-node-ip-2>` with the IP addresses of your Elasticsearch nodes.

- **Master Nodes**: Define the initial set of master-eligible nodes:
  ```yaml
  cluster.initial_master_nodes: ["<elasticsearch-master-node-1>", "<elasticsearch-master-node-2>"]
  ```
  Replace `<elasticsearch-master-node-1>` and `<elasticsearch-master-node-2>` with the names of the nodes eligible to be master nodes.

## Security Settings
- **Security Configuration**: For development environments, security features are currently disabled:
  ```yaml
  xpack.security.enabled: false
  xpack.security.transport.ssl.enabled: false
  xpack.security.http.ssl.enabled: false
  ```

> **Note**: For production deployments, it is strongly recommended to enable TLS/SSL to secure communication between nodes and clients.

## Customization Guidelines
- **Node Names**: Use descriptive names to identify each node, ensuring they are unique within the cluster.
- **Paths for Data and Logs**: The paths (`path.data` and `path.logs`) must be customized for each node to point to the specific directories on your file system where data and logs will be stored.
- **IP Addresses**: Replace placeholders like `<elasticsearch-node-ip>`, `<elasticsearch-node-ip-1>`, and `<elasticsearch-node-ip-2>` with the actual IP addresses of your nodes.
- **Cluster Name**: It is recommended to keep the cluster name as `kafka-metrics-cluster` unless you have a specific reason to change it.

## Additional Resources
- For detailed information on configuring Elasticsearch, please refer to the official [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/index.html).
