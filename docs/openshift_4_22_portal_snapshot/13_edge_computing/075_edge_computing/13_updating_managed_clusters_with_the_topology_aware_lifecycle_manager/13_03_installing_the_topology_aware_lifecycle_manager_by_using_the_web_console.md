# 13.3. Installing the Topology Aware Lifecycle Manager by using the web console

You can use the OpenShift Container Platform web console to install the Topology Aware Lifecycle Manager. 

**Prerequisites**

  * Install the latest version of the RHACM Operator. 
  * TALM requires RHACM 2.9 or later. 
  * Set up a hub cluster with a disconnected registry. 
  * Log in as a user with `cluster-admin` privileges. 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Ecosystem** **Software Catalog**. 
  2. Search for the **Topology Aware Lifecycle Manager** from the list of available Operators, and then click **Install**. 
  3. Keep the default selection of **Installation mode** ["All namespaces on the cluster (default)"] and **Installed Namespace** ("openshift-operators") to ensure that the Operator is installed properly. 
  4. Click **Install**. 



**Verification**

To confirm that the installation is successful: 

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Check that the Operator is installed in the `All Namespaces` namespace and its status is `Succeeded`. 



If the Operator is not installed successfully: 

  1. Navigate to the **Ecosystem** **Installed Operators** page and inspect the `Status` column for any errors or failures. 
  2. Navigate to the **Workloads** **Pods** page and check the logs in any containers in the `cluster-group-upgrades-controller-manager` pod that are reporting issues.
