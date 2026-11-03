# 4.21. Creating compute machines on RHOSP

After standing up the control plane, create compute machines. Red Hat provides an Ansible playbook that you run to simplify this process. 

**Prerequisites**

  * You downloaded the modules in "Downloading playbook dependencies". 
  * You downloaded the playbooks in "Downloading the installation playbooks". 
  * The `inventory.yaml`, `common.yaml`, and `compute-nodes.yaml` Ansible playbooks are in a common directory. 
  * The `metadata.json` file that the installation program created is in the same directory as the Ansible playbooks. 
  * The control plane is active. 



**Procedure**

  1. On a command line, change the working directory to the location of the playbooks. 
  2. On a command line, run the playbook: 

```shell-session
$ ansible-playbook -i inventory.yaml compute-nodes.yaml
```


**Next steps**

  * Approve the certificate signing requests for the machines.
