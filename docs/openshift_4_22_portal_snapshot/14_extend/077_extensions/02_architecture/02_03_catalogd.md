# 2.3. Catalogd

Operator Lifecycle Manager (OLM) v1 uses the catalogd component and its resources to manage Operator and extension catalogs. 

## 2.3.1. About catalogs in OLM v1

You can discover installable content by querying a catalog for Kubernetes extensions, such as Operators and controllers, by using the catalogd component. 

Catalogd is a Kubernetes extension that unpacks catalog content for on-cluster clients and is part of the Operator Lifecycle Manager (OLM) v1 suite of microservices. Currently, catalogd unpacks catalog content that is packaged and distributed as container images. 

**Additional resources**

  * [File-based catalogs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/catalogs#fbc "4.1. File-based catalogs")
  * [Adding a catalog to a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/catalogs#olmv1-adding-a-catalog-to-a-cluster_managing-catalogs "4.3.3. Add a catalog to a cluster")
  * [Red Hat-provided catalogs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/catalogs#rh-catalogs "4.2. Red Hat-provided catalogs")
