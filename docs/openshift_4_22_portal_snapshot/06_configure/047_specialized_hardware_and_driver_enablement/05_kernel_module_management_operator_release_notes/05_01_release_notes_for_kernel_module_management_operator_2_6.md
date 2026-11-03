# 5.1. Release notes for Kernel Module Management Operator 2.6

Review what is new, changed, or fixed in Kernel Module Management Operator 2.6 on OpenShift Container Platform. 

The following new features and enhancements are included in this release: 

  * In this release, wildcard and glob pattern support for the `filesToSign` field has been added for signing kernel modules in a specific folder. Previously, you had to specify the exact path to each `.ko` file you wanted to sign. Now, you can add the full path to explicit files, as previously required, or any glob patterns supported by the `Ash` shell. 

The `DirName` value from `moduleLoader.container.modprobe` is propagated into the sign image. The validation webhook also verifies that all `filesToSign` entries fall under the configured `DirName`. 

For more information, see [Specifying files to sign](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/kernel-module-management-operator#kmm-specifying-files-to-sign_kernel-module-management-operator "4.14. Specify files to sign"). 




  * In this release, you can use the `AutomountServiceAccountToken` parameter to disable the auto-mounting of the projected volume. You can set `AutomountServiceAccountToken` to `false` to disable auto-mounting and mount the configmaps and tokens necessary for the `DevicePlugin` application. 

Kubernetes automatically mounts the service account token and root Certificate Authoritys (CAs) into the `/var/run/secrets/kubernetes.io/serviceaccount` of the device-plugin pods using projected volumes. In some cases, you may want to use additional custom CAs or tokens for the device-plugin but Kubernetes does not allow mounting them to the same path unless the auto-mount is disabled. 




  * In this release, new security settings have been added to prevent filesystem tampering and remove privileged kernel operations. The new settings enhance container security by restricting system capabilities and enabling read-only root filesystems across manager, webhook-server, and Operator components to strengthen security posture and reduce attack surface. For more information, see [KMM RapiDAST "Root file system is not read-only" while checking DAST](https://redhat.atlassian.net/browse/MGMT-20929). 



  * In this release, when installing KMM using OLM, you can add additional tolerations to the Operator where worker nodes have custom taints or no accessible control-plane nodes. 

By default, the KMM Operator is installed on control plane nodes when possible and includes tolerations that allow for the KMM Operator to be scheduled on the nodes. In environments where the control plane is not accessible, the KMM Operator is installed on worker nodes. 




  * In this release, a new optional `imageRebuildTriggerGeneration` counter field has been added in the `Module`, `ManagedClusterModule`, and `ModuleImagesConfig` CRDs that allows you to force Kernel Module Management (KMM) to reverify and rebuild module images when using ephemeral image registries. When this counter’s value changes, the system automatically clears cached image statuses and reverifies the image existence, potentially triggering rebuilds. 



The following bug fixes are included in this release: 

  * Unwarranted kernel module removal due to memory and disk limitations. 

    * **Cause** : Memory and disk limitations can cause the removal of kernel modules. 
    * **Consequence** : The kernel module is removed. 
    * **Fix** : This release contains a new set of internal tolerations such as `DiskPressure`, `MemoryPressure`, and `PIDPressure` that are propagated through the module loader data flow and node selection process. These internal tolerations are appended to module-specific tolerations when handling module scheduling. 
    * **Result** : The internal tolerations improve module scheduling to account for additional system resource pressure conditions. Modules can now be deployed across a broader range of cluster nodes, enhancing resource utilization and deployment flexibility. 




  * Kernel Module Management (KMM) cannot delete module names that contain a `.`. 

    * **Cause** : The Kernel Module Management (KMM) Operator cannot delete modules that contain a `.` in their name. 
    * **Consequence** : The module intended for deletion hangs indefinitely. 
    * **Fix** : The finalizer `regexp` used to remove the node label has been modified to complete deletion. 
    * **Result** : When the node label has been correctly deleted, the module deletes successfully. 

For more information, see [MGMT-19647](https://redhat.atlassian.net/browse/MGMT-19647). 




  * Build and sign pods do not inherit Module tolerations. 

    * **Cause** : Build and sign pods created through the `ModuleImagesConfig` (MIC) and `ModuleBuildSignConfig` (MBSC) flows do not inherit tolerations from the parent Module. 
    * **Consequence** : Build pods fail scheduling on nodes with custom taints. Build pods should have the same tolerations as defined in the `Module.spec.tolerations` parameter, allowing them to schedule on tainted nodes where kernel headers are available. 
    * **Fix** : Added a `Tolerations` field to module build and image configurations that specifies the tolerations for build and sign pods. 
    * **Result** : You can now specify tolerations for build and sign pods, enabling control over pod scheduling on nodes with taints. This fix supports standard toleration properties including effect, key, operator, and duration settings. 




The following known issues apply to this release: 

  * Issues have been encountered when loading out-of-tree (OOT) drivers for QDU x100 DU PCIe cards from v4.14. For more information, see [Case 04245147](https://access.redhat.com/support/cases/#/case/04245147).
