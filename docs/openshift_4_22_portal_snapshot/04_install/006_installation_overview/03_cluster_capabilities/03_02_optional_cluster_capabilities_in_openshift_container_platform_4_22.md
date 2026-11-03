# 3.2. Optional cluster capabilities in OpenShift Container Platform 4.22

Currently, cluster Operators provide the features for these optional capabilities. 

The following sections summarize the features provided by each capability and what functionality you lose if you disable a functionality. 

**Additional resources**

  * [Cluster Operators reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#cluster-operator-reference)



## 3.2.1. Cluster Baremetal Operator

The Cluster Baremetal Operator provides the features for the `baremetal` capability. 

The Cluster Baremetal Operator (CBO) deploys all the components necessary to take a bare-metal server to a fully functioning worker node ready to run OpenShift Container Platform compute nodes. 

The CBO ensures that the metal3 deployment, which consists of the Bare Metal Operator (BMO) and Ironic containers, runs on one of the control plane nodes within the OpenShift Container Platform cluster. The CBO also listens for OpenShift Container Platform updates to resources that it watches and takes appropriate action. 

The bare-metal capability is required for deployments using installer-provisioned infrastructure. Disabling the bare-metal capability can result in unexpected problems with these deployments. 

Important

If the bare-metal capability is disabled, the cluster cannot provision or manage bare-metal nodes. Only disable the capability if there are no `BareMetalHost` resources in your deployment. The `baremetal` capability depends on the `MachineAPI` capability. If you enable the `baremetal` capability, you must also enable `MachineAPI`. 

Note

Red Hat recommends that cluster administrators only disable the bare-metal capability during installations with user-provisioned infrastructure that do not have any `BareMetalHost` resources in the cluster. 

**Additional resources**

  * [Deploying installer-provisioned clusters on bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#ipi-install-overview)
  * [Preparing for bare metal cluster installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#preparing-to-install-on-bare-metal)
  * [Configuration using the Bare Metal Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#bmo-config-using-bare-metal-operator_bare-metal-postinstallation-configuration)



## 3.2.2. Build capability

The `Build` capability enables the `Build` API. The `Build` API manages the lifecycle of `Build` and `BuildConfig` objects. 

Important

If you disable the `Build` capability, the following resources will not be available in the cluster: 

  * `Build` and `BuildConfig` resources 
  * The `builder` service account 



Disable the `Build` capability only if you do not require `Build` and `BuildConfig` resources or the `builder` service account in the cluster. 

## 3.2.3. Cloud Controller Manager Operator

The Cloud Controller Manager Operator provides features for the `CloudControllerManager` capability. 

Note

Currently, disabling the `CloudControllerManager` capability is not supported on all platforms. 

You can determine if your cluster supports disabling the `CloudControllerManager` capability by checking values in the installation configuration (`install-config.yaml`) file for your cluster. 

In the `install-config.yaml` file, locate the `platform` parameter. 

  * If the value of the `platform` parameter is `Baremetal` or `None`, you can disable the `CloudControllerManager` capability on your cluster. 
  * If the value of the `platform` parameter is `External`, locate the `platform.external.cloudControllerManager` parameter. If the value of the `platform.external.cloudControllerManager` parameter is `None`, you can disable the `CloudControllerManager` capability on your cluster. 



Important

If these parameters contain any other values than those listed, you cannot disable the `CloudControllerManager` capability on your cluster. 

Note

The status of this Operator is General Availability for Amazon Web Services (AWS), Google Cloud, IBM Cloud®, global Microsoft Azure, Microsoft Azure Stack Hub, Nutanix, Red Hat OpenStack Platform (RHOSP), and VMware vSphere. 

The Operator is available as a Technology Preview for IBM Power® Virtual Server. 

The Cloud Controller Manager Operator manages and updates the cloud controller managers deployed on top of OpenShift Container Platform. The Operator is based on the Kubebuilder framework and `controller-runtime` libraries. You can install the Cloud Controller Manager Operator by using the Cluster Version Operator (CVO). 

The Cloud Controller Manager Operator includes the following components: 

  * Operator 
  * Cloud configuration observer 



By default, the Operator exposes Prometheus metrics through the `metrics` service. 

**Additional resources**

  * [Technology Preview](https://access.redhat.com/support/offerings/techpreview)
  * [`cluster-cloud-controller-manager-operator`](https://github.com/openshift/cluster-cloud-controller-manager-operator)



## 3.2.4. Cloud Credential Operator

The Cloud Credential Operator provides features for the `CloudCredential` capability. 

Note

Currently, disabling the `CloudCredential` capability is only supported for bare-metal clusters. 

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). 

The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with the specific permissions that are required for the cluster to run. 

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in several different modes. If no mode is specified, or the `credentialsMode` parameter is set to an empty string (`""`), the CCO operates in its default mode. 

**Additional resources**

  * [About the Cloud Credential Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#about-cloud-credential-operator)
  * [`openshift-cloud-credential-operator`](https://github.com/openshift/cloud-credential-operator)



## 3.2.5. Cluster Image Registry Operator

The Cluster Image Registry Operator provides features for the `ImageRegistry` capability. 

The Cluster Image Registry Operator manages a singleton instance of the OpenShift image registry. It manages all configuration of the registry, including creating storage. 

On initial start up, the Operator creates a default `image-registry` resource instance based on the configuration detected in the cluster. This indicates what cloud storage type to use based on the cloud provider. 

If insufficient information is available to define a complete `image-registry` resource, then an incomplete resource is defined and the Operator updates the resource status with information about what is missing. 

The Cluster Image Registry Operator runs in the `openshift-image-registry` namespace and it also manages the registry instance in that location. All configuration and workload resources for the registry reside in that namespace. 

In order to integrate the image registry into the cluster’s user authentication and authorization system, an image pull secret is generated for each service account in the cluster. 

Important

If you disable the `ImageRegistry` capability or if you disable the integrated OpenShift image registry in the Cluster Image Registry Operator’s configuration, the image pull secret is not generated for each service account. 

If you disable the `ImageRegistry` capability, you can reduce the overall resource footprint of OpenShift Container Platform in Telco environments. Depending on your deployment, you can disable this component if you do not need it. 

**Additional resources**

  * [Image Registry Operator in OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/registry/#configuring-registry-operator)
  * [Automatically generated secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#auto-generated-sa-token-secrets_nodes-pods-secrets)
  * [cluster-image-registry-operator](https://github.com/openshift/cluster-image-registry-operator)



## 3.2.6. Cluster Storage Operator

The Cluster Storage Operator provides the features for the `Storage` capability. 

The Cluster Storage Operator sets OpenShift Container Platform cluster-wide storage defaults. It ensures a default `storageclass` exists for OpenShift Container Platform clusters. It also installs Container Storage Interface (CSI) drivers which enable your cluster to use various storage backends. 

Important

If the cluster storage capability is disabled, the cluster will not have a default `storageclass` or any CSI drivers. Users with administrator privileges can create a default `storageclass` and manually install CSI drivers if the cluster storage capability is disabled. 

Notes
     The storage class that the Operator creates can be made non-default by editing its annotation, but this storage class cannot be deleted if the Operator runs. 

**Additional resources**

  * [cluster-storage-operator](https://github.com/openshift/cluster-storage-operator)



## 3.2.7. Console Operator

The Console Operator provides the features for the `Console` capability. 

The Console Operator installs and maintains the OpenShift Container Platform web console on a cluster. The Console Operator is installed by default and automatically maintains a console. 

**Additional resources**

  * [Web console overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#web-console-overview)
  * [console-operator](https://github.com/openshift/console-operator)



## 3.2.8. Cluster CSI Snapshot Controller Operator

The Cluster CSI Snapshot Controller Operator provides the features for the `CSISnapshot` capability. 

The Cluster CSI Snapshot Controller Operator installs and maintains the CSI Snapshot Controller. The CSI Snapshot Controller is responsible for watching the `VolumeSnapshot` CRD objects and manages the creation and deletion lifecycle of volume snapshots. 

**Additional resources**

  * [CSI volume snapshots](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-snapshots)
  * [cluster-csi-snapshot-controller-operator](https://github.com/openshift/cluster-csi-snapshot-controller-operator)



## 3.2.9. DeploymentConfig capability

The `DeploymentConfig` capability enables and manages the `DeploymentConfig` API. 

Important

If you disable the `DeploymentConfig` capability, the following resources will not be available in the cluster: 

  * `DeploymentConfig` resources 
  * The `deployer` service account 



Disable the `DeploymentConfig` capability only if you do not require `DeploymentConfig` resources and the `deployer` service account in the cluster. 

## 3.2.10. Ingress Operator

The Ingress Operator provides the features for the `Ingress` capability. 

The Ingress Operator configures and manages the OpenShift Container Platform router. 

CRDs
    

  * `clusteringresses.ingress.openshift.io`

    * Scope: Namespaced 
    * CR: `clusteringresses`
    * Validation: No 




Configuration objects
    

  * Cluster config 

    * Type Name: `clusteringresses.ingress.openshift.io`
    * Instance Name: `default`
    * View Command: 

```shell-session
$ oc get clusteringresses.ingress.openshift.io -n openshift-ingress-operator default -o yaml
```


Notes
    

The Ingress Operator sets up the router in the `openshift-ingress` project and creates the deployment for the router: 

```shell-session
$ oc get deployment -n openshift-ingress
```


The Ingress Operator uses the `clusterNetwork[].cidr` from the `network/cluster` status to determine what mode (IPv4, IPv6, or dual stack) the managed Ingress Controller (router) should operate in. For example, if `clusterNetwork` contains only a v6 `cidr`, then the Ingress Controller operates in IPv6-only mode. 

In the following example, Ingress Controllers managed by the Ingress Operator will run in IPv4-only mode because only one cluster network exists and the network is an IPv4 `cidr`: 

```shell-session
$ oc get network/cluster -o jsonpath='{.status.clusterNetwork[*]}'
```


**Example output**

```shell-session
map[cidr:10.128.0.0/14 hostPrefix:23]
```


**Additional resources**

  * [openshift-ingress-operator](https://github.com/openshift/cluster-ingress-operator)



## 3.2.11. Insights Operator

The Insights Operator provides the features for the `Insights` capability. 

The Insights Operator gathers OpenShift Container Platform configuration data and sends it to Red Hat. 

The data is used to produce proactive insights recommendations about potential issues that a cluster might be exposed to. These insights are communicated to cluster administrators through the Red Hat Lightspeed advisor service on [console.redhat.com](https://console.redhat.com/). 

Notes
     Insights Operator complements OpenShift Container Platform Telemetry. 

**Additional resources**

  * [Using Insights Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#using-insights-operator)
  * [Red Hat Hybrid Cloud Console](https://console.redhat.com/)
  * [insights-operator](https://github.com/openshift/insights-operator)



## 3.2.12. Machine API capability

The `machine-api-operator`, `cluster-autoscaler-operator`, and `cluster-control-plane-machine-set-operator` Operators provide the features for the `MachineAPI` capability. You can disable this capability only if you install a cluster with user-provisioned infrastructure. 

The Machine API capability is responsible for all machine configuration and management in the cluster. If you disable the Machine API capability during installation, you need to manage all machine-related tasks manually. 

**Additional resources**

  * [Overview of machine management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#index)
  * [Machine API Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#machine-api-operator_operator-reference)
  * [Cluster Autoscaler Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#cluster-autoscaler-operator_operator-reference)
  * [Control Plane Machine Set Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#control-plane-machine-set-operator_operator-reference)



## 3.2.13. Marketplace Operator

The Marketplace Operator provides the features for the `marketplace` capability. 

The Marketplace Operator simplifies the process for bringing off-cluster Operators to your cluster by using a set of default Operator Lifecycle Manager (OLM) catalogs on the cluster. 

When the Marketplace Operator is installed, it creates the `openshift-marketplace` namespace. OLM ensures catalog sources installed in the `openshift-marketplace` namespace are available for all namespaces on the cluster. 

If you disable the `marketplace` capability, the Marketplace Operator does not create the `openshift-marketplace` namespace. Catalog sources can still be configured and managed on the cluster manually, but OLM depends on the `openshift-marketplace` namespace in order to make catalogs available to all namespaces on the cluster. Users with elevated permissions to create namespaces prefixed with `openshift-`, such as system or cluster administrators, can manually create the `openshift-marketplace` namespace. 

If you enable the `marketplace` capability, you can enable and disable individual catalogs by configuring the Marketplace Operator. 

**Additional resources**

  * [Red Hat-provided Operator catalogs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-rh-catalogs)
  * [operator-marketplace](https://github.com/operator-framework/operator-marketplace)



## 3.2.14. Node Tuning Operator

The Node Tuning Operator provides features for the `NodeTuning` capability. 

The Node Tuning Operator helps you manage node-level tuning by orchestrating the TuneD daemon and achieves low latency performance by using the Performance Profile controller. 

The majority of high-performance applications require some level of kernel tuning. The Node Tuning Operator provides a unified management interface to users of node-level sysctls and more flexibility to add custom tuning specified by user needs. 

If you disable the NodeTuning capability, some default tuning settings will not be applied to the control-plane nodes. This might limit the scalability and performance of large clusters with over 900 nodes or 900 routes. 

**Additional resources**

  * [Using the Node Tuning Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#using-node-tuning-operator)
  * [cluster-node-tuning-operator](https://github.com/openshift/cluster-node-tuning-operator)



## 3.2.15. Cluster Samples Operator

The Cluster Samples Operator provides the features for the `openshift-samples` capability. 

The Cluster Samples Operator manages the sample image streams and templates stored in the `openshift` namespace. 

On initial start up, the Operator creates the default samples configuration resource to initiate the creation of the image streams and templates. The configuration object is a cluster scoped object with the key `cluster` and type `configs.samples`. 

The image streams are the Red Hat Enterprise Linux CoreOS (RHCOS)-based OpenShift Container Platform image streams pointing to images on `registry.redhat.io`. Similarly, the templates are those categorized as OpenShift Container Platform templates. 

If you disable the samples capability, users cannot access the image streams, samples, and templates it provides. Depending on your deployment, you might want to disable this component if you do not need it. 

**Additional resources**

  * [Configuring the Cluster Samples Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#configuring-samples-operator)
  * [cluster-samples-operator](https://github.com/openshift/cluster-samples-operator)



## 3.2.16. About Operator Lifecycle Manager (OLM) Classic

OLM (Classic) provides the features for the `OperatorLifecycleManager` capability. 

Operator Lifecycle Manager (OLM) Classic helps users install, update, and manage the lifecycle of Kubernetes native applications (Operators) and their associated services running across their OpenShift Container Platform clusters. 

Operator Lifecycle Manager (OLM) Classic forms part of the Operator Framework, an open source toolkit designed to manage Operators in an effective, automated, and scalable way. 

If an Operator requires any of the following APIs, then you must enable the `OperatorLifecycleManager` capability: 

  * `ClusterServiceVersion`
  * `CatalogSource`
  * `Subscription`
  * `InstallPlan`
  * `OperatorGroup`



Important

The `marketplace` capability depends on the `OperatorLifecycleManager` capability. You cannot disable the `OperatorLifecycleManager` capability and enable the `marketplace` capability. 

**Additional resources**

  * [Operator Lifecycle Manager concepts and resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-understanding-olm)
  * [Operator Framework](https://operatorframework.io/)



## 3.2.17. Operator Lifecycle Manager (OLM) v1 Operator

OLM v1 provides the features for the `OperatorLifecycleManagerV1` capability. 

Starting in OpenShift Container Platform 4.18, OLM v1 is enabled by default alongside OLM (Classic). This next-generation iteration provides an updated framework that evolves many of OLM (Classic) concepts that enable cluster administrators to extend capabilities for their users. 

OLM v1 manages the lifecycle of the new `ClusterExtension` object, which includes Operators via the `registry+v1` bundle format, and controls installation, upgrade, and role-based access control (RBAC) of extensions within a cluster. 

In OpenShift Container Platform, OLM v1 is provided by the `olm` cluster Operator. 

Note

The `olm` cluster Operator informs cluster administrators if there are any installed extensions blocking cluster upgrade, based on their `olm.maxOpenShiftVersion` properties. For more information, see "Compatibility with OpenShift Container Platform versions". 

Operator Lifecycle Manager (OLM) v1 comprises the following component projects: 

  * Operator Controller: The central component of OLM v1 that extends Kubernetes with an API through which users can install and manage the lifecycle of Operators and extensions. It consumes information from catalogd. 
  * Catalogd: A Kubernetes extension that unpacks file-based catalog (FBC) content packaged and shipped in container images for consumption by on-cluster clients. As a component of the OLM v1 microservices architecture, catalogd hosts metadata for Kubernetes extensions packaged by the authors of the extensions, and as a result helps users discover installable content. 
  * CRDs: 

    * `clusterextension.olm.operatorframework.io`

      * Scope: Cluster 
      * CR: `ClusterExtension`

    * `clustercatalog.olm.operatorframework.io`

      * Scope: Cluster 
      * CR: `ClusterCatalog`

  * See the following projects in the _Additional resources_ section: 

    * `operator-framework/operator-controller`
    * `operator-framework/catalogd`




**Additional resources**

  * [Extensions overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extensions/#olmv1-about)
  * [operator-framework/operator-controller](https://github.com/operator-framework/operator-controller)
  * [operator-framework/catalogd](https://github.com/operator-framework/catalogd)
