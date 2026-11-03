# 1.7. Verifying a successful cluster installation on Oracle Distributed Cloud

Verify that your cluster was installed and is running effectively on Oracle® Distributed Cloud. 

**Procedure**

  1. From the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift), go to **Clusters > Assisted Clusters** and select your cluster’s name. 
  2. On the **Installation Progress** page, check that the Installation progress bar is at 100% and a message displays indicating `Installation completed successfully`. 
  3. Under **Host inventory** , confirm that the status of all control plane and compute nodes is `Installed`. 

Note

OpenShift Container Platform designates one of the control plane nodes as the bootstrap virtual machine, eliminating the need for a separate bootstrap machine. 

  4. Click the Web Console URL, to access the OpenShift Container Platform web console. 
  5. From the menu, select **Compute > Nodes**. 
  6. Locate your node from the **Nodes** table. 
  7. From the **Terminal** tab, verify that iSCSI appears next to the serial number. 
  8. From the **Overview** tab, check that your node has a **Ready** status. 
  9. Select the **YAML** tab. 
  10. Check the `labels` parameter, and verify that the listed labels apply to your configuration. For example, the `topology.kubernetes.io/region=us-sanjose-1` label indicates in what Oracle Distributed Cloud region the node was deployed.
