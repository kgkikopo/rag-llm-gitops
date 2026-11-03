# 2.4. Google Cloud account limits

A default OpenShift Container Platform cluster consumes specific Google Cloud resource quotas that you might need to increase before installation, depending on your region and cluster size. 

A default cluster, which contains three compute and three control plane machines, uses the following resources. Note that some resources are required only during the bootstrap process and are removed after the cluster deploys. 

Table 2.3. Google Cloud resources used in a default clusterService| Component| Location| Total resources required| Resources removed after bootstrap  
---|---|---|---|---  
Service account  |  IAM  |  Global  |  6  |  1   
Firewall rules  |  Compute  |  Global  |  11  |  1   
Forwarding rules  |  Compute  |  Global  |  2  |  0   
In-use global IP addresses  |  Compute  |  Global  |  4  |  1   
Health checks  |  Compute  |  Global  |  3  |  0   
Images  |  Compute  |  Global  |  1  |  0   
Networks  |  Compute  |  Global  |  2  |  0   
Static IP addresses  |  Compute  |  Region  |  4  |  1   
Routers  |  Compute  |  Global  |  1  |  0   
Routes  |  Compute  |  Global  |  2  |  0   
Subnetworks  |  Compute  |  Global  |  2  |  0   
Target pools  |  Compute  |  Global  |  3  |  0   
CPUs  |  Compute  |  Region  |  28  |  4   
Persistent disk SSD (GB)  |  Compute  |  Region  |  896  |  128   
Show more

Note

If any of the quotas are insufficient during installation, the installation program displays an error that states both which quota was exceeded and the region. 

Be sure to consider your actual cluster size, planned cluster growth, and any usage from other clusters that are associated with your account. The CPU, static IP addresses, and persistent disk SSD (storage) quotas are the ones that are most likely to be insufficient. 

If you plan to deploy your cluster in one of the following regions, you will exceed the maximum storage quota and are likely to exceed the CPU quota limit: 

  * `asia-east2`
  * `asia-northeast2`
  * `asia-south1`
  * `australia-southeast1`
  * `europe-north1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west6`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-west2`



You can increase resource quotas from the Google Cloud console, but you might need to file a support ticket. Be sure to plan your cluster size early so that you can allow time to resolve the support ticket before you install your OpenShift Container Platform cluster. 

**Additional resources**

  * [Manage your quotas using the console (Google Cloud documentation)](https://cloud.google.com/docs/quota)
  * [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas)
