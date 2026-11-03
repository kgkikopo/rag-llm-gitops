# 3.18. Telco core reference configuration software specifications

The Red Hat telco core 4.22 solution has been validated using the following Red Hat software products for OpenShift Container Platform clusters. 

Table 3.9. Telco core cluster validated software componentsComponent| Software version  
---|---  
Red Hat Advanced Cluster Management (RHACM)  |  2.17   
Red Hat OpenShift GitOps  |  1.20   
cert-manager Operator  |  1.19   
Cluster Logging Operator  |  6.6   
OpenShift Data Foundation  |  4.22   
SR-IOV Network Operator  |  4.22   
MetalLB  |  4.22   
NMState Operator  |  4.22   
NUMA-aware scheduler  |  4.22   
Show more

  * The cert-manager Operator and Red Hat OpenShift GitOps Operator are platform-agnostic operators. The support lifecycle for these operators is independent from the support lifecycle for OpenShift Container Platform. You might need to update to a newer minor version of these operators at the end of an operator lifecycle, or when planning to update the OpenShift Container Platform cluster to continue support. For support lifecycle details for platform-agnostic operators, see [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators).
