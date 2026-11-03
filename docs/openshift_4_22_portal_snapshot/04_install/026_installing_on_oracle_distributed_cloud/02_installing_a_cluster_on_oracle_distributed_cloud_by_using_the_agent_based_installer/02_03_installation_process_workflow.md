# 2.3. Installation process workflow

To better understand the process, see a high-level outline of installing an OpenShift Container Platform cluster on Oracle Distributed Cloud using the Agent-based Installer. 

The following workflow describes the general installation process: 

  1. Create Oracle Cloud Infrastructure (OCI) resources and services (Oracle). 
  2. Disconnected environments: Prepare a web server that is accessible by OCI instances (Red Hat). 
  3. Prepare configuration files for the Agent-based Installer (Red Hat). 
  4. Generate the agent ISO image (Red Hat). 
  5. Disconnected environments: Upload the rootfs image to the web server (Red Hat). 
  6. Configure your firewall for OpenShift Container Platform (Red Hat). 
  7. Upload the agent ISO image to a storage bucket (Oracle). 
  8. Create a custom image from the uploaded agent ISO image (Oracle). 
  9. Create compute instances on Oracle Distributed Cloud (Oracle). 
  10. Verify that your cluster runs on Oracle Distributed Cloud (Oracle).
