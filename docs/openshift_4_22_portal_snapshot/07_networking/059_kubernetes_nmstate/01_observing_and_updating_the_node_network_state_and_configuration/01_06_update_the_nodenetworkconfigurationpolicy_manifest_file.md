# 1.6. Update the NodeNetworkConfigurationPolicy manifest file

To modify the network configuration for nodes in your OpenShift Container Platform cluster, you can update the `NodeNetworkConfigurationPolicy` manifest file. 

## 1.6.1. Update the policy by using form

You can update a `NodeNetworkConfigurationPolicy` object by using the form view in the web console. 

Note

Addition of a VLAN interface using the form is not supported. To add a VLAN interface, you must use YAML to create the policy. Once added, you cannot edit the policy using form. 

**Procedure**

  1. Navigate to **Networking** **NodeNetworkConfigurationPolicy**. 
  2. In the **NodeNetworkConfigurationPolicy** page, click the ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Kubernetes_NMState-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) icon placed next to the policy you want to edit, and click **Edit**. 
  3. Edit the fields that you want to update. 
  4. Click **Save**. 



## 1.6.2. Update the policy by using YAML

You can update a `NodeNetworkConfigurationPolicy` object by editing the YAML in the web console. 

**Procedure**

  1. Navigate to **Networking** **NodeNetworkConfigurationPolicy**. 
  2. In the **NodeNetworkConfigurationPolicy** page, click the policy name under the **Name** column for the policy you want to edit. 
  3. Click the **YAML** tab, and edit the YAML. 
  4. Click **Save**. 



## 1.6.3. Delete the policy

You can delete a `NodeNetworkConfigurationPolicy` object when it is no longer needed. 

**Procedure**

  1. Navigate to **Networking** **NodeNetworkConfigurationPolicy**. 
  2. In the **NodeNetworkConfigurationPolicy** page, click the ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Kubernetes_NMState-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) icon placed next to the policy you want to delete, and click **Delete**. 
  3. In the pop-up window, enter the policy name to confirm deletion, and click **Delete**.
