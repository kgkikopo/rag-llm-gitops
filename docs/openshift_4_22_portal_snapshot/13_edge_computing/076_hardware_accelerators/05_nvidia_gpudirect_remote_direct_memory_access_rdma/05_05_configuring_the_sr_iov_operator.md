# 5.5. Configuring the SR-IOV Operator

Single root I/O virtualization (SR-IOV) enhances the performance of NVIDIA GPUDirect RDMA by providing sharing across multiple pods from a single device. 

**Prerequisites**

  * You have installed the SR-IOV Operator. 



**Procedure**

  1. Validate that the Operator is installed and running by looking at the pods in the `openshift-sriov-network-operator` namespace by running the following command: 

```shell-session
$ oc get pods -n openshift-sriov-network-operator
```


**Example output**

```shell-session
NAME                                      READY   STATUS    RESTARTS   AGE
sriov-network-operator-7cb6c49868-89486   1/1     Running   0          22s
```


  2. For the default `SriovOperatorConfig` CR to work with the MLNX_OFED container, run this command to update the following values: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  enableInjector: true
  enableOperatorWebhook: true
  logLevel: 2
```


  3. Create the resource on the cluster by running the following command: 

```shell-session
$ oc create -f sriov-operator-config.yaml
```


**Example output**

```shell-session
sriovoperatorconfig.sriovnetwork.openshift.io/default created
```


  4. Patch the sriov-operator so the MOFED container can work with it by running the following command: 

```shell-session
$ oc patch sriovoperatorconfig default   --type=merge -n openshift-sriov-network-operator   --patch '{ "spec": { "configDaemonNodeSelector": { "network.nvidia.com/operator.mofed.wait": "false", "node-role.kubernetes.io/worker": "", "feature.node.kubernetes.io/pci-15b3.sriov.capable": "true" } } }'
```


**Example output**

```shell-session
sriovoperatorconfig.sriovnetwork.openshift.io/default patched
```
