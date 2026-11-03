# 15.2. Gathering OpenShift Container Platform data for a hosted cluster

You can gather OpenShift Container Platform debugging information for a hosted cluster by using the multicluster engine Operator web console or by using the CLI. 

## 15.2.1. Gathering data for a hosted cluster by using the CLI

You can gather OpenShift Container Platform debugging information for a hosted cluster by using the command-line interface (CLI). 

**Prerequisites**

  * You must have `cluster-admin` access to the management cluster. 
  * You need the `name` value for the `HostedCluster` resource and the namespace where the CR is deployed. 
  * You must have the `hcp` command-line interface installed. For more information, see "Installing the hosted control planes command-line interface". 
  * You must have the OpenShift CLI (`oc`) installed. 
  * You must ensure that the `kubeconfig` file is loaded and is pointing to the management cluster. 



**Procedure**

  1. Generate the `kubeconfig` file by entering the following command: 

```shell-session
$ hcp create kubeconfig --namespace <hosted_cluster_namespace> \
  --name <hosted_cluster_name> > <hosted_cluster_name>.kubeconfig
```


  2. After you save the `kubeconfig` file, you can access the hosted cluster by entering the following example command: 

```shell-session
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
```


  3. Collect the must-gather information by entering the following command: 

```shell-session
$ oc adm must-gather
```


## 15.2.2. Gathering data for a hosted cluster by using the web console

You can gather OpenShift Container Platform debugging information for a hosted cluster by using the multicluster engine Operator web console. 

**Prerequisites**

  * You must have `cluster-admin` access to the management cluster. 
  * You need the `name` value for the `HostedCluster` resource and the namespace where the CR is deployed. 
  * You must have the `hcp` command-line interface installed. For more information, see "Installing the hosted control planes command-line interface". 
  * You must have the OpenShift CLI (`oc`) installed. 
  * You must ensure that the `kubeconfig` file is loaded and is pointing to the management cluster. 



**Procedure**

  1. In the web console, select **All Clusters** and select the cluster you want to troubleshoot. 
  2. In the upper-right corner, select **Download kubeconfig**. 
  3. Export the downloaded `kubeconfig` file. 
  4. Collect the must-gather information by entering the following command: 

```shell-session
$ oc adm must-gather
```
