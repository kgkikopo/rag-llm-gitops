# 8.14. Control virtual machine states

You can use `virtctl` to manage virtual machine states and perform other actions from the CLI. For example, you can use `virtctl` to force stop a VM or expose a port. 

You can stop, start, restart, reset, pause, and unpause virtual machines from the web console. 

## 8.14.1. Configure RBAC permissions for managing VM states

You can grant users permission to start and stop virtual machines (VMs) from the OpenShift Container Platform web console. Create a role-based access control (RBAC) cluster role and a cluster role binding to apply the permission. 

**Prerequisites**

  * You have cluster administrator access to an OpenShift Container Platform cluster where OpenShift Virtualization is installed. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `ClusterRole` object that allows the target user or group to manage VM states: 

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: vm-manager-access
rules:
  - apiGroups:
      - subresources.kubevirt.io
    resources:
      - virtualmachines/start
      - virtualmachines/stop
    verbs:
      - update
# ...
```


  2. Run the following command to apply the cluster role: 

```shell-session
$ oc apply -f <filename>.yaml
```


  3. Confirm that the cluster role was created by running the following command and observing the output: 

```shell-session
$ oc get clusterrole <name>
```


Example output: 

```shell-session
NAME                AGE
vm-manager-access   15s
```


  4. Inspect the details of the cluster role, and ensure the intended rules for `subresources.kubevirt.io` are present, specifically the `virtualmachines/start` and `virtualmachines/stop` subresources. 

Run the following command and observe the output: 

```shell-session
$ oc describe clusterrole <name>
```


Example output: 

```shell-session
Name:         vm-manager-access
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  ---------  -----------------  --------------  -----
  virtualmachines/start, virtualmachines/stop with subresources.kubevirt.io group  []  []  [update]
```


  5. Create a `ClusterRoleBinding` object to bind the cluster role you have created to the target user or group: 

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: vm-manager-access-binding
subjects:
  - kind: User
    name: test-user
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: vm-manager-access
  apiGroup: rbac.authorization.k8s.io
```


  6. Run the following command to apply the cluster role binding: 

```shell-session
$ oc apply -f <filename>.yaml
```


  7. Confirm that the cluster role binding was created by running the following command and observing the output: 

```shell-session
$ oc get clusterrolebinding <name>
```


Example output: 

```shell-session
NAME                        AGE
vm-manager-access-binding   15s
```


**Verification**

  1. Check if the user can start a VM by running the following command: 

```shell-session
$ oc auth can-i update virtualmachines/start --namespace=<namespace> --as=<user_name> --subresource=subresources.kubevirt.io
```


Example output: 

```shell-session
yes
```


  2. Check if the user can stop a VM by running the following command: 

```shell-session
$ oc auth can-i update virtualmachines/stop --namespace=<namespace> --as=<user_name> --group=subresources.kubevirt.io
```


Example output: 

```shell-session
yes
```


## 8.14.2. Enable confirmations of VM actions

You can require a confirmation dialog before the **Stop** , **Restart** , and **Pause** actions run on a virtual machine (VM). Confirmation is disabled by default. 

**Procedure**

  1. Click **Virtualization** **Settings** **Cluster** **General settings**. 
  2. Click **VirtualMachine actions confirmation**. 
  3. Toggle the **VirtualMachine actions confirmation** setting to **On**. 



## 8.14.3. Start a VM

You can start a virtual machine (VM) from the **VirtualMachines** page, the tree view, or the **VirtualMachine details** page of the OpenShift Container Platform web console. 

**Procedure**

  1. Click **Virtualization** **VirtualMachines** from the side menu. 
  2. In the tree view, select the project that contains the VM that you want to start. 
  3. Navigate to the appropriate menu for your use case: 

     * To stay on this page, where you can perform actions on multiple VMs: 

       1. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) located at the far right end of the row and click **Control** **Start VirtualMachine**. 

     * To start the VM from the tree view: 

       1. Click the **>** icon next to the project name to open the list of VMs. 
       2. Right-click the name of the VM and select **Control** **Start**. 

     * To view comprehensive information about the selected VM before you start it: 

       1. Access the **VirtualMachine details** page by clicking the name of the VM. 
       2. Click **Actions** **Control** **Start**. 

Note

When you start VM that is provisioned from a `URL` source for the first time, the VM has a status of **Importing** while OpenShift Virtualization imports the container from the URL endpoint. Depending on the size of the image, this process might take several minutes. 




## 8.14.4. Stop a VM

You can stop a virtual machine (VM) from the **VirtualMachines** page, the tree view, or the **VirtualMachine details** page of the OpenShift Container Platform web console. 

**Procedure**

  1. Click **Virtualization** **VirtualMachines** from the side menu. 
  2. In the tree view, select the project that contains the VM that you want to stop. 
  3. Navigate to the appropriate menu for your use case: 

     * To stay on this page, where you can perform actions on multiple VMs: 

       1. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) located at the far right end of the row and click **Control** **Stop VirtualMachine**. 
       2. If action confirmation is enabled, click **Stop** in the confirmation dialog. 

     * To stop the VM from the tree view: 

       1. Click the **>** icon next to the project name to open the list of VMs. 
       2. Right-click the name of the VM and select **Control** **Stop**. 
       3. If action confirmation is enabled, click **Stop** in the confirmation dialog. 

     * To view comprehensive information about the selected VM before you stop it: 

       1. Access the **VirtualMachine details** page by clicking the name of the VM. 
       2. Click **Actions** **Control** **Stop**. 
       3. If action confirmation is enabled, click **Stop** in the confirmation dialog. 




## 8.14.5. Restart a VM

You can restart a running virtual machine (VM) from the OpenShift Container Platform web console. The **Restart** action shuts down the VM and starts a new pod for it. 

Important

The **Restart** action shuts down the VM and starts a new pod. This action removes all related resources including the `virt-launcher` pod and recreates them. 

To avoid errors, do not restart a VM while it has a status of **Importing**. 

**Procedure**

  1. Click **Virtualization** **VirtualMachines** from the side menu. 
  2. In the tree view, select the project that contains the VM that you want to restart. 
  3. Navigate to the appropriate menu for your use case: 

     * To stay on this page, where you can perform actions on multiple VMs: 

       1. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) located at the far right end of the row and click **Control** **Restart**. 
       2. If action confirmation is enabled, click **Restart** in the confirmation dialog. 

     * To restart the VM from the tree view: 

       1. Click the **>** icon next to the project name to open the list of VMs. 
       2. Right-click the name of the VM and select **Control** **Restart**. 
       3. If action confirmation is enabled, click **Restart** in the confirmation dialog. 

     * To view comprehensive information about the selected VM before you restart it: 

       1. Access the **VirtualMachine details** page by clicking the name of the virtual machine. 
       2. Click **Actions** **Restart**. 
       3. If action confirmation is enabled, click **Restart** in the confirmation dialog. 




## 8.14.6. Reset a VM

You can reset a virtual machine (VM) from the OpenShift Container Platform web console when the VM is unresponsive or has failed to boot. Unlike **Restart** , the **Reset** action keeps the existing pod and hard resets the VM inside it. 

**Procedure**

  1. Click **Virtualization** **VirtualMachines** from the side menu. 
  2. In the tree view, select the project that contains the VM that you want to restart. 
  3. Navigate to the appropriate menu for your use case: 

     * To stay on this page, where you can perform actions on multiple VMs: 

       1. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) located at the far right end of the row and click **Control** **Reset**. 
       2. If action confirmation is enabled, click **Reset** in the confirmation dialog. 

     * To reset the VM from the tree view: 

       1. Click the **>** icon next to the project name to open the list of VMs. 
       2. Right-click the name of the VM and select **Control** **Reset**. 
       3. If action confirmation is enabled, click **Reset** in the confirmation dialog. 

     * To view comprehensive information about the selected VM before you reset it: 

       1. Access the **VirtualMachine details** page by clicking the name of the virtual machine. 
       2. Click **Actions** **Control** **Reset**. 
       3. If action confirmation is enabled, click **Reset** in the confirmation dialog. 




## 8.14.7. Pause a VM

You can pause a virtual machine (VM) from the **VirtualMachines** page, the tree view, or the **VirtualMachine details** page of the OpenShift Container Platform web console. 

**Procedure**

  1. Click **Virtualization** **VirtualMachines** from the side menu. 
  2. In the tree view, select the project that contains the VM that you want to pause. 
  3. Navigate to the appropriate menu for your use case: 

     * To stay on this page, where you can perform actions on multiple VMs: 

       1. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) located at the far right end of the row and click **Control** **Pause VirtualMachine**. 
       2. If action confirmation is enabled, click **Pause** in the confirmation dialog. 

     * To pause the VM from the tree view: 

       1. Click the **>** icon next to the project name to open the list of VMs. 
       2. Right-click the name of the VM and select **Control** **Pause**. 
       3. If action confirmation is enabled, click **Pause** in the confirmation dialog. 

     * To view comprehensive information about the selected VM before you pause it: 

       1. Access the **VirtualMachine details** page by clicking the name of the VM. 
       2. Click **Actions** **Control** **Pause**. 
       3. If action confirmation is enabled, click **Pause** in the confirmation dialog. 




## 8.14.8. Unpause a VM

You can unpause a paused virtual machine (VM) from the **VirtualMachines** page, the tree view, or the **VirtualMachine details** page of the OpenShift Container Platform web console. 

**Prerequisites**

  * At least one of your VMs must have a status of **Paused**. 



**Procedure**

  1. Click **Virtualization** **VirtualMachines** from the side menu. 
  2. In the tree view, select the project that contains the VM that you want to unpause. 
  3. Navigate to the appropriate menu for your use case: 

     * To stay on this page, where you can perform actions on multiple VMs: 

       1. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) located at the far right end of the row and click **Control** **Unpause VirtualMachine**. 

     * To unpause the VM from the tree view: 

       1. Click the **>** icon next to the project name to open the list of VMs. 
       2. Right-click the name of the VM and select **Control** **Unpause**. 

     * To view comprehensive information about the selected VM before you unpause it: 

       1. Access the **VirtualMachine details** page by clicking the name of the virtual machine. 
       2. Click **Actions** **Control** **Unpause**. 




## 8.14.9. Control the state of multiple VMs

You can start, stop, restart, pause, and unpause several virtual machines (VMs) at once from the OpenShift Container Platform web console. The action applies to every VM in a project or only to the VMs that you select. 

**Procedure**

  1. Navigate to **Virtualization** **VirtualMachines** in the web console. 
  2. Optional: Enable the **Show only projects with VirtualMachines** option above the tree view to limit the displayed projects. 
  3. Select a relevant project from the tree view. 
  4. Navigate to the appropriate menu for your use case: 

     * To change the state of all VMs in the selected project: 

       1. Right-click the name of the project in the tree view and select the intended action from the menu. 
       2. If action confirmation is enabled, confirm the action in the confirmation dialog. 

     * To change the state of specific VMs: 

       1. Select a checkbox next to the VMs you want to work with. To select all VMs, click the checkbox in the **VirtualMachines** table header. 
       2. Click **Actions** and select the intended action from the menu. 
       3. If action confirmation is enabled, confirm the action in the confirmation dialog. 




## 8.14.10. Additional resources

  * [Using the CLI tools](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/getting-started#virt-using-the-cli-tools "3.2. Using the CLI tools")
