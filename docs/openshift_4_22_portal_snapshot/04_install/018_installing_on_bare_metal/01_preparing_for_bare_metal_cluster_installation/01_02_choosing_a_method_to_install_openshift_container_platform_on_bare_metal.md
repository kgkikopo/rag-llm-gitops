# 1.2. Choosing a method to install OpenShift Container Platform on bare metal

The OpenShift Container Platform installation program offers four methods for deploying a cluster: 

  * **Interactive** : You can deploy a cluster with the web-based Assisted Installer. This is the recommended approach for clusters with networks connected to the internet. The Assisted Installer is the easiest way to install OpenShift Container Platform, it provides smart defaults, and it performs pre-flight validations before installing the cluster. It also provides a RESTful API for automation and advanced configuration scenarios. 
  * **Local Agent-based** : You can deploy a cluster locally with the agent-based installer for air-gapped or restricted networks. It provides many of the benefits of the Assisted Installer, but you must download and configure the agent-based installer first. Configuration is done with a commandline interface. This approach is ideal for air-gapped or restricted networks. 
  * **Automated** : You can deploy a cluster on installer-provisioned infrastructure and the cluster it maintains. The installation program uses each cluster host’s baseboard management controller (BMC) for provisioning. You can deploy clusters with both connected or air-gapped or restricted networks. 
  * **Full control** : You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters with both connected or air-gapped or restricted networks. 



The clusters have the following characteristics: 

  * Highly available infrastructure with no single points of failure is available by default. 
  * Administrators maintain control over what updates are applied and when.
