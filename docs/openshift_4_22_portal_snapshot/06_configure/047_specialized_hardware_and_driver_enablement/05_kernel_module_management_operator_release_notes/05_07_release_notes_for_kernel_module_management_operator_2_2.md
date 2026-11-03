# 5.7. Release notes for Kernel Module Management Operator 2.2

Review what is new, changed, or fixed in Kernel Module Management Operator 2.2 on OpenShift Container Platform. 

The following new features are included in this release: 

  * KMM is now using the CRI-O container engine to pull container images in the worker pod instead of using HTTP calls directly from the worker container. For more information, see [Example Module CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/kernel-module-management-operator#kmm-example-cr_kernel-module-management-operator "4.7.1. Example Module CR"). 



  * The Kernel Module Management (KMM) Operator images are now based on `rhel-els-minimal` container images instead of the `rhel-els` images. This change results in a greatly reduced image footprint, while still maintaining FIPS compliance. 
  * In this release, the firmware search path has been updated to copy the contents of the specified path into the path specified in worker.setFirmwareClassPath (default: /var/lib/firmware). For more information, see [Example Module CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/kernel-module-management-operator#kmm-example-cr_kernel-module-management-operator "4.7.1. Example Module CR"). 



  * For each node running a kernel matching the regular expression, KMM now checks if you have included a tag or a digest. If you have not specified a tag or digest in the container image, then the validation webhook returns an error and does not apply the module. For more information, see [Example Module CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/kernel-module-management-operator#kmm-example-cr_kernel-module-management-operator "4.7.1. Example Module CR").
