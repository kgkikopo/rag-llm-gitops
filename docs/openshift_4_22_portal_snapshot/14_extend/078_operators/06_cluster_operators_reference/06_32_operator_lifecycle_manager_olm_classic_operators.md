# 6.32. Operator Lifecycle Manager (OLM) Classic Operators

Operator Lifecycle Manager (OLM) Classic has been included with OpenShift Container Platform 4 since its initial release and manages the lifecycle of cluster Operators and add-on Operators. 

## 6.32.1. About Operator Lifecycle Manager (OLM) Classic

Operator Lifecycle Manager (OLM) Classic helps users install, update, and manage the lifecycle of Kubernetes native applications (Operators) and their associated services running across their OpenShift Container Platform clusters. 

Operator Lifecycle Manager (OLM) Classic forms part of the Operator Framework, an open source toolkit designed to manage Operators in an effective, automated, and scalable way. 

**Figure 6.1. OLM (Classic) workflow**

![olm workflow](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/c8a00bac5df42a702ff1b826333610d0/olm-workflow.png) ![olm workflow](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Operators-en-US/images/c8a00bac5df42a702ff1b826333610d0/olm-workflow.png)

OLM runs by default in OpenShift Container Platform 4.22, which aids cluster administrators in installing, upgrading, and granting access to Operators running on their cluster. The OpenShift Container Platform web console provides management screens for cluster administrators to install Operators, as well as grant specific projects access to use the catalog of Operators available on the cluster. 

For developers, a self-service experience allows provisioning and configuring instances of databases, monitoring, and big data services without having to be subject matter experts, because the Operator has that knowledge baked into it. 

## 6.32.2. OLM Operator

The OLM Operator deploys applications defined by cluster service versions (CSVs) after their required resources are present in the cluster. It watches CSVs in a namespace, verifies requirements, and runs the install strategy when conditions are met. 

The OLM Operator is not concerned with the creation of the required resources; you can choose to manually create these resources using the CLI or using the Catalog Operator. This separation of concern allows users incremental buy-in in terms of how much of the OLM framework they choose to leverage for their application. 

The OLM Operator uses the following workflow: 

  1. Watch for cluster service versions (CSVs) in a namespace and check that requirements are met. 
  2. If requirements are met, run the install strategy for the CSV. 

Note

A CSV must be an active member of an Operator group for the install strategy to run. 




## 6.32.3. Catalog Operator

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



## 6.32.4. Catalog Registry

The Catalog Registry stores cluster service versions (CSVs), custom resource definitions (CRDs), and metadata about packages and channels for Operator installation in OpenShift Container Platform. Package manifests link package identities to CSVs so the Catalog Operator can step through channel upgrade paths. 

A _package manifest_ is an entry in the Catalog Registry that associates a package identity with sets of CSVs. Within a package, channels point to a particular CSV. Because CSVs explicitly reference the CSV that they replace, a package manifest provides the Catalog Operator with all of the information that is required to update a CSV to the latest version in a channel, stepping through each intermediate version. 

## 6.32.5. CRDs

Operator Lifecycle Manager (OLM) and the Catalog Operator manage the following custom resource definitions (CRDs) that form the basis of the Operator Framework. 

Table 6.1. CRDs managed by OLM and Catalog OperatorsResource| Short name| Owner| Description  
---|---|---|---  
`ClusterServiceVersion` (CSV)  |  `csv` |  OLM  |  Application metadata: name, version, icon, required resources, installation, and so on.   
`InstallPlan` |  `ip` |  Catalog  |  Calculated list of resources to be created to automatically install or upgrade a CSV.   
`CatalogSource` |  `catsrc` |  Catalog  |  A repository of CSVs, CRDs, and packages that define an application.   
`Subscription` |  `sub` |  Catalog  |  Used to keep CSVs up to date by tracking a channel in a package.   
`OperatorGroup` |  `og` |  OLM  |  Configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their custom resource (CR) in a list of namespaces or cluster-wide.   
Show more

Each of these Operators is also responsible for creating the following resources: 

Table 6.2. Resources created by OLM and Catalog OperatorsResource| Owner  
---|---  
`Deployments` |  OLM   
`ServiceAccounts`  
`(Cluster)Roles`  
`(Cluster)RoleBindings`  
`CustomResourceDefinitions` (CRDs)  |  Catalog   
`ClusterServiceVersions`  
Show more

## 6.32.6. Cluster Operators

Operator Lifecycle Manager (OLM) Classic functionality in OpenShift Container Platform is provided by a set of cluster Operators. 

`operator-lifecycle-manager`
     Provides the OLM Operator. Also informs cluster administrators if there are any installed Operators blocking cluster upgrade, based on their `olm.maxOpenShiftVersion` properties. For more information, see "Controlling Operator compatibility with OpenShift Container Platform versions". 
`operator-lifecycle-manager-catalog`
     Provides the Catalog Operator. 
`operator-lifecycle-manager-packageserver`
     Represents an API extension server responsible for collecting metadata from all catalogs on the cluster and serves the user-facing `PackageManifest` API. 

**Additional resources**

  * [Understanding Operator Lifecycle Manager (OLM)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-understanding-olm "2.4.1. Operator Lifecycle Manager concepts and resources")
