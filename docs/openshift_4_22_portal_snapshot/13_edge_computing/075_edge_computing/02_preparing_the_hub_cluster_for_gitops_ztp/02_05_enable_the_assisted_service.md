# 2.5. Enable the assisted service

Red Hat Advanced Cluster Management (RHACM) uses the assisted service to deploy OpenShift Container Platform clusters. The assisted service is deployed automatically when you enable the MultiClusterHub Operator on RHACM. 

After enabling the MultiClusterHub Operator, configure the `Provisioning` resource to watch all namespaces and update the `AgentServiceConfig` CR with references to the ISO and RootFS images hosted on the mirror registry HTTP server. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have RHACM with `MultiClusterHub` enabled. 



**Procedure**

  1. Enable the `Provisioning` resource to watch all namespaces and configure mirrors for disconnected environments. For more information, see [Enabling the central infrastructure management service](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.9/html/clusters/cluster_mce_overview#enable-cim). 
  2. Open the `AgentServiceConfig` CR to update the `spec.osImages` field by running the following command: 

```shell-session
$ oc edit AgentServiceConfig
```


  3. Update the `spec.osImages` field in the `AgentServiceConfig` CR: 

```yaml
apiVersion: agent-install.openshift.io/v1beta1
kind: AgentServiceConfig
metadata:
 name: agent
spec:
# ...
  osImages:
    - cpuArchitecture: x86_64
      openshiftVersion: "4.22"
      rootFSUrl: https://<host>/<path>/rhcos-live-rootfs.x86_64.img
      url: https://<host>/<path>/rhcos-live.x86_64.iso
```


where: 

`<host>`
     Specifies the fully qualified domain name (FQDN) for the target mirror registry HTTP server. 
`<path>`
     Specifies the path to the image on the target mirror registry. 

  4. Save and quit the editor to apply the changes.
