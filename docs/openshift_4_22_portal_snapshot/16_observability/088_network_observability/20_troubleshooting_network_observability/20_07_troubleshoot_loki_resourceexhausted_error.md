# 20.7. Troubleshoot Loki ResourceExhausted error

Resolve Loki `ResourceExhausted` errors by adjusting the `batchSize` in the `FlowCollector` resource or the maximum message size settings in your Loki configuration to ensure flow data stays within memory limits. 

Loki may return a `ResourceExhausted` error when network flow data sent by network observability exceeds the configured maximum message size. If you are using the Red Hat Loki Operator, this maximum message size is configured to 100 MiB. 

**Procedure**

  1. Navigate to **Ecosystem** **Installed Operators** , viewing **All projects** from the **Project** drop-down menu. 
  2. In the **Provided APIs** list, select the Network Observability Operator. 
  3. Click the **Flow Collector** then the **YAML view** tab. 

     1. If you are using the Loki Operator, check that the `spec.loki.batchSize` value does not exceed 98 MiB. 
     2. If you are using a Loki installation method that is different from the Red Hat Loki Operator, such as Grafana Loki, verify that the `grpc_server_max_recv_msg_size` [Grafana Loki server setting](https://grafana.com/docs/loki/latest/configure/#server) is higher than the `FlowCollector` resource `spec.loki.batchSize` value. If it is not, you must either increase the `grpc_server_max_recv_msg_size` value, or decrease the `spec.loki.batchSize` value so that it is lower than the limit. 

  4. Click **Save** if you edited the **FlowCollector**.
