# 4.11. Creating network resources on RHOSP

Create the network resources that an OpenShift Container Platform on Red Hat OpenStack Platform (RHOSP) installation on your own infrastructure requires. To save time, run supplied Ansible playbooks that generate security groups, networks, subnets, routers, and ports. 

**Prerequisites**

  * You downloaded the modules in "Downloading playbook dependencies". 
  * You downloaded the playbooks in "Downloading the installation playbooks". 



**Procedure**

  1. For a dual stack cluster deployment, edit the `inventory.yaml` file and uncomment the `os_subnet6` attribute. 
  2. To ensure that your network resources have unique names on the RHOSP deployment, create an environment variable and JSON file for use in the Ansible playbooks: 

     1. Create an environment variable that has a unique name value by running the following command: 

```shell-session
$ export OS_NET_ID="openshift-$(dd if=/dev/urandom count=4 bs=1 2>/dev/null |hexdump -e '"%02x"')"
```


     2. Verify that the variable is set by running the following command on a command line: 

```shell-session
$ echo $OS_NET_ID
```


     3. Create a JSON object that includes the variable in a file called `netid.json` by running the following command: 

```shell-session
$ echo "{\"os_net_id\": \"$OS_NET_ID\"}" | tee netid.json
```


  3. On a command line, create the network resources by running the following command: 

```shell-session
$ ansible-playbook -i inventory.yaml network.yaml
```


Note

The API and Ingress VIP fields will be overwritten in the `inventory.yaml` playbook with the IP addresses assigned to the network ports. 

Note

The resources created by the `network.yaml` playbook are deleted by the `down-network.yaml` playbook.
