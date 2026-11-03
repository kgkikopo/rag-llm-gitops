# 3.1. Getting started with OpenShift Virtualization

Explore OpenShift Virtualization by taking guided tours, installing the Operator, and configuring a basic environment. Learn how to migrate from your current platform, then learn more about how to deploy and manage virtual machines (VMs) by following the additional resources links. 

Note

Cluster configuration procedures require `cluster-admin` privileges. 

## 3.1.1. Take the Getting started tour

The **Getting started** tour introduces several key aspects of using OpenShift Virtualization. There are two ways to start the tour. 

**Prerequisites**

  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  * If you see the **Welcome to OpenShift Virtualization** dialog, click **Start Tour**. 
  * Otherwise, go to **Virtualization** **Settings** **User** **Getting started resources** **Guided tour**. 



## 3.1.2. Take a quick start tour

You can explore several OpenShift Virtualization capabilities by taking quick start tours in the web console. 

**Prerequisites**

  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  1. Click the **Help** icon **?** in the menu bar on the header of the OpenShift Container Platform web console. 
  2. Select **Quick Starts**. You can filter the list of tours by entering the keyword `virtual` in the **Filter** field. 



## 3.1.3. Self-service Technical Supportability Review

You can use the self-service Technical Supportability Review (TSR) on the Red Hat Customer Portal to validate your cluster configuration against Red Hat common practices. 

Note

The `must-gather` tool collects diagnostic information about your cluster, including resource definitions, service logs, and configuration data. For more information, see "Gathering data about your cluster" in the OpenShift Container Platform documentation. 

The self-service TSR uses AI to evaluate your cluster’s `must-gather` data and provides a prioritized executive summary of recommendations. This serves as a starting point to help you identify and resolve potential issues before they impact your environment. 

The TSR performs hundreds of checks across the OpenShift Container Platform platform, including OpenShift Virtualization. Coverage is continually expanding. 

### 3.1.3.1. When to use the self-service TSR tool

Integrating the self-service TSR into your regular operational workflow can be helpful in the following scenarios: 

Routine benchmarking
     Use the TSR quarterly to benchmark cluster health and plan for routine maintenance activities. 
Pre-flight checks
     Validate your cluster configuration before major structural changes, including upgrades, migrations, and expansions. 
Critical event preparation
     Confirm cluster stability ahead of high-traffic business events, such as seasonal peaks, or operational milestones, such as year-end shutdowns, business continuity drills, and compliance audits. 

### 3.1.3.2. How to access the TSR

To run a self-service review, upload your cluster’s `must-gather` data to the **Analyze** tab in the **Support** section of the Red Hat Customer Portal. For a direct link, see "Technical Supportability Review with AI tool" in the Additional resources section. The **Analyze** feature generates a prioritized executive summary that identifies your cluster’s top risks and recommends corrective actions. Review the recommendations and implement the suggested corrective actions to address the identified risks. 

The self-service TSR provides a solid baseline for cluster health. If you need additional guidance or a more comprehensive review, contact your Red Hat account team to arrange an assisted review through a Technical Account Manager (TAM) or Red Hat consultant. An assisted review includes human analysis, deeper coverage, and access to checks that are updated more frequently than the self-service version. 

### 3.1.3.3. Additional resources

  * [Technical Supportability Review with AI tool](https://access.redhat.com/support/cases/#/analyze)
  * [Red Hat Technical Supportability Review with AI: Proactive AI-Driven Cluster Assessments for OpenShift Container Platform](https://access.redhat.com/solutions/7141255)



## 3.1.4. Additional resources

  * [Plan your bare-metal cluster for OpenShift Virtualization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#virt-planning-bare-metal-cluster-for-ocp-virt_preparing-to-install-on-bare-metal)
  * [Prepare your cluster for OpenShift Virtualization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#preparing-cluster-for-virt "4.1. Preparing your cluster for OpenShift Virtualization")
  * [Learn about storage volumes for VM disks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#virt-about-storage-volumes-for-vm-disks_virt-requirements "4.2.3.2. Volume and access modes for VM disks")
  * [Use a CSI-enabled storage provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi)
  * [Configure local storage for virtual machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/storage#virt-configuring-local-storage-with-hpp "10.6. Configuring local storage by using the hostpath provisioner")
  * [Install the OpenShift Virtualization Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#virt-installing-virt-operator_installing-virt "4.3.2. Install the OpenShift Virtualization Operator by using the web console")
  * [Install the Kubernetes NMState Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-the-kubernetes-nmstate-operator-cli_k8s-nmstate-about-the-k8s-nmstate-operator)
  * [Specify nodes for virtual machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-specifying-nodes-for-vms "8.18.3. Specifying nodes for virtual machines")
  * [Install and use the `virtctl` command-line interface (CLI) tool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/getting-started#virt-using-the-cli-tools "3.2. Using the CLI tools")
  * [Create a VM by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/creating-virtual-machines#virt-creating-vms-web "7.1. Create virtual machines by using the web console")
  * [Import a custom image from a web page](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/creating-virtual-machines#virt-creating-vm-web-page-cli_virt-creating-vms-cli "7.2.2. Create a VM from a web-hosted image")
  * [Upload an image from your local machine](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/creating-virtual-machines#virt-uploading-image-virtctl_virt-creating-vms-cli "7.2.5. Upload a VM image by using the CLI")
  * [Clone a persistent volume claim (PVC)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/creating-virtual-machines#virt-creating-vm-by-cloning-pvcs-cli_virt-creating-vms-cli "7.2.10. VM creation from a cloned PVC")
  * [Connect a VM to a Linux bridge network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-connecting-vm-to-linux-bridge "9.7. Connecting a virtual machine to a Linux bridge network")
  * [Connect a VM to an Open Virtual Network (OVN)-Kubernetes secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-connecting-vm-to-ovn-secondary-network "9.10. Connecting a virtual machine to an OVN-Kubernetes layer 2 secondary network")
  * [Connect a VM to a Single Root I/O Virtualization (SR-IOV) network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-connecting-vm-to-sriov "9.8. Connecting a virtual machine to an SR-IOV network")
  * [Connect to a virtual machine console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-accessing-vm-consoles "8.5. Connect to a virtual machine console")
  * [SSH access for virtual machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-accessing-vm-ssh "8.6.1. SSH access for virtual machines")
  * [Connect to the desktop viewer by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-connecting-desktop-viewer-web_virt-accessing-vm-consoles "8.5.9. Connect to the desktop viewer by using the web console")
  * [Manage a VM by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-controlling-vm-states "8.14. Control virtual machine states")
  * [Export a VM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-accessing-exported-vm-manifests_virt-exporting-vms "8.12.2. Access exported VM manifests")
  * [Review post-installation configuration options](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/postinstallation-configuration#virt-post-install-config "5.1. Postinstallation configuration")
  * [Configure storage options and automatic boot source updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/storage#virt-storage-config-overview "10.1. Storage configuration overview")
  * [Learn about monitoring and health checks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/monitoring#virt-monitoring-overview "13.1. Monitoring overview")
  * [Learn about live migration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/live-migration#virt-about-live-migration "11.1. About live migration")
  * [Back up and restore VMs by using the OpenShift API for Data Protection (OADP)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/#installing-oadp-kubevirt)
  * [Tune and scale your cluster](https://access.redhat.com/articles/6994974)
