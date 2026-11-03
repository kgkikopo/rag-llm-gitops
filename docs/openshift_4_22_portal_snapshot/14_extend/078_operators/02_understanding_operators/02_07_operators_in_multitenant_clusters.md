# 2.7. Operators in multitenant clusters

The default behavior for Operator Lifecycle Manager (OLM) aims to provide simplicity during Operator installation. However, this behavior can lack flexibility, especially in multitenant clusters. In order for multiple tenants on an OpenShift Container Platform cluster to use an Operator, the default behavior of OLM requires that administrators install the Operator in **All namespaces** mode, which can be considered to violate the principle of least privilege. 

Consider the following scenarios to determine which Operator installation workflow works best for your environment and requirements. 

**Additional resources**

  * [Common terms: Multitenant](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-common-terms-multitenancy_olm-common-terms "2.3.11. Multitenancy")
  * [Limitations for multitenant Operator management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-operatorgroups-limitations "2.4.5.10. Limitations for multitenant Operator management")



## 2.7.1. Default Operator install modes and behavior

When you install Operators in OpenShift Container Platform by using the web console as an administrator, you can choose between single namespace and all namespaces install modes. 

Single namespace
     Installs the Operator in the chosen single namespace, and makes all permissions that the Operator requests available in that namespace. Because the Operator itself installs in the chosen namespace, its pod and service account are also located there. 
All namespaces
     Installs the Operator in the default `openshift-operators` namespace to watch and be made available to all namespaces in the cluster. Makes all permissions that the Operator requests available in all namespaces. In some cases, an Operator author can define metadata to give the user a second option for that Operator’s suggested namespace. 

This choice also means that users in the affected namespaces get access to the Operators APIs, which can leverage the custom resources (CRs) they own, depending on their role in the namespace: 

  * The `namespace-admin` and `namespace-edit` roles can read/write to the Operator APIs, meaning they can use them. 
  * The `namespace-view` role can read CR objects of that Operator. 



**Additional resources**

  * [Adding Operators to a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-adding-operators-to-a-cluster "4.1. Adding Operators to a cluster")
  * [Install modes types](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-operatorgroups-membership_olm-understanding-operatorgroups "2.4.5.2. Operator group membership")



## 2.7.2. Recommended solution for multitenant clusters

While a **Multinamespace** install mode does exist, it is supported by very few Operators. As a middle ground solution between the standard **All namespaces** and **Single namespace** install modes, you can install multiple instances of the same Operator, one for each tenant. 

Use the following workflow to install multiple instances of the same Operator: 

  1. Create a namespace for the tenant Operator that is separate from the tenant’s namespace. 
  2. Create an Operator group for the tenant Operator scoped only to the tenant’s namespace. 
  3. Install the Operator in the tenant Operator namespace. 



As a result, the Operator resides in the tenant Operator namespace and watches the tenant namespace, but neither the Operator’s pod nor its service account are visible or usable by the tenant. 

This solution provides better tenant separation, least privilege principle at the cost of resource usage, and additional orchestration to ensure the constraints are met. For a detailed procedure, see "Preparing for multiple instances of an Operator for multitenant clusters". 

### 2.7.2.1. Limitations and considerations

This solution only works when the following constraints are met: 

  * All instances of the same Operator must be the same version. 
  * The Operator cannot have dependencies on other Operators. 
  * The Operator cannot ship a CRD conversion webhook. 



Important

You cannot use different versions of the same Operator on the same cluster. Eventually, the installation of another instance of the Operator would be blocked when it meets the following conditions: 

  * The instance is not the newest version of the Operator. 
  * The instance ships an older revision of the CRDs that lack information or versions that newer revisions have that are already in use on the cluster. 



Warning

As an administrator, use caution when allowing non-cluster administrators to install Operators self-sufficiently, as explained in "Allowing non-cluster administrators to install Operators". These tenants should only have access to a curated catalog of Operators that are known to not have dependencies. These tenants must also be forced to use the same version line of an Operator, to ensure the CRDs do not change. This requires the use of namespace-scoped catalogs and likely disabling the global default catalogs. 

**Additional resources**

  * [Preparing for multiple instances of an Operator for multitenant clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-preparing-operators-multitenant_olm-adding-operators-to-a-cluster "4.1.4. Preparing for multiple instances of an Operator for multitenant clusters")
  * [Allowing non-cluster administrators to install Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-creating-policy "4.8. Allowing non-cluster administrators to install Operators")
  * [Disabling the default OperatorHub catalog sources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-restricted-networks-operatorhub_olm-managing-custom-catalogs "4.9.7. Disabling the default software catalog sources")



## 2.7.3. Operator colocation and Operator groups

Operator Lifecycle Manager (OLM) handles OLM-managed Operators that are installed in the same namespace, meaning their `Subscription` resources are colocated in the same namespace, as related Operators. 

Even if they are not actually related, OLM considers their states, such as their version and update policy, when any one of them is updated. 

**Additional resources**

  * [Multitenancy and Operator colocation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-colocation "2.4.6. Multitenancy and Operator colocation")
