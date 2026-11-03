# Chapter 1. About hardware accelerators

Specialized hardware accelerators play a key role in the emerging generative artificial intelligence and machine learning (AI/ML) industry. Specifically, hardware accelerators are essential to the training and serving of large language and other foundational models that power this new technology. Data scientists, data engineers, ML engineers, and developers can take advantage of the specialized hardware acceleration for data-intensive transformations and model development and serving. Much of that ecosystem is open source, with several contributing partners and open source foundations. 

Red Hat OpenShift Container Platform provides support for cards and peripheral hardware that add processing units that comprise hardware accelerators: 

  * Graphical processing units (GPUs) 
  * Neural processing units (NPUs) 
  * Application-specific integrated circuits (ASICs) 
  * Data processing units (DPUs) 



![Supported hardware accelerators cards and peripherals](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hardware_accelerators-en-US/images/d9c0d6e40142a3b7b0405d0efe663ad2/OCP_HW_Accelerators_5.png) ![Supported hardware accelerators cards and peripherals](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hardware_accelerators-en-US/images/d9c0d6e40142a3b7b0405d0efe663ad2/OCP_HW_Accelerators_5.png)

Specialized hardware accelerators provide a rich set of benefits for AI/ML development: 

One platform for all
     A collaborative environment for developers, data engineers, data scientists, and DevOps 
Extended capabilities with Operators
     Operators allow for bringing AI/ML capabilities to OpenShift Container Platform 
Hybrid-cloud support
     On-premise support for model development, delivery, and deployment 
Support for AI/ML workloads
     Model testing, iteration, integration, promotion, and serving into production as services 

Red Hat provides an optimized platform to enable these specialized hardware accelerators in Red Hat Enterprise Linux (RHEL) and OpenShift Container Platform platforms at the Linux (kernel and userspace) and Kubernetes layers. To do this, Red Hat combines the proven capabilities of Red Hat OpenShift AI and Red Hat OpenShift Container Platform in a single enterprise-ready AI application platform. 

Hardware Operators use the operating framework of a Kubernetes cluster to enable the required accelerator resources. You can also deploy the provided device plugin manually or as a daemon set. This plugin registers the GPU in the cluster. 

Certain specialized hardware accelerators are designed to work within disconnected environments where a secure environment must be maintained for development and testing.

- [1.1. Hardware accelerators](01_01_hardware_accelerators.md)
