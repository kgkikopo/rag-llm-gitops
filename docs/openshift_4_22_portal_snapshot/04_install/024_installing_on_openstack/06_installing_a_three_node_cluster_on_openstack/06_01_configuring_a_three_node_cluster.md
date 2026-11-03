# 6.1. Configuring a three-node cluster

To configure a three-node cluster, set the number of worker nodes to `0` in the `install-config.yaml` file before you deploy the cluster. 

Setting the number of worker nodes to `0` ensures that the control plane machines are schedulable. This allows application workloads to be scheduled to run from the control plane nodes. 

Note

Because application workloads run from control plane nodes, additional subscriptions are required, as the control plane nodes are considered to be compute nodes. 

**Prerequisites**

  * You have an existing `install-config.yaml` file. 



**Procedure**

  * Set the number of compute replicas to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza: 

**Example`install-config.yaml` file for a three-node cluster**

```yaml
apiVersion: v1
baseDomain: example.com
compute:
- name: worker
  platform: {}
  replicas: 0
# ...
```
