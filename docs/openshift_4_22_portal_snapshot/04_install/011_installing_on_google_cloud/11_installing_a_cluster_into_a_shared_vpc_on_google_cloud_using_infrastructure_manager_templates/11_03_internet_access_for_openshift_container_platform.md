# 11.3. Internet access for OpenShift Container Platform

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster. 

You must have internet access to perform the following actions: 

  * Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster. 
  * Access Quay.io to obtain the packages that are required to install your cluster. 
  * Obtain the packages that are required to perform cluster updates. 



Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.
