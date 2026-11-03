# 1.9. Checking cluster resource availability and utilization

OpenShift Container Platform provides a comprehensive set of monitoring dashboards that you can analyze to better understand the state of cluster components. 

As an administrator, you can access dashboards for core OpenShift Container Platform components, including: 

  * etcd 
  * Kubernetes compute resources 
  * Kubernetes network resources 
  * Prometheus 
  * Dashboards relating to cluster and node performance 



**Figure 1.1. Example compute resources dashboard**

![Screenshot of the OpenShift Container Platform monitoring dashboard showing compute resources including CPU usage](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Validation_and_troubleshooting-en-US/images/b2d5f6ce1d0581d56b0bf88e26721b63/monitoring-dashboard-compute-resources.png) ![Screenshot of the OpenShift Container Platform monitoring dashboard showing compute resources including CPU usage](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Validation_and_troubleshooting-en-US/images/b2d5f6ce1d0581d56b0bf88e26721b63/monitoring-dashboard-compute-resources.png)

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Observe** **Dashboards**. 
  2. Choose a dashboard in the **Dashboard** list. Some dashboards, such as the **etcd** dashboard, produce additional sub-menus when selected. 
  3. Optional: Select a time range for the graphs in the **Time Range** list. 

     * Select a pre-defined time period. 
     * Set a custom time range by selecting **Custom time range** in the **Time Range** list. 

       1. Input or select the **From** and **To** dates and times. 
       2. Click **Save** to save the custom time range. 

  4. Optional: Select a **Refresh Interval**. 
  5. Hover over each of the graphs within a dashboard to display detailed information about specific items. 



**Additional resources**

  * [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/about_monitoring/about-ocp-monitoring)
