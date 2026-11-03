# 7.7. Site-wide policy enforcement and distribution

After deploying applications on a cluster, it becomes challenging to manage all of the objects that make up the security rules. It becomes critical to be able to apply site-wide policies and audit the deployed objects for compliance with the policies. This should allow for delegation of some permissions to users and cluster administrators within defined bounds, and should allow for exceptions to the policies if necessary. 

Leverage: 

  * [Red Hat OpenShift Service Mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#ossm-about): RBAC to [control policy object](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#security-platform-multi-tenancy_security-platform)s and delegate control. 
  * [Red Hat Advanced Cluster Security for Kubernetes](https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes): [Policy enforcement](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_security_for_kubernetes/4.1/html/operating/manage-security-policies#doc-wrapper) engine. 
  * [Red Hat Advanced Cluster Management (RHACM) for Kubernetes](https://www.redhat.com/en/technologies/management/advanced-cluster-management): Centralized policy control.
