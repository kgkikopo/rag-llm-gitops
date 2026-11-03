# 5.2. Downloading the installation ISO

You must first download the ISO image that will be used to run the installation on your bare-metal machines. This image includes all of the necessary OpenShift Container Platform release images, as well as the Operator Lifecycle Manager (OLM) Operators needed to install Virtualization on the cluster. 

Note

The size of the ISO image can vary depending on the release you select. 

**Procedure**

  1. Log in to the [Red Hat Hybrid Cloud Console](https://console.redhat.com). 
  2. On the **Red Hat OpenShift** tile, click **OpenShift**. 
  3. On the **Red Hat OpenShift Container Platform** tile, click **Create cluster**. 
  4. Click the **Datacenter** tab. 
  5. Under **Assisted Installer** , click **Create cluster**. 
  6. In the **Cluster details** page, select the toggle for "I’m installing on a disconnected/air-gapped/secured environment". 
  7. Select a version from the **OpenShift version** dropdown menu. 
  8. Click **Next**. 
  9. Optional: Preconfigure the ISO on the **Optional configurations** page: 

     1. Enter the Rendezvous IP in the **Rendezvous IP** field. 
     2. Upload a SSH public key in the **SSH public key** field. 
     3. Click **Replace default NTP sources** and add any NTP pools or servers in the **NTP sources** field. 

  10. Click **Next**. 
  11. Click **Download ISO**.
