# 1.8. Reviewing the cluster status from Red Hat OpenShift Cluster Manager

From the OpenShift Container Platform web console, you can review detailed information about the status of your cluster on OpenShift Cluster Manager. 

**Prerequisites**

  * You have logged in to [OpenShift Cluster Manager](https://console.redhat.com/openshift). 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Go to the **Cluster List** in [OpenShift Cluster Manager](https://console.redhat.com/openshift) and locate your OpenShift Container Platform cluster. 
  2. Click the **Overview** tab for your cluster. 
  3. Review the following information about your cluster: 

     * vCPU and memory availability and resource usage 
     * The cluster ID, status, type, region, and the provider name 
     * Node counts by node type 
     * Cluster version details, the creation date of the cluster, and the name of the cluster owner 
     * The life cycle support status of the cluster 
     * Subscription information, including the service level agreement (SLA) status, the subscription unit type, the production status of the cluster, the subscription obligation, and the service level 

Tip

To view the history for your cluster, click the **Cluster history** tab. 

  4. Go to the **Monitoring** page to review the following information: 

     * A list of any issues that have been detected 
     * A list of alerts that are firing 
     * The cluster Operator status and version 
     * The cluster’s resource usage 

  5. Optional: Go to the **Overview** menu to view information that Red Hat Lightspeed collects about your cluster: 

     * Potential issues that your cluster might be exposed to, categorized by risk level 
     * Health-check status by category 




**Additional resources**

  * [Using Red Hat Lightspeed to identify issues with your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#using-insights-to-identify-issues-with-your-cluster)
