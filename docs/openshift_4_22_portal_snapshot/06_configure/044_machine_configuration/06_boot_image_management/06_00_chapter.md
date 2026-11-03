# Chapter 6. Boot image management

For supported platforms, the Machine Config Operator (MCO) can manage and update the boot image on each node to ensure the Red Hat Enterprise Linux CoreOS (RHCOS) version of the boot image matches the Red Hat Enterprise Linux CoreOS (RHCOS) version appropriate for your cluster. 

The following table lists the platforms on which boot image management is available: 

Platform| Worker machine sets| Control plane machine sets  
---|---|---  
Google Cloud  |  Enabled by default  |  Disabled by default   
Amazon Web Services (AWS)  |  Enabled by default  |  Disabled by default   
Microsoft Azure  |  Enabled by default  |  Disabled by default   
VMware vSphere  |  Enabled by default  |  Not supported   
Show more

For all other platforms, the MCO does not automatically update the boot image with each cluster update. Images from the Google Cloud Marketplace or AWS Marketplace are not automatically updated. 

For clusters where automatic updates are disabled or not supported, you can manually update the boot image on your cluster. See "Manually updating the boot image" for information. The method to update or specify the image varies by platform. 

**Additional resources**

  * [Manually updating the boot image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/mco-update-boot-images-manual "Chapter 8. Manually updating the boot image")

- [6.1. About boot image management](06_01_about_boot_image_management.md)
- [6.2. Enable boot image management](06_02_enable_boot_image_management.md)
- [6.3. Disable boot image management](06_03_disable_boot_image_management.md)
