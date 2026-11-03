# 1.6. Deprecated features

Deprecation of Fujitsu Integrated Remote Management Controller (iRMC) driver for bare-metal machines
    

As of OpenShift Container Platform 4.21, support for the Fujitsu iRMC baseboard management controller (BMC) driver has been deprecated and will be removed in a future release. If a `BareMetalHost` resource contains a BMC address with `irmc://` as its URI scheme, the resource must be updated to use another BMC scheme, such as `redfish://` or `ipmi://`. Once support for this driver is removed, hosts that use `irmc://` URI schemes will become unmanageable. 

For information about updating the `BareMetalHost` resource, see [Editing a BareMetalHost resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#bmo-editing-a-baremetalhost-resource_bare-metal-postinstallation-configuration). 

Deprecation of the `oc adm release mirror` command
    

As of OpenShift Container Platform 4.22, using the `oc adm release mirror` command to mirror release images has been deprecated and will be removed in a future release. 

As an alternative, use the [oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-installing-oc-mirror-v2). 

Deprecation of adding kernel modules to nodes with KVC
     As of OpenShift Container Platform 4.22, support for adding kernel modules to nodes with kmods-via-containers software (KVC) has been deprecated and will be removed in a future release. 
Deprecation of the runC container runtime
     As of OpenShift Container Platform 4.22, support for using the runC container runtime is deprecated and will be removed in a future release.
