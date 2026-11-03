# 4.1. Prerequisites

* You have reviewed details about the OpenShift Container Platform installation and update processes. 
  * The installation program requires access to port 9440 on Prism Central and Prism Element. You verified that port 9440 is accessible. 
  * If you use a firewall, you have met these prerequisites: 

    * You confirmed that port 9440 is accessible. Control plane nodes must be able to reach Prism Central and Prism Element on port 9440 for the installation to succeed. 
    * You configured the firewall to grant access to the sites that OpenShift Container Platform requires. This includes the use of Telemetry. 

  * If your Nutanix environment is using the default self-signed SSL/TLS certificate, replace it with a certificate that is signed by a CA. The installation program requires a valid CA-signed certificate to access to the Prism Central API. For more information about replacing the self-signed certificate, see the Nutanix AOS Security Guide. 

If your Nutanix environment uses an internal CA to issue certificates, you must configure a cluster-wide proxy as part of the installation process. For more information, see "Configuring a custom PKI". 

Important

Use 2048-bit certificates. The installation fails if you use 4096-bit certificates with Prism Central 2022.x. 

  * You have a container image registry, such as Red Hat Quay. If you do not already have a registry, you can create a mirror registry using the _mirror registry for Red Hat OpenShift_. 
  * You have used the oc-mirror OpenShift CLI (oc) plugin to mirror all of the required OpenShift Container Platform content and other images, including the Nutanix CSI Operator, to your mirror registry. 

Important

Because the installation media is on the mirror host, you can use that computer to complete all installation steps.
