# 2.3. GPU sharing methods

Red Hat and NVIDIA have developed GPU concurrency and sharing mechanisms to simplify GPU-accelerated computing on an enterprise-level OpenShift Container Platform cluster. 

Applications typically have different compute requirements that can leave GPUs underutilized. Providing the right amount of compute resources for each workload is critical to reduce deployment cost and maximize GPU utilization. 

Concurrency mechanisms for improving GPU utilization exist in the range from programming model APIs to system software and hardware partitioning, including virtualization. 

The following list shows the GPU concurrency mechanisms: 

  * Compute Unified Device Architecture (CUDA) streams 
  * Time-slicing 
  * CUDA Multi-Process Service (MPS) 
  * Multi-instance GPU (MIG) 
  * Virtualization with vGPU 



Consider the following GPU sharing suggestions when using the GPU concurrency mechanisms for different OpenShift Container Platform scenarios: 

Bare metal
     vGPU is not available. Consider using MIG-enabled cards. 
VMs
     vGPU is the preferred choice. 
Older NVIDIA cards with no MIG on bare metal
     Consider using time-slicing. 
VMs with multiple GPUs and you want passthrough and vGPU
     Consider using separate VMs. 
Bare metal with OpenShift Virtualization and multiple GPUs
     Consider using pass-through for hosted VMs and time-slicing for containers. 

**Additional resources**

  * [Improving GPU Utilization](https://developer.nvidia.com/blog/improving-gpu-utilization-in-kubernetes/)



## 2.3.1. CUDA streams

Compute Unified Device Architecture (CUDA) is a parallel computing platform and programming model developed by NVIDIA for general computing on GPUs. 

A stream is a sequence of operations that executes in issue-order on the GPU. CUDA commands are typically executed sequentially in a default stream and a task does not start until a preceding task has completed. 

Asynchronous processing of operations across different streams allows for parallel execution of tasks. A task issued in one stream runs before, during, or after another task is issued into another stream. This task process allows the GPU to run multiple tasks simultaneously in no prescribed order, leading to improved performance. 

**Additional resources**

  * [Asynchronous Concurrent Execution](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#asynchronous-concurrent-execution)



## 2.3.2. Time-slicing

GPU time-slicing interleaves workloads scheduled on overloaded GPUs when you are running multiple CUDA applications. 

You can enable time-slicing of GPUs on Kubernetes by defining a set of replicas for a GPU, each of which can be independently distributed to a pod to run workloads on. Unlike multi-instance GPU (MIG), no memory or fault isolation between replicas, but for some workloads this is better than not sharing at all. Internally, GPU time-slicing is used to multiplex workloads from replicas of the same underlying GPU. 

You can apply a cluster-wide default configuration for time-slicing. You can also apply node-specific configurations. For example, you can apply a time-slicing configuration only to nodes with Tesla T4 GPUs and not modify nodes with other GPU models. 

You can combine these two approaches by applying a cluster-wide default configuration and then labeling nodes to give those nodes a node-specific configuration. 

## 2.3.3. CUDA Multi-Process Service

CUDA Multi-Process Service (MPS) allows a single GPU to use multiple CUDA processes. The processes run in parallel on the GPU, eliminating saturation of the GPU compute resources. 

MPS also enables concurrent execution, or overlapping, of kernel operations and memory copying from different processes to enhance utilization. 

**Additional resources**

  * [CUDA MPS](https://docs.nvidia.com/deploy/mps/index.html)



## 2.3.4. Multi-instance GPU

Using Multi-instance GPU (MIG), you can split GPU compute units and memory into multiple MIG instances. Each of these instances represents a standalone GPU device from a system perspective and can be connected to any application, container, or virtual machine running on the node. 

The software that uses the GPU treats each of these MIG instances as an individual GPU. 

MIG is useful when you have an application that does not require the full power of an entire GPU. By using the MIG feature of the new NVIDIA Ampere architecture, you can split your hardware resources into multiple GPU instances, each of which is available to the operating system as an independent CUDA-enabled GPU. 

NVIDIA GPU Operator version 1.7.0 and later provides MIG support for the A100 and A30 Ampere cards. These GPU instances are designed to support up to seven independent CUDA applications so that they operate completely isolated with dedicated hardware resources. 

**Additional resources**

  * [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/)



## 2.3.5. Virtualization with vGPU

Virtual machines (VMs) can directly access a single physical GPU using NVIDIA vGPU. You can create virtual GPUs that can be shared by VMs across the enterprise and accessed by other devices. 

This capability combines the power of GPU performance with the management and security benefits that vGPU provides. The following list details additional benefits provided by vGPU: 

  * Proactive management and monitoring for your VM environment 
  * Workload balancing for mixed VDI and compute workloads 
  * Resource sharing across multiple VMs 



**Additional resources**

  * [Virtual GPUs](https://www.nvidia.com/en-us/data-center/virtual-solutions/)
