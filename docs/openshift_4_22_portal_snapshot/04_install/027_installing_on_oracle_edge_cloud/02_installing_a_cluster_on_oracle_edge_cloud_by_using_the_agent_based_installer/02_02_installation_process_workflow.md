# 2.2. Installation process workflow

To better understand the process, see a high-level outline of installing an OpenShift Container Platform cluster on Oracle Edge Cloud using the Agent-based Installer. 

The following workflow describes the general installation process: 

  1. Create Oracle Cloud Infrastructure (OCI) resources and services (Oracle). 
  2. Prepare configuration files for the Agent-based Installer (Red Hat). 
  3. Generate the agent ISO image (Red Hat). 
  4. Convert the ISO image to an OCI image, upload it to an OCI Home Region Bucket, and then import the uploaded image to the Oracle Edge Cloud system (Oracle). 
  5. Disconnected environments: Prepare a web server that is accessible by Oracle Edge Cloud instances (Red Hat). 
  6. Disconnected environments: Upload the rootfs image to the web server (Red Hat). 
  7. Configure your firewall for OpenShift Container Platform (Red Hat). 
  8. Create control plane nodes and configure load balancers (Oracle). 
  9. Create compute nodes and configure load balancers (Oracle). 
  10. Verify that your cluster runs on Oracle Edge Cloud (Oracle).
