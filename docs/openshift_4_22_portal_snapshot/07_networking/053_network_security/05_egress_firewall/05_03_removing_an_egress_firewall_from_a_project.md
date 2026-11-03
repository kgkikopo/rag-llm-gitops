# 5.3. Removing an egress firewall from a project

As a cluster administrator, you can remove an egress firewall from a project to remove all restrictions on network traffic from the project that leaves the OpenShift Container Platform cluster. 

## 5.3.1. Remove an EgressFirewall CR

As a cluster administrator, you can remove an egress firewall from a project. 

**Prerequisites**

  * A cluster using the OVN-Kubernetes network plugin. 
  * Install the OpenShift CLI (`oc`). 
  * You must log in to the cluster as a cluster administrator. 



**Procedure**

  1. Find the name of the `EgressFirewall` CR for the project. Replace `<project>` with the name of the project. 

```shell-session
$ oc get egressfirewall -n <project>
```


  2. Delete the `EgressFirewall` CR by entering the following command. Replace `<project>` with the name of the project and `<name>` with the name of the object. 

```shell-session
$ oc delete -n <project> egressfirewall <name>
```
