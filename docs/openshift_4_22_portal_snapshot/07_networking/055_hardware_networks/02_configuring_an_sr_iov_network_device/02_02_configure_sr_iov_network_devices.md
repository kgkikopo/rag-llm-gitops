# 2.2. Configure SR-IOV network devices

The SR-IOV Network Operator adds the `SriovNetworkNodePolicy.sriovnetwork.openshift.io` custom resource definition (CRD) to OpenShift Container Platform. You can configure an SR-IOV network device by creating a `SriovNetworkNodePolicy` custom resource (CR). 

Note

When applying the configuration specified in a `SriovNetworkNodePolicy` CR, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. Reboot only happens in the following cases: 

  * With Mellanox NICs (`mlx5` driver) a node reboot happens every time the number of virtual functions (VFs) increase on a physical function (PF). 
  * With Intel NICs, a reboot only happens if the kernel parameters do not include `intel_iommu=on` and `iommu=pt`. 



It might take several minutes for a configuration change to apply. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the SR-IOV Network Operator. 
  * You have enough available nodes in your cluster to handle the evicted workload from drained nodes. 
  * You have not selected any control plane nodes for SR-IOV network device configuration. 



**Procedure**

  1. Create an `SriovNetworkNodePolicy` object, and then save the YAML in the `<name>-sriov-node-network.yaml` file. Replace `<name>` with the name for this configuration. 
  2. Optional: Label the SR-IOV capable cluster nodes with `SriovNetworkNodePolicy.Spec.NodeSelector` if they are not already labeled. For more information about labeling nodes, see "Understanding how to update labels on nodes". 
  3. Create the `SriovNetworkNodePolicy` object. When running the following command, replace `<name>` with the name for this configuration: 

```shell-session
$ oc create -f <name>-sriov-node-network.yaml
```


After applying the configuration update, all the pods in the `sriov-network-operator` namespace change to the `Running` status. 

  4. To verify your SR-IOV network device configuration, enter the following command and replace `<node_name>` with the name of the node where you configured the device. 

```shell-session
$ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name> -o jsonpath='{.status.syncStatus}'
```


**Additional resources**

  * [Understanding how to update labels on nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-working-updating_nodes-nodes-working)
