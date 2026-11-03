# 6.17. Control Plane Machine Set Operator

The Control Plane Machine Set Operator automates the management of control plane machine resources within an OpenShift Container Platform cluster. 

Note

This Operator is available for Amazon Web Services (AWS), Google Cloud, Microsoft Azure, Nutanix, and VMware vSphere. 

## 6.17.1. CRDs

  * `controlplanemachineset.machine.openshift.io`

    * Scope: Namespaced 
    * CR: `ControlPlaneMachineSet`
    * Validation: Yes 




**Additional resources**

  * [About control plane machine sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#cpmso-about)
  * [`ControlPlaneMachineSet` custom resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#controlplanemachineset-machine-openshift-io-v1)
  * [cluster-control-plane-machine-set-operator](https://github.com/openshift/cluster-control-plane-machine-set-operator)
