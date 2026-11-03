# 1.3. Technology Preview features status

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use. Note the following scope of support on the Red Hat Customer Portal for these features: 

[Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview)

In the following table, features are marked with the following statuses: 

  * _Not Available_
  * _Technology Preview_
  * _General Availability_
  * _Deprecated_
  * _Removed_



Important

For IBM Power and IBM Z, the following exceptions apply: 

  * For version 4.20 and later, you must run the control plane on machine types that are based on 64-bit x86 architecture or s390x architecture, and node pools on IBM Power or IBM Z. 
  * For version 4.19 and earlier, you must run the control plane on machine types that are based on 64-bit x86 architecture, and node pools on IBM Power or IBM Z. 



Table 1.1. Hosted control planes GA and TP trackerFeature| 4.20| 4.21| 4.22  
---|---|---|---  
Hosted control planes for OpenShift Container Platform using non-bare-metal agent machines  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Hosted control planes for OpenShift Container Platform on RHOSP  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Custom taints and tolerations  |  Technology Preview  |  Technology Preview  |  Technology Preview   
NVIDIA GPU devices on hosted control planes for OpenShift Virtualization  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Hosted control planes for OpenShift Virtualization on IBM Z [1] |  Not Available  |  Technology Preview  |  General Availability   
Hosted control planes on IBM Z in a disconnected environment  |  General Availability  |  General Availability  |  General Availability   
Hosted control planes for OpenShift Container Platform on Microsoft Azure  |  Not Available  |  Not Available  |  Technology Preview   
Backup and restore with the etcd snapshot method  |  Not Available  |  Not Available  |  Technology Preview   
Restoring a hosted cluster to a new management cluster by using OADP  |  Technology Preview  |  Technology Preview  |  Technology Preview   
Show more

  1. Hosted control planes for OpenShift Virtualization on IBM Z is supported as Technology Preview starting with OpenShift Container Platform 4.21, multicluster engine for Kubernetes Operator 2.11, and Red Hat Advanced Cluster Management (RHACM) 2.16. Creating hosted control planes with external infrastructure is not supported.
