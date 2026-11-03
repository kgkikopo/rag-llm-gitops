# 5.7. Hub cluster topology

In production environments, the OpenShift Container Platform hub cluster must be highly available to maintain high availability of the management functions. 

Limits and requirements
    

Use a highly available cluster topology for the hub cluster, for example: 

  * Compact (3 nodes combined control plane and compute nodes) 
  * Standard (3 control plane nodes + N compute nodes) 



Engineering considerations
    

  * In non-production environments, a single-node OpenShift cluster can be used for limited hub cluster functionality. 
  * Certain capabilities, for example Red Hat OpenShift Data Foundation, are not supported on single-node OpenShift. In this configuration, some hub cluster features might not be available. 
  * The number of optional compute nodes can vary depending on the scale of the specific use case. 
  * Compute nodes can be added later as required. 
  * Consult the 4.21 release notes regarding the decrease in the default maximum open files soft limit for containers in this release. 



**Additional resources**

  * [OpenShift Container Platform architecture](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/overview/#architecture)
  * [Postinstallation node tasks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#post-install-node-tasks)
