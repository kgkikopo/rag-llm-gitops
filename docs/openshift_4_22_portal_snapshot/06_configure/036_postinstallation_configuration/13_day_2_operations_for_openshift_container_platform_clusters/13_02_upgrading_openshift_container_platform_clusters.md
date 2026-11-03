# 13.2. Upgrading OpenShift Container Platform clusters

## 13.2.1. Upgrading an OpenShift Container Platform cluster

OpenShift Container Platform has long term support or extended update support (EUS) on all even releases and update paths between EUS releases. You can update from one EUS version to the next EUS version. It is also possible to update between y-stream and z-stream versions. 

### 13.2.1.1. Cluster updates for OpenShift clusters

Updating your cluster is a critical task that ensures that bugs and potential security vulnerabilities are patched. 

Often, updates to cloud-native applications require additional functionality from the platform that comes when you update the cluster version. You also must update the cluster periodically to ensure that the cluster platform version is supported. 

You can minimize the effort required to stay current with updates by keeping up-to-date with EUS releases and upgrading to select important z-stream releases only. 

Note

The update path for the cluster can vary depending on the size and topology of the cluster. 

The following update scenarios are described: 

  * Control Plane Only updates 
  * Y-stream updates 
  * Z-stream updates 



Important

Control Plane Only updates were previously known as EUS-to-EUS updates. Control Plane Only updates are only viable between even-numbered minor versions of OpenShift Container Platform. 

## 13.2.2. Verifying cluster API versions between update versions

APIs change over time as components are updated. It is important to verify that your application APIs are compatible with the updated cluster version. 

### 13.2.2.1. OpenShift Container Platform API compatibility

When considering what z-stream release to update to as part of a new y-stream update, you must be sure that all the patches that are in the z-stream version you are moving from are in the new z-stream version. 

If the version you update to does not have all the required patches, the built-in compatibility of Kubernetes is broken. 

For example, if the cluster version is 4.15.32, you must update to 4.16 z-stream release that has all of the patches that are applied to 4.15.32. 

Each cluster Operator supports specific API versions. Kubernetes APIs evolve over time, and newer versions can be deprecated or change existing APIs. This is referred to as "version skew". For every new release, you must review the API changes. The APIs might be compatible across several releases of an Operator, but compatibility is not guaranteed. To mitigate against problems that arise from version skew, follow a well-defined update strategy. 

**Additional resources**

  * [Understanding API tiers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/api_overview/#understanding-api-support-tiers)
  * [Kubernetes version skew policy](https://kubernetes.io/releases/version-skew-policy/)



### 13.2.2.2. Determining the cluster version update path

Use the Red Hat OpenShift Container Platform Update Graph tool to determine if the path is valid for the z-stream release you want to update to. 

Important

The <4.y+1.z> or <4.y+2.z> version that you update to must have the same patch level as the <4.y.z> release you are updating from. 

The OpenShift Container Platform update process mandates that if a fix is present in a specific <4.y.z> release, then the that fix must be present in the <4.y+1.z> release that you update to. 

**Figure 13.1. Bug fix backporting and the update graph**

![Bug fix backporting and the update graph](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Postinstallation_configuration-en-US/images/172af557896318c1efd6a2c37022467c/openshift-bug-fix-backporting-update-graph.png) ![Bug fix backporting and the update graph](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Postinstallation_configuration-en-US/images/172af557896318c1efd6a2c37022467c/openshift-bug-fix-backporting-update-graph.png)

Important

OpenShift Container Platform development has a strict backport policy that prevents regressions. For example, a bug must be fixed in 4.16.z before it is fixed in 4.15.z. This means that the update graph does not allow for updates to chronologically older releases even if the minor version is greater, for example, updating from 4.15.24 to 4.16.2. 

**Additional resources**

  * [Red Hat OpenShift Container Platform Update Graph](https://access.redhat.com/labs/ocpupgradegraph/update_path/)



**Additional resources**

  * [Understanding update channels and releases](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#understanding-update-channels-releases)



### 13.2.2.3. Selecting the target release

Use the Red Hat OpenShift Container Platform Update Graph or the cincinnati-graph-data repository to determine what release to update to. 

#### 13.2.2.3.1. Determining what z-stream updates are available

Before you can update to a new z-stream release, you need to know what versions are available. 

Note

You do not need to change the channel when performing a z-stream update. 

  1. Determine which z-stream releases are available. Run the following command: 

```shell-session
$ oc adm upgrade
```


**Example output**

```shell-session
Cluster version is 4.14.34

Upstream is unset, so the cluster will use an appropriate default.
Channel: stable-4.14 (available channels: candidate-4.14, candidate-4.15, eus-4.14, eus-4.16, fast-4.14, fast-4.15, stable-4.14, stable-4.15)

Recommended updates:

  VERSION     IMAGE
  4.14.37     quay.io/openshift-release-dev/ocp-release@sha256:14e6ba3975e6c73b659fa55af25084b20ab38a543772ca70e184b903db73092b
  4.14.36     quay.io/openshift-release-dev/ocp-release@sha256:4bc4925e8028158e3f313aa83e59e181c94d88b4aa82a3b00202d6f354e8dfed
  4.14.35     quay.io/openshift-release-dev/ocp-release@sha256:883088e3e6efa7443b0ac28cd7682c2fdbda889b576edad626769bf956ac0858
```


#### 13.2.2.3.2. Changing the channel for a Control Plane Only update

You must change the channel to the required version for a Control Plane Only update. 

Note

You do not need to change the channel when performing a z-stream update. 

  1. Determine the currently configured update channel by running the following command: 

```shell-session
$ oc get clusterversion -o=jsonpath='{.items[*].spec}' | jq
```


**Example output**

```shell-session
{
  "channel": "stable-4.14",
  "clusterID": "01eb9a57-2bfb-4f50-9d37-dc04bd5bac75"
}
```


  2. Change the channel to point to the new channel you want to update to by running the following command: 

```shell-session
$ oc adm upgrade channel eus-4.16
```


  3. Confirm the updated channel by running the following command: 

```shell-session
$ oc get clusterversion -o=jsonpath='{.items[*].spec}' | jq
```


**Example output**

```shell-session
{
  "channel": "eus-4.16",
  "clusterID": "01eb9a57-2bfb-4f50-9d37-dc04bd5bac75"
}
```


#### 13.2.2.3.3. Changing the channel for an early EUS to EUS update

The update path to a brand new release of OpenShift Container Platform is not available in either the EUS channel or the stable channel until 45 to 90 days after the initial GA of a minor release. 

To begin testing an update to a new release, you can use the fast channel. 

  1. Change the channel to `fast-<y+1>`. For example, run the following command: 

```shell-session
$ oc adm upgrade channel fast-4.16
```


  2. Check the update path from the new channel. Run the following command: 

```shell-session
$ oc adm upgrade
```


```shell-session
Cluster version is 4.15.33

Upgradeable=False

  Reason: AdminAckRequired
  Message: Kubernetes 1.28 and therefore {product-title} 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/6958394 for details and instructions.

Upstream is unset, so the cluster will use an appropriate default.
Channel: fast-4.16 (available channels: candidate-4.15, candidate-4.16, eus-4.15, eus-4.16, fast-4.15, fast-4.16, stable-4.15, stable-4.16)

Recommended updates:

  VERSION     IMAGE
  4.16.14     quay.io/openshift-release-dev/ocp-release@sha256:6618dd3c0f5
  4.16.13     quay.io/openshift-release-dev/ocp-release@sha256:7a72abc3
  4.16.12     quay.io/openshift-release-dev/ocp-release@sha256:1c8359fc2
  4.16.11     quay.io/openshift-release-dev/ocp-release@sha256:bc9006febfe
  4.16.10     quay.io/openshift-release-dev/ocp-release@sha256:dece7b61b1
  4.15.36     quay.io/openshift-release-dev/ocp-release@sha256:c31a56d19
  4.15.35     quay.io/openshift-release-dev/ocp-release@sha256:f21253
  4.15.34     quay.io/openshift-release-dev/ocp-release@sha256:2dd69c5
```


  3. Follow the update procedure to get to version 4.16 (<y+1> from version 4.15) 

Note

You can keep your worker nodes paused between EUS releases even if you are using the fast channel. 

  4. When you get to the required <y+1> release, change the channel again, this time to `fast-<y+2>`. 
  5. Follow the EUS update procedure to get to the required <y+2> release. 



#### 13.2.2.3.4. Changing the channel for a y-stream update

In a y-stream update you change the channel to the next release channel. 

Note

Use the stable or EUS release channels for production clusters. 

  1. Change the update channel by running the following command: 

```shell-session
$ oc adm upgrade channel stable-4.15
```


  2. Check the update path from the new channel. Run the following command: 

```shell-session
$ oc adm upgrade
```


**Example output**

```shell-session
Cluster version is 4.14.34

Upgradeable=False

  Reason: AdminAckRequired
  Message: Kubernetes 1.27 and therefore {product-title} 4.15 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/6958394 for details and instructions.

Upstream is unset, so the cluster will use an appropriate default.
Channel: stable-4.15 (available channels: candidate-4.14, candidate-4.15, eus-4.14, eus-4.15, fast-4.14, fast-4.15, stable-4.14, stable-4.15)

Recommended updates:

  VERSION     IMAGE
  4.15.33     quay.io/openshift-release-dev/ocp-release@sha256:7142dd4b560
  4.15.32     quay.io/openshift-release-dev/ocp-release@sha256:cda8ea5b13dc9
  4.15.31     quay.io/openshift-release-dev/ocp-release@sha256:07cf61e67d3eeee
  4.15.30     quay.io/openshift-release-dev/ocp-release@sha256:6618dd3c0f5
  4.15.29     quay.io/openshift-release-dev/ocp-release@sha256:7a72abc3
  4.15.28     quay.io/openshift-release-dev/ocp-release@sha256:1c8359fc2
  4.15.27     quay.io/openshift-release-dev/ocp-release@sha256:bc9006febfe
  4.15.26     quay.io/openshift-release-dev/ocp-release@sha256:dece7b61b1
  4.14.38     quay.io/openshift-release-dev/ocp-release@sha256:c93914c62d7
  4.14.37     quay.io/openshift-release-dev/ocp-release@sha256:c31a56d19
  4.14.36     quay.io/openshift-release-dev/ocp-release@sha256:f21253
  4.14.35     quay.io/openshift-release-dev/ocp-release@sha256:2dd69c5
```


**Additional resources**

  * [Red Hat OpenShift Container Platform Update Graph](https://access.redhat.com/labs/ocpupgradegraph/update_path)
  * [cincinnati-graph-data repository](https://github.com/openshift/cincinnati-graph-data/tree/master/channels)



## 13.2.3. Preparing a bare-metal cluster for platform update

On bare-metal hardware, you often must update the firmware to take on important security fixes, take on new functionality, or maintain compatibility with the new release of OpenShift Container Platform. 

### 13.2.3.1. Disconnected environment considerations

To update clusters in disconnected environments, you must update your offline image repository. 

**Additional resources**

  * [API compatibility guidelines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/api_overview/#api-compatibility-guidelines_compatibility-guidelines)
  * [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-installing-oc-mirror-v2)



### 13.2.3.2. Ensuring the host firmware is compatible with the update

You are responsible for the firmware versions that you run in your clusters. Updating host firmware is not a part of the OpenShift Container Platform update process. It is not recommended to update firmware in conjunction with the OpenShift Container Platform version. 

Important

Hardware vendors advise that it is best to apply the latest certified firmware version for the specific hardware that you are running. For each different use case, always verify firmware updates in test environments before applying them in production. For example, workloads with high throughput requirements can be negatively affected outdated host firmware. 

You should thoroughly test new firmware updates to ensure that they work as expected with the current version of OpenShift Container Platform. For best results, test the latest firmware version with the target OpenShift Container Platform update version. 

### 13.2.3.3. Ensuring that layered products are compatible with the update

**Procedure**

Verify that all layered products run on the version of OpenShift Container Platform that you are updating to before you begin the update. This generally includes all Operators. 

**Procedure**

  1. Verify the currently installed Operators in the cluster. For example, run the following command: 

```shell-session
$ oc get csv -A
```


**Example output**

```shell-session
NAMESPACE                              NAME            DISPLAY          VERSION   REPLACES                             PHASE
gitlab-operator-kubernetes.v0.17.2     GitLab                           0.17.2    gitlab-operator-kubernetes.v0.17.1   Succeeded
openshift-operator-lifecycle-manager   packageserver   Package Server   0.19.0                                         Succeeded
```


  2. Check that Operators that you install with OLM are compatible with the update version. 

Operators that are installed with the Operator Lifecycle Manager (OLM) are not part of the standard cluster Operators set. 

Use the [Operator Update Information Checker](https://access.redhat.com/labs/ocpouic/?upgrade_path=4.14%20to%204.16) to understand if you must update an Operator after each y-stream update or if you can wait until you have fully updated to the next EUS release. 

Tip

You can also use the [Operator Update Information Checker](https://access.redhat.com/labs/ocpouic/?upgrade_path=4.14%20to%204.16) to see what versions of OpenShift Container Platform are compatible with specific releases of an Operator. 

  3. Check that Operators that you install outside of OLM are compatible with the update version. 

For all OLM-installed Operators that are not directly supported by Red Hat, contact the Operator vendor to ensure release compatibility. 

     * Some Operators are compatible with several releases of OpenShift Container Platform. 

See "Updating the worker nodes" for more information. 

     * See "Updating all the OLM Operators" for information about updating an Operator after performing the first y-stream control plane update. 




**Additional resources**

  * [Updating the worker nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-updating-the-worker-nodes_completing-the-update "13.2.6.8. Updating the worker nodes")
  * [Updating all the OLM Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-updating-all-the-olm-operators_completing-the-update "13.2.6.7. Updating all the OLM Operators")



### 13.2.3.4. Applying MachineConfigPool labels to nodes before the update

Prepare `MachineConfigPool` (MCP) node labels to group nodes together in groups of roughly 8 to 10 nodes. With MCP groups, you can reboot groups of nodes independently from the rest of the cluster. 

You use the MCP node labels to pause and unpause the set of nodes during the update process so that you can do the update and reboot at a time of your choosing. 

**Staggering the cluster update**

Sometimes there are problems during the update. Often the problem is related to hardware failure or nodes needing to be reset. Using MCP node labels, you can update nodes in stages by pausing the update at critical moments, tracking paused and unpaused nodes as you proceed. When a problem occurs, you use the nodes that are in an unpaused state to ensure that there are enough nodes running to keep all applications pods running. 

**Dividing worker nodes into MachineConfigPool groups**

How you divide worker nodes into MCPs can vary depending on how many nodes are in the cluster or how many nodes you assign to a node role. By default, the two roles in a cluster are control plane and worker roles. 

You can also move nodes between MCP groups if both groups have the same machine config, which is important if you have too many nodes in one large machine config pool. For more information about MCP groups, see _Additional resources_. 

Note

Larger clusters can have as many as 100 worker nodes. No matter how many nodes there are in the cluster, keep each `MachineConfigPool` group to around 10 nodes. This allows you to control how many nodes are taken down at a time. With multiple `MachineConfigPool` groups, you can unpause several groups at a time to accelerate the update, or separate the update over two or more maintenance windows. 

Example cluster with 15 worker nodes
    

Consider a cluster with 15 worker nodes: 

  * 10 worker nodes are control plane nodes. 
  * 5 worker nodes are data plane nodes. 



Split the control plane and data plane worker node roles into at least 2 MCP groups each. Having 2 MCP groups per role means that you can have one set of nodes that are not affected by the update. 

Example cluster with 6 worker nodes
    

Consider a cluster with 6 worker nodes: 

  * Split the worker nodes into 3 MCP groups of 2 nodes each. 



Upgrade one of the MCP groups. Allow the updated nodes to sit through a day to allow for verification of application compatibility before completing the update on the other 4 nodes. 

Important

The process and pace at which you unpause the MCP groups is determined by your applications and configuration. 

If your pod can handle being scheduled across nodes in a cluster, you can unpause several MCP groups at a time and set the `MaxUnavailable` field in the MCP custom resource (CR) to as high as 50%. This allows up to half of the nodes in an MCP group to restart and get updated. 

**Additional resources**

  * [Node configuration management with machine config pools](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#architecture-machine-config-pools_machine-config-overview)



#### 13.2.3.4.1. Reviewing configured cluster MachineConfigPool roles

Review the currently configured `MachineConfigPool` roles in the cluster. 

**Procedure**

  1. Get the currently configured `mcp` groups in the cluster: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME     CONFIG                   UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-bere83   True      False      False      3              3                   3                     0                      25d
worker   rendered-worker-245c4f   True      False      False      2              2                   2                     0                      25d
```


  2. Compare the list of `mcp` roles to list of nodes in the cluster: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE   VERSION
ctrl-plane-0   Ready    control-plane,master   39d   v1.27.15+6147456
ctrl-plane-1   Ready    control-plane,master   39d   v1.27.15+6147456
ctrl-plane-2   Ready    control-plane,master   39d   v1.27.15+6147456
worker-0       Ready    worker                 39d   v1.27.15+6147456
worker-1       Ready    worker                 39d   v1.27.15+6147456
```


Note

When you apply an `mcp` group change, the node roles are updated. 

Determine how you want to separate the worker nodes into `mcp` groups. 




#### 13.2.3.4.2. Creating MachineConfigPool groups for the cluster

To control the rollout of configuration updates across worker nodes in OpenShift Container Platform, you can create MachineConfigPool (mcp) groups. Label nodes with `mcp` roles and apply `MachineConfigPool` custom resources (CRs) to organize them into groups. 

**Procedure**

  1. Label the nodes so that they can be put into `mcp` groups. Run the following commands: 

```shell-session
$ oc label node worker-0 node-role.kubernetes.io/mcp-1=
```


```shell-session
$ oc label node worker-1 node-role.kubernetes.io/mcp-2=
```


The `mcp-1` and `mcp-2` labels are applied to the nodes. For example: 

**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE   VERSION
ctrl-plane-0   Ready    control-plane,master   39d   v1.27.15+6147456
ctrl-plane-1   Ready    control-plane,master   39d   v1.27.15+6147456
ctrl-plane-2   Ready    control-plane,master   39d   v1.27.15+6147456
worker-0       Ready    mcp-1,worker           39d   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           39d   v1.27.15+6147456
```


  2. Create YAML custom resources (CRs) that apply the labels as `mcp` CRs in the cluster. Save the following YAML in the `mcps.yaml` file: 

```yaml
---
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: mcp-2
spec:
  machineConfigSelector:
    matchExpressions:
      - {
         key: machineconfiguration.openshift.io/role,
         operator: In,
         values: [worker,mcp-2]
        }
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/mcp-2: ""
---
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: mcp-1
spec:
  machineConfigSelector:
    matchExpressions:
      - {
         key: machineconfiguration.openshift.io/role,
         operator: In,
         values: [worker,mcp-1]
        }
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/mcp-1: ""
```


  3. Create the `MachineConfigPool` resources: 

```shell-session
$ oc apply -f mcps.yaml
```


**Example output**

```shell-session
machineconfigpool.machineconfiguration.openshift.io/mcp-2 created
```


**Verification**

Monitor the `MachineConfigPool` resources as they are applied in the cluster. After you apply the `mcp` resources, the nodes are added into the new machine config pools. This takes a few minutes. 

Note

The nodes do not reboot while being added into the `mcp` groups. The original worker and master `mcp` groups remain unchanged. 

  * Check the status of the new `mcp` resources: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME     CONFIG                   UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-be3e83   True      False      False      3              3                 3                     0                      25d
mcp-1    rendered-mcp-1-2f4c4f    False     True       True       1              0                 0                     0                      10s
mcp-2    rendered-mcp-2-2r4s1f    False     True       True       1              0                 0                     0                      10s
worker   rendered-worker-23fc4f   False     True       True       0              0                 0                     2                      25d
```


Eventually, the resources are fully applied: 

```shell-session
NAME     CONFIG                   UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-be3e83   True      False      False      3              3                 3                     0                      25d
mcp-1    rendered-mcp-1-2f4c4f    True      False      False      1              1                 1                     0                      7m33s
mcp-2    rendered-mcp-2-2r4s1f    True      False      False      1              1                 1                     0                      51s
worker   rendered-worker-23fc4f   True      False      False      0              0                 0                     0                      25d
```


**Additional resources**

  * [Performing a Control Plane Only update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#control-plane-only-update)
  * [Factors affecting update duration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#factors-affecting-update-duration_openshift-update-duration)
  * [Ensuring that CNF workloads run uninterrupted with pod disruption budgets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-pdb_update-cnf-update-prep "13.2.4.1. Ensuring that workloads run uninterrupted with pod disruption budgets")
  * [Ensuring that pods do not run on the same cluster node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-pod-anti-affinity_update-cnf-update-prep "13.2.4.2. Ensuring that pods do not run on the same cluster node")



### 13.2.3.5. Preparing the cluster platform for update

Before you update the cluster, perform basic checks and verifications to ensure that the cluster is ready for the update. 

**Procedure**

  1. Verify that there are no failed or in progress pods in the cluster by running the following command: 

```shell-session
$ oc get pods -A | grep -E -vi 'complete|running'
```


Note

You might have to run this command more than once if there are pods that are in a pending state. 

  2. Verify that all nodes in the cluster are available: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE   VERSION
ctrl-plane-0   Ready    control-plane,master   32d   v1.27.15+6147456
ctrl-plane-1   Ready    control-plane,master   32d   v1.27.15+6147456
ctrl-plane-2   Ready    control-plane,master   32d   v1.27.15+6147456
worker-0       Ready    mcp-1,worker           32d   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           32d   v1.27.15+6147456
```


  3. Verify that all bare-metal nodes are provisioned and ready. 

```shell-session
$ oc get bmh -n openshift-machine-api
```


**Example output**

```shell-session
NAME           STATE         CONSUMER                   ONLINE   ERROR   AGE
ctrl-plane-0   unmanaged     cnf-58879-master-0         true             33d
ctrl-plane-1   unmanaged     cnf-58879-master-1         true             33d
ctrl-plane-2   unmanaged     cnf-58879-master-2         true             33d
worker-0       unmanaged     cnf-58879-worker-0-45879   true             33d
worker-1       progressing   cnf-58879-worker-0-dszsh   false            1d
```


An error occurred while provisioning the `worker-1` node. 




**Verification**

  * Verify that all cluster Operators are ready: 

```shell-session
$ oc get co
```


**Example output**

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.14.34   True        False         False      17h
baremetal                                  4.14.34   True        False         False      32d

...

service-ca                                 4.14.34   True        False         False      32d
storage                                    4.14.34   True        False         False      32d
```


**Additional resources**

  * [Investigating pod issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#investigating-pod-issues)



## 13.2.4. Configuring application pods before updating your OpenShift Container Platform cluster

Configure application pods to ensure workload availability during OpenShift Container Platform updates. For example, use deployment strategies, pod disruption budgets, anti-affinity rules, and health probes to maintain high availability and prevent service disruption. In the telecommunications industry, most containerized network function (CNF) vendors follow the guidance in Red Hat best practices for Kubernetes to ensure that the cluster can schedule pods properly during an upgrade. 

Important

Always deploy pods in groups by using `Deployment` resources. `Deployment` resources spread the workload across all of the available pods ensuring there is no single point of failure. When a pod that is managed by a `Deployment` resource is deleted, a new pod takes its place automatically. 

**Additional resources**

  * [Red Hat best practices for Kubernetes](https://redhat-best-practices-for-k8s.github.io/guide/)



### 13.2.4.1. Ensuring that workloads run uninterrupted with pod disruption budgets

To prevent interruption of upgrading worker nodes, configure the pod disruption budget properly. For more information, see _Additional resources_. 

**Additional resources**

  * [Specifying the number of pods that must be up with pod disruption budgets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-cluster-tasks#nodes-pods-pod-disruption-configuring_post-install-cluster-tasks "4.13.2. Specify the number of pods that must be up with pod disruption budgets")
  * [Configuring an OpenShift Container Platform cluster for pods](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-pod-disruption-configuring_nodes-pods-configuring)
  * [Pod preemption and other scheduler settings](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#priority-preemption-other_nodes-pods-priority)



### 13.2.4.2. Ensuring that pods do not run on the same cluster node

High availability in Kubernetes requires duplicate processes to be running on separate nodes in the cluster. 

This ensures that the application continues to run even if one node becomes unavailable. In OpenShift Container Platform, processes can be automatically duplicated in separate pods in a deployment. You configure anti-affinity in the `Pod` resource to ensure that the pods in a deployment do not run on the same cluster node. 

During an update, setting pod anti-affinity ensures that pods are distributed evenly across nodes in the cluster. This means that node reboots are easier during an update. For example, if there are 4 pods from a single deployment on a node, and the pod disruption budget is set to only allow 1 pod to be deleted at a time, then it will take 4 times as long for that node to reboot. Setting pod anti-affinity spreads pods across the cluster to prevent such occurrences. 

**Additional resources**

  * [Configuring a pod affinity rule](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-pod-affinity-configuring_nodes-scheduler-pod-affinity)



### 13.2.4.3. Application liveness, readiness, and startup probes

You can use liveness, readiness and startup probes to check the health of your live application containers before you schedule an update. These are very useful tools to use with pods that are dependent upon keeping state for their application containers. 

Liveness health check
     Determines if a container is running. If the liveness probe fails for a container, the pod responds based on the restart policy. 
Readiness probe
     Determines if a container is ready to accept service requests. If the readiness probe fails for a container, the kubelet removes the container from the list of available service endpoints. 
Startup probe
     A startup probe indicates whether the application within a container is started. All other probes are disabled until the startup succeeds. If the startup probe does not succeed, the kubelet stops the container, and the container is subject to the pod `restartPolicy` setting. 

**Additional resources**

  * [Understanding health checks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#application-health-about_application-health)



## 13.2.5. Before you update the telco core CNF cluster

Before you start the cluster update, you must pause worker nodes, back up the etcd database, and do a final cluster health check before proceeding. 

### 13.2.5.1. Pausing worker nodes before the update

You must pause the worker nodes before you proceed with the update. In the following example, there are 2 `mcp` groups, `mcp-1` and `mcp-2`. You patch the `spec.paused` field to `true` for each of the `MachineConfigPool` groups. 

**Procedure**

  1. Patch the `mcp` CRs to pause the nodes and drain and remove the pods from those nodes by running the following command: 

```shell-session
$ oc patch mcp/mcp-1 --type merge --patch '{"spec":{"paused":true}}'
```


```shell-session
$ oc patch mcp/mcp-2 --type merge --patch '{"spec":{"paused":true}}'
```


  2. Get the status of the paused `mcp` groups: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   true
mcp-2   true
```


Note

The default control plane and worker `mcp` groups are not changed during an update. 




### 13.2.5.2. Backup the etcd database before you proceed with the update

You must backup the etcd database before you proceed with the update. 

#### 13.2.5.2.1. Backing up etcd data

You can back up etcd data by creating an etcd snapshot and saving the static pod resources on a control plane host. This backup preserves the cluster state and provides the resources required to restore etcd at a later time. 

Important

Only save a backup from a single control plane host. Do not take a backup from each control plane host in the cluster. 

For a Two-Node with Fencing (TNF) setup, follow the steps to back up etcd data on only one node in the cluster. The cluster restore process is driven by data from a single node, so you can perform the etcd backup steps on only one node. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have verified whether the cluster-wide proxy is enabled. 

Tip

You can check whether the proxy is enabled by reviewing the output of `oc get proxy cluster -o yaml`. The proxy is enabled if the `httpProxy`, `httpsProxy`, and `noProxy` fields have values set. 




**Procedure**

  1. Start a debug session as root for a control plane node: 

```shell-session
$ oc debug --as-root node/<node_name>
```


  2. Change your root directory to `/host` in the debug shell: 

```shell-session
sh-4.4# chroot /host
```


  3. If the cluster-wide proxy is enabled, export the `NO_PROXY`, `HTTP_PROXY`, and `HTTPS_PROXY` environment variables by running the following commands: 

```shell-session
$ export HTTP_PROXY=http://<your_proxy.example.com>:8080
```


```shell-session
$ export HTTPS_PROXY=https://<your_proxy.example.com>:8080
```


```shell-session
$ export NO_PROXY=<example.com>
```


  4. Run the `cluster-backup.sh` script with the path to the directory where you want to save the backup: 

Tip

The `cluster-backup.sh` script is maintained as a component of the etcd Cluster Operator and is a wrapper around the `etcdctl snapshot save` command. 

```shell-session
sh-4.4# /usr/local/bin/cluster-backup.sh /home/core/assets/backup
```


**Example script output**

```shell-session
found latest kube-apiserver: /etc/kubernetes/static-pod-resources/kube-apiserver-pod-6
found latest kube-controller-manager: /etc/kubernetes/static-pod-resources/kube-controller-manager-pod-7
found latest kube-scheduler: /etc/kubernetes/static-pod-resources/kube-scheduler-pod-6
found latest etcd: /etc/kubernetes/static-pod-resources/etcd-pod-3
ede95fe6b88b87ba86a03c15e669fb4aa5bf0991c180d3c6895ce72eaade54a1
etcdctl version: 3.4.14
API version: 3.4
{"level":"info","ts":1624647639.0188997,"caller":"snapshot/v3_snapshot.go:119","msg":"created temporary db file","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db.part"}
{"level":"info","ts":"2021-06-25T19:00:39.030Z","caller":"clientv3/maintenance.go:200","msg":"opened snapshot stream; downloading"}
{"level":"info","ts":1624647639.0301006,"caller":"snapshot/v3_snapshot.go:127","msg":"fetching snapshot","endpoint":"https://10.0.0.5:2379"}
{"level":"info","ts":"2021-06-25T19:00:40.215Z","caller":"clientv3/maintenance.go:208","msg":"completed snapshot read; closing"}
{"level":"info","ts":1624647640.6032252,"caller":"snapshot/v3_snapshot.go:142","msg":"fetched snapshot","endpoint":"https://10.0.0.5:2379","size":"114 MB","took":1.584090459}
{"level":"info","ts":1624647640.6047094,"caller":"snapshot/v3_snapshot.go:152","msg":"saved","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db"}
Snapshot saved at /home/core/assets/backup/snapshot_2021-06-25_190035.db
{"hash":3866667823,"revision":31407,"totalKey":12828,"totalSize":114446336}
snapshot db and kube resources are successfully saved to /home/core/assets/backup
```


In this example, two files are created in the `/home/core/assets/backup/` directory on the control plane host: 

     * `snapshot_<datetimestamp>.db`: This file is the etcd snapshot. The `cluster-backup.sh` script confirms the validity of the snapshot. 
     * `static_kuberesources_<datetimestamp>.tar.gz`: This file contains the resources for the static pods. If etcd encryption is enabled, it also contains the encryption keys for the etcd snapshot. 

Note

If etcd encryption is enabled, store this second file separately from the etcd snapshot for security reasons. However, this file is required to restore from the etcd snapshot. 

The etcd encryption only encrypts values, not keys. This means that resource types, namespaces, and object names are not encrypted. 




#### 13.2.5.2.2. Creating a single automated etcd backup

You can create a single automated etcd backup by applying an `EtcdBackup` custom resource (CR). Backup data is stored on either dynamically-provisioned or local storage. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have access to the OpenShift CLI (`oc`). 



**Procedure**

  1. If dynamically-provisioned storage is available, complete the following steps to create a single automated etcd backup: 

     1. Create a persistent volume claim (PVC) named `etcd-backup-pvc.yaml` with contents such as the following example: 

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: etcd-backup-pvc
  namespace: openshift-etcd
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: <storage_amount>
  volumeMode: Filesystem
```


where: 

`<storage_amount>`
     Specifies the amount of storage available to the PVC. Adjust this value for your requirements, such as `200Gi`. 

     2. Apply the PVC by running the following command: 

```shell-session
$ oc apply -f etcd-backup-pvc.yaml
```


     3. Verify that the PVC was created by running the following command: 

```shell-session
$ oc get pvc
```


**Example output**

```shell-session
NAME              STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
etcd-backup-pvc   Bound                                                       51s
```


Note

Dynamic PVCs stay in the `Pending` state until they are mounted. 

     4. Create a CR file named `etcd-single-backup.yaml` with contents such as the following example: 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: EtcdBackup
metadata:
  name: etcd-single-backup
  namespace: openshift-etcd
spec:
  pvcName: <pvc_name>
```


where: 

`<pvc_name>`
     Specifies the name of the PVC to save the backup to. Adjust this value according to your environment, such as `etcd-backup-pvc`. 

     5. Apply the CR to start a single backup by running the following command: 

```shell-session
$ oc apply -f etcd-single-backup.yaml
```


  2. If dynamically-provisioned storage is not available, complete the following steps to create a single automated etcd backup: 

     1. Create a `StorageClass` CR file named `etcd-backup-local-storage.yaml` with the following contents: 

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: etcd-backup-local-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: Immediate
```


     2. Apply the `StorageClass` CR by running the following command: 

```shell-session
$ oc apply -f etcd-backup-local-storage.yaml
```


     3. Create a PV named `etcd-backup-pv-fs.yaml` with contents such as the following example: 

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: etcd-backup-pv-fs
spec:
  capacity:
    storage: <storage_amount>
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: etcd-backup-local-storage
  local:
    path: /mnt
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
      - key: kubernetes.io/hostname
         operator: In
         values:
         - <node_name>
```


where: 

`<storage_amount>`
     Specifies the amount of storage available to the PV. Adjust this value for your requirements, such as `100Gi`. 
`<node_name>`
     Specifies the control plane node to attach this PV to. Replace with the actual node name. 

     4. Verify that the PV was created by running the following command: 

```shell-session
$ oc get pv
```


**Example output**

```shell-session
NAME                    CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS                REASON   AGE
etcd-backup-pv-fs       100Gi      RWO            Retain           Available           etcd-backup-local-storage            10s
```


     5. Create a PVC named `etcd-backup-pvc.yaml` with contents such as the following example: 

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: etcd-backup-pvc
  namespace: openshift-etcd
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: <storage_amount>
```


where: 

`<storage_amount>`
     Specifies the amount of storage available to the PVC. Adjust this value for your requirements, such as `10Gi`. 

     6. Apply the PVC by running the following command: 

```shell-session
$ oc apply -f etcd-backup-pvc.yaml
```


     7. Create a CR file named `etcd-single-backup.yaml` with contents such as the following example: 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: EtcdBackup
metadata:
  name: etcd-single-backup
  namespace: openshift-etcd
spec:
  pvcName: <pvc_name>
```


where: 

`<pvc_name>`
     Specifies the name of the PVC to save the backup to. Adjust this value according to your environment, such as `etcd-backup-pvc`. 

     8. Apply the CR to start a single backup by running the following command: 

```shell-session
$ oc apply -f etcd-single-backup.yaml
```


**Additional resources**

  * [Backing up etcd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/#backup-etcd)



### 13.2.5.3. Checking the cluster health

You should check the cluster health often during the update. Check for the node status, cluster Operators status and failed pods. 

**Procedure**

  1. Check the status of the cluster Operators by running the following command: 

```shell-session
$ oc get co
```


**Example output**

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.14.34   True        False         False      4d22h
baremetal                                  4.14.34   True        False         False      4d22h
cloud-controller-manager                   4.14.34   True        False         False      4d23h
cloud-credential                           4.14.34   True        False         False      4d23h
cluster-autoscaler                         4.14.34   True        False         False      4d22h
config-operator                            4.14.34   True        False         False      4d22h
console                                    4.14.34   True        False         False      4d22h
...
service-ca                                 4.14.34   True        False         False      4d22h
storage                                    4.14.34   True        False         False      4d22h
```


  2. Check the status of the cluster nodes: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE     VERSION
ctrl-plane-0   Ready    control-plane,master   4d22h   v1.27.15+6147456
ctrl-plane-1   Ready    control-plane,master   4d22h   v1.27.15+6147456
ctrl-plane-2   Ready    control-plane,master   4d22h   v1.27.15+6147456
worker-0       Ready    mcp-1,worker           4d22h   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           4d22h   v1.27.15+6147456
```


  3. Check that there are no in-progress or failed pods. There should be no pods returned when you run the following command. 

```shell-session
$ oc get po -A | grep -E -iv 'running|complete'
```


## 13.2.6. Completing the control plane Only cluster update

Complete the following steps to perform the control plane only cluster update. 

Important

Control plane only updates were previously known as EUS-to-EUS updates. Control plane only updates are only viable between even-numbered minor versions of OpenShift Container Platform. 

### 13.2.6.1. Acknowledging the control plane only or y-stream update

When you update to all versions from 4.11 and later, you must manually acknowledge that the update can continue. 

Important

Before you acknowledge the update, verify that you are not using any of the Kubernetes APIs that are removed from the version you are updating to. For example, in OpenShift Container Platform 4.17, there are no API removals. See "Kubernetes API removals" for more information. 

**Prerequisites**

  * You have verified that APIs for all of the applications running on your cluster are compatible with the next Y-stream release of OpenShift Container Platform. For more details about compatibility, see "Verifying cluster API versions between update versions". 



**Procedure**

  * Check the cluster update status to determine if administrative acknowledgment is required by running the following command: 

```shell-session
$ oc adm upgrade
```


If the cluster update does not complete successfully, more details about the update failure are provided in the `Reason` and `Message` sections. 

Example output: 

```shell-session
Cluster version is 4.15.45

Upgradeable=False

  Reason: MultipleReasons
  Message: Cluster should not be upgraded between minor versions for multiple reasons: AdminAckRequired,ResourceDeletesInProgress
  * Kubernetes 1.29 and therefore OpenShift 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/7031404 for details and instructions.
  * Cluster minor level upgrades are not allowed while resource deletions are in progress; resources=PrometheusRule "openshift-kube-apiserver/kube-apiserver-recording-rules"

ReleaseAccepted=False

  Reason: PreconditionChecks
  Message: Preconditions failed for payload loaded version="4.16.34" image="quay.io/openshift-release-dev/ocp-release@sha256:41bb08c560f6db5039ccdf242e590e8b23049b5eb31e1c4f6021d1d520b353b8": Precondition "ClusterVersionUpgradeable" failed because of "MultipleReasons": Cluster should not be upgraded between minor versions for multiple reasons: AdminAckRequired,ResourceDeletesInProgress
  * Kubernetes 1.29 and therefore OpenShift 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/7031404 for details and instructions.
  * Cluster minor level upgrades are not allowed while resource deletions are in progress; resources=PrometheusRule "openshift-kube-apiserver/kube-apiserver-recording-rules"

Upstream is unset, so the cluster will use an appropriate default.
Channel: eus-4.16 (available channels: candidate-4.15, candidate-4.16, eus-4.16, fast-4.15, fast-4.16, stable-4.15, stable-4.16)

Recommended updates:

  VERSION     IMAGE
  4.16.34     quay.io/openshift-release-dev/ocp-release@sha256:41bb08c560f6db5039ccdf242e590e8b23049b5eb31e1c4f6021d1d520b353b8
```


Note

In this example, a linked Red Hat Knowledgebase article ([Preparing to upgrade to OpenShift Container Platform 4.16](https://access.redhat.com/articles/7031404)) provides more detail about verifying API compatibility between releases. 




**Verification**

  * Verify the update by running the following command: 

```shell-session
$ oc get configmap admin-acks -n openshift-config -o json | jq .data
```


If the acknowledgment was successful, the output shows the acknowledged API removals for each update: 

```shell-session
{
  "ack-4.14-kube-1.28-api-removals-in-4.15": "true",
  "ack-4.15-kube-1.29-api-removals-in-4.16": "true"
}
```


Note

In this example, the cluster is updated from version 4.14 to 4.15, and then from 4.15 to 4.16 in a Control Plane Only update. 




**Additional resources**

  * [Kubernetes API removals](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#kube-api-removals_updating-cluster-prepare)



### 13.2.6.2. Starting the cluster update

When updating from one y-stream release to the next, you must ensure that the intermediate z-stream releases are also compatible. 

Note

You can verify that you are updating to a viable release by running the `oc adm upgrade` command. The `oc adm upgrade` command lists the compatible update releases. 

**Procedure**

  1. Start the update: 

```shell-session
$ oc adm upgrade --to=4.15.33
```


Important

     * **Control plane only update** : Ensure you point to the interim <y+1> release path 
     * **Y-stream update** \- Ensure you use the correct <y.z> release that follows the Kubernetes [version skew policy](https://kubernetes.io/releases/version-skew-policy/). 
     * **Z-stream update** \- Verify that there are no problems moving to that specific release 

```shell-session
Requested update to <version>
```


\+ where: 

\+ `<version>`:: Specifies the version number for your particular update, such as `4.15.33`. 




**Additional resources**

  * [Selecting the target release](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-selecting-the-target-release_update-api "13.2.2.3. Selecting the target release")



### 13.2.6.3. Monitoring the cluster update

You should check the cluster health often during the update. Check for the node status, cluster Operators status and failed pods. 

**Procedure**

  * Monitor the cluster update. For example, to monitor the cluster update from version 4.14 to 4.15, run the following command: 

```shell-session
$ watch "oc get clusterversion; echo; oc get co | head -1; oc get co | grep 4.14; oc get co | grep 4.15; echo; oc get no; echo; oc get po -A | grep -E -iv 'running|complete'"
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.14.34   True        True          4m6s    Working towards 4.15.33: 111 of 873 done (12% complete), waiting on kube-apiserver

NAME                           VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                 4.14.34   True        False         False      4d22h
baremetal                      4.14.34   True        False         False      4d23h
cloud-controller-manager       4.14.34   True        False         False      4d23h
cloud-credential               4.14.34   True        False         False      4d23h
cluster-autoscaler             4.14.34   True        False         False      4d23h
console                        4.14.34   True        False         False      4d22h

...

storage                        4.14.34   True        False         False      4d23h
config-operator                4.15.33   True        False         False      4d23h
etcd                           4.15.33   True        False         False      4d23h

NAME           STATUS   ROLES                  AGE     VERSION
ctrl-plane-0   Ready    control-plane,master   4d23h   v1.27.15+6147456
ctrl-plane-1   Ready    control-plane,master   4d23h   v1.27.15+6147456
ctrl-plane-2   Ready    control-plane,master   4d23h   v1.27.15+6147456
worker-0       Ready    mcp-1,worker           4d23h   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           4d23h   v1.27.15+6147456

NAMESPACE               NAME                       READY   STATUS              RESTARTS   AGE
openshift-marketplace   redhat-marketplace-rf86t   0/1     ContainerCreating   0          0s
```


**Verification**

During the update the `watch` command cycles through one or several of the cluster Operators at a time, providing a status of the Operator update in the `MESSAGE` column. 

When the cluster Operators update process is complete, each control plane nodes is rebooted, one at a time. 

Note

During this part of the update, messages are reported that state cluster Operators are being updated again or are in a degraded state. This is because the control plane node is offline while it reboots nodes. 

As soon as the last control plane node reboot is complete, the cluster version is displayed as updated. 

When the control plane update is complete a message such as the following is displayed. This example shows an update completed to the intermediate y-stream release. 

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.15.33   True        False         28m     Cluster version is 4.15.33

NAME                         VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication               4.15.33   True        False         False	  5d
baremetal                    4.15.33   True        False         False	  5d
cloud-controller-manager     4.15.33   True        False         False	  5d1h
cloud-credential             4.15.33   True        False         False	  5d1h
cluster-autoscaler           4.15.33   True        False         False	  5d
config-operator              4.15.33   True        False         False	  5d
console                      4.15.33   True        False         False	  5d

...

service-ca                   4.15.33   True        False         False	  5d
storage                      4.15.33   True        False         False	  5d

NAME           STATUS   ROLES                  AGE   VERSION
ctrl-plane-0   Ready    control-plane,master   5d    v1.28.13+2ca1a23
ctrl-plane-1   Ready    control-plane,master   5d    v1.28.13+2ca1a23
ctrl-plane-2   Ready    control-plane,master   5d    v1.28.13+2ca1a23
worker-0       Ready    mcp-1,worker           5d    v1.28.13+2ca1a23
worker-1       Ready    mcp-2,worker           5d    v1.28.13+2ca1a23
```


### 13.2.6.4. Updating the OLM Operators

Software needs to vetted before it is loaded onto a production cluster. 

Production clusters are also quite often configured in disconnected network, which means that they are not always directly connected to the internet. Because the clusters are in a disconnected network, the OpenShift Container Platform Operators are configured for manual update during installation so that new versions can be managed on a cluster-by-cluster basis. Complete the following procedure to move the Operators to the newer versions. 

**Procedure**

  1. Check to see which Operators need to be updated: 

```shell-session
$ oc get installplan -A | grep -E 'APPROVED|false'
```


**Example output**

```shell-session
NAMESPACE           NAME            CSV                                               APPROVAL   APPROVED
metallb-system      install-nwjnh   metallb-operator.v4.16.0-202409202304             Manual     false
openshift-nmstate   install-5r7wr   kubernetes-nmstate-operator.4.16.0-202409251605   Manual     false
```


  2. Patch the `InstallPlan` resources for those Operators: 

```shell-session
$ oc patch installplan -n metallb-system install-nwjnh --type merge --patch \
'{"spec":{"approved":true}}'
```


**Example output**

```shell-session
installplan.operators.coreos.com/install-nwjnh patched
```


  3. Monitor the namespace by running the following command: 

```shell-session
$ oc get all -n metallb-system
```


**Example output**

```shell-session
NAME                                                       READY   STATUS              RESTARTS   AGE
pod/metallb-operator-controller-manager-69b5f884c-8bp22    0/1     ContainerCreating   0          4s
pod/metallb-operator-controller-manager-77895bdb46-bqjdx   1/1     Running             0          4m1s
pod/metallb-operator-webhook-server-5d9b968896-vnbhk       0/1     ContainerCreating   0          4s
pod/metallb-operator-webhook-server-d76f9c6c8-57r4w        1/1     Running             0          4m1s

...

NAME                                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/metallb-operator-controller-manager-69b5f884c    1         1         0       4s
replicaset.apps/metallb-operator-controller-manager-77895bdb46   1         1         1       4m1s
replicaset.apps/metallb-operator-controller-manager-99b76f88     0         0         0       4m40s
replicaset.apps/metallb-operator-webhook-server-5d9b968896       1         1         0       4s
replicaset.apps/metallb-operator-webhook-server-6f7dbfdb88       0         0         0       4m40s
replicaset.apps/metallb-operator-webhook-server-d76f9c6c8        1         1         1       4m1s
```


When the update is complete, the required pods should be in a `Running` state, and the required `ReplicaSet` resources should be ready: 

```shell-session
NAME                                                      READY   STATUS    RESTARTS   AGE
pod/metallb-operator-controller-manager-69b5f884c-8bp22   1/1     Running   0          25s
pod/metallb-operator-webhook-server-5d9b968896-vnbhk      1/1     Running   0          25s

...

NAME                                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/metallb-operator-controller-manager-69b5f884c    1         1         1       25s
replicaset.apps/metallb-operator-controller-manager-77895bdb46   0         0         0       4m22s
replicaset.apps/metallb-operator-webhook-server-5d9b968896       1         1         1       25s
replicaset.apps/metallb-operator-webhook-server-d76f9c6c8        0         0         0       4m22s
```


**Verification**

  * Verify that the Operators do not need to be updated for a second time: 

```shell-session
$ oc get installplan -A | grep -E 'APPROVED|false'
```


There should be no output returned. 

Note

Sometimes you have to approve an update twice because some Operators have interim z-stream release versions that need to be installed before the final version. 




**Additional resources**

  * [Updating the worker nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-updating-the-worker-nodes_completing-the-update "13.2.6.8. Updating the worker nodes")



#### 13.2.6.4.1. Performing the second y-stream update

After completing the first y-stream update, you must update the y-stream control plane version to the new EUS version. 

**Procedure**

  1. Verify that the <4.y.z> release that you selected is still listed as a good channel to move to: 

```shell-session
$ oc adm upgrade
```


**Example output**

```shell-session
Cluster version is 4.15.33

Upgradeable=False

  Reason: AdminAckRequired
  Message: Kubernetes 1.29 and therefore OpenShift 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/7031404 for details and instructions.

Upstream is unset, so the cluster will use an appropriate default.
Channel: eus-4.16 (available channels: candidate-4.15, candidate-4.16, eus-4.16, fast-4.15, fast-4.16, stable-4.15, stable-4.16)

Recommended updates:

  VERSION     IMAGE
  4.16.14     quay.io/openshift-release-dev/ocp-release@sha256:0521a0f1acd2d1b77f76259cb9bae9c743c60c37d9903806a3372c1414253658
  4.16.13     quay.io/openshift-release-dev/ocp-release@sha256:6078cb4ae197b5b0c526910363b8aff540343bfac62ecb1ead9e068d541da27b
  4.15.34     quay.io/openshift-release-dev/ocp-release@sha256:f2e0c593f6ed81250c11d0bac94dbaf63656223477b7e8693a652f933056af6e
```


Note

If you update soon after the initial GA of a new Y-stream release, you might not see new y-stream releases available when you run the `oc adm upgrade` command. 

  2. Optional: View the potential update releases that are not recommended. Run the following command: 

```shell-session
$ oc adm upgrade --include-not-recommended
```


**Example output**

```shell-session
Cluster version is 4.15.33

Upgradeable=False

  Reason: AdminAckRequired
  Message: Kubernetes 1.29 and therefore OpenShift 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/7031404 for details and instructions.

Upstream is unset, so the cluster will use an appropriate default.Channel: eus-4.16 (available channels: candidate-4.15, candidate-4.16, eus-4.16, fast-4.15, fast-4.16, stable-4.15, stable-4.16)

Recommended updates:

  VERSION     IMAGE
  4.16.14     quay.io/openshift-release-dev/ocp-release@sha256:0521a0f1acd2d1b77f76259cb9bae9c743c60c37d9903806a3372c1414253658
  4.16.13     quay.io/openshift-release-dev/ocp-release@sha256:6078cb4ae197b5b0c526910363b8aff540343bfac62ecb1ead9e068d541da27b
  4.15.34     quay.io/openshift-release-dev/ocp-release@sha256:f2e0c593f6ed81250c11d0bac94dbaf63656223477b7e8693a652f933056af6e

Supported but not recommended updates:

  Version: 4.16.15
  Image: quay.io/openshift-release-dev/ocp-release@sha256:671bc35e
  Recommended: Unknown
  Reason: EvaluationFailed
  Message: Exposure to AzureRegistryImagePreservation is unknown due to an evaluation failure: invalid PromQL result length must be one, but is 0
  In Azure clusters, the in-cluster image registry may fail to preserve images on update. https://issues.redhat.com/browse/IR-461
```


Note

The example shows a potential error that can affect clusters hosted in Microsoft Azure. It does not show risks for bare-metal clusters. 




#### 13.2.6.4.2. Acknowledging the y-stream release update

When moving between y-stream releases, you must run a patch command to explicitly acknowledge the update. In the output of the `oc adm upgrade` command, a URL is provided that shows the specific command to run. 

**Prerequisites**

  * You have verified that APIs for all of the applications running on your cluster are compatible with the next Y-stream release of OpenShift Container Platform. For more details about compatibility, see "Verifying cluster API versions between update versions". 
  * Complete the administrative acknowledgment to start the cluster update by running the following command: 

```shell-session
$ oc adm upgrade
```


If the cluster update does not complete successfully, more details about the update failure are provided in the `Reason` and `Message` sections. 

```shell-session
Cluster version is 4.15.45

Upgradeable=False

  Reason: MultipleReasons
  Message: Cluster should not be upgraded between minor versions for multiple reasons: AdminAckRequired,ResourceDeletesInProgress
  * Kubernetes 1.29 and therefore OpenShift 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/7031404 for details and instructions.
  * Cluster minor level upgrades are not allowed while resource deletions are in progress; resources=PrometheusRule "openshift-kube-apiserver/kube-apiserver-recording-rules"

ReleaseAccepted=False

  Reason: PreconditionChecks
  Message: Preconditions failed for payload loaded version="4.16.34" image="quay.io/openshift-release-dev/ocp-release@sha256:41bb08c560f6db5039ccdf242e590e8b23049b5eb31e1c4f6021d1d520b353b8": Precondition "ClusterVersionUpgradeable" failed because of "MultipleReasons": Cluster should not be upgraded between minor versions for multiple reasons: AdminAckRequired,ResourceDeletesInProgress
  * Kubernetes 1.29 and therefore OpenShift 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/7031404 for details and instructions.
  * Cluster minor level upgrades are not allowed while resource deletions are in progress; resources=PrometheusRule "openshift-kube-apiserver/kube-apiserver-recording-rules"

Upstream is unset, so the cluster will use an appropriate default.
Channel: eus-4.16 (available channels: candidate-4.15, candidate-4.16, eus-4.16, fast-4.15, fast-4.16, stable-4.15, stable-4.16)

Recommended updates:

  VERSION     IMAGE
  4.16.34     quay.io/openshift-release-dev/ocp-release@sha256:41bb08c560f6db5039ccdf242e590e8b23049b5eb31e1c4f6021d1d520b353b8
```


Note

In this example, a linked Red Hat Knowledgebase article ([Preparing to upgrade to OpenShift Container Platform 4.16](https://access.redhat.com/articles/7031404)) provides more detail about verifying API compatibility between releases. 

  * Verify the update by running the following command: 

```shell-session
$ oc get configmap admin-acks -n openshift-config -o json | jq .data
```


```shell-session
{
  "ack-4.14-kube-1.28-api-removals-in-4.15": "true",
  "ack-4.15-kube-1.29-api-removals-in-4.16": "true"
}
```


Note

In this example, the cluster is updated from version 4.14 to 4.15, and then from 4.15 to 4.16 in a Control Plane Only update. 




**Additional resources**

  * [Preparing to update to OpenShift Container Platform 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-prepare)



### 13.2.6.5. Starting the y-stream control plane update

After you have determined the full new release that you are moving to, you can run the `oc adm upgrade –to=x.y.z` command. 

**Procedure**

  * Start the y-stream control plane update. For example, run the following command: 

```plaintext
$ oc adm upgrade --to=4.16.14
```


**Example output**

```plaintext
Requested update to 4.16.14
```


You might move to a z-stream release that has potential issues with platforms other than the one you are running on. The following example shows a potential problem for cluster updates on Microsoft Azure: 

```plaintext
$ oc adm upgrade --to=4.16.15
```


**Example output**

```plaintext
error: the update 4.16.15 is not one of the recommended updates, but is available as a conditional update. To accept the Recommended=Unknown risk and to proceed with update use --allow-not-recommended.
  Reason: EvaluationFailed
  Message: Exposure to AzureRegistryImagePreservation is unknown due to an evaluation failure: invalid PromQL result length must be one, but is 0
  In Azure clusters, the in-cluster image registry may fail to preserve images on update. https://issues.redhat.com/browse/IR-461
```


Note

The example shows a potential error that can affect clusters hosted in Microsoft Azure. It does not show risks for bare-metal clusters. 

```plaintext
$ oc adm upgrade --to=4.16.15 --allow-not-recommended
```


**Example output**

```plaintext
warning: with --allow-not-recommended you have accepted the risks with 4.14.11 and bypassed Recommended=Unknown EvaluationFailed: Exposure to AzureRegistryImagePreservation is unknown due to an evaluation failure: invalid PromQL result length must be one, but is 0
In Azure clusters, the in-cluster image registry may fail to preserve images on update. https://issues.redhat.com/browse/IR-461

Requested update to 4.16.15
```


### 13.2.6.6. Monitoring the second part of a  cluster update

Monitor the second part of the cluster update to the <y+1> version. 

**Procedure**

  * Monitor the progress of the second part of the <y+1> update. For example, to monitor the update from 4.15 to 4.16, run the following command: 

```shell-session
$ watch "oc get clusterversion; echo; oc get co | head -1; oc get co | grep 4.15; oc get co | grep 4.16; echo; oc get no; echo; oc get po -A | grep -E -iv 'running|complete'"
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.15.33   True        True          10m     Working towards 4.16.14: 132 of 903 done (14% complete), waiting on kube-controller-manager, kube-scheduler

NAME                         VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication               4.15.33   True        False         False      5d3h
baremetal                    4.15.33   True        False         False      5d4h
cloud-controller-manager     4.15.33   True        False         False      5d4h
cloud-credential             4.15.33   True        False         False      5d4h
cluster-autoscaler           4.15.33   True        False         False      5d4h
console                      4.15.33   True        False         False      5d3h
...
config-operator              4.16.14   True        False         False      5d4h
etcd                         4.16.14   True        False         False      5d4h
kube-apiserver               4.16.14   True        True          False      5d4h    NodeInstallerProgressing: 1 node is at revision 15; 2 nodes are at revision 17

NAME           STATUS   ROLES                  AGE    VERSION
ctrl-plane-0   Ready    control-plane,master   5d4h   v1.28.13+2ca1a23
ctrl-plane-1   Ready    control-plane,master   5d4h   v1.28.13+2ca1a23
ctrl-plane-2   Ready    control-plane,master   5d4h   v1.28.13+2ca1a23
worker-0       Ready    mcp-1,worker           5d4h   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           5d4h   v1.27.15+6147456

NAMESPACE                                          NAME                                                              READY   STATUS      RESTARTS       AGE
openshift-kube-apiserver                           kube-apiserver-ctrl-plane-0                                       0/5     Pending     0              <invalid>
```


As soon as the last control plane node is complete, the cluster version is updated to the new EUS release. For example: 

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.16.14   True        False         123m    Cluster version is 4.16.14

NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.16.14   True        False         False	  5d6h
baremetal                                  4.16.14   True        False         False	  5d7h
cloud-controller-manager                   4.16.14   True        False         False	  5d7h
cloud-credential                           4.16.14   True        False         False	  5d7h
cluster-autoscaler                         4.16.14   True        False         False	  5d7h
config-operator                            4.16.14   True        False         False	  5d7h
console                                    4.16.14   True        False         False	  5d6h
#...
operator-lifecycle-manager-packageserver   4.16.14   True        False         False	  5d7h
service-ca                                 4.16.14   True        False         False	  5d7h
storage                                    4.16.14   True        False         False	  5d7h

NAME           STATUS   ROLES                  AGE     VERSION
ctrl-plane-0   Ready    control-plane,master   5d7h    v1.29.8+f10c92d
ctrl-plane-1   Ready    control-plane,master   5d7h    v1.29.8+f10c92d
ctrl-plane-2   Ready    control-plane,master   5d7h    v1.29.8+f10c92d
worker-0       Ready    mcp-1,worker           5d7h    v1.27.15+6147456
worker-1       Ready    mcp-2,worker           5d7h    v1.27.15+6147456
```


**Additional resources**

  * [Monitoring the cluster update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-monitoring-the-cluster-update_completing-the-update "13.2.6.3. Monitoring the cluster update")



### 13.2.6.7. Updating all the OLM Operators

In the second phase of a multi-version upgrade, you must approve all of the Operators and additionally add installations plans for any other Operators that you want to upgrade. 

Follow the same procedure as outlined in "Updating the OLM Operators". Ensure that you also update any non-OLM Operators as required. 

**Procedure**

  1. Monitor the cluster update. For example, to monitor the cluster update from version 4.14 to 4.15, run the following command: 

```shell-session
$ watch "oc get clusterversion; echo; oc get co | head -1; oc get co | grep 4.14; oc get co | grep 4.15; echo; oc get no; echo; oc get po -A | grep -E -iv 'running|complete'"
```


  2. Check to see which Operators need to be updated: 

```shell-session
$ oc get installplan -A | grep -E 'APPROVED|false'
```


  3. Patch the `InstallPlan` resources for those Operators: 

```shell-session
$ oc patch installplan -n metallb-system install-nwjnh --type merge --patch \
'{"spec":{"approved":true}}'
```


  4. Monitor the namespace by running the following command: 

```shell-session
$ oc get all -n metallb-system
```


When the update is complete, the required pods should be in a `Running` state, and the required `ReplicaSet` resources should be ready. 




**Verification**

During the update the `watch` command cycles through one or several of the cluster Operators at a time, providing a status of the Operator update in the `MESSAGE` column. 

When the cluster Operators update process is complete, each control plane nodes is rebooted, one at a time. 

Note

During this part of the update, messages are reported that state cluster Operators are being updated again or are in a degraded state. This is because the control plane node is offline while it reboots nodes. 

**Additional resources**

  * [Monitoring the cluster update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-monitoring-the-cluster-update_completing-the-update "13.2.6.3. Monitoring the cluster update")
  * [Updating the OLM Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-updating-the-olm-operators_completing-the-update "13.2.6.4. Updating the OLM Operators")



### 13.2.6.8. Updating the worker nodes

You upgrade the worker nodes after you have updated the control plane by unpausing the relevant `mcp` groups you created. 

Unpausing the `mcp` group starts the upgrade process for the worker nodes in that group. Each of the worker nodes in the cluster reboot to upgrade to the new EUS, y-stream or z-stream version as required. 

In the case of control plane only upgrades, note that when a worker node is updated it will only require one reboot and will jump <y+2>-release versions. This is a feature that was added to decrease the amount of time that it takes to upgrade large bare-metal clusters. 

Important

This is a potential holding point. You can have a cluster version that is fully supported to run in production with the control plane that is updated to a new EUS release while the worker nodes are at a <y-2>-release. This allows large clusters to upgrade in steps across several maintenance windows. 

**Procedure**

  1. You can check how many nodes are managed in an `mcp` group. Run the following command to get the list of `mcp` groups: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-c9a52144456dbff9c9af9c5a37d1b614   True      False      False      3              3                   3                     0                      36d
mcp-1    rendered-mcp-1-07fe50b9ad51fae43ed212e84e1dcc8e    False     False      False      1              0                   0                     0                      47h
mcp-2    rendered-mcp-2-07fe50b9ad51fae43ed212e84e1dcc8e    False     False      False      1              0                   0                     0                      47h
worker   rendered-worker-f1ab7b9a768e1b0ac9290a18817f60f0   True      False      False      0              0                   0                     0                      36d
```


Note

You decide how many `mcp` groups to upgrade at a time. This depends on how many pods can be taken down at a time and how your pod disruption budget and anti-affinity settings are configured. 

  2. Get the list of nodes in the cluster: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE    VERSION
ctrl-plane-0   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-1   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-2   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
worker-0       Ready    mcp-1,worker           5d8h   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           5d8h   v1.27.15+6147456
```


  3. Confirm the `MachineConfigPool` groups that are paused: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   true
mcp-2   true
```


Note

Each `MachineConfigPool` can be unpaused independently. Therefore, if a maintenance window runs out of time other MCPs do not need to be unpaused immediately. The cluster is supported to run with some worker nodes still at <y-2>-release version. 

  4. Unpause the required `mcp` group to begin the upgrade: 

```shell-session
$ oc patch mcp/mcp-1 --type merge --patch '{"spec":{"paused":false}}'
```


**Example output**

```shell-session
machineconfigpool.machineconfiguration.openshift.io/mcp-1 patched
```


  5. Confirm that the required `mcp` group is unpaused: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   false
mcp-2   true
```


  6. As each `mcp` group is upgraded, continue to unpause and upgrade the remaining nodes. 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS                        ROLES                  AGE    VERSION
ctrl-plane-0   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-1   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-2   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
worker-0       Ready                         mcp-1,worker           5d8h   v1.29.8+f10c92d
worker-1       NotReady,SchedulingDisabled   mcp-2,worker           5d8h   v1.27.15+6147456
```


### 13.2.6.9. Verifying the health of the newly updated cluster

After updating the cluster, verify that the cluster is back up and running. 

**Procedure**

  1. Check the cluster version by running the following command: 

```shell-session
$ oc get clusterversion
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.16.14   True        False         4h38m   Cluster version is 4.16.14
```


This should return the new cluster version and the `PROGRESSING` column should return `False`. 

  2. Check that all nodes are ready: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE    VERSION
ctrl-plane-0   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
ctrl-plane-1   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
ctrl-plane-2   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
worker-0       Ready    mcp-1,worker           5d9h   v1.29.8+f10c92d
worker-1       Ready    mcp-2,worker           5d9h   v1.29.8+f10c92d
```


All nodes in the cluster should be in a `Ready` status and running the same version. 

  3. Check that there are no paused `mcp` resources in the cluster: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   false
mcp-2   false
```


  4. Check that all cluster Operators are available: 

```shell-session
$ oc get co
```


**Example output**

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.16.14   True        False         False      5d9h
baremetal                                  4.16.14   True        False         False      5d9h
cloud-controller-manager                   4.16.14   True        False         False      5d10h
cloud-credential                           4.16.14   True        False         False      5d10h
cluster-autoscaler                         4.16.14   True        False         False      5d9h
config-operator                            4.16.14   True        False         False      5d9h
console                                    4.16.14   True        False         False      5d9h
control-plane-machine-set                  4.16.14   True        False         False      5d9h
csi-snapshot-controller                    4.16.14   True        False         False      5d9h
dns                                        4.16.14   True        False         False      5d9h
etcd                                       4.16.14   True        False         False      5d9h
image-registry                             4.16.14   True        False         False      85m
ingress                                    4.16.14   True        False         False      5d9h
insights                                   4.16.14   True        False         False      5d9h
kube-apiserver                             4.16.14   True        False         False      5d9h
kube-controller-manager                    4.16.14   True        False         False      5d9h
kube-scheduler                             4.16.14   True        False         False      5d9h
kube-storage-version-migrator              4.16.14   True        False         False      4h48m
machine-api                                4.16.14   True        False         False      5d9h
machine-approver                           4.16.14   True        False         False      5d9h
machine-config                             4.16.14   True        False         False      5d9h
marketplace                                4.16.14   True        False         False      5d9h
monitoring                                 4.16.14   True        False         False      5d9h
network                                    4.16.14   True        False         False      5d9h
node-tuning                                4.16.14   True        False         False      5d7h
openshift-apiserver                        4.16.14   True        False         False      5d9h
openshift-controller-manager               4.16.14   True        False         False      5d9h
openshift-samples                          4.16.14   True        False         False      5h24m
operator-lifecycle-manager                 4.16.14   True        False         False      5d9h
operator-lifecycle-manager-catalog         4.16.14   True        False         False      5d9h
operator-lifecycle-manager-packageserver   4.16.14   True        False         False      5d9h
service-ca                                 4.16.14   True        False         False      5d9h
storage                                    4.16.14   True        False         False      5d9h
```


All cluster Operators should report `True` in the `AVAILABLE` column. 

  5. Check that all pods are healthy: 

```shell-session
$ oc get po -A | grep -E -iv 'complete|running'
```


This should not return any pods. 

Note

You might see a few pods still moving after the update. Watch this for a while to make sure all pods are cleared. 




## 13.2.7. Completing the y-stream cluster update

Complete the following steps to perform a y-stream cluster update. 

### 13.2.7.1. Acknowledging the control plane only or y-stream update

When you update to all versions from 4.11 and later, you must manually acknowledge that the update can continue. 

Important

Before you acknowledge the update, verify that you are not using any of the Kubernetes APIs that are removed from the version you are updating to. For example, in OpenShift Container Platform 4.17, there are no API removals. See "Kubernetes API removals" for more information. 

**Prerequisites**

  * You have verified that APIs for all of the applications running on your cluster are compatible with the next Y-stream release of OpenShift Container Platform. For more details about compatibility, see "Verifying cluster API versions between update versions". 



**Procedure**

  * Check the cluster update status to determine if administrative acknowledgment is required by running the following command: 

```shell-session
$ oc adm upgrade
```


If the cluster update does not complete successfully, more details about the update failure are provided in the `Reason` and `Message` sections. 

Example output: 

```shell-session
Cluster version is 4.15.45

Upgradeable=False

  Reason: MultipleReasons
  Message: Cluster should not be upgraded between minor versions for multiple reasons: AdminAckRequired,ResourceDeletesInProgress
  * Kubernetes 1.29 and therefore OpenShift 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/7031404 for details and instructions.
  * Cluster minor level upgrades are not allowed while resource deletions are in progress; resources=PrometheusRule "openshift-kube-apiserver/kube-apiserver-recording-rules"

ReleaseAccepted=False

  Reason: PreconditionChecks
  Message: Preconditions failed for payload loaded version="4.16.34" image="quay.io/openshift-release-dev/ocp-release@sha256:41bb08c560f6db5039ccdf242e590e8b23049b5eb31e1c4f6021d1d520b353b8": Precondition "ClusterVersionUpgradeable" failed because of "MultipleReasons": Cluster should not be upgraded between minor versions for multiple reasons: AdminAckRequired,ResourceDeletesInProgress
  * Kubernetes 1.29 and therefore OpenShift 4.16 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/7031404 for details and instructions.
  * Cluster minor level upgrades are not allowed while resource deletions are in progress; resources=PrometheusRule "openshift-kube-apiserver/kube-apiserver-recording-rules"

Upstream is unset, so the cluster will use an appropriate default.
Channel: eus-4.16 (available channels: candidate-4.15, candidate-4.16, eus-4.16, fast-4.15, fast-4.16, stable-4.15, stable-4.16)

Recommended updates:

  VERSION     IMAGE
  4.16.34     quay.io/openshift-release-dev/ocp-release@sha256:41bb08c560f6db5039ccdf242e590e8b23049b5eb31e1c4f6021d1d520b353b8
```


Note

In this example, a linked Red Hat Knowledgebase article ([Preparing to upgrade to OpenShift Container Platform 4.16](https://access.redhat.com/articles/7031404)) provides more detail about verifying API compatibility between releases. 




**Verification**

  * Verify the update by running the following command: 

```shell-session
$ oc get configmap admin-acks -n openshift-config -o json | jq .data
```


If the acknowledgment was successful, the output shows the acknowledged API removals for each update: 

```shell-session
{
  "ack-4.14-kube-1.28-api-removals-in-4.15": "true",
  "ack-4.15-kube-1.29-api-removals-in-4.16": "true"
}
```


Note

In this example, the cluster is updated from version 4.14 to 4.15, and then from 4.15 to 4.16 in a Control Plane Only update. 




**Additional resources**

  * [Kubernetes API removals](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#kube-api-removals_updating-cluster-prepare)



### 13.2.7.2. Starting the cluster update

When updating from one y-stream release to the next, you must ensure that the intermediate z-stream releases are also compatible. 

Note

You can verify that you are updating to a viable release by running the `oc adm upgrade` command. The `oc adm upgrade` command lists the compatible update releases. 

**Procedure**

  1. Start the update: 

```shell-session
$ oc adm upgrade --to=4.15.33
```


Important

     * **Control plane only update** : Ensure you point to the interim <y+1> release path 
     * **Y-stream update** \- Ensure you use the correct <y.z> release that follows the Kubernetes [version skew policy](https://kubernetes.io/releases/version-skew-policy/). 
     * **Z-stream update** \- Verify that there are no problems moving to that specific release 

```shell-session
Requested update to <version>
```


\+ where: 

\+ `<version>`:: Specifies the version number for your particular update, such as `4.15.33`. 




**Additional resources**

  * [Selecting the target release](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-selecting-the-target-release_update-api "13.2.2.3. Selecting the target release")



### 13.2.7.3. Monitoring the cluster update

You should check the cluster health often during the update. Check for the node status, cluster Operators status and failed pods. 

**Procedure**

  * Monitor the cluster update. For example, to monitor the cluster update from version 4.14 to 4.15, run the following command: 

```shell-session
$ watch "oc get clusterversion; echo; oc get co | head -1; oc get co | grep 4.14; oc get co | grep 4.15; echo; oc get no; echo; oc get po -A | grep -E -iv 'running|complete'"
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.14.34   True        True          4m6s    Working towards 4.15.33: 111 of 873 done (12% complete), waiting on kube-apiserver

NAME                           VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                 4.14.34   True        False         False      4d22h
baremetal                      4.14.34   True        False         False      4d23h
cloud-controller-manager       4.14.34   True        False         False      4d23h
cloud-credential               4.14.34   True        False         False      4d23h
cluster-autoscaler             4.14.34   True        False         False      4d23h
console                        4.14.34   True        False         False      4d22h

...

storage                        4.14.34   True        False         False      4d23h
config-operator                4.15.33   True        False         False      4d23h
etcd                           4.15.33   True        False         False      4d23h

NAME           STATUS   ROLES                  AGE     VERSION
ctrl-plane-0   Ready    control-plane,master   4d23h   v1.27.15+6147456
ctrl-plane-1   Ready    control-plane,master   4d23h   v1.27.15+6147456
ctrl-plane-2   Ready    control-plane,master   4d23h   v1.27.15+6147456
worker-0       Ready    mcp-1,worker           4d23h   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           4d23h   v1.27.15+6147456

NAMESPACE               NAME                       READY   STATUS              RESTARTS   AGE
openshift-marketplace   redhat-marketplace-rf86t   0/1     ContainerCreating   0          0s
```


**Verification**

During the update the `watch` command cycles through one or several of the cluster Operators at a time, providing a status of the Operator update in the `MESSAGE` column. 

When the cluster Operators update process is complete, each control plane nodes is rebooted, one at a time. 

Note

During this part of the update, messages are reported that state cluster Operators are being updated again or are in a degraded state. This is because the control plane node is offline while it reboots nodes. 

As soon as the last control plane node reboot is complete, the cluster version is displayed as updated. 

When the control plane update is complete a message such as the following is displayed. This example shows an update completed to the intermediate y-stream release. 

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.15.33   True        False         28m     Cluster version is 4.15.33

NAME                         VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication               4.15.33   True        False         False	  5d
baremetal                    4.15.33   True        False         False	  5d
cloud-controller-manager     4.15.33   True        False         False	  5d1h
cloud-credential             4.15.33   True        False         False	  5d1h
cluster-autoscaler           4.15.33   True        False         False	  5d
config-operator              4.15.33   True        False         False	  5d
console                      4.15.33   True        False         False	  5d

...

service-ca                   4.15.33   True        False         False	  5d
storage                      4.15.33   True        False         False	  5d

NAME           STATUS   ROLES                  AGE   VERSION
ctrl-plane-0   Ready    control-plane,master   5d    v1.28.13+2ca1a23
ctrl-plane-1   Ready    control-plane,master   5d    v1.28.13+2ca1a23
ctrl-plane-2   Ready    control-plane,master   5d    v1.28.13+2ca1a23
worker-0       Ready    mcp-1,worker           5d    v1.28.13+2ca1a23
worker-1       Ready    mcp-2,worker           5d    v1.28.13+2ca1a23
```


### 13.2.7.4. Updating the OLM Operators

Software needs to vetted before it is loaded onto a production cluster. 

Production clusters are also quite often configured in disconnected network, which means that they are not always directly connected to the internet. Because the clusters are in a disconnected network, the OpenShift Container Platform Operators are configured for manual update during installation so that new versions can be managed on a cluster-by-cluster basis. Complete the following procedure to move the Operators to the newer versions. 

**Procedure**

  1. Check to see which Operators need to be updated: 

```shell-session
$ oc get installplan -A | grep -E 'APPROVED|false'
```


**Example output**

```shell-session
NAMESPACE           NAME            CSV                                               APPROVAL   APPROVED
metallb-system      install-nwjnh   metallb-operator.v4.16.0-202409202304             Manual     false
openshift-nmstate   install-5r7wr   kubernetes-nmstate-operator.4.16.0-202409251605   Manual     false
```


  2. Patch the `InstallPlan` resources for those Operators: 

```shell-session
$ oc patch installplan -n metallb-system install-nwjnh --type merge --patch \
'{"spec":{"approved":true}}'
```


**Example output**

```shell-session
installplan.operators.coreos.com/install-nwjnh patched
```


  3. Monitor the namespace by running the following command: 

```shell-session
$ oc get all -n metallb-system
```


**Example output**

```shell-session
NAME                                                       READY   STATUS              RESTARTS   AGE
pod/metallb-operator-controller-manager-69b5f884c-8bp22    0/1     ContainerCreating   0          4s
pod/metallb-operator-controller-manager-77895bdb46-bqjdx   1/1     Running             0          4m1s
pod/metallb-operator-webhook-server-5d9b968896-vnbhk       0/1     ContainerCreating   0          4s
pod/metallb-operator-webhook-server-d76f9c6c8-57r4w        1/1     Running             0          4m1s

...

NAME                                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/metallb-operator-controller-manager-69b5f884c    1         1         0       4s
replicaset.apps/metallb-operator-controller-manager-77895bdb46   1         1         1       4m1s
replicaset.apps/metallb-operator-controller-manager-99b76f88     0         0         0       4m40s
replicaset.apps/metallb-operator-webhook-server-5d9b968896       1         1         0       4s
replicaset.apps/metallb-operator-webhook-server-6f7dbfdb88       0         0         0       4m40s
replicaset.apps/metallb-operator-webhook-server-d76f9c6c8        1         1         1       4m1s
```


When the update is complete, the required pods should be in a `Running` state, and the required `ReplicaSet` resources should be ready: 

```shell-session
NAME                                                      READY   STATUS    RESTARTS   AGE
pod/metallb-operator-controller-manager-69b5f884c-8bp22   1/1     Running   0          25s
pod/metallb-operator-webhook-server-5d9b968896-vnbhk      1/1     Running   0          25s

...

NAME                                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/metallb-operator-controller-manager-69b5f884c    1         1         1       25s
replicaset.apps/metallb-operator-controller-manager-77895bdb46   0         0         0       4m22s
replicaset.apps/metallb-operator-webhook-server-5d9b968896       1         1         1       25s
replicaset.apps/metallb-operator-webhook-server-d76f9c6c8        0         0         0       4m22s
```


**Verification**

  * Verify that the Operators do not need to be updated for a second time: 

```shell-session
$ oc get installplan -A | grep -E 'APPROVED|false'
```


There should be no output returned. 

Note

Sometimes you have to approve an update twice because some Operators have interim z-stream release versions that need to be installed before the final version. 




**Additional resources**

  * [Updating the worker nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-updating-the-worker-nodes_completing-the-update "13.2.6.8. Updating the worker nodes")



### 13.2.7.5. Updating the worker nodes

You upgrade the worker nodes after you have updated the control plane by unpausing the relevant `mcp` groups you created. 

Unpausing the `mcp` group starts the upgrade process for the worker nodes in that group. Each of the worker nodes in the cluster reboot to upgrade to the new EUS, y-stream or z-stream version as required. 

In the case of control plane only upgrades, note that when a worker node is updated it will only require one reboot and will jump <y+2>-release versions. This is a feature that was added to decrease the amount of time that it takes to upgrade large bare-metal clusters. 

Important

This is a potential holding point. You can have a cluster version that is fully supported to run in production with the control plane that is updated to a new EUS release while the worker nodes are at a <y-2>-release. This allows large clusters to upgrade in steps across several maintenance windows. 

**Procedure**

  1. You can check how many nodes are managed in an `mcp` group. Run the following command to get the list of `mcp` groups: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-c9a52144456dbff9c9af9c5a37d1b614   True      False      False      3              3                   3                     0                      36d
mcp-1    rendered-mcp-1-07fe50b9ad51fae43ed212e84e1dcc8e    False     False      False      1              0                   0                     0                      47h
mcp-2    rendered-mcp-2-07fe50b9ad51fae43ed212e84e1dcc8e    False     False      False      1              0                   0                     0                      47h
worker   rendered-worker-f1ab7b9a768e1b0ac9290a18817f60f0   True      False      False      0              0                   0                     0                      36d
```


Note

You decide how many `mcp` groups to upgrade at a time. This depends on how many pods can be taken down at a time and how your pod disruption budget and anti-affinity settings are configured. 

  2. Get the list of nodes in the cluster: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE    VERSION
ctrl-plane-0   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-1   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-2   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
worker-0       Ready    mcp-1,worker           5d8h   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           5d8h   v1.27.15+6147456
```


  3. Confirm the `MachineConfigPool` groups that are paused: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   true
mcp-2   true
```


Note

Each `MachineConfigPool` can be unpaused independently. Therefore, if a maintenance window runs out of time other MCPs do not need to be unpaused immediately. The cluster is supported to run with some worker nodes still at <y-2>-release version. 

  4. Unpause the required `mcp` group to begin the upgrade: 

```shell-session
$ oc patch mcp/mcp-1 --type merge --patch '{"spec":{"paused":false}}'
```


**Example output**

```shell-session
machineconfigpool.machineconfiguration.openshift.io/mcp-1 patched
```


  5. Confirm that the required `mcp` group is unpaused: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   false
mcp-2   true
```


  6. As each `mcp` group is upgraded, continue to unpause and upgrade the remaining nodes. 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS                        ROLES                  AGE    VERSION
ctrl-plane-0   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-1   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-2   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
worker-0       Ready                         mcp-1,worker           5d8h   v1.29.8+f10c92d
worker-1       NotReady,SchedulingDisabled   mcp-2,worker           5d8h   v1.27.15+6147456
```


### 13.2.7.6. Verifying the health of the newly updated cluster

After updating the cluster, verify that the cluster is back up and running. 

**Procedure**

  1. Check the cluster version by running the following command: 

```shell-session
$ oc get clusterversion
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.16.14   True        False         4h38m   Cluster version is 4.16.14
```


This should return the new cluster version and the `PROGRESSING` column should return `False`. 

  2. Check that all nodes are ready: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE    VERSION
ctrl-plane-0   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
ctrl-plane-1   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
ctrl-plane-2   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
worker-0       Ready    mcp-1,worker           5d9h   v1.29.8+f10c92d
worker-1       Ready    mcp-2,worker           5d9h   v1.29.8+f10c92d
```


All nodes in the cluster should be in a `Ready` status and running the same version. 

  3. Check that there are no paused `mcp` resources in the cluster: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   false
mcp-2   false
```


  4. Check that all cluster Operators are available: 

```shell-session
$ oc get co
```


**Example output**

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.16.14   True        False         False      5d9h
baremetal                                  4.16.14   True        False         False      5d9h
cloud-controller-manager                   4.16.14   True        False         False      5d10h
cloud-credential                           4.16.14   True        False         False      5d10h
cluster-autoscaler                         4.16.14   True        False         False      5d9h
config-operator                            4.16.14   True        False         False      5d9h
console                                    4.16.14   True        False         False      5d9h
control-plane-machine-set                  4.16.14   True        False         False      5d9h
csi-snapshot-controller                    4.16.14   True        False         False      5d9h
dns                                        4.16.14   True        False         False      5d9h
etcd                                       4.16.14   True        False         False      5d9h
image-registry                             4.16.14   True        False         False      85m
ingress                                    4.16.14   True        False         False      5d9h
insights                                   4.16.14   True        False         False      5d9h
kube-apiserver                             4.16.14   True        False         False      5d9h
kube-controller-manager                    4.16.14   True        False         False      5d9h
kube-scheduler                             4.16.14   True        False         False      5d9h
kube-storage-version-migrator              4.16.14   True        False         False      4h48m
machine-api                                4.16.14   True        False         False      5d9h
machine-approver                           4.16.14   True        False         False      5d9h
machine-config                             4.16.14   True        False         False      5d9h
marketplace                                4.16.14   True        False         False      5d9h
monitoring                                 4.16.14   True        False         False      5d9h
network                                    4.16.14   True        False         False      5d9h
node-tuning                                4.16.14   True        False         False      5d7h
openshift-apiserver                        4.16.14   True        False         False      5d9h
openshift-controller-manager               4.16.14   True        False         False      5d9h
openshift-samples                          4.16.14   True        False         False      5h24m
operator-lifecycle-manager                 4.16.14   True        False         False      5d9h
operator-lifecycle-manager-catalog         4.16.14   True        False         False      5d9h
operator-lifecycle-manager-packageserver   4.16.14   True        False         False      5d9h
service-ca                                 4.16.14   True        False         False      5d9h
storage                                    4.16.14   True        False         False      5d9h
```


All cluster Operators should report `True` in the `AVAILABLE` column. 

  5. Check that all pods are healthy: 

```shell-session
$ oc get po -A | grep -E -iv 'complete|running'
```


This should not return any pods. 

Note

You might see a few pods still moving after the update. Watch this for a while to make sure all pods are cleared. 




## 13.2.8. Completing the z-stream cluster update

Complete the following steps to perform a z-stream cluster update. 

### 13.2.8.1. Starting the cluster update

When updating from one y-stream release to the next, you must ensure that the intermediate z-stream releases are also compatible. 

Note

You can verify that you are updating to a viable release by running the `oc adm upgrade` command. The `oc adm upgrade` command lists the compatible update releases. 

**Procedure**

  1. Start the update: 

```shell-session
$ oc adm upgrade --to=4.15.33
```


Important

     * **Control plane only update** : Ensure you point to the interim <y+1> release path 
     * **Y-stream update** \- Ensure you use the correct <y.z> release that follows the Kubernetes [version skew policy](https://kubernetes.io/releases/version-skew-policy/). 
     * **Z-stream update** \- Verify that there are no problems moving to that specific release 

```shell-session
Requested update to <version>
```


\+ where: 

\+ `<version>`:: Specifies the version number for your particular update, such as `4.15.33`. 




**Additional resources**

  * [Selecting the target release](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-selecting-the-target-release_update-api "13.2.2.3. Selecting the target release")



### 13.2.8.2. Updating the worker nodes

You upgrade the worker nodes after you have updated the control plane by unpausing the relevant `mcp` groups you created. 

Unpausing the `mcp` group starts the upgrade process for the worker nodes in that group. Each of the worker nodes in the cluster reboot to upgrade to the new EUS, y-stream or z-stream version as required. 

In the case of control plane only upgrades, note that when a worker node is updated it will only require one reboot and will jump <y+2>-release versions. This is a feature that was added to decrease the amount of time that it takes to upgrade large bare-metal clusters. 

Important

This is a potential holding point. You can have a cluster version that is fully supported to run in production with the control plane that is updated to a new EUS release while the worker nodes are at a <y-2>-release. This allows large clusters to upgrade in steps across several maintenance windows. 

**Procedure**

  1. You can check how many nodes are managed in an `mcp` group. Run the following command to get the list of `mcp` groups: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-c9a52144456dbff9c9af9c5a37d1b614   True      False      False      3              3                   3                     0                      36d
mcp-1    rendered-mcp-1-07fe50b9ad51fae43ed212e84e1dcc8e    False     False      False      1              0                   0                     0                      47h
mcp-2    rendered-mcp-2-07fe50b9ad51fae43ed212e84e1dcc8e    False     False      False      1              0                   0                     0                      47h
worker   rendered-worker-f1ab7b9a768e1b0ac9290a18817f60f0   True      False      False      0              0                   0                     0                      36d
```


Note

You decide how many `mcp` groups to upgrade at a time. This depends on how many pods can be taken down at a time and how your pod disruption budget and anti-affinity settings are configured. 

  2. Get the list of nodes in the cluster: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE    VERSION
ctrl-plane-0   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-1   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-2   Ready    control-plane,master   5d8h   v1.29.8+f10c92d
worker-0       Ready    mcp-1,worker           5d8h   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           5d8h   v1.27.15+6147456
```


  3. Confirm the `MachineConfigPool` groups that are paused: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   true
mcp-2   true
```


Note

Each `MachineConfigPool` can be unpaused independently. Therefore, if a maintenance window runs out of time other MCPs do not need to be unpaused immediately. The cluster is supported to run with some worker nodes still at <y-2>-release version. 

  4. Unpause the required `mcp` group to begin the upgrade: 

```shell-session
$ oc patch mcp/mcp-1 --type merge --patch '{"spec":{"paused":false}}'
```


**Example output**

```shell-session
machineconfigpool.machineconfiguration.openshift.io/mcp-1 patched
```


  5. Confirm that the required `mcp` group is unpaused: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   false
mcp-2   true
```


  6. As each `mcp` group is upgraded, continue to unpause and upgrade the remaining nodes. 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS                        ROLES                  AGE    VERSION
ctrl-plane-0   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-1   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
ctrl-plane-2   Ready                         control-plane,master   5d8h   v1.29.8+f10c92d
worker-0       Ready                         mcp-1,worker           5d8h   v1.29.8+f10c92d
worker-1       NotReady,SchedulingDisabled   mcp-2,worker           5d8h   v1.27.15+6147456
```


### 13.2.8.3. Verifying the health of the newly updated cluster

After updating the cluster, verify that the cluster is back up and running. 

**Procedure**

  1. Check the cluster version by running the following command: 

```shell-session
$ oc get clusterversion
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.16.14   True        False         4h38m   Cluster version is 4.16.14
```


This should return the new cluster version and the `PROGRESSING` column should return `False`. 

  2. Check that all nodes are ready: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME           STATUS   ROLES                  AGE    VERSION
ctrl-plane-0   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
ctrl-plane-1   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
ctrl-plane-2   Ready    control-plane,master   5d9h   v1.29.8+f10c92d
worker-0       Ready    mcp-1,worker           5d9h   v1.29.8+f10c92d
worker-1       Ready    mcp-2,worker           5d9h   v1.29.8+f10c92d
```


All nodes in the cluster should be in a `Ready` status and running the same version. 

  3. Check that there are no paused `mcp` resources in the cluster: 

```shell-session
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
```


**Example output**

```shell-session
MCP     Paused
---     ------
master  false
mcp-1   false
mcp-2   false
```


  4. Check that all cluster Operators are available: 

```shell-session
$ oc get co
```


**Example output**

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.16.14   True        False         False      5d9h
baremetal                                  4.16.14   True        False         False      5d9h
cloud-controller-manager                   4.16.14   True        False         False      5d10h
cloud-credential                           4.16.14   True        False         False      5d10h
cluster-autoscaler                         4.16.14   True        False         False      5d9h
config-operator                            4.16.14   True        False         False      5d9h
console                                    4.16.14   True        False         False      5d9h
control-plane-machine-set                  4.16.14   True        False         False      5d9h
csi-snapshot-controller                    4.16.14   True        False         False      5d9h
dns                                        4.16.14   True        False         False      5d9h
etcd                                       4.16.14   True        False         False      5d9h
image-registry                             4.16.14   True        False         False      85m
ingress                                    4.16.14   True        False         False      5d9h
insights                                   4.16.14   True        False         False      5d9h
kube-apiserver                             4.16.14   True        False         False      5d9h
kube-controller-manager                    4.16.14   True        False         False      5d9h
kube-scheduler                             4.16.14   True        False         False      5d9h
kube-storage-version-migrator              4.16.14   True        False         False      4h48m
machine-api                                4.16.14   True        False         False      5d9h
machine-approver                           4.16.14   True        False         False      5d9h
machine-config                             4.16.14   True        False         False      5d9h
marketplace                                4.16.14   True        False         False      5d9h
monitoring                                 4.16.14   True        False         False      5d9h
network                                    4.16.14   True        False         False      5d9h
node-tuning                                4.16.14   True        False         False      5d7h
openshift-apiserver                        4.16.14   True        False         False      5d9h
openshift-controller-manager               4.16.14   True        False         False      5d9h
openshift-samples                          4.16.14   True        False         False      5h24m
operator-lifecycle-manager                 4.16.14   True        False         False      5d9h
operator-lifecycle-manager-catalog         4.16.14   True        False         False      5d9h
operator-lifecycle-manager-packageserver   4.16.14   True        False         False      5d9h
service-ca                                 4.16.14   True        False         False      5d9h
storage                                    4.16.14   True        False         False      5d9h
```


All cluster Operators should report `True` in the `AVAILABLE` column. 

  5. Check that all pods are healthy: 

```shell-session
$ oc get po -A | grep -E -iv 'complete|running'
```


This should not return any pods. 

Note

You might see a few pods still moving after the update. Watch this for a while to make sure all pods are cleared.
