# 2.4. Operator Lifecycle Manager (OLM)

## 2.4.1. Operator Lifecycle Manager concepts and resources

Key concepts for understanding Operator Lifecycle Manager (OLM) include cluster service versions (CSVs), catalog sources, subscriptions, and Operator groups. 

### 2.4.1.1. About Operator Lifecycle Manager (OLM) Classic

Operator Lifecycle Manager (OLM) Classic helps users install, update, and manage the lifecycle of Kubernetes native applications (Operators) and their associated services running across their OpenShift Container Platform clusters. 

Operator Lifecycle Manager (OLM) Classic forms part of the Operator Framework, an open source toolkit designed to manage Operators in an effective, automated, and scalable way. 

**Figure 2.2. OLM (Classic) workflow**

![olm workflow](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/c8a00bac5df42a702ff1b826333610d0/olm-workflow.png) ![olm workflow](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/c8a00bac5df42a702ff1b826333610d0/olm-workflow.png)

OLM runs by default in OpenShift Container Platform 4.22, which aids cluster administrators in installing, upgrading, and granting access to Operators running on their cluster. The OpenShift Container Platform web console provides management screens for cluster administrators to install Operators, as well as grant specific projects access to use the catalog of Operators available on the cluster. 

For developers, a self-service experience allows provisioning and configuring instances of databases, monitoring, and big data services without having to be subject matter experts, because the Operator has that knowledge baked into it. 

### 2.4.1.2. OLM resources

The following custom resource definitions (CRDs) are defined and managed by Operator Lifecycle Manager (OLM) in OpenShift Container Platform. Use these resources to configure catalog sources, subscriptions, install plans, cluster service versions (CSVs), and Operator groups. 

Table 2.2. CRDs managed by OLM and Catalog OperatorsResource| Short name| Description  
---|---|---  
`ClusterServiceVersion` (CSV)  |  `csv` |  Application metadata. For example: name, version, icon, required resources.   
`CatalogSource` |  `catsrc` |  A repository of CSVs, CRDs, and packages that define an application.   
`Subscription` |  `sub` |  Keeps CSVs up to date by tracking a channel in a package.   
`InstallPlan` |  `ip` |  Calculated list of resources to be created to automatically install or upgrade a CSV.   
`OperatorGroup` |  `og` |  Configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their custom resource (CR) in a list of namespaces or cluster-wide.   
`OperatorConditions` |  \-  |  Creates a communication channel between OLM and an Operator it manages. Operators can write to the `Status.Conditions` array to communicate complex states to OLM.   
Show more

#### 2.4.1.2.1. Cluster service version

A cluster service version (CSV) is a YAML manifest that represents a specific version of a running Operator on your OpenShift Container Platform cluster. OLM uses CSV metadata to run Operators safely and determine how to apply upgrades when new versions are published. 

A CSV includes the metadata that accompanies an Operator container image, used to populate user interfaces with information such as its name, version, description, labels, repository link, and logo. 

A CSV is also a source of technical information required to run the Operator, such as which custom resources (CRs) it manages or depends on, RBAC rules, cluster requirements, and install strategies. This information tells OLM how to create required resources and set up the Operator as a deployment. 

#### 2.4.1.2.2. Catalog source

A _catalog source_ represents a store of metadata, typically by referencing an _index image_ stored in a container registry. Operator Lifecycle Manager (OLM) queries catalog sources to discover and install Operators and their dependencies. 

The software catalog in the OpenShift Container Platform web console also displays the Operators provided by catalog sources. 

Tip

Cluster administrators can view the full list of Operators provided by an enabled catalog source on a cluster by using the **Administration** **Cluster Settings** **Configuration** **OperatorHub** page in the web console. 

The `spec` of a `CatalogSource` object indicates how to construct a pod or how to communicate with a service that serves the Operator Registry gRPC API. 

**Example`CatalogSource` object**

```yaml
﻿apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  generation: 1
  name: example-catalog
  namespace: openshift-marketplace
  annotations:
    olm.catalogImageTemplate:
      "quay.io/example-org/example-catalog:v{kube_major_version}.{kube_minor_version}.{kube_patch_version}"
spec:
  displayName: Example Catalog
  image: quay.io/example-org/example-catalog:v1
  priority: -400
  publisher: Example Org
  sourceType: grpc
  grpcPodConfig:
    securityContextConfig: <security_mode>
    nodeSelector:
      custom_label: <label>
    priorityClassName: system-cluster-critical
    tolerations:
      - key: "key1"
        operator: "Equal"
        value: "value1"
        effect: "NoSchedule"
  updateStrategy:
    registryPoll:
      interval: 30m0s
status:
  connectionState:
    address: example-catalog.openshift-marketplace.svc:50051
    lastConnect: 2021-08-26T18:14:31Z
    lastObservedState: READY
  latestImageRegistryPoll: 2021-08-26T18:46:25Z
  registryService:
    createdAt: 2021-08-26T16:16:37Z
    port: 50051
    protocol: grpc
    serviceName: example-catalog
    serviceNamespace: openshift-marketplace
```


where: 

`metadata.name`
     Specifies the name for the `CatalogSource` object. This value is also used as part of the name for the related pod that is created in the requested namespace. 
`metadata.namespace`
     Specifies the namespace to create the catalog in. To make the catalog available cluster-wide in all namespaces, set this value to `openshift-marketplace`. The default Red Hat-provided catalog sources also use the `openshift-marketplace` namespace. Otherwise, set the value to a specific namespace to make the Operator only available in that namespace. 
`metadata.annotations.olm.catalogImageTemplate`
    

To avoid cluster upgrades potentially leaving Operator installations in an unsupported state or without a continued update path, you can enable automatically changing your Operator catalog’s index image version as part of cluster upgrades. This field is optional. 

Set the `olm.catalogImageTemplate` annotation to your index image name and use one or more of the Kubernetes cluster version variables as shown when constructing the template for the image tag. The annotation overwrites the `spec.image` field at run time. See the "Image template for custom catalog sources" section for more details. 

`spec.displayName`
     Specifies the display name for the catalog in the web console and CLI. 
`spec.image`
     Specifies the index image for the catalog. Optionally, this spec can be omitted when using the `olm.catalogImageTemplate` annotation, which sets the pull spec at run time. 
`spec.priority`
     Specifies the weight for the catalog source. OLM uses the weight for prioritization during dependency resolution. A higher weight indicates the catalog is preferred over lower-weighted catalogs. 
`spec.sourceType`
    

Specifies one of the following source types: 

  * `grpc` with an `image` reference: OLM pulls the image and runs the pod, which is expected to serve a compliant API. 
  * `grpc` with an `address` field: OLM attempts to contact the gRPC API at the given address. This should not be used in most cases. 
  * `configmap`: OLM parses config map data and runs a pod that can serve the gRPC API over it. 



`spec.grpcPodConfig.securityContextConfig`
    

Specifies the pod security admissions (PSA) policy for the catalog source pod. It accepts the values of `legacy` or `restricted`. If the field is not set, the default value is `legacy`. In a future OpenShift Container Platform release, it is planned that the default value will be `restricted`. 

Note

If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`. 

`spec.grpcPodConfig.nodeSelector`
     Overrides the default node selector for the pod serving the content in `spec.image` for `grpc` type catalog sources. This field is optional. 
`spec.grpcPodConfig.priorityClassName`
     Overrides the default priority class name for the pod serving the content in `spec.image` for `grpc` type catalog sources. Kubernetes provides `system-cluster-critical` and `system-node-critical` priority classes by default. Setting the field to empty (`""`) assigns the pod the default priority. Other priority classes can be defined manually. This field is optional. 
`spec.grpcPodConfig.tolerations`
     Overrides the default tolerations for the pod serving the content in `spec.image` for `grpc` type catalog sources. This field is optional. 
`spec.updateStrategy.registryPoll`
     Specifies how often OLM polls the container registry for updates. 
`status.connectionState.lastObservedState`
    

Displays the last observed state of the catalog connection. For example: 

  * `READY`: A connection is successfully established. 
  * `CONNECTING`: A connection is attempting to establish. 
  * `TRANSIENT_FAILURE`: A temporary problem has occurred while attempting to establish a connection, such as a timeout. The state will eventually switch back to `CONNECTING` and try again. 



`status.latestImageRegistryPoll`
     Displays the last time OLM polled the container registry for catalog image updates. 
`status.registryService`
     Displays status information for the catalog’s Operator Registry service. 

Referencing the `name` of a `CatalogSource` object in a subscription instructs OLM where to search to find a requested Operator: 

**Example`Subscription` object referencing a catalog source**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: example-operator
  namespace: example-namespace
spec:
  channel: stable
  name: example-operator
  source: example-catalog
  sourceNamespace: openshift-marketplace
```


**Additional resources**

  * [Understanding the software catalog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-understanding-software-catalog "2.5. Understanding the software catalog")
  * [Red Hat-provided Operator catalogs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-rh-catalogs "2.6. Red Hat-provided Operator catalogs")
  * [Adding a catalog source to a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-creating-catalog-from-index_olm-managing-custom-catalogs "4.9.5. Add a catalog source to a cluster")
  * [Catalog priority](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-dependency-catalog-priority_olm-understanding-dependency-resolution "2.4.4.5.1. Catalog priority")
  * [Viewing Operator catalog source status by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-cs-status-cli_olm-status "4.6.3. View Operator catalog source status by using the CLI")
  * [States of Connectivity (gRPC documentation)](https://grpc.github.io/grpc/core/md_doc_connectivity-semantics-and-api.html)
  * [Understanding and managing pod security admission](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-and-managing-pod-security-admission)
  * [Catalog source pod scheduling](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-cs-podsched "4.11. Catalog source pod scheduling")



##### 2.4.1.2.2.1. Image template for custom catalog sources

Operator compatibility with the underlying cluster can be expressed by a catalog source in various ways. 

One way, which is used for the default Red Hat-provided catalog sources, is to identify image tags for index images that are specifically created for a particular platform release, for example OpenShift Container Platform 4.22. 

During a cluster upgrade, the index image tag for the default Red Hat-provided catalog sources are updated automatically by the Cluster Version Operator (CVO) so that Operator Lifecycle Manager (OLM) pulls the updated version of the catalog. For example during an upgrade from OpenShift Container Platform 4.21 to 4.22 4.22, the `spec.image` field in the `CatalogSource` object for the `redhat-operators` catalog is updated from: 

```shell-session
registry.redhat.io/redhat/redhat-operator-index:v4.21
```


to: 

```shell-session
registry.redhat.io/redhat/redhat-operator-index:v4.22
```


However, the CVO does not automatically update image tags for custom catalogs. To ensure users are left with a compatible and supported Operator installation after a cluster upgrade, custom catalogs should also be kept updated to reference an updated index image. 

Starting in OpenShift Container Platform 4.9, cluster administrators can add the `olm.catalogImageTemplate` annotation in the `CatalogSource` object for custom catalogs to an image reference that includes a template. The following Kubernetes version variables are supported for use in the template: 

  * `kube_major_version`
  * `kube_minor_version`
  * `kube_patch_version`



Note

You must specify the Kubernetes cluster version and not the OpenShift Container Platform cluster version, as the latter is not currently available for templating. 

Provided that you have created and pushed an index image with a tag specifying the updated Kubernetes version, setting this annotation enables the index image versions in custom catalogs to be automatically changed after a cluster upgrade. The annotation value is used to set or update the image reference in the `spec.image` field of the `CatalogSource` object. This helps avoid cluster upgrades leaving Operator installations in unsupported states or without a continued update path. 

Important

You must ensure that the index image with the updated tag, in whichever registry it is stored in, is accessible by the cluster at the time of the cluster upgrade. 

**Example 2.4. Example catalog source with an image template**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  generation: 1
  name: example-catalog
  namespace: openshift-marketplace
  annotations:
    olm.catalogImageTemplate:
      "quay.io/example-org/example-catalog:v{kube_major_version}.{kube_minor_version}"
spec:
  displayName: Example Catalog
  image: quay.io/example-org/example-catalog:v1.35
  priority: -400
  publisher: Example Org
```


Note

If the `spec.image` field and the `olm.catalogImageTemplate` annotation are both set, the `spec.image` field is overwritten by the resolved value from the annotation. If the annotation does not resolve to a usable pull spec, the catalog source falls back to the set `spec.image` value. 

If the `spec.image` field is not set and the annotation does not resolve to a usable pull spec, OLM stops reconciliation of the catalog source and sets it into a human-readable error condition. 

For an OpenShift Container Platform 4.22 cluster, which uses Kubernetes 1.35, the `olm.catalogImageTemplate` annotation in the preceding example resolves to the following image reference: 

```shell-session
quay.io/example-org/example-catalog:v1.35
```


For future releases of OpenShift Container Platform, you can create updated index images for your custom catalogs that target the later Kubernetes version that is used by the later OpenShift Container Platform version. With the `olm.catalogImageTemplate` annotation set before the upgrade, upgrading the cluster to the later OpenShift Container Platform version would then automatically update the catalog’s index image as well. 

##### 2.4.1.2.2.2. Catalog health requirements

Operator Lifecycle Manager (OLM) requires that all Operator catalogs in a shared global namespace are healthy. When a catalog is unhealthy, Operator installation and update operations in that namespace fail with a `CatalogSourcesUnhealthy` condition. 

Operator catalogs on a cluster are interchangeable from the perspective of installation resolution; a `Subscription` object might reference a specific catalog, but dependencies are resolved using all catalogs on the cluster. 

For example, if Catalog A is unhealthy, a subscription referencing Catalog A could resolve a dependency in Catalog B, which the cluster administrator might not have been expecting, because B normally had a lower catalog priority than A. 

As a cluster administrator, if you observe an unhealthy catalog and want to consider the catalog as invalid and resume Operator installations, see the "Removing custom catalogs" or "Disabling the default software catalog sources" sections for information about removing the unhealthy catalog. 

**Additional resources**

  * [Removing custom catalogs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-removing-catalogs_olm-managing-custom-catalogs "4.9.8. Removing custom catalogs")
  * [Disabling the default OperatorHub catalog sources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-restricted-networks-operatorhub_olm-managing-custom-catalogs "4.9.7. Disabling the default software catalog sources")



#### 2.4.1.2.3. Subscription

A _subscription_ , defined by a `Subscription` object, represents an intention to install an Operator. It is the custom resource that relates an Operator to a catalog source. 

Subscriptions describe which channel of an Operator package to subscribe to, and whether to perform updates automatically or manually. If set to automatic, the subscription ensures Operator Lifecycle Manager (OLM) manages and upgrades the Operator to ensure that the latest version is always running in the cluster. 

**Example`Subscription` object**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: example-operator
  namespace: example-namespace
spec:
  channel: stable
  name: example-operator
  source: example-catalog
  sourceNamespace: openshift-marketplace
```


This `Subscription` object defines the name and namespace of the Operator, as well as the catalog from which the Operator data can be found. The channel, such as `alpha`, `beta`, or `stable`, helps determine which Operator stream should be installed from the catalog source. 

The names of channels in a subscription can differ between Operators, but the naming scheme should follow a common convention within a given Operator. For example, channel names might follow a minor release update stream for the application provided by the Operator (`1.2`, `1.3`) or a release frequency (`stable`, `fast`). 

In addition to being easily visible from the OpenShift Container Platform web console, it is possible to identify when there is a newer version of an Operator available by inspecting the status of the related subscription. The value associated with the `currentCSV` field is the newest version that is known to OLM, and `installedCSV` is the version that is installed on the cluster. 

**Additional resources**

  * [Multitenancy and Operator colocation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-colocation "2.4.6. Multitenancy and Operator colocation")
  * [Viewing Operator subscription status by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-status-viewing-cli_olm-status "4.6.2. View Operator subscription status by using the CLI")



#### 2.4.1.2.4. Install plan

An _install plan_ , defined by an `InstallPlan` object, describes a set of resources that Operator Lifecycle Manager (OLM) creates to install or upgrade to a specific version of an Operator. The version is defined by a cluster service version (CSV). 

To install an Operator, a cluster administrator, or a user who has been granted Operator installation permissions, must first create a `Subscription` object. A subscription represents the intent to subscribe to a stream of available versions of an Operator from a catalog source. The subscription then creates an `InstallPlan` object to facilitate the installation of the resources for the Operator. 

The install plan must then be approved according to one of the following approval strategies: 

  * If the subscription’s `spec.installPlanApproval` field is set to `Automatic`, the install plan is approved automatically. 
  * If the subscription’s `spec.installPlanApproval` field is set to `Manual`, the install plan must be manually approved by a cluster administrator or user with proper permissions. 



After the install plan is approved, OLM creates the specified resources and installs the Operator in the namespace that is specified by the subscription. 

**Example 2.5. Example`InstallPlan` object**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: InstallPlan
metadata:
  name: install-abcde
  namespace: operators
spec:
  approval: Automatic
  approved: true
  clusterServiceVersionNames:
    - my-operator.v1.0.1
  generation: 1
status:
  ...
  catalogSources: []
  conditions:
    - lastTransitionTime: '2021-01-01T20:17:27Z'
      lastUpdateTime: '2021-01-01T20:17:27Z'
      status: 'True'
      type: Installed
  phase: Complete
  plan:
    - resolving: my-operator.v1.0.1
      resource:
        group: operators.coreos.com
        kind: ClusterServiceVersion
        manifest: >-
        ...
        name: my-operator.v1.0.1
        sourceName: redhat-operators
        sourceNamespace: openshift-marketplace
        version: v1alpha1
      status: Created
    - resolving: my-operator.v1.0.1
      resource:
        group: apiextensions.k8s.io
        kind: CustomResourceDefinition
        manifest: >-
        ...
        name: webservers.web.servers.org
        sourceName: redhat-operators
        sourceNamespace: openshift-marketplace
        version: v1beta1
      status: Created
    - resolving: my-operator.v1.0.1
      resource:
        group: ''
        kind: ServiceAccount
        manifest: >-
        ...
        name: my-operator
        sourceName: redhat-operators
        sourceNamespace: openshift-marketplace
        version: v1
      status: Created
    - resolving: my-operator.v1.0.1
      resource:
        group: rbac.authorization.k8s.io
        kind: Role
        manifest: >-
        ...
        name: my-operator.v1.0.1-my-operator-6d7cbc6f57
        sourceName: redhat-operators
        sourceNamespace: openshift-marketplace
        version: v1
      status: Created
    - resolving: my-operator.v1.0.1
      resource:
        group: rbac.authorization.k8s.io
        kind: RoleBinding
        manifest: >-
        ...
        name: my-operator.v1.0.1-my-operator-6d7cbc6f57
        sourceName: redhat-operators
        sourceNamespace: openshift-marketplace
        version: v1
      status: Created
      ...
```


**Additional resources**

  * [Multitenancy and Operator colocation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-colocation "2.4.6. Multitenancy and Operator colocation")
  * [Allowing non-cluster administrators to install Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-creating-policy "4.8. Allowing non-cluster administrators to install Operators")



#### 2.4.1.2.5. Operator groups

An Operator group defines multitenant configuration for OLM-installed Operators through an `OperatorGroup` resource. An Operator group selects target namespaces where the required RBAC access is generated for member Operators . 

The set of target namespaces is provided by a comma-delimited string stored in the `olm.targetNamespaces` annotation of a cluster service version (CSV). This annotation is applied to the CSV instances of member Operators and is projected into their deployments. 

Warning

Do not install Operators that require cluster-scoped permissions in namespaces where non-administrator users have any of the following permissions: 

  * Default `edit` cluster role 
  * Service account token creation 
  * Workload creation, for example: 

    * Pods 
    * Replica sets 
    * Deployments 
    * Jobs 
    * Cron jobs 
    * Daemon sets 




For more information, see [Audit and secure delegated Operator installations (Red Hat Knowledgebase)](https://access.redhat.com/articles/7149230). 

**Additional resources**

  * [Operator groups](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-understanding-operatorgroups "2.4.5. Operator groups")



#### 2.4.1.2.6. Operator conditions

Operator Lifecycle Manager (OLM) infers Operator state from Kubernetes resources, but some conditions require explicit communication. You can use the `OperatorCondition` custom resource definition (CRD) to tell OLM about supported conditions that affect lifecycle management. 

Note

By default, the `Spec.Conditions` array is not present in an `OperatorCondition` object until it is either added by a user or as a result of custom Operator logic. 

**Additional resources**

  * [Operator conditions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-operatorconditions "2.4.7. Operator conditions")



## 2.4.2. Operator Lifecycle Manager architecture

You can learn how Operator Lifecycle Manager (OLM) components interact to manage Operators in OpenShift Container Platform. The architecture includes the OLM Operator, Catalog Operator, and Catalog Registry. 

### 2.4.2.1. CRDs

Operator Lifecycle Manager (OLM) and the Catalog Operator manage the following custom resource definitions (CRDs) that form the basis of the Operator Framework. 

Table 2.3. CRDs managed by OLM and Catalog OperatorsResource| Short name| Owner| Description  
---|---|---|---  
`ClusterServiceVersion` (CSV)  |  `csv` |  OLM  |  Application metadata: name, version, icon, required resources, installation, and so on.   
`InstallPlan` |  `ip` |  Catalog  |  Calculated list of resources to be created to automatically install or upgrade a CSV.   
`CatalogSource` |  `catsrc` |  Catalog  |  A repository of CSVs, CRDs, and packages that define an application.   
`Subscription` |  `sub` |  Catalog  |  Used to keep CSVs up to date by tracking a channel in a package.   
`OperatorGroup` |  `og` |  OLM  |  Configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their custom resource (CR) in a list of namespaces or cluster-wide.   
Show more

Each of these Operators is also responsible for creating the following resources: 

Table 2.4. Resources created by OLM and Catalog OperatorsResource| Owner  
---|---  
`Deployments` |  OLM   
`ServiceAccounts`  
`(Cluster)Roles`  
`(Cluster)RoleBindings`  
`CustomResourceDefinitions` (CRDs)  |  Catalog   
`ClusterServiceVersions`  
Show more

### 2.4.2.2. OLM Operator

The OLM Operator deploys applications defined by cluster service versions (CSVs) after their required resources are present in the cluster. It watches CSVs in a namespace, verifies requirements, and runs the install strategy when conditions are met. 

The OLM Operator is not concerned with the creation of the required resources; you can choose to manually create these resources using the CLI or using the Catalog Operator. This separation of concern allows users incremental buy-in in terms of how much of the OLM framework they choose to leverage for their application. 

The OLM Operator uses the following workflow: 

  1. Watch for cluster service versions (CSVs) in a namespace and check that requirements are met. 
  2. If requirements are met, run the install strategy for the CSV. 

Note

A CSV must be an active member of an Operator group for the install strategy to run. 




### 2.4.2.3. Catalog Operator

The Catalog Operator in OpenShift Container Platform resolves and installs cluster service versions (CSVs) and their required resources from catalog sources. It watches subscriptions and catalog sources to create install plans and upgrade packages in channels. 

To track a package in a channel, you can create a `Subscription` object configuring the desired package, channel, and the `CatalogSource` object you want to use for pulling updates. When updates are found, an appropriate `InstallPlan` object is written into the namespace on behalf of the user. 

The Catalog Operator uses the following workflow: 

  1. Connect to each catalog source in the cluster. 
  2. Watch for unresolved install plans created by a user, and if found: 

     1. Find the CSV matching the name requested and add the CSV as a resolved resource. 
     2. For each managed or required CRD, add the CRD as a resolved resource. 
     3. For each required CRD, find the CSV that manages it. 

  3. Watch for resolved install plans and create all of the discovered resources for it, if approved by a user or automatically. 
  4. Watch for catalog sources and subscriptions and create install plans based on them. 



### 2.4.2.4. Catalog Registry

The Catalog Registry stores cluster service versions (CSVs), custom resource definitions (CRDs), and metadata about packages and channels for Operator installation in OpenShift Container Platform. Package manifests link package identities to CSVs so the Catalog Operator can step through channel upgrade paths. 

A _package manifest_ is an entry in the Catalog Registry that associates a package identity with sets of CSVs. Within a package, channels point to a particular CSV. Because CSVs explicitly reference the CSV that they replace, a package manifest provides the Catalog Operator with all of the information that is required to update a CSV to the latest version in a channel, stepping through each intermediate version. 

## 2.4.3. Operator Lifecycle Manager workflow

The Operator Lifecycle Manager (OLM) resolves Operator installs and upgrades in OpenShift Container Platform. The OLM lifecycle involves interacting with catalog sources, subscriptions, and cluster service versions (CSVs). 

### 2.4.3.1. Operator installation and upgrade workflow in OLM

In the Operator Lifecycle Manager (OLM) ecosystem, the `ClusterServiceVersion` (CSV), `CatalogSource`, and `Subscription` resources are used to resolve Operator installations and upgrades. 

The following resources are used to resolve Operator installations and upgrades: 

  * `ClusterServiceVersion` (CSV) 
  * `CatalogSource`
  * `Subscription`



Operator metadata, defined in CSVs, can be stored in a collection called a catalog source. OLM uses catalog sources, which use the [Operator Registry API](https://github.com/operator-framework/operator-registry), to query for available Operators as well as upgrades for installed Operators. 

**Figure 2.3. Catalog source overview**

![olm catalogsource](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/a4756a206580a0a1ab0e6a170ddc75e3/olm-catalogsource.png) ![olm catalogsource](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/a4756a206580a0a1ab0e6a170ddc75e3/olm-catalogsource.png)

Within a catalog source, Operators are organized into _packages_ and streams of updates called _channels_ , which should be a familiar update pattern from OpenShift Container Platform or other software on a continuous release cycle like web browsers. 

**Figure 2.4. Packages and channels in a Catalog source**

![olm channels](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/52025648e55a627b8be314426148fb97/olm-channels.png) ![olm channels](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/52025648e55a627b8be314426148fb97/olm-channels.png)

A user indicates a particular package and channel in a particular catalog source in a _subscription_ , for example an `etcd` package and its `alpha` channel. If a subscription is made to a package that has not yet been installed in the namespace, the latest Operator for that package is installed. 

Note

OLM deliberately avoids version comparisons, so the "latest" or "newest" Operator available from a given _catalog_ _channel_ _package_ path does not necessarily need to be the highest version number. It should be thought of more as the _head_ reference of a channel, similar to a Git repository. 

Each CSV has a `replaces` parameter that indicates which Operator it replaces. This builds a graph of CSVs that can be queried by OLM, and updates can be shared between channels. Channels can be thought of as entry points into the graph of updates: 

**Figure 2.5. OLM graph of available channel updates**

![olm replaces](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/6990efb545ef499e93732227bbe7df68/olm-replaces.png) ![olm replaces](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/6990efb545ef499e93732227bbe7df68/olm-replaces.png)

**Example channels in a package**

```yaml
packageName: example
channels:
- name: alpha
  currentCSV: example.v0.1.2
- name: beta
  currentCSV: example.v0.1.3
defaultChannel: alpha
```


For OLM to successfully query for updates, given a catalog source, package, channel, and CSV, a catalog must be able to return, unambiguously and deterministically, a single CSV that `replaces` the input CSV. 

#### 2.4.3.1.1. Example upgrade path

For an example upgrade scenario, consider an installed Operator corresponding to CSV version `0.1.1`. OLM queries the catalog source and detects an upgrade in the subscribed channel with new CSV version `0.1.3` that replaces an older but not-installed CSV version `0.1.2`, which in turn replaces the older and installed CSV version `0.1.1`. 

OLM walks back from the channel head to previous versions via the `replaces` field specified in the CSVs to determine the upgrade path `0.1.3` `0.1.2` `0.1.1`; the direction of the arrow indicates that the former replaces the latter. OLM upgrades the Operator one version at the time until it reaches the channel head. 

For this given scenario, OLM installs Operator version `0.1.2` to replace the existing Operator version `0.1.1`. Then, it installs Operator version `0.1.3` to replace the previously installed Operator version `0.1.2`. At this point, the installed operator version `0.1.3` matches the channel head and the upgrade is completed. 

#### 2.4.3.1.2. Skipping upgrades

The basic path for upgrades in OLM is: 

  * A catalog source is updated with one or more updates to an Operator. 
  * OLM traverses every version of the Operator until reaching the latest version the catalog source contains. 



However, sometimes this is not a safe operation to perform. There will be cases where a published version of an Operator should never be installed on a cluster if it has not already, for example because a version introduces a serious vulnerability. 

In those cases, OLM must consider two cluster states and provide an update graph that supports both: 

  * The "bad" intermediate Operator has been seen by the cluster and installed. 
  * The "bad" intermediate Operator has not yet been installed onto the cluster. 



By shipping a new catalog and adding a _skipped_ release, OLM is ensured that it can always get a single unique update regardless of the cluster state and whether it has seen the bad update yet. 

**Example CSV with skipped release**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  name: etcdoperator.v0.9.2
  namespace: placeholder
  annotations:
spec:
    displayName: etcd
    description: Etcd Operator
    replaces: etcdoperator.v0.9.0
    skips:
    - etcdoperator.v0.9.1
```


Consider the following example of **Old CatalogSource** and **New CatalogSource**. 

**Figure 2.6. Skipping updates**

![olm skipping updates](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/da1fe891cee5ba712308b9d0e08b91e0/olm-skipping-updates.png) ![olm skipping updates](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/da1fe891cee5ba712308b9d0e08b91e0/olm-skipping-updates.png)

This graph maintains that: 

  * Any Operator found in **Old CatalogSource** has a single replacement in **New CatalogSource**. 
  * Any Operator found in **New CatalogSource** has a single replacement in **New CatalogSource**. 
  * If the bad update has not yet been installed, it will never be. 



#### 2.4.3.1.3. Replacing multiple Operators

Creating **New CatalogSource** as described requires publishing CSVs that `replace` one Operator, but can `skip` several. This can be accomplished using the `skipRange` annotation: 

```yaml
olm.skipRange: <semver_range>
```


where `<semver_range>` has the version range format supported by the [semver library](https://github.com/blang/semver#ranges). 

When searching catalogs for updates, if the head of a channel has a `skipRange` annotation and the currently installed Operator has a version field that falls in the range, OLM updates to the latest entry in the channel. 

The order of precedence is: 

  1. Channel head in the source specified by `sourceName` on the subscription, if the other criteria for skipping are met. 
  2. The next Operator that replaces the current one, in the source specified by `sourceName`. 
  3. Channel head in another source that is visible to the subscription, if the other criteria for skipping are met. 
  4. The next Operator that replaces the current one in any source visible to the subscription. 



**Example CSV with`skipRange`**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
    name: elasticsearch-operator.v4.1.2
    namespace: <namespace>
    annotations:
        olm.skipRange: '>=4.1.0 <4.1.2'
```


#### 2.4.3.1.4. Z-stream support

A _z-stream_ , or patch release, must replace all previous z-stream releases for the same minor version. OLM does not consider major, minor, or patch versions, it just needs to build the correct graph in a catalog. 

In other words, OLM must be able to take a graph as in **Old CatalogSource** and, similar to before, generate a graph as in **New CatalogSource** : 

**Figure 2.7. Replacing several Operators**

![olm z stream](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/9d8f445a920be612fe82454a3a545e70/olm-z-stream.png) ![olm z stream](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/9d8f445a920be612fe82454a3a545e70/olm-z-stream.png)

This graph maintains that: 

  * Any Operator found in **Old CatalogSource** has a single replacement in **New CatalogSource**. 
  * Any Operator found in **New CatalogSource** has a single replacement in **New CatalogSource**. 
  * Any z-stream release in **Old CatalogSource** will update to the latest z-stream release in **New CatalogSource**. 
  * Unavailable releases can be considered "virtual" graph nodes; their content does not need to exist, the registry just needs to respond as if the graph looks like this. 



## 2.4.4. Operator Lifecycle Manager dependency resolution

To keep installed Operators compatible with each other, Operator Lifecycle Manager (OLM) resolves dependencies and manages custom resource definition (CRD) upgrades in OpenShift Container Platform. 

### 2.4.4.1. About dependency resolution

Operator Lifecycle Manager (OLM) manages the dependency resolution and upgrade lifecycle of running Operators. In many ways, the problems OLM faces are similar to other system or language package managers, such as `yum` and `rpm`. 

However, there is one constraint that similar systems do not generally have that OLM does: because Operators are always running, OLM attempts to ensure that you are never left with a set of Operators that do not work with each other. 

As a result, OLM must never create the following scenarios: 

  * Install a set of Operators that require APIs that cannot be provided 
  * Update an Operator in a way that breaks another that depends upon it 



This is made possible with two types of data: 

Properties  |  Typed metadata about the Operator that constitutes the public interface for it in the dependency resolver. Examples include the group/version/kind (GVK) of the APIs provided by the Operator and the semantic version (semver) of the Operator.   
---|---  
Constraints or dependencies  |  An Operator’s requirements that should be satisfied by other Operators that might or might not have already been installed on the target cluster. These act as queries or filters over all available Operators and constrain the selection during dependency resolution and installation. Examples include requiring a specific API to be available on the cluster or expecting a particular Operator with a particular version to be installed.   
  
OLM converts these properties and constraints into a system of Boolean formulas and passes them to a SAT solver, a program that establishes Boolean satisfiability, which does the work of determining what Operators should be installed. 

### 2.4.4.2. Operator properties

OLM uses the `olm.package` and `olm.gvk` properties of every Operator in a catalog to identify the Operator and resolve its dependencies. 

`olm.package`
     Includes the name of the package and the version of the Operator 
`olm.gvk`
     A single property for each provided API from the cluster service version (CSV) 

Additional properties can also be directly declared by an Operator author by including a `properties.yaml` file in the `metadata/` directory of the Operator bundle. 

**Example arbitrary property**

```yaml
properties:
- type: olm.kubeversion
  value:
    version: "1.16.0"
```


#### 2.4.4.2.1. Arbitrary properties

Operator authors can declare arbitrary properties in a `properties.yaml` file in the `metadata/` directory of the Operator bundle. These properties are translated into a map data structure that is used as an input to the Operator Lifecycle Manager (OLM) resolver at runtime. 

These properties are opaque to the resolver as it does not understand the properties, but it can evaluate the generic constraints against those properties to determine if the constraints can be satisfied given the properties list. 

**Example arbitrary properties**

```yaml
properties:
  - property:
      type: color
      value: red
  - property:
      type: shape
      value: square
  - property:
      type: olm.gvk
      value:
        group: olm.coreos.io
        version: v1alpha1
        kind: myresource
```


This structure can be used to construct a Common Expression Language (CEL) expression for generic constraints. 

**Additional resources**

  * [Common Expression Language (CEL) constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-cel_olm-understanding-dependency-resolution "2.4.4.4.1. Common Expression Language \(CEL\) constraints")



### 2.4.4.3. Operator dependencies

Operator dependencies define relationships between Operators that Operator Lifecycle Manager (OLM) must resolve during installation on OpenShift Container Platform. You can list these dependencies in the optional `dependencies.yaml` file in a bundle’s `metadata/` folder. 

The dependency list contains a `type` field for each item to specify what kind of dependency this is. The following types of Operator dependencies are supported: 

`olm.package`
     This type indicates a dependency for a specific Operator version. The dependency information must include the package name and the version of the package in semver format. For example, you can specify an exact version such as `0.5.2` or a range of versions such as `>0.5.1`. 
`olm.gvk`
     With this type, the author can specify a dependency with group/version/kind (GVK) information, similar to existing CRD and API-based usage in a CSV. This is a path to enable Operator authors to consolidate all dependencies, API or explicit versions, to be in the same place. 
`olm.constraint`
     This type declares generic constraints on arbitrary Operator properties. 

In the following example, dependencies are specified for a Prometheus Operator and etcd CRDs: 

**Example`dependencies.yaml` file**

```yaml
dependencies:
  - type: olm.package
    value:
      packageName: prometheus
      version: ">0.27.0"
  - type: olm.gvk
    value:
      group: etcd.database.coreos.com
      kind: EtcdCluster
      version: v1beta2
```


### 2.4.4.4. Generic constraints

An `olm.constraint` property declares a dependency constraint of a particular type. The `value` field is an object containing a `failureMessage` field holding a string-representation of the constraint message. If the constraint cannot be satisfied at runtime, OLM prints the message to users. 

The following keys denote the available constraint types: 

`gvk`
     Type whose value and interpretation is identical to the `olm.gvk` type 
`package`
     Type whose value and interpretation is identical to the `olm.package` type 
`cel`
     A Common Expression Language (CEL) expression evaluated at runtime by the Operator Lifecycle Manager (OLM) resolver over arbitrary bundle properties and cluster information 
`all`, `any`, `not`
     Conjunction, disjunction, and negation constraints, respectively, containing one or more concrete constraints, such as `gvk` or a nested compound constraint 

#### 2.4.4.4.1. Common Expression Language (CEL) constraints

The `cel` constraint type supports Common Expression Language (CEL) as the expression language. The `cel` struct has a `rule` field which contains the CEL expression string that is evaluated against Operator properties at runtime to determine if the Operator satisfies the constraint. 

**Example`cel` constraint**

```yaml
type: olm.constraint
value:
  failureMessage: 'require to have "certified"'
  cel:
    rule: 'properties.exists(p, p.type == "certified")'
```


The CEL syntax supports a wide range of logical operators, such as `AND` and `OR`. As a result, a single CEL expression can have multiple rules for multiple conditions that are linked together by these logical operators. These rules are evaluated against a data set of multiple different properties from a bundle or any given source, and the output is solved into a single bundle or Operator that satisfies all of those rules within a single constraint. 

**Example`cel` constraint with multiple rules**

```yaml
type: olm.constraint
value:
  failureMessage: 'require to have "certified" and "stable" properties'
  cel:
    rule: 'properties.exists(p, p.type == "certified") && properties.exists(p, p.type == "stable")'
```


#### 2.4.4.4.2. Compound constraints (all, any, not)

Compound constraint types are evaluated following their logical definitions. 

The following is an example of a conjunctive constraint (`all`) of two packages and one GVK. That is, they must all be satisfied by installed bundles: 

**Example`all` constraint**

```yaml
schema: olm.bundle
name: red.v1.0.0
properties:
- type: olm.constraint
  value:
    failureMessage: All are required for Red because...
    all:
      constraints:
      - failureMessage: Package blue is needed for...
        package:
          name: blue
          versionRange: '>=1.0.0'
      - failureMessage: GVK Green/v1 is needed for...
        gvk:
          group: greens.example.com
          version: v1
          kind: Green
```


The following is an example of a disjunctive constraint (`any`) of three versions of the same GVK. That is, at least one must be satisfied by installed bundles: 

**Example`any` constraint**

```yaml
schema: olm.bundle
name: red.v1.0.0
properties:
- type: olm.constraint
  value:
    failureMessage: Any are required for Red because...
    any:
      constraints:
      - gvk:
          group: blues.example.com
          version: v1beta1
          kind: Blue
      - gvk:
          group: blues.example.com
          version: v1beta2
          kind: Blue
      - gvk:
          group: blues.example.com
          version: v1
          kind: Blue
```


The following is an example of a negation constraint (`not`) of one version of a GVK. That is, this GVK cannot be provided by any bundle in the result set: 

**Example`not` constraint**

```yaml
schema: olm.bundle
name: red.v1.0.0
properties:
- type: olm.constraint
  value:
  all:
    constraints:
    - failureMessage: Package blue is needed for...
      package:
        name: blue
        versionRange: '>=1.0.0'
    - failureMessage: Cannot be required for Red because...
      not:
        constraints:
        - gvk:
            group: greens.example.com
            version: v1alpha1
            kind: greens
```


The negation semantics might appear unclear in the `not` constraint context. To clarify, the negation is really instructing the resolver to remove any possible solution that includes a particular GVK, package at a version, or satisfies some child compound constraint from the result set. 

As a corollary, the `not` compound constraint should only be used within `all` or `any` constraints, because negating without first selecting a possible set of dependencies does not make sense. 

#### 2.4.4.4.3. Nested compound constraints

A nested compound constraint, one that contains at least one child compound constraint along with zero or more simple constraints, is evaluated from the bottom up following the procedures for each previously described constraint type. 

The following is an example of a disjunction of conjunctions, where one, the other, or both can satisfy the constraint: 

**Example nested compound constraint**

```yaml
schema: olm.bundle
name: red.v1.0.0
properties:
- type: olm.constraint
  value:
    failureMessage: Required for Red because...
    any:
      constraints:
      - all:
          constraints:
          - package:
              name: blue
              versionRange: '>=1.0.0'
          - gvk:
              group: blues.example.com
              version: v1
              kind: Blue
      - all:
          constraints:
          - package:
              name: blue
              versionRange: '<1.0.0'
          - gvk:
              group: blues.example.com
              version: v1beta1
              kind: Blue
```


Note

The maximum raw size of an `olm.constraint` type is 64KB to limit resource exhaustion attacks. 

**Additional resources**

  * [Common Expression Language (CEL)](https://github.com/google/cel-go)



### 2.4.4.5. Dependency preferences

To help predict and control the outcome of an installation or update, review the dependency resolver workflow in Operator Lifecycle Manager (OLM). The dependency resolver selects between multiple options that satisfy a dependency. 

#### 2.4.4.5.1. Catalog priority

On OpenShift Container Platform clusters, OLM reads catalog sources to know which Operators are available for installation. 

**Example`CatalogSource` object**

```yaml
apiVersion: "operators.coreos.com/v1alpha1"
kind: "CatalogSource"
metadata:
  name: "my-operators"
  namespace: "operators"
spec:
  sourceType: grpc
  grpcPodConfig:
    securityContextConfig: <security_mode>
  image: example.com/my/operator-index:v1
  displayName: "My Operators"
  priority: 100
```


Specify the value of `legacy` or `restricted` for the `<security_mode>` variable. If the field is not set, the default value is `legacy`. In a future OpenShift Container Platform release, it is planned that the default value will be `restricted`. 

Note

If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`. 

A `CatalogSource` object has a `priority` field, which is used by the resolver to know how to prefer options for a dependency. 

There are two rules that govern catalog preference: 

  * Options in higher-priority catalogs are preferred to options in lower-priority catalogs. 
  * Options in the same catalog as the dependent are preferred to any other catalogs. 



#### 2.4.4.5.2. Channel ordering

An Operator package in a catalog is a collection of update channels that a user can subscribe to in OpenShift Container Platform clusters. Channels can be used to provide a particular stream of updates for a minor release (`1.2`, `1.3`) or a release frequency (`stable`, `fast`). 

It is likely that a dependency might be satisfied by Operators in the same package, but different channels. For example, version `1.2` of an Operator might exist in both the `stable` and `fast` channels. 

Each package has a default channel, which is always preferred to non-default channels. If no option in the default channel can satisfy a dependency, options are considered from the remaining channels in lexicographic order of the channel name. 

#### 2.4.4.5.3. Order within a channel

There are almost always multiple options to satisfy a dependency within a single channel. For example, Operators in one package and channel provide the same set of APIs. 

When a user creates a subscription, they indicate which channel to receive updates from. This immediately reduces the search to just that one channel. But within the channel, it is likely that many Operators satisfy a dependency. 

Within a channel, newer Operators that are higher up in the update graph are preferred. If the head of a channel satisfies a dependency, it will be tried first. 

#### 2.4.4.5.4. Other constraints

In addition to the constraints supplied by package dependencies, OLM includes additional constraints to represent the desired user state and enforce resolution invariants. 

Subscription constraint
     A subscription constraint filters the set of Operators that can satisfy a subscription. Subscriptions are user-supplied constraints for the dependency resolver. They declare the intent to either install a new Operator if it is not already on the cluster, or to keep an existing Operator updated. 
Package constraint
     Within a namespace, no two Operators may come from the same package. 

**Additional resources**

  * [Catalog health requirements](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-cs-health_olm-understanding-olm "2.4.1.2.2.2. Catalog health requirements")



### 2.4.4.6. CRD upgrades

Operator Lifecycle Manager (OLM) upgrades a custom resource definition (CRD) immediately if a single cluster service version (CSV) owns it. When multiple CSVs share ownership, OLM upgrades the CRD only after verifying compatibility with earlier versions. 

### 2.4.4.7. Dependency best practices

A deliberate dependency management workflow helps you avoid update conflicts and keep your Operators compatible with each other. 

Depend on APIs or a specific version range of Operators
     Operators can add or remove APIs at any time; always specify an `olm.gvk` dependency on any APIs your Operators requires. The exception to this is if you are specifying `olm.package` constraints instead. 
Set a minimum version
    

The Kubernetes documentation on API changes describes what changes are allowed for Kubernetes-style Operators. These versioning conventions allow an Operator to update an API without bumping the API version, provided that the API is compatible with earlier versions. 

For Operator dependencies, this means that knowing the API version of a dependency might not be enough to ensure the dependent Operator works as intended. 

For example: 

  * TestOperator v1.0.0 provides v1alpha1 API version of the `MyObject` resource. 
  * TestOperator v1.0.1 adds a new field `spec.newfield` to `MyObject`, but still at v1alpha1. 



Your Operator might require the ability to write `spec.newfield` into the `MyObject` resource. An `olm.gvk` constraint alone is not enough for OLM to determine that you need TestOperator v1.0.1 and not TestOperator v1.0.0. 

Whenever possible, if a specific Operator that provides an API is known ahead of time, specify an additional `olm.package` constraint to set a minimum. 

Omit a maximum version or allow a very wide range
    

Because Operators provide cluster-scoped resources such as API services and CRDs, an Operator that specifies a small window for a dependency might unnecessarily constrain updates for other consumers of that dependency. 

Whenever possible, do not set a maximum version. Alternatively, set a very wide semantic range to prevent conflicts with other Operators. For example, `>1.0.0 <2.0.0`. 

Unlike with conventional package managers, Operator authors explicitly encode that updates are safe through channels in OLM. If an update is available for an existing subscription, it is assumed that the Operator author is indicating that it can update from the previous version. Setting a maximum version for a dependency overrides the update stream of the author by unnecessarily truncating it at a particular upper bound. 

Note

Cluster administrators cannot override dependencies set by an Operator author. 

However, maximum versions can and should be set if there are known incompatibilities that must be avoided. Specific versions can be omitted with the version range syntax, for example `> 1.0.0 !1.2.1`. 

**Additional resources**

  * [Changing the API (Kubernetes documentation)](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api_changes.md#readme)



### 2.4.4.8. Dependency caveats

To avoid unresolvable constraints and update deadlocks between Operators, review the dependency resolution caveats. 

No compound constraints (AND)
    

There is currently no method for specifying an AND relationship between constraints. That is, there is no way to specify that one Operator depends on another Operator that both provides a given API and has version `>1.1.0`. 

This means that when specifying a dependency such as: 

```yaml
dependencies:
- type: olm.package
  value:
    packageName: etcd
    version: ">3.1.0"
- type: olm.gvk
  value:
    group: etcd.database.coreos.com
    kind: EtcdCluster
    version: v1beta2
```


It would be possible for OLM to satisfy this with two Operators: one that provides EtcdCluster and one that has version `>3.1.0`. Whether that happens, or whether an Operator is selected that satisfies both constraints, depends on the ordering that potential options are visited. Dependency preferences and ordering options are well-defined and can be reasoned about, but to exercise caution, Operators should stick to one mechanism or the other. 

Cross-namespace compatibility
     OLM performs dependency resolution at the namespace scope. It is possible to get into an update deadlock if updating an Operator in one namespace would be an issue for an Operator in another namespace, and vice-versa. 

### 2.4.4.9. Example dependency resolution scenarios

Reference example scenarios to understand how OLM prevents dependency conflicts and update deadlocks between Operators that provide or depend on the same API. 

#### 2.4.4.9.1. Example: Deprecating dependent APIs

A and B are APIs (CRDs): 

  * The provider of A depends on B. 
  * The provider of B has a subscription. 
  * The provider of B updates to provide C but deprecates B. 



This results in: 

  * B no longer has a provider. 
  * A no longer works. 



This is a case OLM prevents with its upgrade strategy. 

#### 2.4.4.9.2. Example: Version deadlock

A and B are APIs: 

  * The provider of A requires B. 
  * The provider of B requires A. 
  * The provider of A updates to (provide A2, require B2) and deprecate A. 
  * The provider of B updates to (provide B2, require A2) and deprecate B. 



If OLM attempts to update A without simultaneously updating B, or vice-versa, it is unable to progress to new versions of the Operators, even though a new compatible set can be found. 

This is another case OLM prevents with its upgrade strategy. 

## 2.4.5. Operator groups

Operator groups control which namespaces an Operator watches and how Operator Lifecycle Manager (OLM) manages related Operators in OpenShift Container Platform. You can use them to configure install modes, target namespaces, and access for OLM-managed Operators. 

### 2.4.5.1. About Operator groups

An Operator group defines multitenant configuration for OLM-installed Operators through an `OperatorGroup` resource. An Operator group selects target namespaces where the required RBAC access is generated for member Operators . 

The set of target namespaces is provided by a comma-delimited string stored in the `olm.targetNamespaces` annotation of a cluster service version (CSV). This annotation is applied to the CSV instances of member Operators and is projected into their deployments. 

Warning

Do not install Operators that require cluster-scoped permissions in namespaces where non-administrator users have any of the following permissions: 

  * Default `edit` cluster role 
  * Service account token creation 
  * Workload creation, for example: 

    * Pods 
    * Replica sets 
    * Deployments 
    * Jobs 
    * Cron jobs 
    * Daemon sets 




For more information, see [Audit and secure delegated Operator installations (Red Hat Knowledgebase)](https://access.redhat.com/articles/7149230). 

### 2.4.5.2. Operator group membership

An Operator becomes a member of an Operator group when its cluster service version (CSV) is in the same namespace and its install modes support the group’s target namespaces. 

An install mode in a CSV consists of an `InstallModeType` field and a boolean `Supported` field. The spec of a CSV can contain a set of install modes of four distinct `InstallModeTypes`: 

Table 2.5. Install modes and supported Operator groupsInstallModeType| Description  
---|---  
`OwnNamespace` |  The Operator can be a member of an Operator group that selects its own namespace.   
`SingleNamespace` |  The Operator can be a member of an Operator group that selects one namespace.   
`MultiNamespace` |  The Operator can be a member of an Operator group that selects more than one namespace.   
`AllNamespaces` |  The Operator can be a member of an Operator group that selects all namespaces (target namespace set is the empty string `""`).   
Show more

Note

If the spec of a CSV omits an entry of `InstallModeType`, then that type is considered unsupported unless support can be inferred by an existing entry that implicitly supports it. 

### 2.4.5.3. Target namespace selection

You can explicitly name the target namespace for an Operator group using the `spec.targetNamespaces` parameter. 

**Example Operator group**

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
spec:
  targetNamespaces:
  - my-namespace
```


You can alternatively specify a namespace using a label selector with the `spec.selector` parameter: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
spec:
  selector:
    cool.io/prod: "true"
```


Important

Listing multiple namespaces via `spec.targetNamespaces` or use of a label selector via `spec.selector` is not recommended, as the support for more than one target namespace in an Operator group will likely be removed in a future release. 

If both `spec.targetNamespaces` and `spec.selector` are defined, `spec.selector` is ignored. Alternatively, you can omit both `spec.selector` and `spec.targetNamespaces` to specify a _global_ Operator group, which selects all namespaces: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
```


The resolved set of selected namespaces is shown in the `status.namespaces` parameter of an Opeator group. The `status.namespace` of a global Operator group contains the empty string (`""`), which signals to a consuming Operator that it should watch all namespaces. 

### 2.4.5.4. Operator group CSV annotations

Member cluster service versions (CSVs) of an Operator group carry annotations that identify the group name, namespace, and target namespace selection. 

Member CSVs of an Operator group have the following annotations: 

Annotation| Description  
---|---  
`olm.operatorGroup=<group_name>` |  Contains the name of the Operator group.   
`olm.operatorNamespace=<group_namespace>` |  Contains the namespace of the Operator group.   
`olm.targetNamespaces=<target_namespaces>` |  Contains a comma-delimited string that lists the target namespace selection of the Operator group.   
Show more

Note

All annotations except `olm.targetNamespaces` are included with copied CSVs. Omitting the `olm.targetNamespaces` annotation on copied CSVs prevents the duplication of target namespaces between tenants. 

### 2.4.5.5. Provided APIs annotation

A _group/version/kind (GVK)_ is a unique identifier for a Kubernetes API. Information about what GVKs are provided by an Operator group are shown in an `olm.providedAPIs` annotation. 

The value of the annotation is a string consisting of `<kind>.<version>.<group>` delimited with commas. The GVKs of CRDs and API services provided by all active member CSVs of an Operator group are included. 

Review the following example of an `OperatorGroup` object with a single active member CSV that provides the `PackageManifest` resource: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  annotations:
    olm.providedAPIs: PackageManifest.v1alpha1.packages.apps.redhat.com
  name: olm-operators
  namespace: local
  ...
spec:
  selector: {}
  serviceAccountName:
    metadata:
      creationTimestamp: null
  targetNamespaces:
  - local
status:
  lastUpdated: 2019-02-19T16:18:28Z
  namespaces:
  - local
```


### 2.4.5.6. Role-based access control

When an Operator group is created, three cluster roles are generated. When the cluster roles are generated, they are automatically suffixed with a hash value to ensure that each cluster role is unique. 

Warning

To prevent privilege escalation, assign a service account with minimum required permissions to the Operator group. 

If no service account is specified, Operator Lifecycle Manager (OLM) Classic installs the Operator using the default cluster-scoped permissions. 

For more information, see [Audit and secure delegated Operator installations (Red Hat Knowledgebase)](https://access.redhat.com/articles/7149230). 

Each Operator group contains a single aggregation rule with a cluster role selector set to match a label, as shown in the following table: 

Cluster role| Label to match  
---|---  
`olm.og.<operatorgroup_name>-admin-<hash_value>` |  `olm.opgroup.permissions/aggregate-to-admin: <operatorgroup_name>`  
`olm.og.<operatorgroup_name>-edit-<hash_value>` |  `olm.opgroup.permissions/aggregate-to-edit: <operatorgroup_name>`  
`olm.og.<operatorgroup_name>-view-<hash_value>` |  `olm.opgroup.permissions/aggregate-to-view: <operatorgroup_name>`  
Show more

Note

To use the cluster role of an Operator group to assign role-based access control (RBAC) to a resource, get the full name of cluster role and hash value by running the following command: 

```shell-session
$ oc get clusterroles | grep <operatorgroup_name>
```


Because the hash value is generated when the Operator group is created, you must create the Operator group before you can look up the complete name of the cluster role. 

The following RBAC resources are generated when a CSV becomes an active member of an Operator group, as long as the CSV is watching all namespaces with the `AllNamespaces` install mode and is not in a failed state with reason `InterOperatorGroupOwnerConflict`: 

  * Cluster roles for each API resource from a CRD 
  * Cluster roles for each API resource from an API service 
  * Additional roles and role bindings 



Table 2.6. Cluster roles generated for each API resource from a CRDCluster role| Settings  
---|---  
`<kind>.<group>-<version>-admin` |  Verbs on `<kind>`: 

  * `*`

Aggregation labels: 

  * `rbac.authorization.k8s.io/aggregate-to-admin: true`
  * `olm.opgroup.permissions/aggregate-to-admin: <operatorgroup_name>`

  
`<kind>.<group>-<version>-edit` |  Verbs on `<kind>`: 

  * `create`
  * `update`
  * `patch`
  * `delete`

Aggregation labels: 

  * `rbac.authorization.k8s.io/aggregate-to-edit: true`
  * `olm.opgroup.permissions/aggregate-to-edit: <operatorgroup_name>`

  
`<kind>.<group>-<version>-view` |  Verbs on `<kind>`: 

  * `get`
  * `list`
  * `watch`

Aggregation labels: 

  * `rbac.authorization.k8s.io/aggregate-to-view: true`
  * `olm.opgroup.permissions/aggregate-to-view: <operatorgroup_name>`

  
`<kind>.<group>-<version>-view-crdview` |  Verbs on `apiextensions.k8s.io` `customresourcedefinitions` `<crd-name>`: 

  * `get`

Aggregation labels: 

  * `rbac.authorization.k8s.io/aggregate-to-view: true`
  * `olm.opgroup.permissions/aggregate-to-view: <operatorgroup_name>`

  
Show more

Table 2.7. Cluster roles generated for each API resource from an API serviceCluster role| Settings  
---|---  
`<kind>.<group>-<version>-admin` |  Verbs on `<kind>`: 

  * `*`

Aggregation labels: 

  * `rbac.authorization.k8s.io/aggregate-to-admin: true`
  * `olm.opgroup.permissions/aggregate-to-admin: <operatorgroup_name>`

  
`<kind>.<group>-<version>-edit` |  Verbs on `<kind>`: 

  * `create`
  * `update`
  * `patch`
  * `delete`

Aggregation labels: 

  * `rbac.authorization.k8s.io/aggregate-to-edit: true`
  * `olm.opgroup.permissions/aggregate-to-edit: <operatorgroup_name>`

  
`<kind>.<group>-<version>-view` |  Verbs on `<kind>`: 

  * `get`
  * `list`
  * `watch`

Aggregation labels: 

  * `rbac.authorization.k8s.io/aggregate-to-view: true`
  * `olm.opgroup.permissions/aggregate-to-view: <operatorgroup_name>`

  
Show more

#### 2.4.5.6.1. Additional roles and role bindings

  * If the CSV defines exactly one target namespace that contains `*`, then a cluster role and corresponding cluster role binding are generated for each permission defined in the `permissions` field of the CSV. All resources generated are given the `olm.owner: <csv_name>` and `olm.owner.namespace: <csv_namespace>` labels. 
  * If the CSV does _not_ define exactly one target namespace that contains `*`, then all roles and role bindings in the Operator namespace with the `olm.owner: <csv_name>` and `olm.owner.namespace: <csv_namespace>` labels are copied into the target namespace. 



### 2.4.5.7. Copied CSVs

Operator Lifecycle Manager (OLM) creates copies of all active member CSVs of an Operator group in each of the target namespaces of that Operator group. The purpose of a copied CSV is to tell users of a target namespace that a specific Operator is configured to watch resources created there. 

Copied CSVs have a status reason `Copied` and are updated to match the status of their source CSV. The `olm.targetNamespaces` annotation is stripped from copied CSVs before they are created on the cluster. Omitting the target namespace selection avoids the duplication of target namespaces between tenants. 

Copied CSVs are deleted when their source CSV no longer exists or the Operator group that their source CSV belongs to no longer targets the namespace of the copied CSV. 

Note

By default, the `disableCopiedCSVs` field is disabled. After enabling a `disableCopiedCSVs` field, the OLM deletes existing copied CSVs on a cluster. When a `disableCopiedCSVs` field is disabled, the OLM adds copied CSVs again. 

  * Disable the `disableCopiedCSVs` field: 

```yaml
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OLMConfig
metadata:
  name: cluster
spec:
  features:
    disableCopiedCSVs: false
EOF
```


  * Enable the `disableCopiedCSVs` field: 

```yaml
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OLMConfig
metadata:
  name: cluster
spec:
  features:
    disableCopiedCSVs: true
EOF
```


### 2.4.5.8. Static Operator groups

A static Operator group has `spec.staticProvidedAPIs` set to `true`, so OLM does not modify the `olm.providedAPIs` annotation. You can set this annotation in advance to reserve API ownership and prevent resource contention without active member CSVs. 

Below is an example of an Operator group that protects `Prometheus` resources in all namespaces with the `something.cool.io/cluster-monitoring: "true"` annotation: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-monitoring
  namespace: cluster-monitoring
  annotations:
    olm.providedAPIs: Alertmanager.v1.monitoring.coreos.com,Prometheus.v1.monitoring.coreos.com,PrometheusRule.v1.monitoring.coreos.com,ServiceMonitor.v1.monitoring.coreos.com
spec:
  staticProvidedAPIs: true
  selector:
    matchLabels:
      something.cool.io/cluster-monitoring: "true"
```


### 2.4.5.9. Operator group intersection

Two Operator groups are said to have _intersecting provided APIs_ if the intersection of their target namespace sets is not an empty set and the intersection of their provided API sets, defined by `olm.providedAPIs` annotations, is not an empty set. 

A potential issue is that Operator groups with intersecting provided APIs can compete for the same resources in the set of intersecting namespaces. 

Note

When checking intersection rules, an Operator group namespace is always included as part of its selected target namespaces. 

#### 2.4.5.9.1. Rules for intersection

Each time an active member CSV synchronizes, OLM queries the cluster for the set of intersecting provided APIs between the Operator group of the CSV and all others. OLM then checks if that set is an empty set: 

  * If `true` and the CSV’s provided APIs are a subset of the Operator group’s: 

    * Continue transitioning. 

  * If `true` and the CSV’s provided APIs are _not_ a subset of the Operator group’s: 

    * If the Operator group is static: 

      * Clean up any deployments that belong to the CSV. 
      * Transition the CSV to a failed state with status reason `CannotModifyStaticOperatorGroupProvidedAPIs`. 

    * If the Operator group is _not_ static: 

      * Replace the Operator group’s `olm.providedAPIs` annotation with the union of itself and the CSV’s provided APIs. 

  * If `false` and the CSV’s provided APIs are _not_ a subset of the Operator group’s: 

    * Clean up any deployments that belong to the CSV. 
    * Transition the CSV to a failed state with status reason `InterOperatorGroupOwnerConflict`. 

  * If `false` and the CSV’s provided APIs are a subset of the Operator group’s: 

    * If the Operator group is static: 

      * Clean up any deployments that belong to the CSV. 
      * Transition the CSV to a failed state with status reason `CannotModifyStaticOperatorGroupProvidedAPIs`. 

    * If the Operator group is _not_ static: 

      * Replace the Operator group’s `olm.providedAPIs` annotation with the difference between itself and the CSV’s provided APIs. 




Note

Failure states caused by Operator groups are non-terminal. 

The following actions are performed each time an Operator group synchronizes: 

  * The set of provided APIs from active member CSVs is calculated from the cluster. Note that copied CSVs are ignored. 
  * The cluster set is compared to `olm.providedAPIs`, and if `olm.providedAPIs` contains any extra APIs, then those APIs are pruned. 
  * All CSVs that provide the same APIs across all namespaces are requeued. This notifies conflicting CSVs in intersecting groups that their conflict has possibly been resolved, either through resizing or through deletion of the conflicting CSV. 



### 2.4.5.10. Limitations for multitenant Operator management

OpenShift Container Platform provides limited support for simultaneously installing different versions of an Operator on the same cluster. Operator Lifecycle Manager (OLM) installs Operators multiple times in different namespaces. One constraint of this is that the Operator’s API versions must be the same. 

Operators are control plane extensions due to their usage of `CustomResourceDefinition` objects (CRDs), which are global resources in Kubernetes. Different major versions of an Operator often have incompatible CRDs. This makes them incompatible to install simultaneously in different namespaces on a cluster. 

All tenants, or namespaces, share the same control plane of a cluster. Therefore, tenants in a multitenant cluster also share global CRDs, which limits the scenarios in which different instances of the same Operator can be used in parallel on the same cluster. 

The supported scenarios include the following: 

  * Operators of different versions that ship the exact same CRD definition (in case of versioned CRDs, the exact same set of versions) 
  * Operators of different versions that do not ship a CRD, and instead have their CRD available in a separate bundle in the software catalog 



All other scenarios are not supported, because the integrity of the cluster data cannot be guaranteed if there are multiple competing or overlapping CRDs from different Operator versions to be reconciled on the same cluster. 

**Additional resources**

  * [Operator Lifecycle Manager (OLM)  Multitenancy and Operator colocation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-colocation "2.4.6. Multitenancy and Operator colocation")
  * [Operators in multitenant clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-multitenancy "2.7. Operators in multitenant clusters")
  * [Allowing non-cluster administrators to install Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-creating-policy "4.8. Allowing non-cluster administrators to install Operators")



### 2.4.5.11. Troubleshooting Operator groups

Use the following information to troubleshoot common Operator group issues in Operator Lifecycle Manager (OLM). 

#### 2.4.5.11.1. Membership

  * An install plan’s namespace must contain only one Operator group. When attempting to generate a cluster service version (CSV) in a namespace, an install plan considers an Operator group invalid in the following scenarios: 

    * No Operator groups exist in the install plan’s namespace. 
    * Multiple Operator groups exist in the install plan’s namespace. 
    * An incorrect or non-existent service account name is specified in the Operator group. 

If an install plan encounters an invalid Operator group, the CSV is not generated and the `InstallPlan` resource continues to install with a relevant message. For example, the following message is provided if more than one Operator group exists in the same namespace: 

```shell-session
attenuated service account query failed - more than one operator group(s) are managing this namespace count=2
```


where `count=` specifies the number of Operator groups in the namespace. 

  * If the install modes of a CSV do not support the target namespace selection of the Operator group in its namespace, the CSV transitions to a failure state with the reason `UnsupportedOperatorGroup`. CSVs in a failed state for this reason transition to pending after either the target namespace selection of the Operator group changes to a supported configuration, or the install modes of the CSV are modified to support the target namespace selection. 



## 2.4.6. Multitenancy and Operator colocation

When Operators share a namespace, Operator Lifecycle Manager (OLM) treats them as related, which affects how they behave during updates. 

### 2.4.6.1. Colocation of Operators in a namespace

Operator Lifecycle Manager (OLM) treats OLM-managed Operators that are installed in the same namespace as related Operators. Even if the Operators are not actually related, OLM considers their states, such as their version and update policy, when any one of them is updated. 

This default behavior manifests in two ways: 

  * `InstallPlan` resources of pending updates include `ClusterServiceVersion` (CSV) resources of all other Operators that are in the same namespace. 
  * All Operators in the same namespace share the same update policy. For example, if one Operator is set to manual updates, all other Operators' update policies are also set to manual. 



These scenarios can lead to the following issues: 

  * It becomes hard to reason about install plans for Operator updates, because there are many more resources defined in them than just the updated Operator. 
  * It becomes impossible to have some Operators in a namespace update automatically while other are updated manually, which is a common desire for cluster administrators. 



These issues usually surface because, when installing Operators with the OpenShift Container Platform web console, the default behavior installs Operators that support the **All namespaces** install mode into the default `openshift-operators` global namespace. 

As a cluster administrator, you can bypass this default behavior manually by using the following workflow: 

  1. Create a namespace for the installation of the Operator. 
  2. Create a custom _global Operator group_ , which is an Operator group that watches all namespaces. By associating this Operator group with the namespace you just created, it makes the installation namespace a global namespace, which makes Operators installed there available in all namespaces. 
  3. Install the desired Operator in the installation namespace. 



If the Operator has dependencies, the dependencies are automatically installed in the pre-created namespace. As a result, it is then valid for the dependency Operators to have the same update policy and shared install plans. For a detailed procedure, see "Installing global Operators in custom namespaces". 

**Additional resources**

  * [Installing global Operators in custom namespaces](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-installing-global-namespaces_olm-adding-operators-to-a-cluster "4.1.5. Install global Operators in custom namespaces")
  * [Operators in multitenant clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-multitenancy "2.7. Operators in multitenant clusters")



## 2.4.7. Operator conditions

Operator Lifecycle Manager (OLM) uses Operator conditions to communicate additional lifecycle information about an Operator that OLM cannot infer on its own. 

### 2.4.7.1. About Operator conditions

Operator Lifecycle Manager (OLM) infers Operator state from Kubernetes resources, but some conditions require explicit communication. You can use the `OperatorCondition` custom resource definition (CRD) to tell OLM about supported conditions that affect lifecycle management. 

Note

By default, the `Spec.Conditions` array is not present in an `OperatorCondition` object until it is either added by a user or as a result of custom Operator logic. 

### 2.4.7.2. Supported conditions

Operator Lifecycle Manager (OLM) supports a specific set of Operator conditions that communicate the state of an Operator. 

#### 2.4.7.2.1. Upgradeable condition

The `Upgradeable` Operator condition prevents an existing cluster service version (CSV) from being replaced by a newer version of the CSV. This condition is useful when: 

  * An Operator is about to start a critical process and should not be upgraded until the process is completed. 
  * An Operator is performing a migration of custom resources (CRs) that must be completed before the Operator is ready to be upgraded. 



Important

Setting the `Upgradeable` Operator condition to the `False` value does not avoid pod disruption. If you must ensure your pods are not disrupted, see "Using pod disruption budgets to specify the number of pods that must be up" and "Graceful termination" in the "Additional resources" section. 

**Example`Upgradeable` Operator condition**

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorCondition
metadata:
  name: my-operator
  namespace: operators
spec:
  conditions:
  - type: Upgradeable
    status: "False"
    reason: "migration"
    message: "The Operator is performing a migration."
    lastTransitionTime: "2020-08-24T23:15:55Z"
```


  * The `type` field sets the name of the condition. 
  * A `False` value in the `status` field indicates the Operator is not ready to be upgraded. OLM prevents a CSV that replaces the existing CSV of the Operator from leaving the `Pending` phase. A `False` value does not block cluster upgrades. 



### 2.4.7.3. Additional resources

  * [Managing Operator conditions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-operatorconditions "2.4.7. Operator conditions")
  * [Understanding how to use pod disruption budgets to specify the number of pods that must be up](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-pod-disruption-about_nodes-pods-configuring)
  * [Graceful termination](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#deployments-graceful-termination_route-based-deployment-strategies)



## 2.4.8. Operator Lifecycle Manager metrics

Operator Lifecycle Manager (OLM) exposes OLM-specific metrics that the Prometheus-based OpenShift Container Platform cluster monitoring stack can use to track catalog sources, cluster service versions, install plans, and subscriptions. 

### 2.4.8.1. Exposed metrics

Operator Lifecycle Manager (OLM) exposes certain OLM-specific resources for use by the Prometheus-based OpenShift Container Platform cluster monitoring stack. 

Table 2.8. Metrics exposed by OLMName| Description  
---|---  
`catalog_source_count` |  Number of catalog sources.   
`catalogsource_ready` |  State of a catalog source. The value `1` indicates that the catalog source is in a `READY` state. The value of `0` indicates that the catalog source is not in a `READY` state.   
`csv_abnormal` |  When reconciling a cluster service version (CSV), present whenever a CSV version is in any state other than `Succeeded`, for example when it is not installed. Includes the `name`, `namespace`, `phase`, `reason`, and `version` labels. A Prometheus alert is created when this metric is present.   
`csv_count` |  Number of CSVs successfully registered.   
`csv_succeeded` |  When reconciling a CSV, represents whether a CSV version is in a `Succeeded` state (value `1`) or not (value `0`). Includes the `name`, `namespace`, and `version` labels.   
`csv_upgrade_count` |  Monotonic count of CSV upgrades.   
`install_plan_count` |  Number of install plans.   
`installplan_warnings_total` |  Monotonic count of warnings generated by resources, such as deprecated resources, included in an install plan.   
`olm_resolution_duration_seconds` |  The duration of a dependency resolution attempt.   
`subscription_count` |  Number of subscriptions.   
`subscription_sync_total` |  Monotonic count of subscription syncs. Includes the `channel`, `installed` CSV, and subscription `name` labels.   
Show more

## 2.4.9. Webhook management in Operator Lifecycle Manager

Webhooks allow Operator authors to intercept, modify, and accept or reject resources before they are saved to the object store and handled by the Operator controller. Operator Lifecycle Manager (OLM) can manage the lifecycle of these webhooks when they are shipped alongside your Operator. 

### 2.4.9.1. Additional resources

  * [Types of webhook admission plugins](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#admission-webhook-types_admission-plug-ins)
  * [Validating admission webhooks (Kubernetes documentation)](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)
  * [Mutating admission webhooks (Kubernetes documentation)](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)
  * [Conversion webhooks (Kubernetes documentation)](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#webhook-conversion)
