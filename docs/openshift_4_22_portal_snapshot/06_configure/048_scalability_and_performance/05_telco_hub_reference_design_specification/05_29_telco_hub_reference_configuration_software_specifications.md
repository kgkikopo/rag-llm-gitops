# 5.29. Telco hub reference configuration software specifications

The following y-stream versions were used in validation of the telco hub solution for OpenShift Container Platform clusters. 

Hub Cluster Component| Software Version (y-stream)  
---|---  
OpenShift Container Platform  |  4.22   
Red Hat Advanced Cluster Management (RHACM)  |  2.17   
Local Storage Operator  |  4.22   
cert-manager Operator  |  1.19   
Red Hat OpenShift Data Foundation (ODF)  |  4.22   
Red Hat OpenShift GitOps  |  1.20   
GitOps Zero Touch Provisioning (ZTP) plugins  |  4.22   
multicluster engine Operator PolicyGenerator plugin  |  2.17   
Topology Aware Lifecycle Manager (TALM)  |  4.22   
Cluster Logging Operator  |  6.6   
OpenShift API for Data Protection (OADP)  |  The version aligned with the RHACM release.   
Show more

  * The cert-manager Operator and Red Hat OpenShift GitOps Operator are platform agnostic operators. The support lifecycle for these operators is independent from the support lifecycle for OpenShift Container Platform. You might need to update to a newer minor version of these operators at the end of an operator lifecycle, or when planning to update the OpenShift Container Platform cluster to continue support. For support lifecycle details for platform agnostic operators, see [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators).
