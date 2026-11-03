# Chapter 5. NVIDIA GPUDirect Remote Direct Memory Access (RDMA)

NVIDIA GPUDirect Remote Direct Memory Access (RDMA) allows for an application in one computer to directly access the memory of another computer without needing access through the operating system. This provides the ability to bypass kernel intervention in the process, freeing up resources and greatly reducing the CPU overhead normally needed to process network communications. This is useful for distributing GPU-accelerated workloads across clusters. And because RDMA is so suited toward high bandwidth and low latency applications, this makes it ideal for big data and machine learning applications. 

There are currently three configuration methods for NVIDIA GPUDirect RDMA: 

Shared device
     This method allows for an NVIDIA GPUDirect RDMA device to be shared among multiple pods on the OpenShift Container Platform worker node where the device is exposed. 
Host device
     This method provides direct physical Ethernet access on the worker node by creating an additional host network on a pod. A plugin allows the network device to be moved from the host network namespace to the network namespace on the pod. 
SR-IOV legacy device
     The Single Root IO Virtualization (SR-IOV) method can share a single network device, such as an Ethernet adapter, with multiple pods. SR-IOV segments the device, recognized on the host node as a physical function (PF), into multiple virtual functions (VFs). The VF is used like any other network device. 

Each of these methods can be used across either the NVIDIA GPUDirect RDMA over Converged Ethernet (RoCE) or Infiniband infrastructures, providing an aggregate total of six methods of configuration.

- [5.1. NVIDIA GPUDirect RDMA prerequisites](05_01_nvidia_gpudirect_rdma_prerequisites.md)
- [5.2. Disabling the IRDMA kernel module](05_02_disabling_the_irdma_kernel_module.md)
- [5.3. Creating persistent naming rules](05_03_creating_persistent_naming_rules.md)
- [5.4. Configuring the NFD Operator](05_04_configuring_the_nfd_operator.md)
- [5.5. Configuring the SR-IOV Operator](05_05_configuring_the_sr_iov_operator.md)
- [5.6. Configuring the NVIDIA network Operator](05_06_configuring_the_nvidia_network_operator.md)
- [5.7. Configuring the GPU Operator](05_07_configuring_the_gpu_operator.md)
- [5.8. Creating the machine configuration](05_08_creating_the_machine_configuration.md)
- [5.9. Creating the workload pods](05_09_creating_the_workload_pods.md)
- [5.10. Verifying RDMA connectivity](05_10_verifying_rdma_connectivity.md)
