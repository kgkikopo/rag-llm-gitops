# 7.2. Enabling route advertisements

To improve network reachability and failover visibility for your cluster, you can enable route advertisements for pod and egress IP addresses. This configuration requires the OVN-Kubernetes network plugin and allows your cluster to share routes with an external provider network. 

As a cluster administrator, you can configure additional route advertisements for your cluster. You must use the OVN-Kubernetes network plugin. 

## 7.2.1. Enabling route advertisements

To improve network reachability and failover visibility, you can enable additional routing support for your cluster. You can enable route advertisements to manage network traffic within your environment. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You are logged in to the cluster as a user with the `cluster-admin` role. 
  * The cluster is installed on compatible infrastructure. 



**Procedure**

  * To enable a routing provider and additional route advertisements, enter the following command: 

```shell-session
$ oc patch Network.operator.openshift.io cluster --type=merge \
  -p='{
    "spec": {
      "additionalRoutingCapabilities": {
        "providers": ["FRR"]
        },
        "defaultNetwork": {
          "ovnKubernetesConfig": {
            "routeAdvertisements": "Enabled"
    }}}}'
```
