# 7.2. Enabling OVS hardware offloading

For clusters that run on Red Hat OpenStack Platform (RHOSP), you can enable [Open vSwitch (OVS)](https://www.openvswitch.org/) hardware offloading. 

OVS is a multi-layer virtual switch that enables large-scale, multi-server network virtualization. 

**Prerequisites**

  * You installed a cluster on RHOSP that is configured for single-root input/output virtualization (SR-IOV). 
  * You installed the SR-IOV Network Operator on your cluster. 
  * You created two `hw-offload` type virtual function (VF) interfaces on your cluster. 



Note

Application layer gateway flows are broken in OpenShift Container Platform version 4.10, 4.11, and 4.12. Also, you cannot offload the application layer gateway flow for OpenShift Container Platform version 4.13. 

**Procedure**

  1. Create an `SriovNetworkNodePolicy` policy for the two `hw-offload` type VF interfaces that are on your cluster: 

**The first virtual function interface**

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: "hwoffload9"
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: true
  nicSelector:
    pfNames:
    - ens6
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 1
  priority: 99
  resourceName: "hwoffload9"
```


where: 

`kind`
     Specifies the `SriovNetworkNodePolicy` value. 
`spec.nicSelector.pfNames`
     Specifies the physical function (PF) name. Both interfaces must include PF names. 

**The second virtual function interface**

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: "hwoffload10"
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: true
  nicSelector:
    pfNames:
    - ens5
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 1
  priority: 99
  resourceName: "hwoffload10"
```


where: 

`kind`
     Specifies the `SriovNetworkNodePolicy` value. 
`spec.nicSelector.pfNames`
     Specifies the physical function (PF) name. Both interfaces must include PF names. 

  2. Create `NetworkAttachmentDefinition` resources for the two interfaces: 

**A`NetworkAttachmentDefinition` resource for the first interface**

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.v1.cni.cncf.io/resourceName: openshift.io/hwoffload9
  name: hwoffload9
  namespace: default
spec:
    config: '{ "cniVersion":"0.3.1", "name":"hwoffload9","type":"host-device","device":"ens6"
    }'
```


**A`NetworkAttachmentDefinition` resource for the second interface**

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.v1.cni.cncf.io/resourceName: openshift.io/hwoffload10
  name: hwoffload10
  namespace: default
spec:
    config: '{ "cniVersion":"0.3.1", "name":"hwoffload10","type":"host-device","device":"ens5"
    }'
```


  3. Use the interfaces that you created with a pod. For example: 

**A pod that uses the two OVS offload interfaces**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dpdk-testpmd
  namespace: default
  annotations:
    irq-load-balancing.crio.io: disable
    k8s.v1.cni.cncf.io/resourceName: openshift.io/hwoffload9
    k8s.v1.cni.cncf.io/resourceName: openshift.io/hwoffload10
spec:
  restartPolicy: Never
  containers:
  - name: dpdk-testpmd
    image: quay.io/krister/centos8_nfv-container-dpdk-testpmd:latest
```
