# 6.5. Cloud Controller Manager Operator

Note

The status of this Operator is General Availability for Amazon Web Services (AWS), Google Cloud, IBM Cloud®, global Microsoft Azure, Microsoft Azure Stack Hub, Nutanix, Red Hat OpenStack Platform (RHOSP), and VMware vSphere. 

The Operator is available as a Technology Preview for IBM Power® Virtual Server. 

The Cloud Controller Manager Operator manages and updates the cloud controller managers deployed on top of OpenShift Container Platform. The Operator is based on the Kubebuilder framework and `controller-runtime` libraries. You can install the Cloud Controller Manager Operator by using the Cluster Version Operator (CVO). 

The Cloud Controller Manager Operator includes the following components: 

  * Operator 
  * Cloud configuration observer 



By default, the Operator exposes Prometheus metrics through the `metrics` service. 

**Additional resources**

  * [cluster-cloud-controller-manager-operator](https://github.com/openshift/cluster-cloud-controller-manager-operator)
