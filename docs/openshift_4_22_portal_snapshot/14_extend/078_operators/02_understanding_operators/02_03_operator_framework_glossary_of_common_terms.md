# 2.3. Operator Framework glossary of common terms

You can use this glossary to learn terminology used across the Operator Framework and Operator Lifecycle Manager (OLM) in OpenShift Container Platform. The terms help you understand concepts for packaging, installing, and managing Operators. 

## 2.3.1. Bundle

In the bundle format, a _bundle_ is a collection of an Operator CSV, manifests, and metadata. Together, they form a unique version of an Operator that can be installed onto the cluster. 

## 2.3.2. Bundle image

In the bundle format, a _bundle image_ is a container image that is built from Operator manifests and that contains one bundle. Bundle images are stored and distributed by Open Container Initiative (OCI) spec container registries, such as Quay.io or DockerHub. 

## 2.3.3. Catalog source

A _catalog source_ represents a store of metadata that OLM can query to discover and install Operators and their dependencies. 

## 2.3.4. Channel

A _channel_ defines a stream of updates for an Operator and is used to roll out updates for subscribers. The head points to the latest version of that channel. For example, a `stable` channel would have all stable versions of an Operator arranged from the earliest to the latest. 

An Operator can have several channels, and a subscription binding to a certain channel would only look for updates in that channel. 

## 2.3.5. Channel head

A _channel head_ refers to the latest known update in a particular channel. 

## 2.3.6. Cluster service version

A _cluster service version (CSV)_ is a YAML manifest created from Operator metadata that assists OLM in running the Operator in a cluster. It is the metadata that accompanies an Operator container image, used to populate user interfaces with information such as its logo, description, and version. 

It is also a source of technical information that is required to run the Operator, like the RBAC rules it requires and which custom resources (CRs) it manages or depends on. 

## 2.3.7. Dependency

An Operator may have a _dependency_ on another Operator being present in the cluster. For example, the Vault Operator has a dependency on the etcd Operator for its data persistence layer. 

OLM resolves dependencies by ensuring that all specified versions of Operators and CRDs are installed on the cluster during the installation phase. This dependency is resolved by finding and installing an Operator in a catalog that satisfies the required CRD API, and is not related to packages or bundles. 

## 2.3.8. Extension

Extensions enable cluster administrators to extend capabilities for users on their OpenShift Container Platform cluster. Extensions are managed by Operator Lifecycle Manager (OLM) v1. 

The `ClusterExtension` API streamlines management of installed extensions, which includes Operators via the `registry+v1` bundle format, by consolidating user-facing APIs into a single object. Administrators and SREs can use the API to automate processes and define desired states by using GitOps principles. 

## 2.3.9. Index image

In the bundle format, an _index image_ refers to an image of a database (a database snapshot) that contains information about Operator bundles including CSVs and CRDs of all versions. This index can host a history of Operators on a cluster and be maintained by adding or removing Operators using the `opm` CLI tool. 

## 2.3.10. Install plan

An _install plan_ is a calculated list of resources to be created to automatically install or upgrade a CSV. 

## 2.3.11. Multitenancy

A _tenant_ in OpenShift Container Platform is a user or group of users that share common access and privileges for a set of deployed workloads, typically represented by a namespace or project. You can use tenants to provide a level of isolation between different groups or teams. 

When a cluster is shared by multiple users or groups, it is considered a _multitenant_ cluster. 

## 2.3.12. Operator

Operators are a method of packaging, deploying, and managing a Kubernetes application. A Kubernetes application is an app that is both deployed on Kubernetes and managed using the Kubernetes APIs and `kubectl` or `oc` tooling. 

In Operator Lifecycle Manager (OLM) v1, the `ClusterExtension` API streamlines management of installed extensions, which includes Operators via the `registry+v1` bundle format. 

## 2.3.13. Operator group

An _Operator group_ configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their CR in a list of namespaces or cluster-wide. 

## 2.3.14. Package

In the bundle format, a _package_ is a directory that encloses all released history of an Operator with each version. A released version of an Operator is described in a CSV manifest alongside the CRDs. 

## 2.3.15. Registry

A _registry_ is a database that stores bundle images of Operators, each with all of its latest and historical versions in all channels. 

## 2.3.16. Subscription

A _subscription_ keeps CSVs up to date by tracking a channel in a package. 

## 2.3.17. Update graph

An _update graph_ links versions of CSVs together, similar to the update graph of any other packaged software. Operators can be installed sequentially, or certain versions can be skipped. The update graph is expected to grow only at the head with newer versions being added. 

Also known as _update edges_ or _update paths_.
