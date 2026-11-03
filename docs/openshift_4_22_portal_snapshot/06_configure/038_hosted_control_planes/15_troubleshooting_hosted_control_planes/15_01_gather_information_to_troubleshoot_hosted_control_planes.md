# 15.1. Gather information to troubleshoot hosted control planes

When you need to troubleshoot an issue with hosted clusters, you can gather information by running the `must-gather` command. The command generates output for the management cluster and the hosted cluster. 

The output for the management cluster contains the following content: 

  * **Cluster-scoped resources:** These resources are node definitions of the management cluster. 
  * **The`hypershift-dump` compressed file:** This file is useful if you need to share the content with other people. 
  * **Namespaced resources:** These resources include all of the objects from the relevant namespaces, such as config maps, services, events, and logs. 
  * **Network logs:** These logs include the OVN northbound and southbound databases and the status for each one. 
  * **Hosted clusters:** This level of output involves all of the resources inside of the hosted cluster. 



The output for the hosted cluster contains the following content: 

  * **Cluster-scoped resources:** These resources include all of the cluster-wide objects, such as nodes and CRDs. 
  * **Namespaced resources:** These resources include all of the objects from the relevant namespaces, such as config maps, services, events, and logs. 



Although the output does not contain any secret objects from the cluster, it can contain references to the names of secrets. 

**Prerequisites**

  * You must have `cluster-admin` access to the management cluster. 
  * You need the `name` value for the `HostedCluster` resource and the namespace where the CR is deployed. 
  * You must have the `hcp` command-line interface installed. For more information, see "Installing the hosted control planes command-line interface". 
  * You must have the OpenShift CLI (`oc`) installed. 
  * You must ensure that the `kubeconfig` file is loaded and is pointing to the management cluster. 



**Procedure**

  * To gather the output for troubleshooting, enter the following command: 

```shell-session
$ oc adm must-gather \
  --image=registry.redhat.io/rhacm2/acm-must-gather-rhel9:v2.17 \
  /usr/bin/gather hosted-cluster-namespace=HOSTEDCLUSTERNAMESPACE \
  hosted-cluster-name=HOSTEDCLUSTERNAME \
  --dest-dir=NAME ; tar -cvzf NAME.tgz NAME
```


where: 

    * The `hosted-cluster-namespace=HOSTEDCLUSTERNAMESPACE` parameter is optional. If you do not include it, the command runs as though the hosted cluster is in the default namespace, which is `clusters`. 
    * If you want to save the results of the command to a compressed file, specify the `--dest-dir=NAME` parameter and replace `NAME` with the name of the directory where you want to save the results. 




**Additional resources**

  * [Installing the hosted control planes command-line interface](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/preparing-to-deploy-hosted-control-planes#hcp-cli "3.4. Installing the hosted control planes command-line interface")
