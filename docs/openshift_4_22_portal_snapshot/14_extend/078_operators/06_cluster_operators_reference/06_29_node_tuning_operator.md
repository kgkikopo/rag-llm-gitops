# 6.29. Node Tuning Operator

The Node Tuning Operator helps you manage node-level tuning by orchestrating the TuneD daemon and achieves low latency performance by using the Performance Profile controller. 

The majority of high-performance applications require some level of kernel tuning. The Node Tuning Operator provides a unified management interface to users of node-level sysctls and more flexibility to add custom tuning specified by user needs. 

The Operator manages the containerized TuneD daemon for OpenShift Container Platform as a Kubernetes daemon set. It ensures the custom tuning specification is passed to all containerized TuneD daemons running in the cluster in the format that the daemons understand. 

The daemons run on all nodes in the cluster, one per node. 

Node-level settings applied by the containerized TuneD daemon are rolled back on an event that triggers a profile change or when the containerized TuneD daemon is terminated gracefully by receiving and handling a termination signal. 

The Node Tuning Operator uses the Performance Profile controller to implement automatic tuning to achieve low latency performance for OpenShift Container Platform applications. 

The cluster administrator configures a performance profile to define node-level settings such as the following: 

  * Updating the kernel to kernel-rt. 
  * Choosing CPUs for housekeeping. 
  * Choosing CPUs for running workloads. 



The Node Tuning Operator is part of a standard OpenShift Container Platform installation in version 4.1 and later. 

Note

In earlier versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator. 

**Additional resources**

  * [About low latency](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#cnf-understanding-low-latency_cnf-understanding-low-latency)
  * [cluster-node-tuning-operator](https://github.com/openshift/cluster-node-tuning-operator)
