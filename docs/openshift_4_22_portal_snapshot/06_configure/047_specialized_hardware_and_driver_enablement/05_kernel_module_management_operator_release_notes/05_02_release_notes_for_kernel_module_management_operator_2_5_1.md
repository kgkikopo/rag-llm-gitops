# 5.2. Release notes for Kernel Module Management Operator 2.5.1

Review what is new, changed, or fixed in Kernel Module Management Operator 2.5.1 on OpenShift Container Platform. 

The following known issues apply to this release: 

  * Kernel Module Management (KMM) version 2.5 does not run on Red Hat OpenShift Service on AWS (ROSA) clusters or any other cluster that doesn’t install the `MachineConfig` CRD. 

    * **Cause** : This happens because the BMC controller that monitors `MachineConfig` objects on clusters cannot find these objects on ROSA clusters because they do not exist. 
    * **Consequence** : Causes the BMC controller to fail and the KMM controller pods to continually restart. 
    * **Fix** : In this version, the Operator verifies that the `MachineConfig` CRD is present on a cluster and runs the BMC controller on a cluster only when the `MachineConfig` CRD is present. 
    * **Result** : ROSA controller pods start successfully.
