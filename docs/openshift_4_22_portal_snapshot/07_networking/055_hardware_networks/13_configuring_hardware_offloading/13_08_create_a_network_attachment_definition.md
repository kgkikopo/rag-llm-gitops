# 13.8. Create a network attachment definition

After you define the machine config pool and the SR-IOV network node policy, you can create a network attachment definition for the network interface controller (NIC) you specified. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Create a file, such as `net-attach-def.yaml`, with content such as the following example: 

```yaml
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: <net_attach_def_name>
  namespace: <net_attach_def_namespace>
  annotations:
    k8s.v1.cni.cncf.io/resourceName: openshift.io/<resource_name>
spec:
  config: '{"cniVersion":"0.3.1","name":"ovn-kubernetes","type":"ovn-k8s-cni-overlay","ipam":{},"dns":{}}'
```


     * `<net_attach_def_name>` specifies the name for your network attachment definition. 
     * `<net_attach_def_namespace>` specifies the namespace for your network attachment definition. 
     * `<resource_name>` specifies the value of the `spec.resourceName` field from the `SriovNetworkNodePolicy` object. 

  2. Apply the configuration for the network attachment definition: 

```shell-session
$ oc create -f net-attach-def.yaml
```


**Verification**

  * Run the following command to check that the new definition exists: 

```shell-session
$ oc get net-attach-def -A
```


The output shows the namespace, name, and age of the new definition.
