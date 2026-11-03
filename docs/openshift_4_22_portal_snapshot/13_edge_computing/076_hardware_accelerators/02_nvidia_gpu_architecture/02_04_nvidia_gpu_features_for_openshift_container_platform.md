# 2.4. NVIDIA GPU features for OpenShift Container Platform

Learn about the NVIDIA GPU features, software components, and monitoring tools available to accelerate containerized workloads in OpenShift Container Platform. 

NVIDIA Container Toolkit
     By using the NVIDIA Container Toolkit, you can create and run GPU-accelerated containers. The toolkit includes a container runtime library and utilities to automatically configure containers to use NVIDIA GPUs. 
NVIDIA AI Enterprise
    

NVIDIA AI Enterprise is an end-to-end, cloud-native suite of AI and data analytics software optimized, certified, and supported with NVIDIA-Certified systems. 

NVIDIA AI Enterprise includes support for Red Hat OpenShift Container Platform. The following installation methods are supported: 

  * OpenShift Container Platform on bare metal or VMware vSphere with GPU Passthrough. 
  * OpenShift Container Platform on VMware vSphere with NVIDIA vGPU. 



GPU Feature Discovery
    

NVIDIA GPU Feature Discovery for Kubernetes is a software component that you can use to automatically generate labels for the GPUs available on a node. GPU Feature Discovery uses node feature discovery (NFD) to perform this labeling. 

The Node Feature Discovery Operator (NFD) manages the discovery of hardware features and configurations in an OpenShift Container Platform cluster by labeling nodes with hardware-specific information. NFD labels the host with node-specific attributes, such as PCI cards, kernel, OS version, and so on. 

You can find the NFD Operator in the Operator Hub by searching for “Node Feature Discovery”. 

NVIDIA GPU Operator with OpenShift Virtualization
    

The GPU Operator only provisioned worker nodes to run GPU-accelerated containers. The GPU Operator can also provision worker nodes for running GPU-accelerated virtual machines (VMs). 

You can configure the GPU Operator to deploy different software components to worker nodes depending on which GPU workload is configured to run on those nodes. 

GPU Monitoring dashboard
     You can install a monitoring dashboard to display GPU usage information on the cluster **Observe** page in the OpenShift Container Platform web console. GPU utilization information includes the number of available GPUs, power consumption (in watts), temperature (in degrees Celsius), utilization (in percent), and other metrics for each GPU. 

**Additional resources**

  * [NVIDIA-Certified Systems](https://docs.nvidia.com/ngc/ngc-deploy-on-premises/nvidia-certified-systems/index.html)
  * [NVIDIA AI Enterprise](https://docs.nvidia.com/ai-enterprise/index.html#deployment-guides)
  * [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html#)
  * [Enabling the GPU Monitoring Dashboard](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/enable-gpu-monitoring-dashboard.html)
  * [MIG Support in OpenShift Container Platform](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/mig-ocp.html)
  * [Time-slicing NVIDIA GPUs in OpenShift](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/time-slicing-gpus-in-openshift.html)
  * [Deploy GPU Operators in a disconnected or airgapped environment](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/mirror-gpu-ocp-disconnected.html)
  * [Node Feature Discovery Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/specialized_hardware_and_driver_enablement/#node-feature-discovery-operator)
