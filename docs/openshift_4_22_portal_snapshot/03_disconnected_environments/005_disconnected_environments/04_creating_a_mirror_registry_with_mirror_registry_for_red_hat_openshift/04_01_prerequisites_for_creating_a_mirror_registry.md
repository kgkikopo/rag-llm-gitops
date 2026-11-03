# 4.1. Prerequisites for creating a mirror registry

There are several prerequisites that you must meet before you can create a mirror registry. 

The following prerequisites must be met: 

  * An OpenShift Container Platform subscription. 
  * Red Hat Enterprise Linux (RHEL) 8 and 9 with Podman 3.4.2 or later and OpenSSL installed. If you are using Podman 5.7 or later, see "Configuring rootless Podman networking". 
  * Fully qualified domain name for the Red Hat Quay service, which must resolve through a DNS server. 
  * Key-based SSH connectivity on the target host. SSH keys are automatically generated for local installs. For remote hosts, you must generate your own SSH keys. 
  * 2 or more vCPUs. 
  * 8 GB of RAM. 
  * About 12 GB for OpenShift Container Platform 4.22 release images, or about 358 GB for OpenShift Container Platform 4.22 release images and OpenShift Container Platform 4.22 Red Hat Operator images. 

Important

    * Up to 1 TB per stream or more is suggested. 
    * These requirements are based on local testing results with only release images and Operator images. Storage requirements can vary based on your organization’s needs. You might require more space, for example, when you mirror multiple z-streams. You can use standard [Red Hat Quay functionality](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html/use_red_hat_quay/index) or the proper [API callout](https://access.redhat.com/documentation/en-us/red_hat_quay/3/html-single/red_hat_quay_api_guide/index#deletefulltag) to remove unnecessary images and free up space.
