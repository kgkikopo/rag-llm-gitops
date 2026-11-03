# 4.1. Windows workload management

To run Windows workloads in your cluster, you must install the Windows Machine Config Operator (WMCO). 

The WMCO is a Linux-based Operator that runs on the Linux-based control plane and compute nodes. The WMCO orchestrates the process of deploying and managing Windows workloads on a cluster. 

**Figure 4.1. WMCO design**

![WMCO workflow](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Windows_Container_Support_for_OpenShift-en-US/images/bfe7300bcc0854c5fcb33a95dceccab4/wmco-design.png) ![WMCO workflow](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Windows_Container_Support_for_OpenShift-en-US/images/bfe7300bcc0854c5fcb33a95dceccab4/wmco-design.png)

Before deploying Windows workloads, you must create a Windows compute node and have it join the cluster. The Windows node hosts the Windows workloads in a cluster, and can run alongside other Linux-based compute nodes. You can create a Windows compute node by creating a Windows compute machine set to host Windows Server compute machines. You must apply a Windows-specific label to the compute machine set that specifies a Windows OS image. 

The WMCO watches for machines with the Windows label. After a Windows compute machine set is detected and its respective machines are provisioned, the WMCO configures the underlying Windows virtual machine (VM) so that it can join the cluster as a compute node. 

**Figure 4.2. Mixed Windows and Linux workloads**

![Mixed Windows and Linux workloads](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Windows_Container_Support_for_OpenShift-en-US/images/517c5b787e48f59fb48fabca18cb2bc0/mixed-windows-linux-workloads.png) ![Mixed Windows and Linux workloads](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Windows_Container_Support_for_OpenShift-en-US/images/517c5b787e48f59fb48fabca18cb2bc0/mixed-windows-linux-workloads.png)

The WMCO expects a predetermined secret in its namespace containing a private key that is used to interact with the Windows instance. WMCO checks for this secret during boot up time and creates a user data secret which you must reference in the Windows `MachineSet` object that you created. Then the WMCO populates the user data secret with a public key that corresponds to the private key. With this data in place, the cluster can connect to the Windows VM using an SSH connection. 

After the cluster establishes a connection with the Windows VM, you can manage the Windows node using similar practices as you would a Linux-based node. 

Note

The OpenShift Container Platform web console provides most of the same monitoring capabilities for Windows nodes that are available for Linux nodes. However, the ability to monitor workload graphs for pods running on Windows nodes is not available at this time. 

Scheduling Windows workloads to a Windows node can be done with typical pod scheduling practices, such as taints, tolerations, and node selectors. Alternatively, you can differentiate your Windows workloads from Linux workloads and other Windows-versioned workloads by using a `RuntimeClass` object.
