# 6.35. vSphere Problem Detector Operator

The vSphere Problem Detector Operator checks clusters that are deployed on vSphere for common installation and misconfiguration issues that are related to storage. 

Note

The vSphere Problem Detector Operator is only started by the Cluster Storage Operator when the Cluster Storage Operator detects that the cluster is deployed on vSphere. 

## 6.35.1. Configuration

No configuration is required. 

## 6.35.2. Notes

  * The Operator supports OpenShift Container Platform installations on vSphere. 
  * The Operator uses the `vsphere-cloud-credentials` to communicate with vSphere. 
  * The Operator performs checks that are related to storage. 



**Additional resources**

  * [Using the vSphere Problem Detector Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#using-vsphere-problem-detector-operator)
