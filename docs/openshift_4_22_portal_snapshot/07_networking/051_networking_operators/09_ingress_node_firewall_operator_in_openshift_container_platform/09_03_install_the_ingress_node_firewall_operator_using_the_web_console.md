# 9.3. Install the Ingress Node Firewall Operator using the web console

As a cluster administrator, you can install the Ingress Node Firewall Operator to enable node-level ingress firewalling by using the web console. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have an account with administrator privileges. 



**Procedure**

  1. Install the Ingress Node Firewall Operator: 

     1. In the OpenShift Container Platform web console, click **Ecosystem** **Software Catalog**. 
     2. Select **Ingress Node Firewall Operator** from the list of available Operators, and then click **Install**. 
     3. On the **Install Operator** page, under **Installed Namespace** , select **Operator recommended Namespace**. 
     4. Click **Install**. 

  2. Verify that the Ingress Node Firewall Operator is installed successfully: 

     1. Navigate to the **Ecosystem** **Installed Operators** page. 
     2. Ensure that **Ingress Node Firewall Operator** is listed in the **openshift-ingress-node-firewall** project with a **Status** of **InstallSucceeded**. 

Note

During installation an Operator might display a **Failed** status. If the installation later succeeds with an **InstallSucceeded** message, you can ignore the **Failed** message. 

If the Operator does not have a **Status** of **InstallSucceeded** , troubleshoot using the following steps: 

        * Inspect the **Operator Subscriptions** and **Install Plans** tabs for any failures or errors under **Status**. 
        * Navigate to the **Workloads** **Pods** page and check the logs for pods in the `openshift-ingress-node-firewall` project. 
        * Check the namespace of the YAML file. If the annotation is missing, you can add the annotation `workload.openshift.io/allowed=management` to the Operator namespace with the following command: 

```shell-session
$ oc annotate ns/openshift-ingress-node-firewall workload.openshift.io/allowed=management
```


Note

For single-node OpenShift clusters, the `openshift-ingress-node-firewall` namespace requires the `workload.openshift.io/allowed=management` annotation.
