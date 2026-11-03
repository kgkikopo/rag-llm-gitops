# 7.1. OpenShift Kubernetes Engine and OpenShift Container Platform comparison

To help decide whether to use OpenShift Kubernetes Engine or OpenShift Container Platform, you should understand the similarities and differences between the two platforms. 

You can see the similarities and differences in the following table: 

Table 7.1. Product comparison for OpenShift Kubernetes Engine and OpenShift Container Platform | OpenShift Kubernetes Engine| OpenShift Container Platform  
---|---|---  
**Fully Automated Installers** |  Yes  |  Yes   
**Over the Air Smart Upgrades** |  Yes  |  Yes   
**Enterprise Secured Kubernetes** |  Yes  |  Yes   
**Kubectl and oc automated command line** |  Yes  |  Yes   
**Operator Lifecycle Manager (OLM)** |  Yes  |  Yes   
**Administrator Web console** |  Yes  |  Yes   
**OpenShift Virtualization** |  Yes  |  Yes   
**User Workload Monitoring** |  |  Yes   
**Cluster Monitoring** |  Yes  |  Yes   
**Cost Management SaaS Service** |  Yes  |  Yes   
**Platform Logging** |  |  Yes   
**Developer Web Console** |  |  Yes   
**Developer Application Catalog** |  |  Yes   
**Source to Image and Builder Automation (Tekton)** |  |  Yes   
**OpenShift Service Mesh (Maistra and Kiali)** |  |  Yes   
**Distributed Tracing Platform** |  |  Yes   
**OpenShift Serverless (Knative)** |  |  Yes   
**OpenShift Pipelines (Jenkins and Tekton)** |  |  Yes   
**Embedded Component of IBM Cloud® Pak and RHT MW Bundles** |  |  Yes   
**OpenShift sandboxed containers** |  |  Yes   
Show more

Core Kubernetes and container orchestration
    

OpenShift Kubernetes Engine offers full access to an enterprise-ready Kubernetes environment that is easy to install and offers an extensive compatibility test matrix with many of the software elements that you might use in your data center. 

OpenShift Kubernetes Engine offers the same service level agreements, bug fixes, and common vulnerabilities and errors protection as OpenShift Container Platform. OpenShift Kubernetes Engine includes a Red Hat Enterprise Linux (RHEL) Virtual Datacenter and Red Hat Enterprise Linux CoreOS (RHCOS) entitlement that allows you to use an integrated Linux operating system with container runtime from the same technology provider. 

The OpenShift Kubernetes Engine subscription is compatible with the Red Hat OpenShift support for Windows Containers subscription. 

Enterprise-ready configurations
    

OpenShift Kubernetes Engine uses the same security options and default settings as the OpenShift Container Platform. Default security context constraints, pod security policies, best practice network and storage settings, service account configuration, SELinux integration, HAproxy edge routing configuration, and all other standard protections that OpenShift Container Platform offers are available in OpenShift Kubernetes Engine. OpenShift Kubernetes Engine offers full access to the integrated monitoring solution that OpenShift Container Platform uses, which is based on Prometheus and offers deep coverage and alerting for common Kubernetes issues. 

OpenShift Kubernetes Engine uses the same installation and upgrade automation as OpenShift Container Platform. 

Standard infrastructure services
    

With an OpenShift Kubernetes Engine subscription, you receive support for all storage plugins that OpenShift Container Platform supports. 

In terms of networking, OpenShift Kubernetes Engine offers full and supported access to the Kubernetes Container Network Interface (CNI) and therefore allows you to use any third-party SDN that supports OpenShift Container Platform. It also allows you to use the included Open vSwitch software defined network to its fullest extent. OpenShift Kubernetes Engine allows you to take full advantage of the OVN Kubernetes overlay, Multus, and Multus plugins that are supported on OpenShift Container Platform. OpenShift Kubernetes Engine allows customers to use a Kubernetes Network Policy to create microsegmentation between deployed application services on the cluster. 

You can also use the `Route` API objects that are found in OpenShift Container Platform, including its sophisticated integration with the HAproxy edge routing layer as an out of the box Kubernetes Ingress Controller. 

Core user experience
     OpenShift Kubernetes Engine users have full access to Kubernetes Operators, pod deployment strategies, Helm, and OpenShift Container Platform templates. OpenShift Kubernetes Engine users can use both the `oc` and `kubectl` command-line interfaces. OpenShift Kubernetes Engine also offers an administrator web-based console that shows all aspects of the deployed container services and offers a container-as-a service experience. OpenShift Kubernetes Engine grants access to the Operator Life Cycle Manager that helps you control access to content on the cluster and life cycle operator-enabled services that you use. With an OpenShift Kubernetes Engine subscription, you receive access to the Kubernetes namespace, the OpenShift `Project` API object, and cluster-level Prometheus monitoring metrics and events. 
Maintained and curated content
     With an OpenShift Kubernetes Engine subscription, you receive access to the OpenShift Container Platform content from the Red Hat Ecosystem Catalog and Red Hat Connect ISV marketplace. You can access all maintained and curated content that the OpenShift Container Platform eco-system offers. 
OpenShift Data Foundation compatible
     OpenShift Kubernetes Engine is compatible and supported with your purchase of OpenShift Data Foundation. 
Red Hat Middleware compatible
     OpenShift Kubernetes Engine is compatible and supported with individual Red Hat Middleware product solutions. Red Hat Middleware Bundles that include OpenShift embedded in them only contain OpenShift Container Platform. 
OpenShift Serverless
     OpenShift Kubernetes Engine does not include OpenShift Serverless support. Use OpenShift Container Platform for this support. 
Quay Integration compatible
     OpenShift Kubernetes Engine is compatible and supported with a Red Hat Quay purchase. 
OpenShift Virtualization
     OpenShift Kubernetes Engine includes support for the Red Hat product offerings derived from the kubevirt.io open source project. 
Advanced cluster management
    

OpenShift Kubernetes Engine is compatible with your additional purchase of Red Hat Advanced Cluster Management (RHACM) for Kubernetes. An OpenShift Kubernetes Engine subscription does not offer a cluster-wide log aggregation solution. 

Red Hat OpenShift Service Mesh capabilities derived from the open-source istio.io and kiali.io projects that offer OpenTracing observability for containerized services on OpenShift Container Platform are not supported in OpenShift Kubernetes Engine. 

Advanced networking
     The standard networking solutions in OpenShift Container Platform are supported with an OpenShift Kubernetes Engine subscription. The OpenShift Container Platform Kubernetes CNI plugin for automation of multi-tenant network segmentation between OpenShift Container Platform projects is entitled for use with OpenShift Kubernetes Engine. OpenShift Kubernetes Engine offers all the granular control of the source IP addresses that are used by application services on the cluster. Those egress IP address controls are entitled for use with OpenShift Kubernetes Engine. OpenShift Container Platform offers ingress routing to on cluster services that use non-standard ports when no public cloud provider is in use via the VIP pods found in OpenShift Container Platform. That ingress solution is supported in OpenShift Kubernetes Engine. OpenShift Kubernetes Engine users are supported for the Kubernetes ingress control object, which offers integrations with public cloud providers. Red Hat Service Mesh, which is derived from the istio.io open source project, is not supported in OpenShift Kubernetes Engine. Also, the Kourier Ingress Controller found in OpenShift Serverless is not supported on OpenShift Kubernetes Engine. 
OpenShift sandboxed containers
     OpenShift Kubernetes Engine does not include OpenShift sandboxed containers. Use OpenShift Container Platform for this support. 
Developer experience
    

With OpenShift Kubernetes Engine, the following capabilities are not supported: 

  * The OpenShift Container Platform developer experience utilities and tools, such as Red Hat OpenShift Dev Spaces. 
  * The OpenShift Container Platform pipeline feature that integrates a streamlined, Kubernetes-enabled Jenkins and Tekton experience in the user’s project space. 
  * The OpenShift Container Platform source-to-image feature, which allows you to easily deploy source code, dockerfiles, or container images across the cluster. 
  * Build strategies, builder pods, or Tekton container deployments. 
  * The `odo` developer command line. 
  * The developer persona in the OpenShift Container Platform web console. 



Feature summary
    

The following table is a summary of the feature availability in OpenShift Kubernetes Engine and OpenShift Container Platform. Where applicable, it includes the name of the Operator that enables a feature. 

Table 7.2. Features in OpenShift Kubernetes Engine and OpenShift Container PlatformFeature| OpenShift Kubernetes Engine| OpenShift Container Platform| Operator name  
---|---|---|---  
**Fully Automated Installers (installer-provisioned infrastructure)** |  Included  |  Included  |  N/A   
**Customizable Installers (user-provisioned infrastructure)** |  Included  |  Included  |  N/A   
**Disconnected Installation** |  Included  |  Included  |  N/A   
**Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) entitlement** |  Included  |  Included  |  N/A   
**Existing RHEL manual attach to cluster (BYO)** |  Included  |  Included  |  N/A   
**CRIO Runtime** |  Included  |  Included  |  N/A   
**Over the Air Smart Upgrades and Operating System (RHCOS) Management** |  Included  |  Included  |  N/A   
**Enterprise Secured Kubernetes** |  Included  |  Included  |  N/A   
**Kubectl and`oc` automated command line** |  Included  |  Included  |  N/A   
**Auth Integrations, RBAC, SCC, Multi-Tenancy Admission Controller** |  Included  |  Included  |  N/A   
**Operator Lifecycle Manager (OLM)** |  Included  |  Included  |  N/A   
**Administrator web console** |  Included  |  Included  |  N/A   
**OpenShift Virtualization** |  Included  |  Included  |  OpenShift Virtualization Operator   
**Compliance Operator provided by Red Hat** |  Included  |  Included  |  Compliance Operator   
**File Integrity Operator** |  Included  |  Included  |  File Integrity Operator   
**Gatekeeper Operator** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Gatekeeper Operator   
**Klusterlet** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  N/A   
**Kube Descheduler Operator provided by Red Hat** |  Included  |  Included  |  Kube Descheduler Operator   
**Local Storage provided by Red Hat** |  Included  |  Included  |  Local Storage Operator   
**Node Feature Discovery provided by Red Hat** |  Included  |  Included  |  Node Feature Discovery Operator   
**Performance Profile controller** |  Included  |  Included  |  N/A   
**PTP Operator provided by Red Hat** |  Included  |  Included  |  PTP Operator   
**Service Telemetry Operator provided by Red Hat** |  Not Included  |  Included  |  Service Telemetry Operator   
**SR-IOV Network Operator** |  Included  |  Included  |  SR-IOV Network Operator   
**Vertical Pod Autoscaler** |  Included  |  Included  |  Vertical Pod Autoscaler   
**Cluster Monitoring (Prometheus)** |  Included  |  Included  |  Cluster Monitoring   
**Device Manager (for example, GPU)** |  Included  |  Included  |  N/A   
**Log Forwarding** |  Included  |  Included  |  Red Hat OpenShift Logging Operator   
**Telemeter and Insights Connected Experience** |  Included  |  Included  |  N/A   
**Feature** |  **OpenShift Kubernetes Engine** |  **OpenShift Container Platform** |  **Operator name**  
**OpenShift Cloud Manager SaaS Service** |  Included  |  Included  |  N/A   
**OVS and OVN SDN** |  Included  |  Included  |  N/A   
**MetalLB** |  Included  |  Included  |  MetalLB Operator   
**HAProxy Ingress Controller** |  Included  |  Included  |  N/A   
**Ingress Cluster-wide Firewall** |  Included  |  Included  |  N/A   
**Egress Pod and Namespace Granular Control** |  Included  |  Included  |  N/A   
**Ingress Non-Standard Ports** |  Included  |  Included  |  N/A   
**Multus and Available Multus Plugins** |  Included  |  Included  |  N/A   
**Network Policies** |  Included  |  Included  |  N/A   
**IPv6 Single and Dual Stack** |  Included  |  Included  |  N/A   
**CNI Plugin ISV Compatibility** |  Included  |  Included  |  N/A   
**CSI Plugin ISV Compatibility** |  Included  |  Included  |  N/A   
**RHT and IBM® middleware à la carte purchases (not included in OpenShift Container Platform or OpenShift Kubernetes Engine)** |  Included  |  Included  |  N/A   
**ISV or Partner Operator and Container Compatibility (not included in OpenShift Container Platform or OpenShift Kubernetes Engine)** |  Included  |  Included  |  N/A   
**Embedded software catalog** |  Included  |  Included  |  N/A   
**Embedded Marketplace** |  Included  |  Included  |  N/A   
**Quay Compatibility (not included)** |  Included  |  Included  |  N/A   
**OpenShift API for Data Protection (OADP)** |  Included  |  Included  |  OADP Operator   
**RHEL Software Collections and RHT SSO Common Service (included)** |  Included  |  Included  |  N/A   
**Embedded Registry** |  Included  |  Included  |  N/A   
**Helm** |  Included  |  Included  |  N/A   
**User Workload Monitoring** |  Not Included  |  Included  |  N/A   
**Cost Management SaaS Service** |  Included  |  Included  |  Cost Management Metrics Operator   
**Platform Logging** |  Not Included  |  Included  |  Red Hat OpenShift Logging Operator   
**Developer Web Console** |  Not Included  |  Included  |  N/A   
**Developer Application Catalog** |  Not Included  |  Included  |  N/A   
**Source to Image and Builder Automation (Tekton)** |  Not Included  |  Included  |  N/A   
**OpenShift Service Mesh** |  Not Included  |  Included  |  OpenShift Service Mesh Operator   
**Feature** |  **OpenShift Kubernetes Engine** |  **OpenShift Container Platform** |  **Operator name**  
**OpenShift Serverless** |  Not Included  |  Included  |  OpenShift Serverless Operator   
**Web Terminal provided by Red Hat** |  Not Included  |  Included  |  Web Terminal Operator   
**Red Hat OpenShift Pipelines** |  Not Included  |  Included  |  OpenShift Pipelines Operator   
**Embedded Component of IBM Cloud® Pak and RHT MW Bundles** |  Not Included  |  Included  |  N/A   
**Red Hat OpenShift GitOps** |  Not Included  |  Included  |  Red Hat OpenShift GitOps Operator   
**Red Hat OpenShift Dev Spaces** |  Not Included  |  Included  |  Red Hat OpenShift Dev Spaces   
**Red Hat OpenShift Local** |  Not Included  |  Included  |  N/A   
**Quay Bridge Operator provided by Red Hat** |  Not Included  |  Included  |  Quay Bridge Operator   
**Quay Container Security provided by Red Hat** |  Not Included  |  Included  |  Quay Operator   
**Red Hat OpenShift Distributed Tracing Platform (Jaeger)** |  Not Included  |  Included  |  Red Hat OpenShift Distributed Tracing Platform (Jaeger) Operator   
**Red Hat OpenShift Kiali** |  Not Included  |  Included  |  Kiali Operator   
**Metering provided by Red Hat (deprecated)** |  Not Included  |  Included  |  N/A   
**Cost management for OpenShift** |  Not included  |  Included  |  N/A   
**JBoss Web Server provided by Red Hat** |  Not included  |  Included  |  JWS Operator   
**Red Hat Build of Quarkus** |  Not included  |  Included  |  N/A   
**Kourier Ingress Controller** |  Not included  |  Included  |  N/A   
**RHT Middleware Bundles Sub Compatibility (not included in OpenShift Container Platform)** |  Not included  |  Included  |  N/A   
**IBM Cloud® Pak Sub Compatibility (not included in OpenShift Container Platform)** |  Not included  |  Included  |  N/A   
**OpenShift Do (`odo`)** |  Not included  |  Included  |  N/A   
**Source to Image and Tekton Builders** |  Not included  |  Included  |  N/A   
**OpenShift Serverless FaaS** |  Not included  |  Included  |  N/A   
**IDE Integrations** |  Not included  |  Included  |  N/A   
**OpenShift sandboxed containers** |  Not included  |  Not included  |  OpenShift sandboxed containers Operator   
**Windows Machine Config Operator** |  Community Windows Machine Config Operator included - no subscription required  |  Red Hat Windows Machine Config Operator included - Requires separate subscription  |  Windows Machine Config Operator   
**Red Hat Quay** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Quay Operator   
**Red Hat Advanced Cluster Management** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Advanced Cluster Management for Kubernetes   
**Red Hat Advanced Cluster Security** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  N/A   
**OpenShift Data Foundation** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  OpenShift Data Foundation   
**Feature** |  **OpenShift Kubernetes Engine** |  **OpenShift Container Platform** |  **Operator name**  
**Ansible Automation Platform Resource Operator** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Ansible Automation Platform Resource Operator   
**Business Automation provided by Red Hat** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Business Automation Operator   
**Data Grid provided by Red Hat** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Data Grid Operator   
**Red Hat Integration provided by Red Hat** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Red Hat Integration Operator   
**Red Hat Integration - 3Scale provided by Red Hat** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  3scale   
**Red Hat Integration - 3Scale APICast gateway provided by Red Hat** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  3scale APIcast   
**Red Hat Integration - AMQ Broker** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  AMQ Broker   
**Red Hat Integration - AMQ Broker LTS** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |   
**Red Hat Integration - AMQ Interconnect** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  AMQ Interconnect   
**Red Hat Integration - AMQ Online** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |   
**Red Hat Integration - AMQ Streams** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  AMQ Streams   
**Red Hat Integration - Camel K** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Camel K   
**Red Hat Integration - Fuse Console** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Fuse Console   
**Red Hat Integration - Fuse Online** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Fuse Online   
**Red Hat Integration - Service Registry Operator** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Service Registry   
**API Designer provided by Red Hat** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  API Designer   
**JBoss EAP provided by Red Hat** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  JBoss EAP   
**Smart Gateway Operator** |  Not Included - Requires separate subscription  |  Not Included - Requires separate subscription  |  Smart Gateway Operator   
**Kubernetes NMState Operator** |  Included  |  Included  |  N/A   
Show more
