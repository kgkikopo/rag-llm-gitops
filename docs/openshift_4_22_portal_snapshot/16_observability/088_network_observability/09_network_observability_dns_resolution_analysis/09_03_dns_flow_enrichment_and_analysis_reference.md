# 9.3. DNS flow enrichment and analysis reference

Identify metadata added to network flows, leverage DNS data for network optimization, and understand the performance and storage impacts on the cluster. 

The following table describes the metadata fields added to network flows when DNS tracking is enabled. 

Note

Query names might be missing or truncated because of compression pointers or cache limitations. 

Table 9.1. DNS flow metadataField| Description| Example  
---|---|---  
`dns_query_name` |  The Fully Qualified Domain Name (FQDN) being queried.  |  `example.com`  
`dns_response_code` |  The status code returned by the DNS server.  |  `NoError`, `NXDomain`  
`dns_id` |  The transaction ID used to match queries with responses.  |  `45213`  
Show more

## 9.3.1. Leverage DNS data for network optimization

Use the captured DNS metadata for the following operational outcomes: 

  * Audit external dependencies: Ensure workloads are not reaching out to unauthorized external APIs or high-risk domains. 
  * Performance tuning: Monitor `DNS Latency` to identify if `CoreDNS` pods require additional scaling or if upstream DNS providers are lagging. 



## 9.3.2. Identify misconfiguration errors

A high frequency of `NXDOMAIN` responses typically indicates service discovery errors in application code or stale environment variables. 

`NXDOMAIN` errors can be frequent in Kubernetes because of DNS searches on services and pods. While these results do not necessarily indicate a misconfiguration or broken URL, they can negatively impact performance. 

When `NXDOMAIN` errors are returned despite an apparently valid Service or Pod host name, such as `my-svc.my-namespace.svc`, the resolver is likely configured to query DNS for different suffixes. You can optimize this by adding a trailing dot to fully qualified domain names to tell the resolver that the name is unambiguous. 

For example, instead of `<https://my-svc.my-namespace.svc>`, use `<https://my-svc.my-namespace.svc.cluster.local>.` with a trailing dot. 

## 9.3.3. Loki storage considerations

DNS tracking increases the number of labels and the amount of metadata per flow. Ensure that the Loki storage is sized to accommodate the increased log volume. 

**Additional resources**

  * [Network flows format reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-api-reference#network-flows-format_network_observability "19.1.4. Network flows format")
  * [Network Observability Operator runbooks](https://github.com/openshift/runbooks/tree/master/alerts/network-observability-operator)
