# Chapter 7. Boot image skew enforcement

You can use boot image skew enforcement to help ensure that the boot images in a cluster are up-to-date with the OpenShift Container Platform and RHCOS version being used in the cluster. Using an older boot image could cause issues when scaling new nodes. If the images are older than a predetermined version, the MCO disables cluster upgrades until it deems the boot images to be compliant. 

Note

Boot image skew enforcement is not supported for single-node OpenShift clusters.

- [7.1. About boot image skew enforcement](07_01_about_boot_image_skew_enforcement.md)
- [7.2. Configuring boot image skew enforcement](07_02_configuring_boot_image_skew_enforcement.md)
- [7.3. Updating the boot image skew enforcement version](07_03_updating_the_boot_image_skew_enforcement_version.md)
- [7.4. Additional resources](07_04_additional_resources.md)
