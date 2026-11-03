# 8.1. Prerequisites for installing a cluster on IBM Cloud(R) in a disconnected environment

Before installing an OpenShift Container Platform cluster on IBM Cloud® in a disconnected environment, ensure that you have configured your IBM Cloud® account, a mirror registry, an existing VPC with access to the mirror registry, and the `ccoctl` utility. 

  * You reviewed details about the OpenShift Container Platform installation and update processes. 
  * You configured an IBM Cloud® account to host the cluster. 
  * You have a container image registry that is accessible to the internet and your restricted network. The container image registry should mirror the contents of the OpenShift image registry and contain the installation media. 
  * You have an existing Virtual Private Cloud (VPC) on IBM Cloud® that meets the following requirements: 

    * The VPC contains the mirror registry or has firewall rules or a peering connection to access the mirror registry that is hosted elsewhere. 
    * The VPC can access IBM Cloud® service endpoints using a public endpoint. If network restrictions limit access to public service endpoints, evaluate those services for alternate endpoints that might be available. 

You cannot use the VPC that the installation program provisions by default. 

  * If you plan on configuring endpoint gateways to use IBM Cloud® Virtual Private Endpoints, consider the following requirements: 

    * Endpoint gateway support is currently limited to the `us-east` and `us-south` regions. 
    * The VPC must allow traffic to and from the endpoint gateways. You can use the VPC’s default security group, or a new security group, to allow traffic on port 443. 

  * You configured the `ccoctl` utility before you installed the cluster. 



**Additional resources**

  * [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Configuring an IBM Cloud® account](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_cloud/installing-ibm-cloud-account "Chapter 2. Configuring an IBM Cloud account")
  * [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-installing-oc-mirror-v2)
  * [Access to IBM service endpoints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_cloud/installing-ibm-cloud-restricted#access-to-ibm-service-endpoints_installing-ibm-cloud-restricted "8.2.3. Access to IBM service endpoints")
  * [Allowing endpoint gateway traffic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_cloud/installing-ibm-cloud-restricted#installation-ibm-cloud-configure-vpc-for-endpoint-gateways_installing-ibm-cloud-restricted "8.3.4. Allowing endpoint gateway traffic")
  * [Configuring your firewall](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall)
  * [Configuring IAM for IBM Cloud®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_cloud/configuring-iam-ibm-cloud "Chapter 3. Configuring IAM for IBM Cloud")
