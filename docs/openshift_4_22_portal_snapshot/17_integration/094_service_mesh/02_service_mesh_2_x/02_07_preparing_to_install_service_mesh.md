# 2.7. Preparing to install Service Mesh

Before you can install Red Hat OpenShift Service Mesh, you must subscribe to OpenShift Container Platform and install OpenShift Container Platform in a supported configuration. 

## 2.7.1. Prerequisites

  * Maintain an active OpenShift Container Platform subscription on your Red Hat account. If you do not have a subscription, contact your sales representative for more information. 
  * Review the [OpenShift Container Platform 4.22 overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#installation-overview_architecture-installation). 
  * Install OpenShift Container Platform 4.22. If you are installing Red Hat OpenShift Service Mesh on a [restricted network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing-supported-installation-methods-reference_installing-preparing), follow the instructions for your chosen OpenShift Container Platform infrastructure. 

    * [Install OpenShift Container Platform 4.22 on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-default)
    * [Install OpenShift Container Platform 4.22 on AWS with user-provisioned infrastructure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-user-infra)
    * [Install OpenShift Container Platform 4.22 on bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal)
    * [Install OpenShift Container Platform 4.22 on vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere)
    * [Install OpenShift Container Platform 4.22 on IBM Z® and IBM® LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z)
    * [Install OpenShift Container Platform 4.22 on IBM Power®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/#installing-ibm-power)

  * Install the version of the OpenShift Container Platform command-line utility (the `oc` client tool) that matches your OpenShift Container Platform version and add it to your path. 

    * If you are using OpenShift Container Platform 4.22, see [About the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#cli-about-cli_cli-developer-commands). 




For additional information about Red Hat OpenShift Service Mesh lifecycle and supported platforms, refer to the [Support Policy](https://access.redhat.com/support/policy/updates/openshift#ossm). 

## 2.7.2. Supported configurations

The following configurations are supported for the current release of Red Hat OpenShift Service Mesh. 

### 2.7.2.1. Supported platforms

The Red Hat OpenShift Service Mesh Operator supports multiple versions of the `ServiceMeshControlPlane` resource. Version 2.6 Service Mesh control planes are supported on the following platform versions: 

  * Red Hat OpenShift Container Platform version 4.10 or later 
  * Red Hat OpenShift Dedicated version 4 
  * Azure Red Hat OpenShift (ARO) version 4 
  * Red Hat OpenShift Service on AWS 
  * Red Hat OpenShift Service on AWS classic architecture 



### 2.7.2.2. Unsupported configurations

Explicitly unsupported cases include: 

  * OpenShift Online is not supported for Red Hat OpenShift Service Mesh. 
  * Red Hat OpenShift Service Mesh does not support the management of microservices outside the cluster where Service Mesh is running. 



### 2.7.2.3. Supported network configurations

Red Hat OpenShift Service Mesh supports the following network configurations. 

  * OpenShift-SDN 
  * OVN-Kubernetes is available on all supported versions of OpenShift Container Platform. 
  * Third-Party Container Network Interface (CNI) plugins that have been certified on OpenShift Container Platform and passed Service Mesh conformance testing. See [Certified OpenShift CNI Plug-ins](https://access.redhat.com/articles/5436171) for more information. 



### 2.7.2.4. Supported configurations for Service Mesh

  * This release of Red Hat OpenShift Service Mesh is only available on OpenShift Container Platform x86_64, IBM Z®, and IBM Power®. 

    * IBM Z® is only supported on OpenShift Container Platform 4.10 and later. 
    * IBM Power® is only supported on OpenShift Container Platform 4.10 and later. 

  * Configurations where all Service Mesh components are contained within a single OpenShift Container Platform cluster. 
  * Configurations that do not integrate external services such as virtual machines. 
  * Red Hat OpenShift Service Mesh does not support `EnvoyFilter` configuration except where explicitly documented. 



### 2.7.2.5. Supported configurations for Kiali

  * The Kiali console is only supported on the two most recent releases of the Google Chrome, Microsoft Edge, Mozilla Firefox, or Apple Safari browsers. 
  * The `openshift` authentication strategy is the only supported authentication configuration when Kiali is deployed with Red Hat OpenShift Service Mesh (OSSM). The `openshift` strategy controls access based on the individual’s role-based access control (RBAC) roles of the OpenShift Container Platform. 



### 2.7.2.6. Supported configurations for Distributed Tracing

  * Jaeger agent as a sidecar is the only supported configuration for Jaeger. Jaeger as a daemonset is not supported for multitenant installations or OpenShift Dedicated. 



### 2.7.2.7. Supported WebAssembly module

  * 3scale WebAssembly is the only provided WebAssembly module. You can create custom WebAssembly modules. 



## 2.7.3. Next steps

  * [Install Red Hat OpenShift Service Mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#installing-ossm "2.8. Installing the Operators") in your OpenShift Container Platform environment.
