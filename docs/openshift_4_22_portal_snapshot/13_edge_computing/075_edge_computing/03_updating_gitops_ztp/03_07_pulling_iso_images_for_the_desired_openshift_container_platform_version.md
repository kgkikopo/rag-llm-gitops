# 3.7. Pulling ISO images for the desired OpenShift Container Platform version

To pull ISO images for the desired OpenShift Container Platform version, update the `AgentServiceConfig` custom resource (CR) with references to the desired ISO and RootFS images that are hosted on the mirror registry HTTP server. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have RHACM with `MultiClusterHub` enabled. 
  * You have enabled the assisted service. 



**Procedure**

  1. Open the `AgentServiceConfig` CR to update the `spec.osImages` field by running the following command: 

```shell-session
$ oc edit AgentServiceConfig
```


  2. Update the `spec.osImages` field in the `AgentServiceConfig` CR: 

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

  3. Save and quit the editor to apply the changes. 



**Additional resources**

  * [Enabling the assisted service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-preparing-the-hub-cluster#enabling-assisted-installer-service-on-bare-metal_ztp-preparing-the-hub-cluster "2.5. Enable the assisted service")
