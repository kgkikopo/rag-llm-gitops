# 15.3. View health information

View the **Netobserv/Health** dashboard within the OpenShift Container Platform web console to monitor the health status and resource usage of the Network Observability Operator and its components. 

**Prerequisites**

  * You have the Network Observability Operator installed. 
  * You have access to the cluster as a user with the `cluster-admin` role or with view permissions for all projects. 



**Procedure**

  1. From the **Administrator** perspective in the web console, navigate to **Observe** **Dashboards**. 
  2. From the **Dashboards** dropdown, select **Netobserv/Health**. 
  3. View the metrics about the health of the Operator that are displayed on the page. 



## 15.3.1. Disable health alerts

Disable specific health alerts, such as `NetObservLokiError` or `NetObservNoFlows`, by editing the `FlowCollector` resource and using the `spec.processor.metrics.disableAlerts` specification. 

**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Under the **Provided APIs** heading for the **NetObserv Operator** , select **Flow Collector**. 
  3. Select **cluster** then select the **YAML** tab. 
  4. Add `spec.processor.metrics.disableAlerts` to disable health alerts, as in the following YAML sample: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    metrics:
      disableAlerts: [NetObservLokiError, NetObservNoFlows]
```


where: 

`spec.processor.metrics.disableAlerts`
     Specifies one or more types of alerts to disable.
