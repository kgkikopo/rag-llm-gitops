# 1.2. Purpose of Operator Lifecycle Manager

The Operator Lifecycle Manager (OLM) simplifies management of extensions on Kubernetes clusters. It provides administrators with a safe, reliable, and centralized way to install, run, and update cluster extensions. 

The initial version of OLM, which launched with OpenShift Container Platform 4 and is included by default, focused on providing unique support for these specific needs for a particular type of cluster extension, known as Operators. Operators are classified as one or more Kubernetes controllers, shipping with one or more API extensions, as `CustomResourceDefinition` (CRD) objects, to provide additional functionality to the cluster. 

After running in production clusters for many releases, the next-generation of OLM aims to encompass lifecycles for cluster extensions that are not just Operators. 

**Additional resources**

  * [Operator Controller](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/architecture#operator-controller "2.2. Operator Controller")
  * [Catalogd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/architecture#catalogd "2.3. Catalogd")
  * [Updating a cluster extension](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/cluster-extensions#olmv1-updating-an-operator_managing-ce "5.2.6. Updating a cluster extension")
  * [Installing extensions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/cluster-extensions#managing-ce "5.2. Managing cluster extensions")
