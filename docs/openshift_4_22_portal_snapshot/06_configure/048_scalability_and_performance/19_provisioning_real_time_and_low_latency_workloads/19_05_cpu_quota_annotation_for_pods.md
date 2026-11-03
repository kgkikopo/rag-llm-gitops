# 19.5. CPU quota annotation for pods

On OpenShift Container Platform, you do not need the `cpu-quota.crio.io` annotation to disable the CPU completely fair scheduler (CFS) quota for pods. 

Starting in OpenShift Container Platform 4.20, the kubelet automatically disables the CPU CFS quota (which prevents CPU throttling) for pods that meet all of the following: 

  * The pod has a `Guaranteed` quality of service (`QoS`) class. 
  * The pod requests whole CPUs. 
  * The CPU manager static policy is enabled, for example by a performance profile. 



If your workloads already include the `cpu-quota.crio.io: "disable"` annotation, you can leave it in place. The annotation has no effect because the kubelet provides this functionality automatically. 

**Additional resources**

  * [Recommended firmware configuration for vDU cluster hosts](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-du-firmware-config-reference_vdu-config-ref)
