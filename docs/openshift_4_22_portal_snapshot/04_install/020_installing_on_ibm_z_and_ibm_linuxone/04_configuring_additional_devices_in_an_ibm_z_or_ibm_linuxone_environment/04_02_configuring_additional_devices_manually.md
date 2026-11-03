# 4.2. Configuring additional devices manually

After installation, you can manually configure additional devices on IBM Z® or IBM® LinuxONE nodes. This configuration persists across node restarts, but you must redo the steps if you replace the node. 

**Prerequisites**

  * You are logged in to the cluster as a user with administrative privileges. 
  * The device must be available to the node. 
  * In a z/VM environment, the device must be attached to the z/VM guest. 



**Procedure**

  1. Connect to the node via SSH by running the following command: 

```shell-session
$ ssh <user>@<node_ip_address>
```


You can also start a debug session to the node by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  2. To enable the devices with the `chzdev` command, enter the following command: 

```shell-session
$ sudo chzdev -e <device>
```


**Additional resources**

  * [chzdev - Configure IBM Z® devices (IBM® Documentation)](https://www.ibm.com/docs/en/linux-on-systems?topic=commands-chzdev)
  * [Persistent device configuration (IBM® Documentation)](https://www.ibm.com/docs/en/linux-on-systems?topic=linuxonibm/com.ibm.linux.z.ludd/ludd_c_perscfg.html)
