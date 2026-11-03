# 2.1. NVIDIA GPU prerequisites

Before using graphics processing unit (GPU) resources on OpenShift Container Platform, you must meet certain prerequisites so that NVIDIA GPU resources can effectively accelerate workloads. 

The following list details these prerequisites: 

  * You have a working OpenShift Container Platform cluster with at least one GPU worker node. 
  * You have access to the OpenShift Container Platform cluster as a `cluster-admin` to perform the required steps. 
  * You installed OpenShift CLI (`oc`). 
  * You installed the node feature discovery (NFD) Operator and created a `nodefeaturediscovery` instance.
