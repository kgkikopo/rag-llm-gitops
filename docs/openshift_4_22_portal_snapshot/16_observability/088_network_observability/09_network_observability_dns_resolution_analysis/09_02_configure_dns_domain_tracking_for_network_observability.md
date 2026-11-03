# 9.2. Configure DNS domain tracking for network observability

Enable DNS tracking in the Network Observability Operator to monitor DNS query names, response codes, and latency for network flows within the cluster. 

**Prerequisites**

  * The Network Observability Operator is installed. 
  * You have `cluster-admin` privileges. 
  * You are familiar with the `FlowCollector` custom resource. 



**Procedure**

  1. Edit the `FlowCollector` resource by running the following command: 

```shell-session
$ oc edit flowcollector cluster
```


  2. Configure the eBPF agent to enable the DNS tracking feature: 

```yaml
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollector
metadata:
  name: cluster
spec:
  agent:
    type: eBPF
    ebpf:
      features:
        - DNSTracking
```


where: 

`spec.agent.type.ebpf.features`
     Specifies the list of features to enable for the eBPF agent. To enable DNS tracking, add `DNSTracking` to this list. 

  3. Save and exit the editor. 



**Verification**

  1. In the OpenShift Container Platform web console, navigate to **Observe** **Network Traffic**. 
  2. In the **Traffic Flows** view, click the **Manage columns** icon. 
  3. Ensure that the **DNS Query Name** , **DNS Response Code** , and **DNS Latency** columns are selected. 
  4. Filter the results by setting **Port** to `53`. 
  5. Confirm that the flow table columns are populated with domain names and DNS metadata.
