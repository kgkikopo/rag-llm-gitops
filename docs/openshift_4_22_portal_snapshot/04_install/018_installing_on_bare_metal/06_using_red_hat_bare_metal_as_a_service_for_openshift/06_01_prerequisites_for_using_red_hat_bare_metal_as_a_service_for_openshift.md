# 6.1. Prerequisites for using Red Hat Bare-Metal-as-a-Service for OpenShift

Red Hat Bare-Metal-as-a-Service for OpenShift lets you apply cloud-native management practices to bare-metal infrastructure, enabling automated provisioning and lifecycle management for workloads that require physical hardware. 

To use Red Hat Bare-Metal-as-a-Service for OpenShift, complete the following prerequisites: 

BareMetalHost Configuration
     All bare-metal hosts must use a Baseboard Management Controller (BMC) configured with the Redfish protocol and virtual media (`redfish-virtualmedia`) driver. Each bare-metal host requires a boot interface with a MAC address configured to receive an IP address lease. 
Network Requirements
     A DHCP server, separate from the OpenShift Container Platform and Metal3 infrastructure, must be operational on the same Layer 2 network as the bare-metal hosts. The DHCP server must be configured to match the MAC addresses of the boot interfaces on the bare-metal hosts, enabling IP address assignment for communication with Metal3 components. 
Cluster Privileges
     You must have `cluster-admin` privileges on the OpenShift Container Platform cluster to perform configuration tasks. 
Web server with images
    

Red Hat Bare-Metal-as-a-Service for OpenShift does not provide images for deployment on hardware. You must configure a web server with the images and checksums you want to use. The `image` field of the `BareMetalHost` spec references these images during deployment. Ensure that the bare-metal hosts can reach the web server URL. Alternatively, you can access images from an OCI registry as a Technology Preview. This can be done by accessing a public registry such as Quay.io, or by hosting OCI images from the built-in registry in your cluster. The following is an example of images and checksums you might include: 

  * `http://example.com/rhel9.qcow2`
  * `http://example.com/rhel9.qcow2.sha512sum`
  * `http://example.com/stream9.qcow2`
  * `http://example.com/stream9.qcow2.sha512sum`
  * `\oci://quay.io/example/image:version`



These prerequisites ensure that Red Hat Bare-Metal-as-a-Service for OpenShift can provision and manage bare-metal hosts effectively. 

Important

Accessing images from an OCI registry is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).
