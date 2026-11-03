# 10.3. Reduce API server load in large clusters

To reduce Kubernetes API server load and optimize resource consumption in large clusters, enable the `flowlogs-pipeline` shared cache. The shared cache is recommended for clusters with more than 3 `flowlogs-pipeline` replicas, especially when API server load becomes a performance concern. 

**Prerequisites**

  * The Network Observability Operator is installed. 
  * Access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Operators** **Installed Operators**. 
  2. Select the **Network Observability Operator** , and then click the **`FlowCollector`** tab. 
  3. Click the `cluster` instance, and then click the **YAML** tab. 
  4. In the `spec.processor` section, set the `informerCacheProxy` configuration to enable the shared cache by using the following example: 

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    informerCacheProxy:
      enabled: true
      replicas: 2
```


where: 

`spec.processor.informerCacheProxy.enabled`
     Set to `true` to enable the informer cache proxy. The default value is `false`. 
`spec.processor.informerCacheProxy.replicas`
     Specifies the number of replicas. For high availability in production environments, the minimum is `2`. The Operator enforces this requirement with leader election to prevent a single point of failure. 

  5. Click **Save**. 



**Verification**

  1. Navigate to **Workloads** **Pods**. 
  2. Ensure that the pods beginning with `flowlogs-pipeline-informers` are in the **Running** state. 
  3. Verify that one pod shows as the active leader by checking the pod logs for leader election messages. 
  4. Confirm that the `flowlogs-pipeline` pods remain **Running** and show decreased CPU and memory use in the **Metrics** tab.
