# 4.18. KMM hub and spoke

In RHACM hub-and-spoke deployments, the KMM-Hub controller offloads kernel module building and signing to the hub cluster. Administrators can use the `ManagedClusterModule` custom resource (CR) to load modules on spoke clusters while preserving resources on managed nodes. 

In hub and spoke setups, spokes are focused, resource-constrained clusters that are centrally managed by a hub cluster. Spokes run the single-cluster edition of KMM, with those resource-intensive features disabled. To adapt KMM to this environment, you should reduce the workload running on the spokes to the minimum, while the hub takes care of the expensive tasks. 

Building kernel module images and signing the `.ko` files, should run on the hub. The scheduling of the Module Loader and Device Plugin `DaemonSets` can only happen on the spokes. 

**Additional resources**

  * [Red Hat Advanced Cluster Management (RHACM)](https://www.redhat.com/en/technologies/management/advanced-cluster-management)



## 4.18.1. KMM-Hub

KMM-Hub is a hub-cluster edition of Kernel Module Management for OpenShift Container Platform multi-cluster deployments. It monitors spoke kernel versions, runs image builds and kmod signing on the hub, and delivers trimmed `Module` resources to spokes through RHACM. 

Note

KMM-Hub cannot be used to load kernel modules on the hub cluster. Install the regular edition of KMM to load kernel modules. 

**Additional resources**

  * [Installing KMM](https://openshift-kmm.netlify.app/documentation/install/)



## 4.18.2. Installing KMM-Hub

To deploy KMM-Hub for multi-cluster kernel module management on OpenShift Container Platform, you can install it with Operator Lifecycle Manager (OLM) or by creating KMM resources manually. 

**Additional resources**

  * [KMM Operator bundle](https://catalog.redhat.com/software/containers/kmm/kernel-module-management-hub-operator-bundle/63d84cc33862da54bb19b8c6?architecture=amd64&image=654273ac86f7e537ae452f6ehttps://catalog.redhat.com/software/containers/kmm/kernel-module-management-hub-operator-bundle/63d84cc33862da54bb19b8c6?architecture=amd64&image=654273ac86f7e537ae452f6e)



### 4.18.2.1. Installing KMM-Hub using the Operator Lifecycle Manager

To install KMM-Hub on OpenShift Container Platform using Operator Lifecycle Manager, you can use the **Operators** section of the OpenShift web console. 

**Procedure**

  * Use the **Operators** section of the OpenShift console to install KMM-Hub. 



### 4.18.2.2. Installing KMM-Hub by creating KMM resources

To install KMM-Hub programmatically on OpenShift Container Platform, you can create `Namespace`, `OperatorGroup`, and `Subscription` resources. 

**Procedure**

  * If you want to install KMM-Hub programmatically, you can use the following resources to create the `Namespace`, `OperatorGroup` and `Subscription` resources: 

```yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-kmm-hub
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: kernel-module-management-hub
  namespace: openshift-kmm-hub
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: kernel-module-management-hub
  namespace: openshift-kmm-hub
spec:
  channel: stable
  installPlanApproval: Automatic
  name: kernel-module-management-hub
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


## 4.18.3. Using the ManagedClusterModule CRD

To deploy kernel modules on spoke clusters with KMM-Hub on OpenShift Container Platform, you can configure a cluster-scoped `ManagedClusterModule` custom resource that wraps a `Module` spec and selects target clusters. 

This CRD is cluster-scoped, wraps a `Module` spec and adds the following additional fields: 

```yaml
apiVersion: hub.kmm.sigs.x-k8s.io/v1beta1
kind: ManagedClusterModule
metadata:
  name: <my-mcm>
  # No namespace, because this resource is cluster-scoped.
spec:
  moduleSpec:
    selector:
      node-wants-my-mcm: 'true'

  spokeNamespace: <some-namespace>

  selector:
    wants-my-mcm: 'true'
```


where: 

`spec.moduleSpec`
     Specifies the `moduleLoader` and `devicePlugin` sections, similar to a `Module` resource. 
`spec.moduleSpec.selector`
     Specifies nodes within the `ManagedCluster`. 
`spec.spokeNamespace`
     Specifies in which namespace the `Module` should be created. 
`spec.selector`
     Specifies `ManagedCluster` objects. 

If build or signing instructions are present in `.spec.moduleSpec`, those pods are run on the hub cluster in the operator’s namespace. 

When the `.spec.selector matches` one or more `ManagedCluster` resources, then KMM-Hub creates a `ManifestWork` resource in the corresponding namespace(s). `ManifestWork` contains a trimmed-down `Module` resource, with kernel mappings preserved but all `build` and `sign` subsections are removed. `containerImage` fields that contain image names ending with a tag are replaced with their digest equivalent. 

## 4.18.4. Running KMM on the spoke

To run Kernel Module Management (KMM) on spoke clusters in OpenShift Container Platform, you can install it with a RHACM `Policy` object. After installation, create a `ManagedClusterModule` object from the hub to deploy kernel modules. 

You can install KMM on the spokes cluster through a RHACM `Policy` object. In addition to installing KMM from the software catalog and running it in a lightweight spoke mode, the `Policy` configures additional RBAC required for the RHACM agent to be able to manage `Module` resources. 

**Procedure**

  * Use the following RHACM policy to install KMM on spoke clusters: 

```plaintext
---
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: install-kmm
spec:
  remediationAction: enforce
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        kind: ConfigurationPolicy
        metadata:
          name: install-kmm
        spec:
          severity: high
          object-templates:
          - complianceType: mustonlyhave
            objectDefinition:
              apiVersion: v1
              kind: Namespace
              metadata:
                name: openshift-kmm
          - complianceType: mustonlyhave
            objectDefinition:
              apiVersion: operators.coreos.com/v1
              kind: OperatorGroup
              metadata:
                name: kmm
                namespace: openshift-kmm
              spec:
                upgradeStrategy: Default
          - complianceType: mustonlyhave
            objectDefinition:
              apiVersion: operators.coreos.com/v1alpha1
              kind: Subscription
              metadata:
                name: kernel-module-management
                namespace: openshift-kmm
              spec:
                channel: stable
                config:
                  env:
                    - name: KMM_MANAGED
                      value: "1"
                installPlanApproval: Automatic
                name: kernel-module-management
                source: redhat-operators
                sourceNamespace: openshift-marketplace
          - complianceType: mustonlyhave
            objectDefinition:
              apiVersion: rbac.authorization.k8s.io/v1
              kind: ClusterRole
              metadata:
                name: kmm-module-manager
              rules:
                - apiGroups: [kmm.sigs.x-k8s.io]
                  resources: [modules]
                  verbs: [create, delete, get, list, patch, update, watch]
          - complianceType: mustonlyhave
            objectDefinition:
              apiVersion: rbac.authorization.k8s.io/v1
              kind: ClusterRoleBinding
              metadata:
                name: klusterlet-kmm
              subjects:
              - kind: ServiceAccount
                name: klusterlet-work-sa
                namespace: open-cluster-management-agent
              roleRef:
                kind: ClusterRole
                name: kmm-module-manager
                apiGroup: rbac.authorization.k8s.io
---
apiVersion: apps.open-cluster-management.io/v1
kind: PlacementRule
metadata:
  name: all-managed-clusters
spec:
  clusterSelector:
    matchExpressions: []
---
apiVersion: policy.open-cluster-management.io/v1
kind: PlacementBinding
metadata:
  name: install-kmm
placementRef:
  apiGroup: apps.open-cluster-management.io
  kind: PlacementRule
  name: all-managed-clusters
subjects:
  - apiGroup: policy.open-cluster-management.io
    kind: Policy
    name: install-kmm
```


where: 

`spec.policy-templates.objectDefinition.spec.object-templates.objectDefinition.spec.config.env.name`
     Specifies the environment variable name on the `Subscription` object entry. This variable is required when running KMM on a spoke cluster. 
`spec.clusterSelector`
     Specifies that on the `PlacementRule` object entry, this field can be customized to target select clusters only.
