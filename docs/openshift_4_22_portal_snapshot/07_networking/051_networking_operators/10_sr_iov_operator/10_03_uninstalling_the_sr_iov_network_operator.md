# 10.3. Uninstalling the SR-IOV Network Operator

To uninstall the SR-IOV Network Operator, you must delete any running SR-IOV workloads, uninstall the Operator, and delete the webhooks that the Operator used. 

## 10.3.1. Uninstall the SR-IOV Network Operator

You can remove the SR-IOV Network Operator from your cluster by uninstalling the Operator. This ensures that the Operator and its associated resources are deleted when you no longer need to manage SR-IOV network devices. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 
  * You have the SR-IOV Network Operator installed. 



**Procedure**

  1. Delete all SR-IOV custom resources (CRs): 

```shell-session
$ oc delete sriovnetwork -n openshift-sriov-network-operator --all
```


```shell-session
$ oc delete sriovnetworknodepolicy -n openshift-sriov-network-operator --all
```


```shell-session
$ oc delete sriovibnetwork -n openshift-sriov-network-operator --all
```


```shell-session
$ oc delete sriovoperatorconfigs -n openshift-sriov-network-operator --all
```


  2. Follow the instructions in the "Deleting Operators from a cluster" section to remove the SR-IOV Network Operator from your cluster. 
  3. Delete the SR-IOV custom resource definitions that remain in the cluster after the SR-IOV Network Operator is uninstalled: 

```shell-session
$ oc delete crd sriovibnetworks.sriovnetwork.openshift.io
```


```shell-session
$ oc delete crd sriovnetworknodepolicies.sriovnetwork.openshift.io
```


```shell-session
$ oc delete crd sriovnetworknodestates.sriovnetwork.openshift.io
```


```shell-session
$ oc delete crd sriovnetworkpoolconfigs.sriovnetwork.openshift.io
```


```shell-session
$ oc delete crd sriovnetworks.sriovnetwork.openshift.io
```


```shell-session
$ oc delete crd sriovoperatorconfigs.sriovnetwork.openshift.io
```


  4. Delete the SR-IOV Network Operator namespace: 

```shell-session
$ oc delete namespace openshift-sriov-network-operator
```


## 10.3.2. Additional resources

  * [Deleting Operators from a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-deleting-operators-from-a-cluster)
