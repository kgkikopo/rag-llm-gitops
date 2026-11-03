# 12.3. Windows node access methods

You cannot use the `oc debug node` command to access Windows nodes because it requires running a privileged pod, which Windows does not support. Instead, access a Windows node by using secure shell (SSH) or Remote Desktop Protocol (RDP) through an SSH bastion. 

## 12.3.1. Access a Windows node by using SSH

You can access a Windows node by using a secure shell (SSH). 

**Prerequisites**

  * You have installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM). 
  * You have created a Windows compute machine set. 
  * You have added the key used in the `cloud-private-key` secret and the key used when creating the cluster to the ssh-agent. For security reasons, remember to remove the keys from the ssh-agent after use. 
  * You have connected to the Windows node [using an `ssh-bastion` pod](https://access.redhat.com/solutions/4073041). 



**Procedure**

  * Access the Windows node by running the following command: 

```shell-session
$ ssh -t -o StrictHostKeyChecking=no -o ProxyCommand='ssh -A -o StrictHostKeyChecking=no \
    -o ServerAliveInterval=30 -W %h:%p core@$(oc get service --all-namespaces -l run=ssh-bastion \
    -o go-template="{{ with (index (index .items 0).status.loadBalancer.ingress 0) }}{{ or .hostname .ip }}{{end}}")' <username>@<windows_node_internal_ip>
```


where: 

`<username>`
     Specifies the cloud provider username, such as `Administrator` for Amazon Web Services (AWS) or `capi` for Microsoft Azure. 
`<windows_node_internal_ip>`
    

Specifies the internal IP address of the node, which can be discovered by running the following command: 

```shell-session
$ oc get nodes <node_name> -o jsonpath={.status.addresses[?\(@.type==\"InternalIP\"\)].address}
```


## 12.3.2. Access a Windows node by using RDP

You can access a Windows node by using a Remote Desktop Protocol (RDP). 

**Prerequisites**

  * You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM). 
  * You have created a Windows compute machine set. 
  * You have added the key used in the `cloud-private-key` secret and the key used when creating the cluster to the ssh-agent. For security reasons, remember to remove the keys from the ssh-agent after use. 
  * You have connected to the Windows node [using an `ssh-bastion` pod](https://access.redhat.com/solutions/4073041). 



**Procedure**

  1. Run the following command to set up an SSH tunnel: 

```shell-session
$ ssh -L 2020:<windows_node_internal_ip>:3389 \
    core@$(oc get service --all-namespaces -l run=ssh-bastion -o go-template="{{ with (index (index .items 0).status.loadBalancer.ingress 0) }}{{ or .hostname .ip }}{{end}}")
```


where: 

`<windows_node_internal_ip>`
    

Specifies the internal IP address of the node, which can be discovered by running the following command: 

```shell-session
$ oc get nodes <node_name> -o jsonpath={.status.addresses[?\(@.type==\"InternalIP\"\)].address}
```


  2. From within the resulting shell, SSH into the Windows node and run the following command to create a password for the user: 

```shell-session
C:\> net user <username> *
```


Specify the cloud provider user name, such as `Administrator` for AWS or `capi` for Azure. You can now remotely access the Windows node at `localhost:2020` using an RDP client.
