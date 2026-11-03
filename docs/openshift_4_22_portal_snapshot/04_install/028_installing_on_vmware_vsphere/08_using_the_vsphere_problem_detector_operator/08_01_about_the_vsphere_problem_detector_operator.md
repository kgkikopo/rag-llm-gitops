# 8.1. About the vSphere Problem Detector Operator

The vSphere Problem Detector Operator checks a cluster that you deployed on VMware vSphere for common installation and configuration issues that relate to storage. 

After the Cluster Storage Operator starts and determines that a cluster runs on VMware vSphere, the Cluster Storage Operator launches the vSphere Problem Detector Operator. When the vSphere Problem Detector Operator starts, the Operator immediately runs the checks. The vSphere Problem Detector Operator communicates with the vSphere vCenter Server to find the virtual machines in the cluster, the default datastore, and other information about the vSphere vCenter Server configuration. The Operator uses the credentials from the Cloud Credential Operator to connect to vSphere. 

The Operator runs the checks according to the following schedule: 

  * The checks run every hour. 
  * If any check fails, the Operator runs the checks again in intervals of 1 minute, 2 minutes, 4, 8, and so on. The Operator doubles the interval up to a maximum interval of 8 hours. 
  * When all checks pass, the schedule returns to an hour interval. 



After a failure, the Operator increases its check frequency to quickly report success when the failure condition gets resolved. You can run the Operator manually for immediate troubleshooting information.
