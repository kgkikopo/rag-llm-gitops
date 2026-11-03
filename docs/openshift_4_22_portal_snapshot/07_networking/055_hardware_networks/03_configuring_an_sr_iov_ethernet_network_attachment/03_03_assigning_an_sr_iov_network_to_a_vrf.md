# 3.3. Assigning an SR-IOV network to a VRF

As a cluster administrator, you can assign an SR-IOV network interface to your VRF domain by using the CNI VRF plugin. 

To do this, add the VRF configuration to the optional `metaPlugins` parameter of the `SriovNetwork` resource. 

Note

Applications that use VRF instances need to bind to a specific device. The common usage is to use the `SO_BINDTODEVICE` option for a socket. `SO_BINDTODEVICE` binds the socket to a device that is specified in the passed interface name, for example, `eth1`. To use `SO_BINDTODEVICE`, the application must have `CAP_NET_RAW` capabilities. 

Using a VRF through the `ip vrf exec` command is not supported in OpenShift Container Platform pods. To use VRF, bind applications directly to the VRF interface. 

## 3.3.1. Creating an additional SR-IOV network attachment with the CNI VRF plugin

The SR-IOV Network Operator manages additional network definitions. When you specify an additional SR-IOV network to create, the SR-IOV Network Operator creates the `NetworkAttachmentDefinition` custom resource (CR) automatically. 

Note

Do not edit `NetworkAttachmentDefinition` custom resources that the SR-IOV Network Operator manages. Doing so might disrupt network traffic on your additional network. 

To create an additional SR-IOV network attachment with the CNI virtual routing and forwarding (VRF) plugin, perform the following procedure. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges. 



**Procedure**

  1. Create the `SriovNetwork` custom resource (CR) for the additional SR-IOV network attachment and insert the `metaPlugins` configuration, as in the following example CR. Save the YAML as the file `sriov-network-attachment.yaml`. 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: example-network
  namespace: additional-sriov-network-1
spec:
  ipam: |
    {
      "type": "host-local",
      "subnet": "10.56.217.0/24",
      "rangeStart": "10.56.217.171",
      "rangeEnd": "10.56.217.181",
      "routes": [{
        "dst": "0.0.0.0/0"
      }],
      "gateway": "10.56.217.1"
    }
  vlan: 0
  resourceName: intelnics
  metaPlugins : |
    {
      "type": "vrf", 
```


1

```yaml
      "vrfname": "example-vrf-name"
    }
```


where: 

`metaPlugins.type`
     Set the `type` parameter to `vrf`. 
`metaPlugins.vrfname`
     Specify a name for the VRF in the `vrfname` parameter. An interface gets assigned to the VRF. If you do not specify a name for the VRF in a pod, the SR-IOV Network Operator automatically generates a name for the VRF. 

  2. Create the `SriovNetwork` resource: 

```shell-session
$ oc create -f sriov-network-attachment.yaml
```


**Verification**

  1. Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command. The expected output shows the name of the NAD CR and the creation age in minutes. 

```shell-session
$ oc get network-attachment-definitions -n <namespace>
```


     * `<namespace>`: Replace `<namespace>` with the namespace that you specified when configuring the network attachment, for example, `additional-sriov-network-1`. 

Note

There might be a delay before the SR-IOV Network Operator creates the CR. 

  2. To verify that the VRF CNI is correctly configured and that the additional SR-IOV network attachment is attached, do the following: 

     1. Create an SR-IOV network that uses the VRF CNI. 
     2. Assign the network to a pod. 
     3. Verify that the pod network attachment connects to the SR-IOV additional network. Ensure that you remote shell login into the pod and run the following command. The expected output shows the name of the VRF interface and its unique ID in the routing table. 

```shell-session
$ ip vrf show
```


     4. Confirm that the VRF interface is `master` for the secondary interface by running the following command. Example output shows `5: net1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master red state UP mode`. 

```shell-session
$ ip link
```
