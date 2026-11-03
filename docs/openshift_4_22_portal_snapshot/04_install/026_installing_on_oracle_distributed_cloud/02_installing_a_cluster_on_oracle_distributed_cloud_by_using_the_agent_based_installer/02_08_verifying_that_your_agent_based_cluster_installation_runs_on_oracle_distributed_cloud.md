# 2.8. Verifying that your Agent-based cluster installation runs on Oracle Distributed Cloud

Verify that your cluster was installed and is running effectively on Oracle® Distributed Cloud. 

**Prerequisites**

  * You created all the required OCI resources and services. See the "Creating Oracle Distributed Cloud infrastructure resources and services" section. 
  * You created `install-config.yaml` and `agent-config.yaml` configuration files. See the "Creating configuration files for installing a cluster on Oracle Distributed Cloud" section. 
  * You uploaded the agent ISO image to a default Oracle Object Storage bucket, and you created a compute instance on Oracle Distributed Cloud. For more information, see "Running a cluster on Oracle Distributed Cloud". 



**Procedure**

  * After you deploy the compute instance on a self-managed node in your OpenShift Container Platform cluster, monitor the cluster’s status by choosing one of the following options: 

    * From the OpenShift Container Platform CLI, enter the following command: 

```shell-session
$ ./openshift-install agent wait-for install-complete --log-level debug
```


Check the status of the `rendezvous` host node that runs the bootstrap node. After the host reboots, the host forms part of the cluster. 

    * Use the `kubeconfig` API to check the status of various OpenShift Container Platform components. For the `KUBECONFIG` environment variable, set the relative path of the cluster’s `kubeconfig` configuration file: 

```shell-session
$  export KUBECONFIG=~/auth/kubeconfig
```


Check the status of each of the cluster’s self-managed nodes. CCM applies a label to each node to designate the node as running in a cluster on OCI. 

```shell-session
$ oc get nodes -A
```


**Output example**

```shell-session
NAME                                   STATUS ROLES                 AGE VERSION
main-0.private.agenttest.oraclevcn.com Ready  control-plane, master 7m  v1.27.4+6eeca63
main-1.private.agenttest.oraclevcn.com Ready  control-plane, master 15m v1.27.4+d7fa83f
main-2.private.agenttest.oraclevcn.com Ready  control-plane, master 15m v1.27.4+d7fa83f
```


Check the status of each of the cluster’s Operators, with the CCM Operator status being a good indicator that your cluster is running. 

```shell-session
$ oc get co
```


**Truncated output example**

```shell-session
NAME           VERSION     AVAILABLE  PROGRESSING    DEGRADED   SINCE   MESSAGE
authentication 4.22.0-0    True       False          False      6m18s
baremetal      4.22.0-0    True       False          False      2m42s
network        4.22.0-0    True       True           False      5m58s  Progressing: …
    …
```
