# 2.2. NVIDIA GPU enablement

NVIDIA GPU enablement makes GPU hardware available to workloads that run on OpenShift Container Platform clusters. 

The following diagram shows how the GPU architecture is enabled for OpenShift: 

**Figure 2.1. NVIDIA GPU enablement**

![NVIDIA GPU enablement](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hardware_accelerators-en-US/images/ab8a6807e4b1b8561dd9cf7d895315fc/512_OpenShift_NVIDIA_GPU_enablement_1223.png) ![NVIDIA GPU enablement](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hardware_accelerators-en-US/images/ab8a6807e4b1b8561dd9cf7d895315fc/512_OpenShift_NVIDIA_GPU_enablement_1223.png)

Note

MIG is supported on GPUs starting with the NVIDIA Ampere generation. For a list of GPUs that support MIG, see "NVIDIA MIG User Guide. 

**Additional resources**

  * [NVIDIA MIG User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#supported-gpus)



## 2.2.1. GPUs and bare metal

You can deploy OpenShift Container Platform on an NVIDIA-certified bare-metal server. However, consider several limitations that might affect your objectives. 

The following list details these limitations: 

  * Control plane nodes can be CPU nodes. 
  * Worker nodes must be GPU nodes, provided that AI/ML workloads are executed on these worker nodes. 

In addition, the worker nodes can host one or more GPUs, but they must be of the same type. For example, a node can have two NVIDIA A100 GPUs, but a node with one A100 GPU and one T4 GPU is not supported. The NVIDIA Device Plugin for Kubernetes does not support mixing different GPU models on the same node. 

  * When using OpenShift Container Platform, note that one or three or more servers are required. Clusters with two servers are not supported. The single server deployment is called single-node OpenShift and using this configuration results in a non-high availability OpenShift Container Platform environment. 



You can choose one of the following methods to access the containerized GPUs: 

  * GPU passthrough 
  * Multi-Instance GPU (MIG) 



**Additional resources**

  * [Red Hat OpenShift on Bare Metal Stack](https://docs.nvidia.com/ai-enterprise/deployment-guide-openshift-on-bare-metal/0.1.0/on-bare-metal.html)



## 2.2.2. GPUs and virtualization

With OpenShift Virtualization, you can develop and maintain applications that run on virtual machines (VMs). These capabilities enable enterprises to incorporate VMs into containerized workflows within clusters. 

Many developers and enterprises are moving to containerized applications and serverless infrastructures, but interest exists in developing and maintaining applications that run on virtual machines (VMs). 

You can choose one of the following methods to connect the worker nodes to the GPUs: 

  * GPU passthrough to access and use GPU hardware within a VM. 
  * GPU (vGPU) time-slicing, when GPU compute capacity is not saturated by workloads. 



**Additional resources**

  * [NVIDIA GPU Operator with OpenShift Virtualization](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/openshift/openshift-virtualization.html)



## 2.2.3. GPUs and vSphere

You can deploy OpenShift Container Platform on an NVIDIA-certified VMware vSphere server that can host different GPU types. 

An NVIDIA GPU driver must be installed in the hypervisor if vGPU instances are used by the VMs. For vSphere, this host driver is provided in the form of a VIB file. 

The maximum number of vGPUs that can be allocated to worker node VMs depends on the version of vSphere: 

  * vSphere 7.0: maximum 4 vGPU per VM 
  * vSphere 8.0: maximum 8 vGPU per VM 

Note

vSphere 8.0 introduced support for multiple full or fractional heterogeneous profiles associated with a VM. 




You can choose one of the following methods to attach the worker nodes to the GPUs: 

  * GPU passthrough for accessing and using GPU hardware within a virtual machine (VM) 
  * GPU (vGPU) time-slicing, when not all of the GPU is needed 



Similar to bare-metal deployments, one or three or more servers are required. Clusters with two servers are not supported. 

**Additional resources**

  * [OpenShift Container Platform on VMware vSphere with NVIDIA vGPUs](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/openshift/nvaie-with-ocp.html#openshift-container-platform-on-vmware-vsphere-with-nvidia-vgpus)



## 2.2.4. GPUs and Red Hat KVM

You can use OpenShift Container Platform on an NVIDIA-certified kernel-based virtual machine (KVM) server. Similar to bare metal deployments, one or three or more servers are required. 

Clusters with two servers are not supported. 

However, unlike bare metal deployments, you can use different types of GPUs in the server. This is because you can assign these GPUs to different VMs that act as Kubernetes nodes. The only limitation is that a Kubernetes node must have the same set of GPU types at its own level. 

You can choose one of the following methods to access the containerized GPUs: 

  * GPU passthrough for accessing and using GPU hardware within a virtual machine (VM) 
  * GPU (vGPU) time-slicing when not all of the GPU is needed 



To enable the vGPU capability, a special driver must be installed at the host level. This driver is delivered as an RPM package. This host driver is not required for GPU passthrough allocation. 

## 2.2.5. GPUs and CSPs

You can deploy OpenShift Container Platform to one of the major cloud service providers (CSPs): Amazon Web Services (AWS), Google Cloud, or Microsoft Azure. 

Two modes of operation are available: a fully managed deployment and a self-managed deployment. 

  * In a fully managed deployment, everything is automated by Red Hat in collaboration with CSP. You can request an OpenShift Container Platform instance through the CSP web console, and the cluster is automatically created and fully managed by Red Hat. Red Hat manages infrastructure operations, including node failure recovery and environment maintenance. Red Hat is fully responsible for maintaining the uptime of the cluster. The fully managed services are available on AWS, Azure, and Google Cloud. For AWS, the OpenShift Container Platform service is called (Red Hat OpenShift Container Platform Service on AWS). For Azure, the service is called Azure Red Hat OpenShift. For Google Cloud, the service is called OpenShift Dedicated on Google Cloud. 
  * In a self-managed deployment, you are responsible for instantiating and maintaining the OpenShift Container Platform cluster. Red Hat provides the OpenShift Container Platform install utility to support the deployment of the OpenShift Container Platform cluster in this case. The self-managed services are available globally to all CSPs. 



Important

The compute instance must be a GPU-accelerated compute instance. Additionally, the GPU type must match the list of supported GPUs from NVIDIA AI Enterprise. For example, T4, V100, and A100 are part of this list. 

You can choose one of the following methods to access the containerized GPUs: 

  * GPU passthrough to access and use GPU hardware within a virtual machine (VM). 
  * GPU (vGPU) time slicing when the entire GPU is not required. 



**Additional resources**

  * [Red Hat Openshift in the Cloud](https://docs.nvidia.com/ai-enterprise/deployment-guide-cloud/0.1.0/aws-redhat-openshift.html)



## 2.2.6. GPUs and Red Hat Device Edge

Red Hat Device Edge provides access to MicroShift. MicroShift provides the simplicity of a single-node deployment with the functionality and services you need for resource-constrained (edge) computing. 

Red Hat Device Edge meets the needs of bare-metal, virtual, containerized, or Kubernetes workloads deployed in resource-constrained environments. 

You can enable NVIDIA GPUs on containers in a Red Hat Device Edge environment. 

You use GPU passthrough to access the containerized GPUs. 

**Additional resources**

  * [How to accelerate workloads with NVIDIA GPUs on Red Hat Device Edge](https://cloud.redhat.com/blog/how-to-accelerate-workloads-with-nvidia-gpus-on-red-hat-device-edge)
