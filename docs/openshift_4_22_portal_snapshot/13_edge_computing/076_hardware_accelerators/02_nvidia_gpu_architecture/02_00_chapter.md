# Chapter 2. NVIDIA GPU architecture

NVIDIA supports the use of graphics processing unit (GPU) resources on OpenShift Container Platform. OpenShift Container Platform is a security-focused and hardened Kubernetes platform developed and supported by Red Hat for deploying and managing Kubernetes clusters at scale. OpenShift Container Platform includes enhancements to Kubernetes so that users can easily configure and use NVIDIA GPU resources to accelerate workloads. 

The NVIDIA GPU Operator uses the Operator framework within OpenShift Container Platform to manage the full lifecycle of NVIDIA software components required to run GPU-accelerated workloads. 

These components include the NVIDIA drivers (to enable CUDA), the Kubernetes device plugin for GPUs, the NVIDIA Container Toolkit, automatic node tagging using GPU feature discovery (GFD), DCGM-based monitoring, and others. 

Note

The NVIDIA GPU Operator is only supported by NVIDIA. For more information about obtaining support from NVIDIA, see [Obtaining Support from NVIDIA](https://access.redhat.com/solutions/5174941).

- [2.1. NVIDIA GPU prerequisites](02_01_nvidia_gpu_prerequisites.md)
- [2.2. NVIDIA GPU enablement](02_02_nvidia_gpu_enablement.md)
- [2.3. GPU sharing methods](02_03_gpu_sharing_methods.md)
- [2.4. NVIDIA GPU features for OpenShift Container Platform](02_04_nvidia_gpu_features_for_openshift_container_platform.md)
