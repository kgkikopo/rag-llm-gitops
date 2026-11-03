# 11.2. Removing a cluster from RHOSP that uses your own infrastructure

You can remove an OpenShift Container Platform cluster on Red Hat OpenStack Platform (RHOSP) that uses your own infrastructure. To complete the removal process quickly, run several Ansible playbooks. 

**Prerequisites**

  * Python 3 is installed on your machine. 
  * You downloaded the modules in "Downloading playbook dependencies." 
  * You have the playbooks that you used to install the cluster. 
  * You modified the playbooks that are prefixed with `down-` to reflect any changes that you made to their corresponding installation playbooks. For example, changes to the `bootstrap.yaml` file are reflected in the `down-bootstrap.yaml` file. 
  * All of the playbooks are in a common directory. 



**Procedure**

  1. On a command line, run the playbooks that you downloaded by entering the following command: 

```shell-session
$ ansible-playbook -i inventory.yaml  \
	down-bootstrap.yaml      \
	down-control-plane.yaml  \
	down-compute-nodes.yaml  \
	down-load-balancers.yaml \
	down-network.yaml        \
	down-security-groups.yaml
```


  2. Remove any DNS record changes you made for the OpenShift Container Platform installation. 

OpenShift Container Platform is removed from your infrastructure.
