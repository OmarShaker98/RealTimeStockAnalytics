The `kibana.yml` file is the primary configuration file for the Kibana server. This file allows you to customize settings for the server's operation, Elasticsearch connectivity, logging, security, and more.

For more configuration options, please see the Kibana configuration guide available at:
[Configuration Guide for Kibana](https://www.elastic.co/guide/index.html).

## Customizing the Elasticsearch Nodes

To configure which Elasticsearch nodes Kibana should connect to, use the following setting in the `kibana.yml` file:

```yaml
elasticsearch.hosts: ["http://elastic-node-01:9200", "http://elastic-node-02:9200"]
```

This setting specifies the URLs of the Elasticsearch instances that Kibana will use for its queries. You can add multiple nodes to increase redundancy and load balancing.

### Authentication Settings

If your Elasticsearch nodes are secured with basic authentication, you can provide the username and password in the configuration file:

```yaml
elasticsearch.username: "kibana_system"
elasticsearch.password: "your_password"
```

Alternatively, you can use service account tokens for authentication:

```yaml
elasticsearch.serviceAccountToken: "your_service_account_token"
```

## Customizing the Kibana Node

### Server Settings

- `server.port`: Specifies the port on which the Kibana server runs. The default port is `5601`.
- `server.host`: Specifies the hostname for the Kibana server. It is set to `kibana-node` in this configuration, allowing remote users to connect.
- `server.maxPayload`: Defines the maximum payload size for incoming requests to the Kibana server.

### SSL Configuration

To enable SSL for the Kibana server, you can set up the following parameters:

```yaml
server.ssl.enabled: true
server.ssl.certificate: /path/to/your/server.crt
server.ssl.key: /path/to/your/server.key
```

### Logging Configuration

The logging setup is configured to write logs to `/var/log/kibana/kibana.log` with a JSON layout:

```yaml
logging:
  appenders:
    file:
      type: file
      fileName: /var/log/kibana/kibana.log
      layout:
        type: json
```

## Saved Objects: Migrations

This section configures saved object migrations that run at startup. These settings are useful if you run into migration-related issues or performance problems during upgrades.

```yaml
migrations.batchSize: 1000
migrations.maxBatchSizeBytes: 100mb
migrations.retryAttempts: 15
```

## Additional Information

For detailed information about each configuration parameter and other advanced settings, refer to the official Kibana documentation:
[Kibana Documentation](https://www.elastic.co/guide/index.html).

## Contributing

If you have any suggestions or improvements for the configuration file, feel free to contribute by submitting a pull request.

## License

This project is licensed under the [Elastic License](https://www.elastic.co/licensing/elastic-license).
