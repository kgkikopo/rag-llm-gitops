# 8.2. Windows Machine Config Operator Control Plane Only update

You can use the **Control Plane Only** process to update the OpenShift Container Platform from one EUS version to another EUS version of OpenShift Container Platform. After you update the cluster, the Windows nodes are updated the new EUS version. 

During the update, the Windows workloads are kept in a healthy state with no disruptions. 

Important

This update was previously known as an **EUS-to-EUS** update and is now referred to as a **Control Plane Only** update. These updates are only viable between **even-numbered minor versions** of OpenShift Container Platform. 

## 8.2.1. WMCO Control Plane Only update by using the web console

You can use the OpenShift Container Platform web console to perform a Control Plane Only update of the Windows Machine Config Operator (WMCO). 

**Prerequisites**

  * The cluster must be running on a supported EUS version of OpenShift Container Platform. 
  * All Windows nodes must be in a healthy state. 
  * All Windows nodes must be running on the same version of the WMCO. 
  * All the of the prerequisites of the Control Plane Only update are met, as described in "Performing a Control Plane Only update." 



**Procedure**

  1. Uninstall WMCO operator by using the following the steps: 

Important

Delete the Operator only. Do not delete the Windows namespace or any Windows workloads. 

     1. Log in to the OpenShift Container Platform web console. 
     2. Navigate to **Ecosystem** **Software Catalog**. 
     3. Use the **Filter by keyword** box to search for `Red Hat Windows Machine Config Operator`. 
     4. Click the **Red Hat Windows Machine Config Operator** tile. The Operator tile indicates it is installed. 
     5. In the **Windows Machine Config Operator** descriptor page, click **Uninstall**. 

  2. Update OpenShift Container Platform by following the steps in "Performing a Control Plane Only update." 
  3. Install the new WMCO version by following the steps in "Installing the Windows Machine Config Operator using the web console." 



## 8.2.2. WMCO Control Plane Only update by using the CLI

You can use the OpenShift CLI (`oc`) to perform a Control Plane Only update of the Windows Machine Config Operator (WMCO). 

**Prerequisites**

  * The cluster must be running on a supported EUS version of OpenShift Container Platform. 
  * All Windows nodes must be in a healthy state. 
  * All Windows nodes must be running on the same version of the WMCO. 
  * All the of the prerequisites of the Control Plane Only update are met, as described in "Performing a Control Plane Only update." 



**Procedure**

  1. Uninstall the WMCO Operator from the cluster by following the steps in "Deleting Operators from a cluster using the CLI." 

Important

Delete the Operator only. Do not delete the Windows namespace or any Windows workloads. 

  2. Update OpenShift Container Platform by following the steps in "Performing a Control Plane Only update." 
  3. Install the new WMCO version by following the steps in "Installing the Windows Machine Config Operator using the CLI." 



**Verification**

  * On the Verify that the **Status** shows **Succeeded** to confirm successful installation of the WMCO.
