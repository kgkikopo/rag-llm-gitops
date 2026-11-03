# 1.1. Managing Windows container workloads

With a Red Hat subscription, you can get support for running Windows workloads in OpenShift Container Platform. 

Windows instances deployed by the WMCO are configured with the containerd container runtime. For more information, see the [release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/release-notes#windows-containers-release-notes "2.1. Red Hat OpenShift support for Windows Containers release notes"). 

You can add Windows nodes either by creating a [compute machine set](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/creating-windows-machine-sets#creating-windows-machineset-aws "6.1. Creating a Windows machine set on AWS") or by specifying existing Bring-Your-Own-Host (BYOH) Windows instances through a [ConfigMap](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/byoh-windows-instance "Chapter 9. Using Bring-Your-Own-Host \(BYOH\) Windows instances as nodes"). 

Note

Compute machine sets are not supported for bare metal or provider agnostic clusters. 

For workloads including both Linux and Windows, OpenShift Container Platform allows you to deploy Windows workloads running on Windows Server containers while also providing traditional Linux workloads hosted on Red Hat Enterprise Linux CoreOS (RHCOS) or Red Hat Enterprise Linux (RHEL). For more information, see [getting started with Windows container workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/understanding-windows-container-workloads "Chapter 4. Understanding Windows container workloads"). 

You need the WMCO to run Windows workloads in your cluster. The WMCO orchestrates the process of deploying and managing Windows workloads on a cluster. For more information, see [how to enable Windows container workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/enabling-windows-container-workloads "Chapter 5. Enabling Windows container workloads"). 

You can create a Windows `MachineSet` object to create infrastructure Windows machine sets and related machines so that you can move supported Windows workloads to the new Windows machines. You can create a Windows `MachineSet` object on multiple platforms. 

You can [schedule Windows workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/scheduling-windows-workloads "Chapter 7. Scheduling Windows container workloads") to Windows compute nodes. 

You can [perform Windows Machine Config Operator upgrades](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/windows-node-upgrades "Chapter 8. Windows node updates") to ensure that your Windows nodes have the latest updates. 

You can [remove a Windows node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/removing-windows-nodes "Chapter 10. Removing Windows nodes") by deleting a specific machine. 

You can [use Bring-Your-Own-Host (BYOH) Windows instances](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/byoh-windows-instance "Chapter 9. Using Bring-Your-Own-Host \(BYOH\) Windows instances as nodes") to repurpose Windows Server VMs and bring them to OpenShift Container Platform. BYOH Windows instances benefit users who are looking to mitigate major disruptions when a Windows server goes offline. You can use BYOH Windows instances as nodes on OpenShift Container Platform 4.8 and later versions. 

You can [disable Windows container workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_container_support_for_openshift/disabling-windows-container-workloads "Chapter 11. Disabling Windows container workloads") by performing the following: 

  * Uninstalling the Windows Machine Config Operator 
  * Deleting the Windows Machine Config Operator namespace
