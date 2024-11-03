
# Zookeeper Configuration Guide

This directory contains the configuration and setup instructions for the Zookeeper nodes in your ensemble.

## Table of Contents
- [Overview](#overview)
- [Configuration Details](#configuration-details)
- [Systemd Setup](#systemd-setup)
- [Customization Instructions](#customization-instructions)

## Overview
The Zookeeper nodes are part of a multi-node ensemble designed for distributed coordination. This setup allows for robust and scalable cluster management for distributed systems such as Apache Kafka.

## Configuration Details
Each Zookeeper node configuration needs to ensure that:
- **Zookeeper IP**: The IP address for each node is specified in the configuration file. Ensure that the name resolves properly to your server's IP, either through DNS or your `/etc/hosts` file.
- **Data Path**: The `dataDir` path specified in the configuration file is a placeholder (e.g., `/home/youruser/zookeeper/zookeeper-01/data`). You need to replace this path with your own directory where the Zookeeper data should be stored.

### Example Configuration Snippet
Here's a snippet of the `zoo.cfg` file relevant to a Zookeeper node:
```plaintext
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/home/youruser/zookeeper/zookeeper-01/data

clientPort=2181

server.1=zookeeper-01:2888:3888
server.2=zookeeper-02:2888:3888
server.3=zookeeper-03:2888:3888
```

## Customization Instructions
### IP Placeholder Customization
- Replace `zookeeper-01`, `zookeeper-02`, and `zookeeper-03` with the actual IP addresses or hostnames of your servers where these Zookeeper nodes are running.

### Data Directory Customization
- Replace `/home/youruser/zookeeper/zookeeper-01/data` with the actual directory path where you want Zookeeper to store its data files.

## Systemd Setup
Instructions for automating the startup of the Zookeeper service using systemd can be found in the `/systemd` folder of this project. Please refer to the relevant files there to create and manage Zookeeper as a system service.

## License
This configuration file is licensed under the Apache License, Version 2.0. You may not use this file except in compliance with the License. For more details, please see the [Apache License](http://www.apache.org/licenses/LICENSE-2.0).

## Troubleshooting
If you encounter issues with your configuration, please check the following:
- **Firewall Settings**: Ensure that port `2181` is open and accessible.
- **Hostname Resolution**: If you are using hostnames, make sure that they resolve correctly to the IP addresses of your servers.

Feel free to reach out if you have any questions or need further assistance with configuring your Zookeeper setup.
