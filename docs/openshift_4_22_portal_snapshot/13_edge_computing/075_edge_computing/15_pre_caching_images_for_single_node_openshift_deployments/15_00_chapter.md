# Chapter 15. Pre-caching images for single-node OpenShift deployments

In environments with limited bandwidth where you use the GitOps Zero Touch Provisioning (ZTP) solution to deploy a large number of clusters, you want to avoid downloading all the images that are required for bootstrapping and installing OpenShift Container Platform. The limited bandwidth at remote single-node OpenShift sites can cause long deployment times. The factory-precaching-cli tool allows you to pre-stage servers before shipping them to the remote site for ZTP provisioning. 

The factory-precaching-cli tool does the following: 

  * Downloads the RHCOS rootfs image that is required by the minimal ISO to boot. 
  * Creates a partition from the installation disk labeled as `data`. 
  * Formats the disk in xfs. 
  * Creates a GUID Partition Table (GPT) data partition at the end of the disk, where the size of the partition is configurable by the tool. 
  * Copies the container images required to install OpenShift Container Platform. 
  * Copies the container images required by ZTP to install OpenShift Container Platform. 
  * Optional: Copies Day-2 Operators to the partition. 



Important

The factory-precaching-cli tool is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

- [15.1. Getting the factory-precaching-cli tool](15_01_getting_the_factory_precaching_cli_tool.md)
- [15.2. Booting from a live operating system image](15_02_booting_from_a_live_operating_system_image.md)
- [15.3. Partitioning the disk](15_03_partitioning_the_disk.md)
- [15.4. Downloading the images](15_04_downloading_the_images.md)
- [15.5. Pre-caching images in GitOps ZTP](15_05_pre_caching_images_in_gitops_ztp.md)
- [15.6. Troubleshooting a "Rendered catalog is invalid" error](15_06_troubleshooting_a_rendered_catalog_is_invalid_error.md)
