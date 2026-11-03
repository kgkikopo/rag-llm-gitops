# 11.2. Installing the PF Status Relay Operator using the web console

Install the PF Status Relay Operator to enable OpenShift Container Platform to use Link Aggregation Control Protocol (LACP) as an active health check on physical functions. 

**Prerequisites**

  * You configured LACP on your upstream switch. 
  * You configured pod-level bonding for your SR-IOV networks. 
  * You have cluster-admin privileges. 



**Procedure**

  1. Install the PF Status Relay Operator: 

     1. In the OpenShift Container Platform web console, click **Ecosystem** **Software Catalog**. 
     2. Select **PF Status Relay Operator** from the list of available Operators, and then click **Install**. 
     3. On the **Install Operator** page, under **Installed Namespace** , select **Operator recommended Namespace**. 
     4. Click **Install**. 




**Verification**

  * Verify that the PF Status Relay Operator shows the **Status** as **Succeeded** on the Installed Operators dashboard.
