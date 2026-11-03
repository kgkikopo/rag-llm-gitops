# 5.12. Verifying cluster status

You can verify your OpenShift Container Platform cluster’s status during or after installation. 

**Procedure**

  1. In the cluster environment, export the administrator’s kubeconfig file by entering the following command: 

```shell-session
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
```


     * For `<installation_directory>`, specify the path to the directory that you stored the installation files in. 

The `kubeconfig` file contains information about the cluster that is used by the CLI to connect a client to the correct cluster and API server. 

  2. View the control plane and compute machines created after a deployment by entering the following command: 

```shell-session
$ oc get nodes
```


  3. View the version of your cluster by entering the following command: 

```shell-session
$ oc get clusterversion
```


  4. View the status of the cluster Operators by entering the following command: 

```shell-session
$ oc get clusteroperator
```


  5. View all running pods in the cluster by entering the following command: 

```shell-session
$ oc get pods -A
```
