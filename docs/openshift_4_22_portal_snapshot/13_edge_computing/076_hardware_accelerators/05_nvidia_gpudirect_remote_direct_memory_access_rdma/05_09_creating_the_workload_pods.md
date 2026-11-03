# 5.9. Creating the workload pods

Use the procedures in this section to create the workload pods for the shared and host devices. 

## 5.9.1. Creating a shared device RDMA on RoCE

Create the workload pods for a shared device RDMA on RDMA over Converged Ethernet (RoCE) for the NVIDIA Network Operator and test the pod configuration. 

The NVIDIA GPUDirect RDMA device is shared among pods on the OpenShift Container Platform worker node where the device is exposed. 

**Prerequisites**

  * Ensure that the Operator is running. 
  * Delete the `NicClusterPolicy` custom resource (CR), if it exists. 



**Procedure**

  1. Generate custom pod resources: 

```yaml
$ cat <<EOF > rdma-eth-32-workload.yaml
apiVersion: v1
kind: Pod
metadata:
  name: rdma-eth-32-workload
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/networks: rdmashared-net
spec:
  nodeSelector:
    kubernetes.io/hostname: nvd-srv-32.nvidia.eng.rdu2.dc.redhat.com
  containers:
  - image: quay.io/edge-infrastructure/nvidia-tools:0.1.5
    name: rdma-eth-32-workload
    resources:
      limits:
        nvidia.com/gpu: 1
        rdma/rdma_shared_device_eth: 1
      requests:
        nvidia.com/gpu: 1
        rdma/rdma_shared_device_eth: 1

EOF

$ cat <<EOF > rdma-eth-33-workload.yaml
apiVersion: v1
kind: Pod
metadata:
  name: rdma-eth-33-workload
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/networks: rdmashared-net
spec:
  nodeSelector:
    kubernetes.io/hostname: nvd-srv-33.nvidia.eng.rdu2.dc.redhat.com
  containers:
  - image: quay.io/edge-infrastructure/nvidia-tools:0.1.5
    name: rdma-eth-33-workload
    securityContext:
      capabilities:
        add: [ "IPC_LOCK" ]
    resources:
      limits:
        nvidia.com/gpu: 1
        rdma/rdma_shared_device_eth: 1
      requests:
        nvidia.com/gpu: 1
        rdma/rdma_shared_device_eth: 1
EOF
```


  2. Create the pods on the cluster by using the following commands: 

```shell-session
$ oc create -f rdma-eth-32-workload.yaml
```


**Example output**

```shell-session
pod/rdma-eth-32-workload created
```


```shell-session
$ oc create -f rdma-eth-33-workload.yaml
```


**Example output**

```shell-session
pod/rdma-eth-33-workload created
```


  3. Verify that the pods are running by using the following command: 

```shell-session
$ oc get pods -n default
```


**Example output**

```shell-session
NAME                   READY   STATUS    RESTARTS   AGE
rdma-eth-32-workload   1/1     Running   0          25s
rdma-eth-33-workload   1/1     Running   0          22s
```


## 5.9.2. Creating a host device RDMA on RoCE

Create the workload pods for a host device Remote Direct Memory Access (RDMA) for the NVIDIA Network Operator and test the pod configuration. 

**Prerequisites**

  * Ensure that the Operator is running. 
  * Delete the `NicClusterPolicy` custom resource (CR), if it exists. 



**Procedure**

  1. Generate a new host device `NicClusterPolicy` (CR), as shown below: 

```yaml
$ cat <<EOF > network-hostdev-nic-cluster-policy.yaml
apiVersion: mellanox.com/v1alpha1
kind: NicClusterPolicy
metadata:
  name: nic-cluster-policy
spec:
  ofedDriver:
    image: doca-driver
    repository: nvcr.io/nvidia/mellanox
    version: 24.10-0.7.0.0-0
    startupProbe:
      initialDelaySeconds: 10
      periodSeconds: 20
    livenessProbe:
      initialDelaySeconds: 30
      periodSeconds: 30
    readinessProbe:
      initialDelaySeconds: 10
      periodSeconds: 30
    env:
    - name: UNLOAD_STORAGE_MODULES
      value: "true"
    - name: RESTORE_DRIVER_ON_POD_TERMINATION
      value: "true"
    - name: CREATE_IFNAMES_UDEV
      value: "true"
  sriovDevicePlugin:
      image: sriov-network-device-plugin
      repository: ghcr.io/k8snetworkplumbingwg
      version: v3.7.0
      config: |
        {
          "resourceList": [
              {
                  "resourcePrefix": "nvidia.com",
                  "resourceName": "hostdev",
                  "selectors": {
                      "vendors": ["15b3"],
                      "isRdma": true
                  }
              }
          ]
        }
EOF
```


  2. Create the `NicClusterPolicy` CR on the cluster by using the following command: 

```shell-session
$ oc create -f network-hostdev-nic-cluster-policy.yaml
```


**Example output**

```shell-session
nicclusterpolicy.mellanox.com/nic-cluster-policy created
```


  3. Verify that the host device `NicClusterPolicy` CR by using the following command in the DOCA/MOFED container: 

```shell-session
$ oc get pods -n nvidia-network-operator
```


**Example output**

```shell-session
NAME                                                          READY   STATUS    RESTARTS   AGE
mofed-rhcos4.16-696886fcb4-ds-9sgvd                           2/2     Running   0          2m37s
mofed-rhcos4.16-696886fcb4-ds-lkjd4                           2/2     Running   0          2m37s
nvidia-network-operator-controller-manager-68d547dbbd-qsdkf   1/1     Running   0          141m
sriov-device-plugin-6v2nz                                     1/1     Running   0          2m14s
sriov-device-plugin-hc4t8                                     1/1     Running   0          2m14s
```


  4. Confirm that the resources appear in the cluster `oc describe node` section by using the following command: 

```shell-session
$ oc describe node -l node-role.kubernetes.io/worker=| grep -E 'Capacity:|Allocatable:' -A7
```


**Example output**

```shell-session
Capacity:
  cpu:                 128
  ephemeral-storage:   1561525616Ki
  hugepages-1Gi:       0
  hugepages-2Mi:       0
  memory:              263596708Ki
  nvidia.com/hostdev:  2
  pods:                250
Allocatable:
  cpu:                 127500m
  ephemeral-storage:   1438028263499
  hugepages-1Gi:       0
  hugepages-2Mi:       0
  memory:              262445732Ki
  nvidia.com/hostdev:  2
  pods:                250
--
Capacity:
  cpu:                 128
  ephemeral-storage:   1561525616Ki
  hugepages-1Gi:       0
  hugepages-2Mi:       0
  memory:              263596704Ki
  nvidia.com/hostdev:  2
  pods:                250
Allocatable:
  cpu:                 127500m
  ephemeral-storage:   1438028263499
  hugepages-1Gi:       0
  hugepages-2Mi:       0
  memory:              262445728Ki
  nvidia.com/hostdev:  2
  pods:                250
```


  5. Create a `HostDeviceNetwork` CR file: 

```yaml
$ cat <<EOF >  hostdev-network.yaml
apiVersion: mellanox.com/v1alpha1
kind: HostDeviceNetwork
metadata:
  name: hostdev-net
spec:
  networkNamespace: "default"
  resourceName: "hostdev"
  ipam: |
    {
      "type": "whereabouts",
      "range": "192.168.3.225/28",
      "exclude": [
       "192.168.3.229/30",
       "192.168.3.236/32"
      ]
    }
EOF
```


  6. Create the `HostDeviceNetwork` resource on the cluster by using the following command: 

```shell-session
$ oc create -f hostdev-network.yaml
```


**Example output**

```shell-session
hostdevicenetwork.mellanox.com/hostdev-net created
```


  7. Confirm that the resources appear in the cluster `oc describe node` section by using the following command: 

```shell-session
$ oc describe node -l node-role.kubernetes.io/worker=| grep -E 'Capacity:|Allocatable:' -A8
```


**Example output**

```shell-session
Capacity:
  cpu:                 128
  ephemeral-storage:   1561525616Ki
  hugepages-1Gi:       0
  hugepages-2Mi:       0
  memory:              263596708Ki
  nvidia.com/gpu:      2
  nvidia.com/hostdev:  2
  pods:                250
Allocatable:
  cpu:                 127500m
  ephemeral-storage:   1438028263499
  hugepages-1Gi:       0
  hugepages-2Mi:       0
  memory:              262445732Ki
  nvidia.com/gpu:      2
  nvidia.com/hostdev:  2
  pods:                250
--
Capacity:
  cpu:                 128
  ephemeral-storage:   1561525616Ki
  hugepages-1Gi:       0
  hugepages-2Mi:       0
  memory:              263596680Ki
  nvidia.com/gpu:      2
  nvidia.com/hostdev:  2
  pods:                250
Allocatable:
  cpu:                 127500m
  ephemeral-storage:   1438028263499
  hugepages-1Gi:       0
  hugepages-2Mi:       0
  memory:              262445704Ki
  nvidia.com/gpu:      2
  nvidia.com/hostdev:  2
  pods:                250
```


## 5.9.3. Creating a SR-IOV legacy mode RDMA on RoCE

Configure a Single Root I/O Virtualization (SR-IOV) legacy mode host device RDMA on RoCE. 

**Procedure**

  1. Generate a new host device `NicClusterPolicy` custom resource (CR): 

```yaml
$ cat <<EOF > network-sriovleg-nic-cluster-policy.yaml
apiVersion: mellanox.com/v1alpha1
kind: NicClusterPolicy
metadata:
  name: nic-cluster-policy
spec:
  ofedDriver:
    image: doca-driver
    repository: nvcr.io/nvidia/mellanox
    version: 24.10-0.7.0.0-0
    startupProbe:
      initialDelaySeconds: 10
      periodSeconds: 20
    livenessProbe:
      initialDelaySeconds: 30
      periodSeconds: 30
    readinessProbe:
      initialDelaySeconds: 10
      periodSeconds: 30
    env:
    - name: UNLOAD_STORAGE_MODULES
      value: "true"
    - name: RESTORE_DRIVER_ON_POD_TERMINATION
      value: "true"
    - name: CREATE_IFNAMES_UDEV
      value: "true"
EOF
```


  2. Create the policy on the cluster by using the following command: 

```shell-session
$ oc create -f network-sriovleg-nic-cluster-policy.yaml
```


**Example output**

```shell-session
nicclusterpolicy.mellanox.com/nic-cluster-policy created
```


  3. Verify the pods by using the following command in the DOCA/MOFED container: 

```shell-session
$ oc get pods -n nvidia-network-operator
```


**Example output**

```shell-session
NAME                                                          READY   STATUS    RESTARTS      AGE
mofed-rhcos4.16-696886fcb4-ds-4mb42                           2/2     Running   0             40s
mofed-rhcos4.16-696886fcb4-ds-8knwq                           2/2     Running   0             40s
nvidia-network-operator-controller-manager-68d547dbbd-qsdkf   1/1     Running   13 (4d ago)   4d21h
```


  4. Create an `SriovNetworkNodePolicy` CR that generates the Virtual Functions (VFs) for the device you want to operate in SR-IOV legacy mode. See the following example: 

```yaml
$ cat <<EOF > sriov-network-node-policy.yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: sriov-legacy-policy
  namespace:  openshift-sriov-network-operator
spec:
  deviceType: netdevice
  mtu: 1500
  nicSelector:
    vendor: "15b3"
    pfNames: ["ens8f0np0#0-7"]
  nodeSelector:
    feature.node.kubernetes.io/pci-15b3.present: "true"
  numVfs: 8
  priority: 90
  isRdma: true
  resourceName: sriovlegacy
EOF
```


  5. Create the CR on the cluster by using the following command: 

Note

Ensure that SR-IOV Global Enable is enabled. For more information, see [Unable to enable SR-IOV and receiving the message "not enough MMIO resources for SR-IOV" in Red Hat Enterprise Linux](https://access.redhat.com/solutions/37376). 

```shell-session
$ oc create -f sriov-network-node-policy.yaml
```


**Example output**

```shell-session
sriovnetworknodepolicy.sriovnetwork.openshift.io/sriov-legacy-policy created
```


  6. Each node has scheduling disabled. The nodes reboot to apply the configuration. You can view the nodes by using the following command: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME                                       STATUS                        ROLES                         AGE     VERSION
edge-19.edge.lab.eng.rdu2.redhat.com       Ready                         control-plane,master,worker   5d      v1.29.8+632b078
nvd-srv-32.nvidia.eng.rdu2.dc.redhat.com   Ready                         worker                        4d22h   v1.29.8+632b078
nvd-srv-33.nvidia.eng.rdu2.dc.redhat.com   NotReady,SchedulingDisabled   worker                        4d22h   v1.29.8+632b078
```


  7. After the nodes have rebooted, verify that the VF interfaces exist by opening up a debug pod on each node. Run the following command: 

```shell-session
a$ oc debug node/nvd-srv-33.nvidia.eng.rdu2.dc.redhat.com
```


**Example output**

```shell-session
Starting pod/nvd-srv-33nvidiaengrdu2dcredhatcom-debug-cqfjz ...
To use host binaries, run `chroot /host`
Pod IP: 10.6.135.12
If you don't see a command prompt, try pressing enter.
sh-5.1# chroot /host
sh-5.1# ip link show | grep ens8
26: ens8f0np0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
42: ens8f0v0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
43: ens8f0v1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
44: ens8f0v2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
45: ens8f0v3: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
46: ens8f0v4: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
47: ens8f0v5: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
48: ens8f0v6: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
49: ens8f0v7: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
```


  8. Repeat the previous steps on the second node, if necessary. 
  9. Optional: Confirm that the resources appear in the cluster `oc describe node` section by using the following command: 

```shell-session
$ oc describe node -l node-role.kubernetes.io/worker=| grep -E 'Capacity:|Allocatable:' -A8
```


**Example output**

```shell-session
Capacity:
  cpu:                       128
  ephemeral-storage:         1561525616Ki
  hugepages-1Gi:             0
  hugepages-2Mi:             0
  memory:                    263596692Ki
  nvidia.com/gpu:            2
  nvidia.com/hostdev:        0
  openshift.io/sriovlegacy:  8
--
Allocatable:
  cpu:                       127500m
  ephemeral-storage:         1438028263499
  hugepages-1Gi:             0
  hugepages-2Mi:             0
  memory:                    262445716Ki
  nvidia.com/gpu:            2
  nvidia.com/hostdev:        0
  openshift.io/sriovlegacy:  8
--
Capacity:
  cpu:                       128
  ephemeral-storage:         1561525616Ki
  hugepages-1Gi:             0
  hugepages-2Mi:             0
  memory:                    263596688Ki
  nvidia.com/gpu:            2
  nvidia.com/hostdev:        0
  openshift.io/sriovlegacy:  8
--
Allocatable:
  cpu:                       127500m
  ephemeral-storage:         1438028263499
  hugepages-1Gi:             0
  hugepages-2Mi:             0
  memory:                    262445712Ki
  nvidia.com/gpu:            2
  nvidia.com/hostdev:        0
  openshift.io/sriovlegacy:  8
```


  10. After the VFs for SR-IOV legacy mode are in place, generate the `SriovNetwork` CR file. See the following example: 

```yaml
$ cat <<EOF > sriov-network.yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: sriov-network
  namespace:  openshift-sriov-network-operator
spec:
  vlan: 0
  networkNamespace: "default"
  resourceName: "sriovlegacy"
  ipam: |
    {
      "type": "whereabouts",
      "range": "192.168.3.225/28",
      "exclude": [
       "192.168.3.229/30",
       "192.168.3.236/32"
      ]
    }
EOF
```


  11. Create the custom resource on the cluster by using the following command: 

```shell-session
$ oc create -f sriov-network.yaml
```


**Example output**

```shell-session
sriovnetwork.sriovnetwork.openshift.io/sriov-network created
```


## 5.9.4. Creating a shared device RDMA on Infiniband

Create the workload pods for a shared device Remote Direct Memory Access (RDMA) for an Infiniband installation. 

**Procedure**

  1. Generate custom pod resources: 

```yaml
$ cat <<EOF > rdma-ib-32-workload.yaml
apiVersion: v1
kind: Pod
metadata:
  name: rdma-ib-32-workload
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/networks: example-ipoibnetwork
spec:
  nodeSelector:
    kubernetes.io/hostname: nvd-srv-32.nvidia.eng.rdu2.dc.redhat.com
  containers:
  - image: quay.io/edge-infrastructure/nvidia-tools:0.1.5
    name: rdma-ib-32-workload
    resources:
      limits:
        nvidia.com/gpu: 1
        rdma/rdma_shared_device_ib: 1
      requests:
        nvidia.com/gpu: 1
        rdma/rdma_shared_device_ib: 1
EOF

$ cat <<EOF > rdma-ib-32-workload.yaml
apiVersion: v1
kind: Pod
metadata:
  name: rdma-ib-33-workload
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/networks: example-ipoibnetwork
spec:
  nodeSelector:
    kubernetes.io/hostname: nvd-srv-33.nvidia.eng.rdu2.dc.redhat.com
  containers:
  - image: quay.io/edge-infrastructure/nvidia-tools:0.1.5
    name: rdma-ib-33-workload
    securityContext:
      capabilities:
        add: [ "IPC_LOCK" ]
    resources:
      limits:
        nvidia.com/gpu: 1
        rdma/rdma_shared_device_ib: 1
      requests:
        nvidia.com/gpu: 1
        rdma/rdma_shared_device_ib: 1
EOF
```


  2. Create the pods on the cluster by using the following commands: 

```shell-session
$ oc create -f rdma-ib-32-workload.yaml
```


**Example output**

```shell-session
pod/rdma-ib-32-workload created
```


```shell-session
$ oc create -f rdma-ib-33-workload.yaml
```


**Example output**

```shell-session
pod/rdma-ib-33-workload created
```


  3. Verify that the pods are running by using the following command: 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME                  READY   STATUS    RESTARTS   AGE
rdma-ib-32-workload   1/1     Running   0          10s
rdma-ib-33-workload   1/1     Running   0          3s
```
