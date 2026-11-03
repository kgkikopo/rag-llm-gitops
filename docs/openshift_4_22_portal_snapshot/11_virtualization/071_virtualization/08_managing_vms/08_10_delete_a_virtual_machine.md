# 8.10. Delete a virtual machine

You can remove virtual machines (VMs) from your cluster to free up resources using either the web console or CLI. Deleting a VM removes the virtual machine definition and optionally its associated storage resources. 

## 8.10.1. Delete a VM by using the web console

You can permanently remove a virtual machine (VM) from the cluster by using the OpenShift Container Platform web console. The **Delete** action is disabled while the VM is delete protected. 

**Prerequisites**

  * You have disabled the VM’s delete protection setting. 
  * You have stopped the VM. 



**Procedure**

  1. From the OpenShift Container Platform web console, choose your view: 

     * For a virtualization-focused view, select **Administrator** **Virtualization** **VirtualMachines**. 
     * For a general view, navigate to **Virtualization** **VirtualMachines**. 

  2. Click the **Options** menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) beside a VM and select **Delete**. 

Alternatively, click the VM’s name to open the **VirtualMachine details** page and click **Actions** **Delete**. 

You can also right-click the VM in the tree view and select **Delete** from the pop-up menu. 

  3. Optional: Select **With grace period** or clear **Delete disks**. 
  4. Click **Delete** to permanently delete the VM. 



## 8.10.2. Delete a VM by using the CLI

You can delete a virtual machine (VM) by using the OpenShift CLI (`oc`). The command deletes a VM in the current project unless you specify another namespace. 

**Prerequisites**

  * You have disabled the VM’s delete protection setting. 
  * You have stopped the VM. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * Delete the VM by running the following command: 

```shell-session
$ oc delete vm <vm_name>
```


Note

This command only deletes a VM in the current project. Specify the `-n <project_name>` option if the VM you want to delete is in a different project or namespace.
