# 1.2. Remote health monitoring issues

Use the Telemetry Client and the Insights Operator to collect cluster telemetry and configuration data. The Red Hat support team uses this diagnostic information to proactively identify and resolve potential infrastructure issues. 

Red Hat uses this data to understand and resolve issues in a _connected cluster_. Similar to connected clusters, you can use remote health monitoring in a restricted network. OpenShift Container Platform collects data and monitors health using the following: 

  * **Telemetry** : The Telemetry Client gathers and uploads the metrics values to Red Hat every four minutes and thirty seconds. Red Hat uses this data to: 

    * Monitor the clusters. 
    * Roll out OpenShift Container Platform upgrades. 
    * Improve the upgrade experience. 

  * **Insights Operator** : By default, OpenShift Container Platform installs and enables the Insights Operator, which reports configuration and component failure status every two hours. The Insights Operator helps to: 

    * Identify potential cluster issues proactively. 
    * Provide a solution and preventive action in Red Hat OpenShift Cluster Manager. 




You can review telemetry information. 

If you have enabled remote health reporting, you can use Red Hat Lightspeed to identify issues with your cluster. You can optionally disable remote health reporting.
