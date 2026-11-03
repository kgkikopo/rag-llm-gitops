# 6.3. Operators in OpenShift Container Platform

Operators are the foundational control plane extensions of OpenShift Container Platform. Use Operators as the preferred method to package, deploy, and manage services on the control plane, and to support your applications. 

Operators integrate with Kubernetes APIs and CLI tools such as `kubectl` and the OpenShift CLI (`oc`). Operators provide the means of monitoring applications, performing health checks, managing over-the-air (OTA) updates, and ensuring that applications remain in your specified state. 

Operators also offer a more granular configuration experience. You configure each component by modifying the API that the Operator exposes instead of modifying a global configuration file. 

Because CRI-O and the Kubelet run on every node, almost every other cluster function can be managed on the control plane by using Operators. Components that are added to the control plane by using Operators include critical networking and credential services. 

While both follow similar Operator concepts and goals, Operators in OpenShift Container Platform are managed by two different systems, depending on their purpose: 

Cluster Operators
     Managed by the Cluster Version Operator (CVO) and installed by default to perform cluster functions. 
Optional add-on Operators
     Managed by Operator Lifecycle Manager (OLM) and can be made accessible for users to run in their applications. Also known as _OLM-based Operators_. 

## 6.3.1. Cluster Operators

In OpenShift Container Platform, all cluster functions are divided into a series of default _cluster Operators_. Cluster Operators manage a particular area of cluster functionality, such as cluster-wide application logging, management of the Kubernetes control plane, or the machine provisioning system. 

Cluster Operators are represented by a `ClusterOperator` object, which cluster administrators can view in the OpenShift Container Platform web console from the **Administration** **Cluster Settings** page. Each cluster Operator provides a simple API for determining cluster functionality. The Operator hides the details of managing the lifecycle of that component. Operators can manage a single component or tens of components, but the end goal is always to reduce operational burden by automating common actions. 

**Additional resources**

  * [Cluster Operators reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#operator-reference)



## 6.3.2. Add-on Operators

Operator Lifecycle Manager (OLM) and the software catalog are default components in OpenShift Container Platform that help manage Kubernetes-native applications as Operators. 

Together they provide the system for discovering, installing, and managing the optional add-on Operators available on the cluster. 

Using the software catalog in the OpenShift Container Platform web console, cluster administrators and authorized users can select Operators to install from catalogs of Operators. After installing an Operator from the software catalog, you can make the Operator available globally or in specific namespaces to run in user applications. 

Default catalog sources are available that include Red Hat Operators, certified Operators, and community Operators. Cluster administrators can also add their own custom catalog sources, which can contain a custom set of Operators. 

Note

OLM does not manage the cluster Operators that comprise the OpenShift Container Platform architecture. 

**Additional resources**

  * [Operator Lifecycle Manager (OLM) concepts and resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-understanding-olm)
  * [Understanding the software catalog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-understanding-software-catalog)
