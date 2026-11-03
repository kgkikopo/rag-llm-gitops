# 3.1. Expand the cluster network IP address range

To expand the cluster network IP address range in OpenShift Container Platform to support more nodes, you can modify the cluster network CIDR mask using the `oc patch` command. 

Note

This change requires rolling out a new Operator configuration across the cluster, and can take up to 30 minutes to take effect. 

For clusters configured with cluster proxy, expanding the cluster network range also triggers a MachineConfigPool update that reboots all nodes. Plan this operation during a maintenance window to avoid service disruption. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the cluster with a user with `cluster-admin` privileges. 
  * You have ensured that the cluster uses the OVN-Kubernetes network plugin. 



**Procedure**

  1. To obtain the cluster network range and host prefix for your cluster, enter the following command: 

```shell-session
$ oc get network.operator.openshift.io \
  -o jsonpath="{.items[0].spec.clusterNetwork}"
```


**Example output**

```plaintext
[{"cidr":"10.217.0.0/22","hostPrefix":23}]
```


  2. To expand the cluster network IP address range, enter the following command. Use the CIDR IP address range and host prefix returned from the output of the previous command. 

```shell-session
$ oc patch Network.config.openshift.io cluster --type='merge' --patch \
  '{
    "spec":{
      "clusterNetwork": [ {"cidr":"<network>/<cidr>","hostPrefix":<prefix>} ],
      "networkType": "OVNKubernetes"
    }
  }'
```


where: 

`<network>`
     Specifies the network part of the `cidr` field that you obtained from the previous step. You cannot change this value. 
`<cidr>`
     Specifies the network prefix length. For example, `14`. Change this value to a smaller number than the value from the output in the previous step to expand the cluster network range. 
`<prefix>`
     Specifies the current host prefix for your cluster. This value must be the same value for the `hostPrefix` field that you obtained from the previous step. 

**Example command**

```shell-session
$ oc patch Network.config.openshift.io cluster --type='merge' --patch \
  '{
    "spec":{
      "clusterNetwork": [ {"cidr":"10.217.0.0/14","hostPrefix": 23} ],
      "networkType": "OVNKubernetes"
    }
  }'
```


**Example output**

```plaintext
network.config.openshift.io/cluster patched
```


  3. To confirm that the configuration is active, enter the following command. It can take up to 30 minutes for this change to take effect. 

```shell-session
$ oc get network.operator.openshift.io \
  -o jsonpath="{.items[0].spec.clusterNetwork}"
```


**Example output**

```plaintext
[{"cidr":"10.217.0.0/14","hostPrefix":23}]
```
