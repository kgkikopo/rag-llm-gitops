# 2.1. Overview of ephemeral storage

Use ephemeral storage to provide temporary local storage for stateless applications that only need data for the duration of the pod lifecycle, such as caches, scratch files, and logs that do not need to persist after the pod terminates. 

Both developers and administrators can use this feature. 

Pods and containers can require ephemeral or transient local storage for their operation. The lifetime of this ephemeral storage does not extend beyond the life of the individual pod, and this ephemeral storage cannot be shared across pods. 

Issues related to the lack of local storage accounting and isolation include the following: 

  * Pods cannot detect how much local storage is available to them. 
  * Pods cannot request guaranteed local storage. 
  * Local storage is a best-effort resource. 
  * Pods can be evicted due to other pods filling the local storage, after which new pods are not admitted until sufficient storage is reclaimed. 



Unlike persistent volumes, ephemeral storage is unstructured and the space is shared between all pods running on a node, in addition to other uses by the system, the container runtime, and OpenShift Container Platform. The ephemeral storage framework allows pods to specify their transient local storage needs. It also allows OpenShift Container Platform to schedule pods where appropriate, and to protect the node against excessive use of local storage. 

While the ephemeral storage framework allows administrators and developers to better manage local storage, I/O throughput and latency are not directly affected.
