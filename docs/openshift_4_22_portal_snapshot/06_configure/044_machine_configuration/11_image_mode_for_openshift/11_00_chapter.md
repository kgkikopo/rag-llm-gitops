# Chapter 11. Image mode for OpenShift

You can extend the functionality of your base RHCOS image by layering additional images onto the base image without modifying the base RHCOS image. 

This layering creates a _custom layered image_ that includes all RHCOS functionality and adds additional functionality to specific nodes in the cluster. 

Image mode is a cloud-native approach to operating system management that treats your OS like a container image. You define your operating system configuration as code, build it as a unified image, and deploy it consistently across your entire fleet.

- [11.1. About image mode for OpenShift](11_01_about_image_mode_for_openshift.md)
- [11.2. Example Containerfiles](11_02_example_containerfiles.md)
- [11.3. About on-cluster image mode](11_03_about_on_cluster_image_mode.md)
- [11.4. Using Out-of-cluster image mode to apply a custom layered image](11_04_using_out_of_cluster_image_mode_to_apply_a_custom_layered_image.md)
- [11.5. Applying a custom layered image during OpenShift Container Platform installation](11_05_applying_a_custom_layered_image_during_openshift_container_platform_installation.md)
- [11.6. Update with a RHCOS custom layered image](11_06_update_with_a_rhcos_custom_layered_image.md)
- [11.7. Additional resources](11_07_additional_resources.md)
