# 1.2. Virtualized control plane deployment workflow

Deploy a virtualized control plane cluster by installing KubeVirt Redfish on your hosting cluster, configuring it to expose your VMs, and running your preferred installation method. 

Note

Virtualized control planes require an OpenShift Container Platform cluster with OpenShift Virtualization installed and operational, which operates as the hosting cluster. 

See the following high-level steps to deploy a virtualized control plane cluster: 

  1. Install and configure KubeVirt Redfish on the hosting cluster. This includes defining which VMs to expose through the Redfish API, configuring authentication credentials, and creating a `Route` CR to expose the endpoint externally. 
  2. Create the control plane VMs on the hosting cluster. Configure the VMs with appropriate resources and network settings, and ensure they remain powered off until the installation begins. 
  3. Configure your installation method to use KubeVirt Redfish. In your configuration files, specify BMC addresses using the KubeVirt Redfish route URL for the virtualized control plane nodes, for example: `redfish-virtualmedia+https://<kubevirt_redfish_route>/redfish/v1/Systems/<vm_namespace>.<vm_name>`. 
  4. Run the installation. The VMs boot from the installation media and communicate with each other to form the cluster. Depending on the installation method, this process is either fully automated or requires manual intervention to boot each node. 
  5. After installation completes, a new OpenShift Container Platform cluster is deployed with its control plane running on VMs hosted by the original OpenShift Virtualization cluster.
