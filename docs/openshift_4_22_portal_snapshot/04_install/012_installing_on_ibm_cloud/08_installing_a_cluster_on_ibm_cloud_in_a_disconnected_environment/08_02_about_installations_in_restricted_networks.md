# 8.2. About installations in restricted networks

You can install OpenShift Container Platform 4.22 in a restricted network that lacks an active internet connection. These restricted installations use installer-provisioned or user-provisioned infrastructure, depending on your cloud platform. 

## 8.2.1. Required internet access and an installation host

You complete the installation using a bastion host or portable device that can access both the internet and your closed network. You must use a host with internet access to: 

  * Download the installation program, the OpenShift CLI (`oc`), and the CCO utility (`ccoctl`). 
  * Use the installation program to locate the Red Hat Enterprise Linux CoreOS (RHCOS) image and create the installation configuration file. 
  * Use `oc` to extract `ccoctl` from the CCO container image. 
  * Use `oc` and `ccoctl` to configure IAM for IBM Cloud®. 



## 8.2.2. Access to a mirror registry

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and contains the installation media. 

You can create this registry on a mirror host, which can access both the internet and your restricted network, or by using other methods that meet your organization’s security restrictions. 

For more information on mirroring images for a disconnected installation, see "Additional resources". 

## 8.2.3. Access to IBM service endpoints

The installation program requires access to the following IBM Cloud® service endpoints: 

  * Cloud Object Storage 
  * DNS Services 
  * Global Search 
  * Global Tagging 
  * Identity Services 
  * Resource Controller 
  * Resource Manager 
  * VPC 



Note

If you are specifying an IBM® Key Protect for IBM Cloud® root key as part of the installation process, the service endpoint for Key Protect is also required. 

By default, the public endpoint is used to access the service. If network restrictions limit access to public service endpoints, you can override the default behavior. 

Before deploying the cluster, you can update the installation configuration file (`install-config.yaml`) to specify the URI of an alternate service endpoint. For more information on usage, see "Additional resources". 

## 8.2.4. Additional limits

Clusters in restricted networks have the following additional limitations and restrictions: 

  * The `ClusterVersion` status includes an `Unable to retrieve available updates` error. 
  * By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags. 



**Additional resources**

  * [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-installing-oc-mirror-v2)
  * [Additional IBM Cloud configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_cloud/installation-config-parameters-ibm-cloud-vpc#installation-configuration-parameters-additional-ibm-cloud_installation-config-parameters-ibm-cloud-vpc "10.1.4. Additional IBM Cloud configuration parameters")
