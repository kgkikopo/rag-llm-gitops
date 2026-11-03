# 2.1. Creating a Google Cloud project

To install OpenShift Container Platform, you must create a project in your Google Cloud account to host the cluster. 

**Procedure**

  * Create a project to host your OpenShift Container Platform cluster. See [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in the Google Cloud documentation. 

Important

Your Google Cloud project must use the Premium Network Service Tier if you are using installer-provisioned infrastructure. The Standard Network Service Tier is not supported for clusters installed using the installation program. The installation program configures internal load balancing for the `api-int.<cluster_name>.<base_domain>` URL; the Premium Tier is required for internal load balancing.
