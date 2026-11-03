# 20.4. Collect low latency tuning debugging data for Red Hat Support

To debug low latency setup issues when opening a support case, collect diagnostic information for Red Hat Support using the `must-gather` tool. This command gathers essential data, such as node tuning and NUMA topology, from your OpenShift Container Platform cluster. 

For prompt support, supply diagnostic information for both OpenShift Container Platform and low latency tuning. 

Use the `oc adm must-gather` CLI command to collect the following information about your cluster, including features and objects associated with low latency tuning: 

  * The Node Tuning Operator namespaces and child objects. 
  * `MachineConfigPool` and associated `MachineConfig` objects. 
  * The Node Tuning Operator and associated Tuned objects. 
  * Linux kernel command-line options. 
  * CPU and NUMA topology 
  * Basic PCI device information and NUMA locality. 



**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * The OpenShift Container Platform OpenShift CLI (`oc`) installed. 



**Procedure**

  1. Navigate to the directory where you want to store the `must-gather` data. 
  2. Collect debugging information by running the following command: 

```shell-session
$ oc adm must-gather
```


**Example output**

```shell-session
[must-gather      ] OUT Using must-gather plug-in image: quay.io/openshift-release
When opening a support case, bugzilla, or issue please include the following summary data along with any other requested information:
ClusterID: 829er0fa-1ad8-4e59-a46e-2644921b7eb6
ClusterVersion: Stable at "<cluster_version>"
ClusterOperators:
	All healthy and stable


[must-gather      ] OUT namespace/openshift-must-gather-8fh4x created
[must-gather      ] OUT clusterrolebinding.rbac.authorization.k8s.io/must-gather-rhlgc created
[must-gather-5564g] POD 2023-07-17T10:17:37.610340849Z Gathering data for ns/openshift-cluster-version...
[must-gather-5564g] POD 2023-07-17T10:17:38.786591298Z Gathering data for ns/default...
[must-gather-5564g] POD 2023-07-17T10:17:39.117418660Z Gathering data for ns/openshift...
[must-gather-5564g] POD 2023-07-17T10:17:39.447592859Z Gathering data for ns/kube-system...
[must-gather-5564g] POD 2023-07-17T10:17:39.803381143Z Gathering data for ns/openshift-etcd...

...

Reprinting Cluster State:
When opening a support case, bugzilla, or issue please include the following summary data along with any other requested information:
ClusterID: 829er0fa-1ad8-4e59-a46e-2644921b7eb6
ClusterVersion: Stable at "<cluster_version>"
ClusterOperators:
	All healthy and stable
```


  3. Create a compressed file from the `must-gather` directory that was created in your working directory. For example, on a computer that uses a Linux operating system, run the following command: 

```shell-session
$ tar cvaf must-gather.tar.gz must-gather-local.5421342344627712289//
```


     * `must-gather-local.5421342344627712289//`: Replace this value with the directory name created by the `must-gather` tool. 

Note

Create a compressed file to attach the data to a support case or to use with the Performance Profile Creator wrapper script when you create a performance profile. 

  4. Attach the compressed file to your support case on the [Red Hat Customer Portal](https://access.redhat.com/). 



**Additional resources**

  * [Gathering data about your cluster with the `must-gather` tool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#gathering-cluster-data)
  * [Managing nodes with MachineConfig and KubeletConfig CRs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-managing)
  * [Using the Node Tuning Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/using-node-tuning-operator "Chapter 10. Using the Node Tuning Operator")
  * [Configuring huge pages at boot time](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/what-huge-pages-do-and-how-they-are-consumed#configuring-huge-pages_huge-pages "15.4. Configure huge pages at boot time")
  * [How huge pages are consumed by apps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/what-huge-pages-do-and-how-they-are-consumed#how-huge-pages-are-consumed-by-apps_huge-pages "15.2. How huge pages are consumed by apps")
