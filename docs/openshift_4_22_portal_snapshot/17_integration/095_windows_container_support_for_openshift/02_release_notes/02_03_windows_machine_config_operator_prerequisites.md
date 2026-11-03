# 2.3. Windows Machine Config Operator prerequisites

You can review the following information for details on the supported platform versions, Windows Server versions, and networking configurations for the Windows Machine Config Operator (WMCO). See the vSphere documentation for any information that is relevant to only that platform. 

## 2.3.1. WMCO supported installation method

The WMCO fully supports installing Windows nodes into installer-provisioned infrastructure (IPI) clusters. This is the preferred OpenShift Container Platform installation method. 

For user-provisioned infrastructure (UPI) clusters, the WMCO supports installing Windows nodes only into a UPI cluster installed with the `platform: none` field set in the `install-config.yaml` file (bare-metal or provider-agnostic) and only for the [BYOH (Bring Your Own Host)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/byoh-windows-instance "Chapter 9. Using Bring-Your-Own-Host \(BYOH\) Windows instances as nodes") use case. UPI is not supported for any other platform. 

## 2.3.2. WMCO supported platforms and Windows Server versions

The following table lists the [Windows Server versions](https://docs.microsoft.com/en-us/windows/release-health/windows-server-release-info) that are supported by WMCO 10.20.0, based on the applicable platform. Windows Server versions not listed are not supported and attempting to use them will cause errors. To prevent these errors, use only an appropriate version for your platform. 

Platform| Supported Windows Server version  
---|---  
Amazon Web Services (AWS)  | 

  * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later 
  * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later [1]
  * Windows Server 2019, version 1809 

  
Microsoft Azure  | 

  * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later 
  * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later 
  * Windows Server 2019, version 1809 

  
VMware vSphere  | 

  * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later 
  * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later 

  
Google Cloud  | 

  * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later 
  * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later 

  
Nutanix  | 

  * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later 
  * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later 

  
Bare metal or provider agnostic  | 

  * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later 
  * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later 

  
Show more

  1. For disconnected clusters, the Windows AMI must have the EC2LaunchV2 agent version 2.0.2107 or later installed. For more information, see "Install the latest version of EC2Launch v2 (AWS documentation)". 



## 2.3.3. Supported networking

Hybrid networking with OVN-Kubernetes is the only supported networking configuration. See the additional resources below for more information on this functionality. The following tables outline the type of networking configuration and Windows Server versions to use based on your platform. You must specify the network configuration when you install the cluster. 

Note

  * The WMCO does not support OVN-Kubernetes without hybrid networking or OpenShift SDN. 
  * Dual NIC is not supported on WMCO-managed Windows instances. 



Table 2.1. Platform networking supportPlatform| Supported networking  
---|---  
Amazon Web Services (AWS)  |  Hybrid networking with OVN-Kubernetes   
Microsoft Azure  |  Hybrid networking with OVN-Kubernetes   
VMware vSphere  |  Hybrid networking with OVN-Kubernetes with a custom VXLAN port   
Google Cloud  |  Hybrid networking with OVN-Kubernetes   
Nutanix  |  Hybrid networking with OVN-Kubernetes   
Bare metal or provider agnostic  |  Hybrid networking with OVN-Kubernetes   
Show more

Table 2.2. Hybrid OVN-Kubernetes Windows Server supportHybrid networking with OVN-Kubernetes| Supported Windows Server version  
---|---  
Default VXLAN port  | 

  * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later 
  * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later 
  * Windows Server 2019, version 1809 

  
Custom VXLAN port  | 

  * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later 
  * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later 

  
Show more

**Additional resources**

  * [Hybrid networking](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#configuring-hybrid-networking)
