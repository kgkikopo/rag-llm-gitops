# 5.7. Rebooting a node gracefully

You can perform a graceful restart of a node, where all workloads are moved to other nodes, without data loss or service disruption. 

The Windows Machine Config Operator (WMCO) minimizes node reboots whenever possible. However, certain operations and updates require a reboot to ensure that changes are applied correctly and securely. To safely reboot your Windows nodes, use the graceful reboot process. For information on gracefully rebooting a standard OpenShift Container Platform node, see "Rebooting a node gracefully" in the Nodes documentation. 

Before rebooting a node, it is recommended to backup etcd data to avoid any data loss on the node. 

Note

For single-node OpenShift clusters that require users to perform the `oc login` command rather than having the certificates in `kubeconfig` file to manage the cluster, the `oc adm` commands might not be available after cordoning and draining the node. This is because the `openshift-oauth-apiserver` pod is not running due to the cordon. You can use SSH to access the nodes as indicated in the following procedure. 

In a single-node OpenShift cluster, pods cannot be rescheduled when cordoning and draining. However, doing so gives the pods, especially your workload pods, time to properly stop and release associated resources. 

The following procedure demonstrates how to perform a graceful restart of a node. 

**Procedure**

  1. Mark the node as unschedulable: 

```shell-session
$ oc adm cordon <node1>
```


  2. Drain the node to remove all the running pods: 

```shell-session
$ oc adm drain <node1> --ignore-daemonsets --delete-emptydir-data --force
```


You might receive errors that pods associated with custom pod disruption budgets (PDB) cannot be evicted. 

**Example error**

```shell-session
error when evicting pods/"rails-postgresql-example-1-72v2w" -n "rails" (will retry after 5s): Cannot evict pod as it would violate the pod's disruption budget.
```


In this case, run the drain command again, adding the `disable-eviction` flag, which bypasses the PDB checks: 

```shell-session
$ oc adm drain <node1> --ignore-daemonsets --delete-emptydir-data --force --disable-eviction
```


  3. SSH into the Windows node and enter PowerShell by running the following command: 

```shell-session
C:\> powershell
```


  4. Restart the node by running the following command: 

```shell-session
C:\>  Restart-Computer -Force
```


  5. Windows nodes on Amazon Web Services (AWS) do not return to `READY` state after a graceful reboot due to an inconsistency with the EC2 instance metadata routes and the Host Network Service (HNS) networks. 

After the reboot, SSH into any Windows node on AWS and add the route by running the following command in a shell prompt: 

```shell-session
C:\> route add 169.254.169.254 mask 255.255.255.0 <gateway_ip>
```


where: 

`169.254.169.254`
     Specifies the address of the EC2 instance metadata endpoint. 
`255.255.255.255`
     Specifies the network mask of the EC2 instance metadata endpoint. 
`<gateway_ip>`
    

Specifies the corresponding IP address of the gateway in the Windows instance, which you can find by running the following command: 

```shell-session
C:\> ipconfig | findstr /C:"Default Gateway"
```


  6. After the reboot is complete, mark the node as schedulable by running the following command: 

```shell-session
$ oc adm uncordon <node1>
```


  7. Verify that the node is ready: 

```shell-session
$ oc get node <node1>
```


**Example output**

```shell-session
NAME    STATUS  ROLES    AGE     VERSION
<node1> Ready   worker   6d22h   v1.18.3+b0068a8
```
