# 1.5. Manage policy from the web console

You can update the node network configuration, such as adding or removing interfaces from nodes, by applying `NodeNetworkConfigurationPolicy` manifests to the cluster. 

Manage the policy from the web console by accessing the list of created policies in the **NodeNetworkConfigurationPolicy** page under the **Networking** menu. This page enables you to create, update, monitor, and delete the policies. 

## 1.5.1. Monitor the policy status

You can monitor the policy status from the **NodeNetworkConfigurationPolicy** page. This page displays all the policies created in the cluster in a tabular format, with the following columns: 

Name
     The name of the policy created. 
Matched nodes
     The count of nodes where the policies are applied. This could be either a subset of nodes based on the node selector or all the nodes on the cluster. 
Node network state
     The enactment state of the matched nodes. You can click on the enactment state and view detailed information on the status. 

To find the desired policy, you can filter the list either based on enactment state by using the **Filter** option, or by using the search option. 

## 1.5.2. Create a policy

You can create a policy by using either a form or YAML in the web console. When creating a policy by using a form, you can see how the new policy changes the topology of the nodes in your cluster in real time. 

**Procedure**

  1. Go to **Networking** **Node Network Configuration**. 
  2. On the **Node Network Configuration** page, click **Create** and select the **From Form** option. 

Note

To create a policy by using YAML, click **Create** **With YAML** option. However, the following steps apply only to the form method. 

  3. Optional: To apply this `NodeNetworkConfigurationPolicy` object only to specific subsets of nodes by using the node selector, select the corresponding checkbox. 
  4. Enter the policy name in the **Policy name** field. 
  5. Click **Next** to move to the **Policy Interfaces** section. 
  6. In the **Bridging** part of the **Policy Interfaces** section, the form adds a bridge interface named `br0` by default with preset values in editable fields. If required, edit the values by performing the following steps: 

     1. Enter the name of the interface in **Interface name** field. 
     2. Select the required network state. The default selected state is **Up**. 
     3. Select the type of interface. The available types are **Bridge** , **Bonding** , and **Ethernet**. The default selected value is **Bridge**. 

Note

Addition of a VLAN interface by using the form is not supported. To add a VLAN interface, you must use YAML to create the policy. Once added, you cannot edit the policy by using form. 

     4. Optional: In the IP configuration section, check **IPv4** checkbox to assign an IPv4 address to the interface, and configure the IP address assignment details: 

        1. Click **IP address** to configure the interface with a static IP address, or **DHCP** to auto-assign an IP address. 
        2. If you have selected **IP address** option, enter the IPv4 address in the **IPv4 address** field, and enter the prefix length in **Prefix length** field. 

If you have selected **DHCP** option, clear the options that you want to disable. The available options are **Auto-DNS** , **Auto-routes** , and **Auto-gateway**. By default, the form selects all options. 

     5. Optional: Enter the port number in **Port** field. 
     6. Optional: Select the **Enable STP** checkbox to enable Spanning Tree Protocol (STP). 
     7. Optional: To add an interface to the policy, click **Add another interface to the policy**. 
     8. Optional: To remove an interface from the policy, click  icon next to the interface. 

Note

You can also click **Edit YAML** at the top of the page to continue editing the form by using YAML. 

  7. Click **Next** to go to the **Review** section of the form. 
  8. Verify the settings and click **Create** to create the policy.
