# 3.5. Add a pod to a secondary network

To enable a pod to use additional network interfaces in OpenShift Container Platform, you can attach the pod to a secondary network. The pod continues to send normal cluster-related network traffic over the default network. 

When a pod is created, a secondary network is attached to the pod. However, if a pod already exists, you cannot attach a secondary network to it. 

The pod must be in the same namespace as the secondary network. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in to the cluster. 



**Procedure**

  1. Add an annotation to the `Pod` object. Only one of the following annotation formats can be used: 

     1. To attach a secondary network without any customization, add an annotation with the following format: 

```yaml
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: <network>[,<network>,...]
```


where: 

`k8s.v1.cni.cncf.io/networks`
     Specifies the name of the secondary network to associate with the pod. To specify more than one secondary network, separate each network with a comma. Do not include whitespace between the comma. If you specify the same secondary network multiple times, that pod will have multiple network interfaces attached to that network. 

     2. To attach a secondary network with customizations, add an annotation with the following format: 

```yaml
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "<network>",
          "namespace": "<namespace>",
          "default-route": ["<default_route>"]
        }
      ]
```


where: 

`<network>`
     Specifies the name of the secondary network defined by a `NetworkAttachmentDefinition` object. 
`<namespace>`
     Specifies the namespace where the `NetworkAttachmentDefinition` object is defined. 
`<default-route>`
     Optional parameter. Specifies an override for the default route, such as `192.168.17.1`. 

  2. Create the pod by entering the following command. 

```shell-session
$ oc create -f <name>.yaml
```


Replace `<name>` with the name of the pod. 

  3. Optional: Confirm that the annotation exists in the `pod` CR by entering the following command. Replace `<name>` with the name of the pod. 

```shell-session
$ oc get pod <name> -o yaml
```


In the following example, the `example-pod` pod is attached to the `net1` secondary network: 

```shell-session
$ oc get pod example-pod -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: macvlan-bridge
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "ovn-kubernetes",
          "interface": "eth0",
          "ips": [
              "10.128.2.14"
          ],
          "default": true,
          "dns": {}
      },{
          "name": "macvlan-bridge",
          "interface": "net1",
          "ips": [
              "20.2.2.100"
          ],
          "mac": "22:2f:60:a5:f8:00",
          "dns": {}
      }]
  name: example-pod
  namespace: default
spec:
  ...
status:
  ...
```


where: 

`k8s.v1.cni.cncf.io/network-status`
     Specifies a JSON array of objects. Each object describes the status of a secondary network attached to the pod. The annotation value is stored as a plain text value. 




## 3.5.1. Expose MTU for vfio-pci SR-IOV devices to pod

After adding a pod to an additional network, you can check that the MTU is available for the SR-IOV network. 

**Procedure**

  1. Check that the pod annotation includes MTU by running the following command: 

```shell-session
$ oc describe pod example-pod
```


The following example shows the sample output: 

```plaintext
"mac": "20:04:0f:f1:88:01",
       "mtu": 1500,
       "dns": {},
       "device-info": {
         "type": "pci",
         "version": "1.1.0",
         "pci": {
           "pci-address": "0000:86:01.3"
    }
  }
```


  2. Verify that the MTU is available in `/etc/podnetinfo/` inside the pod by running the following command: 

```shell-session
$ oc exec example-pod -n sriov-tests -- cat /etc/podnetinfo/annotations | grep mtu
```


The following example shows the sample output: 

```plaintext
k8s.v1.cni.cncf.io/network-status="[{
    \"name\": \"ovn-kubernetes\",
    \"interface\": \"eth0\",
    \"ips\": [
        \"10.131.0.67\"
    ],
    \"mac\": \"0a:58:0a:83:00:43\",
    \"default\": true,
    \"dns\": {}
    },{
    \"name\": \"sriov-tests/sriov-nic-1\",
    \"interface\": \"net1\",
    \"ips\": [
        \"192.168.10.1\"
    ],
    \"mac\": \"20:04:0f:f1:88:01\",
    \"mtu\": 1500,
    \"dns\": {},
    \"device-info\": {
        \"type\": \"pci\",
        \"version\": \"1.1.0\",
        \"pci\": {
            \"pci-address\": \"0000:86:01.3\"
        }
    }
    }]"
```


## 3.5.2. Change the MTU value of a virtual function for a running pod

You can change the maximum transmission unit (MTU) of a virtual function (VF) for a running pod by omitting the `mtu` field from the `SriovNetworkNodePolicy` custom resource (CR) and configuring the physical function (PF) MTU by using the Kubernetes NMState Operator. 

When the `mtu` field is set in the `SriovNetworkNodePolicy` CR, the SR-IOV Network Operator continuously enforces that MTU value on the VF. This reverts any application-level MTU changes and can trigger a node drain. To avoid this conflict, use the following approach: 

  * Omit the `mtu` field from the `SriovNetworkNodePolicy` CR. This allows the SR-IOV Network Operator to provision VFs without managing their MTU. 
  * Use the Kubernetes NMState Operator to set the MTU of the PF to the required value. A VF cannot have a higher MTU than its parent PF, so you must set the PF MTU first. 



With these configurations in place, a pod that has the `NET_ADMIN` Linux capability can safely set its own VF MTU without interference from the SR-IOV Network Operator. 

Important

If you already configured a value for the `mtu` field in your `SriovNetworkNodePolicy` CR, removing it might trigger a node drain. Perform this change during a scheduled maintenance window. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You logged in as a user with `cluster-admin` privileges. 
  * You installed the SR-IOV Network Operator. 
  * You installed the Kubernetes NMState Operator. 



**Procedure**

  1. Verify that the `mtu` field is not present in your `SriovNetworkNodePolicy` CR by running the following command: 

```shell-session
$ oc get sriovnetworknodepolicy <policy_name> -n openshift-sriov-network-operator -o jsonpath='{.spec.mtu}'
```


where: 

`<policy_name>`
    

Specifies the name of the `SriovNetworkNodePolicy` CR. 

If the command returns a value, remove the `mtu` field from the CR by running the following command: 

```shell-session
$ oc patch sriovnetworknodepolicy <policy_name> -n openshift-sriov-network-operator \
  --type=json -p='[{"op": "remove", "path": "/spec/mtu"}]'
```


The SR-IOV Network Operator reconciles and creates the VFs with the default MTU of 1500. 

  2. Verify that the VFs are created with the default MTU by running the following commands: 

```shell-session
$ oc debug node/<node_name>
```


```shell-session
# chroot /host
# ip link show <vf_interface>
```


where: 

`<node_name>`
     Specifies the name of the node where the PF is located. 
`<vf_interface>`
    

Specifies the VF interface name, for example `ens3f0v0`. 

**Example output**

```plaintext
4: ens3f0v0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether aa:bb:cc:dd:ee:01 brd ff:ff:ff:ff:ff:ff
```


  3. Create a `NodeNetworkConfigurationPolicy` CR to set the MTU of the PF: 

     1. Create a file named `nncp-set-pf-mtu.yaml` with the following content: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: set-pf-mtu
spec:
  nodeSelector:
    kubernetes.io/hostname: <node_name>
  desiredState:
    interfaces:
      - name: <pf_interface>
        type: ethernet
        state: up
        mtu: <mtu_value>
```


where: 

`<node_name>`
     Specifies the name of the node where the PF is located. 
`<pf_interface>`
     Specifies the name of the PF interface, for example `ens3f0`. 
`<mtu_value>`
     Specifies the required MTU value for the PF, for example `9000`. This value must be greater than or equal to the MTU that the application sets on the VF. 

     2. Apply the CR by running the following command: 

```shell-session
$ oc apply -f nncp-set-pf-mtu.yaml
```


  4. Verify that the NMState policy has been applied successfully by running the following command: 

```shell-session
$ oc get nodenetworkconfigurationpolicy set-pf-mtu
```


**Example output**

```plaintext
NAME          STATUS      REASON
set-pf-mtu    Available   SuccessfullyConfigured
```


Wait until the `STATUS` column shows `Available` before proceeding. 

  5. Verify that the PF MTU has been updated on the node by running the following commands: 

```shell-session
$ oc debug node/<node_name>
```


```shell-session
# chroot /host
# ip link show <pf_interface>
```


where: 

`<node_name>`
     Specifies the name of the node where the PF is located. 
`<pf_interface>`
    

Specifies the name of the PF interface, for example `ens3f0`. 

**Example output**

```plaintext
2: ens3f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether aa:bb:cc:dd:ee:ff brd ff:ff:ff:ff:ff:ff
```


The VFs retain their default MTU of 1500 at this stage. 

  6. Deploy or update the application pod to set the VF MTU at container startup: 

     1. Create or update the pod spec with a startup command that sets the VF MTU before the application starts: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: <pod_name>
  namespace: <namespace>
  annotations:
    k8s.v1.cni.cncf.io/networks: <sriov_network_name>
spec:
  containers:
    - name: <container_name>
      image: <image>
      command: ["/bin/sh"]
      args:
        - "-c"
        - "ip link set mtu <mtu_value> dev <vf_interface>; <application_command>"
      securityContext:
        capabilities:
          add: ["NET_ADMIN"]
      resources:
        requests:
          <sriov_resource_name>: "1"
        limits:
          <sriov_resource_name>: "1"
```


where: 

`command` and `args`
     Sets the VF MTU to the specified value before running the application command. 
`NET_ADMIN`
     The `NET_ADMIN` Linux capability is required for the container to change network interface settings. 
`<pod_name>`
     Specifies the name of the pod. 
`<namespace>`
     Specifies the namespace where the pod runs. 
`<sriov_network_name>`
     Specifies the name of the `SriovNetwork` CR that provides the VF to the pod. 
`<container_name>`
     Specifies the name of the container. 
`<image>`
     Specifies the container image to use. 
`<mtu_value>`
     Specifies the required MTU value, for example `9000`. 
`<vf_interface>`
     Specifies the VF interface name as it is displayed inside the pod, typically `net1`. 
`<application_command>`
     Specifies the main application command to run after the MTU is set. 
`<sriov_resource_name>`
     Specifies the SR-IOV resource name defined in the `spec.resourceName` field of the `SriovNetworkNodePolicy` CR. 

     2. Apply the pod spec by running the following command: 

```shell-session
$ oc apply -f <pod_spec_file>.yaml
```


where: 

`<pod_spec_file>`
     Specifies the name of the file containing the pod specification. 




**Verification**

  1. Verify that the VF MTU inside the pod has been set to the expected value by running the following command: 

```shell-session
$ oc exec <pod_name> -n <namespace> -- ip link show <vf_interface>
```


where: 

`<pod_name>`
     Specifies the name of the pod. 
`<namespace>`
     Specifies the namespace where the pod is running. 
`<vf_interface>`
    

Specifies the VF interface name inside the pod, for example `net1`. 

**Example output**

```plaintext
3: net1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 00:00:5E:00:53:01 brd ff:ff:ff:ff:ff:ff
```


The example output confirms that the VF MTU matches the value set by the pod startup command. The SR-IOV Network Operator preserves this value because the `SriovNetworkNodePolicy` CR delegates MTU management to the pod.
