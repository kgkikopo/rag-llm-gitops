# 6.33. Operator Lifecycle Manager (OLM) v1 Operator

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

  * [Extensions overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extensions/#extensions-overview)
  * [Compatibility with OpenShift Container Platform versions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extensions/#olmv1-ocp-compat_update-paths)
