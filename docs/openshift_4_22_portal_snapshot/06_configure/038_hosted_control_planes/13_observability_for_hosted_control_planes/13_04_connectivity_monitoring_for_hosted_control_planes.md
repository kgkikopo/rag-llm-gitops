# 13.4. Connectivity monitoring for hosted control planes

Cluster service providers can monitor connectivity metrics to ensure proper function during an update. They can also use the metrics to find connectivity issues between the control plane and the data plane, or vice versa. 

Studying these metrics over time can inform decisions about capacity planning and scaling. 

## 13.4.1. Connectivity monitoring from the control plane to the data plane

Cluster administrators can monitor network activity between a hosted control plane and the compute nodes in a data plane by using the `DataPlaneConnectionAvailable` condition. This condition is useful for identifying and troubleshooting network connectivity issues in hosted clusters. 

The `DataPlaneConnectionAvailable` condition is available by default starting with version 4.21. 

The `DataPlaneConnectionAvailable` condition monitors the connectivity from the control plane to the data plane by taking the following steps: 

  1. Counts available compute nodes in the hosted cluster. 
  2. Lists the `konnectivity-agent` pods that are running in the `kube-system` namespace on the data plane. 
  3. Reads the logs from the running `konnectivity-agent` pod to verify that it can communicate with the data plane. 



The `hosted-cluster-config-operator` component that runs in the control plane namespace evaluates the condition and provides status and reason information. 

The following table details the status and reason values that can be displayed for the condition: 

Status| Reason value| Description  
---|---|---  
`True` |  `AsExpected` |  The control plane can reach the data plane nodes through the `konnectivity-agent` pods.   
`False` |  `KonnectivityAgentPodsNotFound` |  No `konnectivity-agent` pods are running, or none are found.   
`False` |  `ReconciliationError` |  An error occurred while listing the `konnectivity-agent` pods.   
`Unknown` |  `NoWorkerNodesAvailable` |  No compute nodes are available in the cluster. No errors occurred, but no compute nodes were found.   
`Unknown` |  `ReconcileError` |  Unable to count compute nodes because an error occurred.   
Show more

For information about how to troubleshoot connectivity issues, see "Troubleshooting connectivity for hosted control planes". 

**Additional resources**

  * [Troubleshooting connectivity for hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-troubleshooting#hcp-ts-connectivity_hcp-troubleshooting "15.10. Troubleshooting connectivity for hosted control planes")



## 13.4.2. Connectivity monitoring from the data plane to the control plane

Cluster administrators can monitor network activity between the compute nodes in a data plane and a hosted control plane by using the `ControlPlaneConnectionAvailable` condition. This condition is useful for identifying and troubleshooting network connectivity issues in hosted clusters. 

The `ControlPlaneConnectionAvailable` condition detects whether data plane nodes can reach control plane components. The `hosted-cluster-config-operator` component evaluates the condition, and a deployment with 3 replicas checks connectivity. 

The condition monitors the connectivity between the data plane and the control plane by taking the following steps: 

  1. Deploys a `kas-connection-checker` deployment to the `kube-system` namespace on the data plane. 
  2. Each pod runs a shell script in an infinite loop that transfers data to and from the Kubernetes API server endpoint every 60 seconds. On success, the script patches the `control-plane-connectivity-check` config map with a `lastSucceeded` timestamp. 
  3. The `hosted-cluster-config-operator` component checks whether the `control-plane-connectivity-check` config map exists and whether the `lastSucceeded` timestamp is within the last 5 minutes. It does not check pod readiness counts. 



The following table details the status and reason values that can be displayed for the condition: 

Status| Reason value| Description  
---|---|---  
`True` |  `AsExpected` |  All data plane nodes can reach the control plane (`NumberReady = DesiredNumberScheduled`).   
`False` |  `KASAccessFailed` |  At least one data plane node cannot reach the control plane. The message shows the ratio of pods that are ready; for example, `1/3 pods ready`.   
`Unknown` |  `NoWorkerNodesAvailable` |  No compute nodes are available to check connectivity (`DesiredNumberScheduled = 0`).   
`Unknown` |  `StatusUnknown` |  The Kubernetes API server connection checker DaemonSet was not found.   
`Unknown` |  `ReconcileError` |  An API error blocked the retrieval of the DaemonSet status.   
Show more

Important

This condition has a known limitation with HTTPS proxy environments. In HTTPS proxy environments, the condition might incorrectly report `False` because of probe limitations.
