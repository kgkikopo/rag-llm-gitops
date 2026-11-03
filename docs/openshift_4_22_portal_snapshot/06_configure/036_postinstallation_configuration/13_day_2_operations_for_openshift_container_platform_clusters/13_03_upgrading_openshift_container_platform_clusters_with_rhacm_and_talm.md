# 13.3. Upgrading OpenShift Container Platform clusters with RHACM and TALM

## 13.3.1. About cluster updates with RHACM and TALM

You can use Red Hat Advanced Cluster Management (RHACM) and Topology Aware Lifecycle Manager (TALM) to perform z-stream, y-stream, and EUS-to-EUS updates on spoke clusters managed from a hub cluster. 

The policy-based update workflow uses update policies that you define on the RHACM hub while TALM orchestrates their enforcement across target clusters. 

If you are managing a single cluster or troubleshooting a specific cluster directly, see "Updating an OpenShift Container Platform cluster" for manual updates of individual clusters. 

### 13.3.1.1. Policy-based cluster updates with RHACM and TALM

You can use Red Hat Advanced Cluster Management (RHACM) and Topology Aware Lifecycle Manager (TALM) to automate cluster updates across spoke clusters managed from a hub cluster. 

Optionally, you can manage RHACM policies through a GitOps workflow, storing them in a Git repository for versioning, review, and auditability. 

RHACM provides the policy framework for managing cluster configuration across a fleet of spoke clusters from a central hub cluster. You define RHACM policies that declare the target cluster version, and RHACM evaluates compliance across target clusters. 

TALM orchestrates the rollout of RHACM policies to target clusters according to your batching strategy. TALM uses `ClusterGroupUpgrade` custom resources (CRs) to coordinate which clusters to update, which policies to apply, and how to manage concurrency. A `ClusterGroupUpgrade` CR progresses through several states during an update: 

  * `Preparing`: Cluster readiness and policy compliance are being evaluated. 
  * `InProgress`: Policies are being applied to clusters in batches. 
  * `Complete`: All clusters are successfully updated and compliant. 
  * `Failed`: One or more clusters failed to update. 



### 13.3.1.2. Benefits of TALM for large-scale deployments

Topology Aware Lifecycle Manager (TALM) is specifically designed for large-scale deployments with many clusters across many sites. 

With TALM, you can do the following: 

  * Update hundreds or thousands of clusters from a central hub. 
  * Test updates on a single target cluster before rolling out to the fleet. 
  * Schedule updates during planned downtime using blocking custom resources. 
  * Manage update policies through existing GitOps tools, such as Argo CD, and the same workflows and approval processes you already use for cluster configuration. 



### 13.3.1.3. GitOps workflows for RHACM update policies

GitOps provides a declarative approach to managing cluster configuration and lifecycle operations. You define the desired state of your clusters in Git, and automation tools ensure the actual state matches the desired state. 

For cluster updates, the GitOps workflow begins with defining the desired cluster version as a policy in a Git repository. After committing and pushing the policy changes through your review process, you apply the policy to the RHACM hub cluster. TALM then orchestrates the rollout to target clusters according to your batching strategy, using `ClusterGroupUpgrade` custom resources (CRs). You can monitor progress and verify successful updates throughout the process. 

With a GitOps workflow for cluster updates, you can do the following: 

  * Track changes through Git commit history for full audit trails. 
  * Review policy changes through pull requests before application. 
  * Revert to previous policy versions if needed. 
  * Maintain consistent update configurations across all clusters. 



### 13.3.1.4. Cluster update scenarios

You can perform z-stream, y-stream, and EUS-to-EUS updates on clusters managed by Red Hat Advanced Cluster Management (RHACM) and Topology Aware Lifecycle Manager (TALM). 

Each update scenario has different risk profiles, release cadences, and use cases that align with your operational requirements and maintenance windows. 

#### 13.3.1.4.1. Z-stream updates

Z-stream updates apply patch releases within a minor version, such as updating from 4.20.0 to 4.20.1. These updates address security vulnerabilities and bug fixes without introducing new features. 

Z-stream releases follow a weekly cadence and should be applied as soon as they become available. The risk profile for z-stream updates is low because they do not include API changes or feature modifications. 

The following list describes use cases for z-stream updates: 

  * Applying critical security patches (CVEs) 
  * Resolving production bugs identified in the current minor version 
  * Maintaining compliance with security policies that require timely patching 
  * Performing regular maintenance updates during normal operating windows 



When configured with proper pod disruption budgets, z-stream updates cause minimal workload disruption. Control plane nodes update in a rolling fashion, and worker nodes update one at a time or in small batches. 

#### 13.3.1.4.2. Y-stream updates

Y-stream updates move between minor versions, such as updating from 4.20.x to 4.21.0. These updates introduce new features, performance improvements, and might include API deprecations. 

Typically, Y-stream releases follow a four-month release cadence. You must update through consecutive y-stream versions and cannot skip versions. For example, to update from 4.20 to 4.22, you must update from 4.20 to 4.21, and then from 4.21 to 4.22. If you need to move 2 y-stream versions, consider EUS-to-EUS updates instead. 

The risk profile for y-stream updates is medium because they might include deprecated APIs and configuration changes. Review release notes carefully before updating to identify breaking changes that affect your workloads. 

The following list describes use cases for y-stream updates: 

  * Accessing new OpenShift Container Platform features and capabilities 
  * Maintaining support lifecycle compliance because older versions eventually lose support 
  * Meeting requirements for updated Operator versions 
  * Adopting performance improvements and optimizations 



Y-stream updates require a planned maintenance window. The control plane update typically completes in 60 to 120 minutes, and worker node updates take an additional 30 to 60 minutes. You can minimize workload disruption by pausing worker nodes and updating the control plane first. 

**Additional resources**

  * [EUS-to-EUS updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrade-scenario-eus_core-cluster-upgrades-overview "13.3.1.4.3. EUS-to-EUS updates")



#### 13.3.1.4.3. EUS-to-EUS updates

Extended Update Support (EUS) releases receive 18 months of support and include even-numbered minor versions such as 4.18, 4.20, and 4.22. With EUS-to-EUS updates, the worker nodes in your cluster can jump versions, reducing your upgrade timeline. 

With control-plane-only updates, you can update the control plane to a new EUS version while leaving worker nodes at the previous version. The control plane and workers can be up to two minor versions apart during this staged approach. 

The risk profile for EUS-to-EUS updates is medium to high because they involve larger version jumps. Thorough testing and validation are critical before performing EUS-to-EUS updates in production. 

The following list describes use cases for EUS-to-EUS updates: 

  * Staging control plane updates separately from worker node updates 
  * Minimizing workload disruption by deferring worker updates to a later maintenance window 
  * Aligning updates with long-term support cycles that have 18-month support windows 
  * Managing capacity-constrained environments where full cluster downtime is not feasible 



Control-plane-only EUS updates affect only control plane components. Workloads continue running on worker nodes at the previous version. Worker nodes can be updated days or weeks after the control plane, depending on your maintenance schedule. 

#### 13.3.1.4.4. Selecting an update scenario

The following decision matrix helps you determine which update scenario to use: 

Table 13.1. Decision matrix for update scenariosScenario| When to use| Key considerations  
---|---|---  
Z-stream  |  Security patches or bug fixes needed  |  Apply weekly. Minimal risk and minimal downtime.   
Y-stream  |  New features required or approaching end of support  |  Typically a four-month cadence. Review release notes and plan a maintenance window.   
EUS-to-EUS  |  Long-term planning with staged rollouts  |  18-month support. Control plane and workers can update separately. Larger version jumps require more validation.   
Show more

#### 13.3.1.4.5. Application and cluster configuration policy changes

In addition to OpenShift Container Platform and OLM Operator update policies, review and prepare policies for application and cluster configuration changes that the update might require. 

This can include changes to user policies, security context constraints (SCCs), or version-specific configuration for your cluster. 

For further policy configuration, see the Red Hat Advanced Cluster Management (RHACM) documentation. 

### 13.3.1.5. Additional resources

  * [Updating an OpenShift Container Platform cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-welcome "13.2.1. Upgrading an OpenShift Container Platform cluster")
  * [Verifying cluster API versions between update versions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-api "13.2.2. Verifying cluster API versions between update versions")
  * [Using the Topology Aware Lifecycle Manager for cluster updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-talm-for-cluster-updates)
  * [Bare metal Core reference design specifications](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#telco-core-ref-design-specs)
  * [How to use the Topology Aware Lifecycle Manager](https://www.redhat.com/en/blog/how-to-use-the-topology-aware-lifecycle-manager)
  * [The ultimate guide to OpenShift release and update process for cluster administrators](https://www.redhat.com/en/blog/the-ultimate-guide-to-openshift-release-and-upgrade-process-for-cluster-administrators)
  * [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)
  * [OpenShift Container Platform update lifecycle and support policy](https://access.redhat.com/support/policy/updates/openshift)



## 13.3.2. Prepare RHACM policies and TALM for cluster updates

Before you can perform policy-based cluster updates, you must configure your hub cluster with the required Red Hat Advanced Cluster Management (RHACM) policies, placement rules, and Topology Aware Lifecycle Manager (TALM) `ClusterGroupUpgrade` custom resources (CRs). 

### 13.3.2.1. Preparing RHACM policies and placement rules for cluster updates

You can organize your Git repository, configure cluster labels, and create placement rules to target clusters for policy-based updates. 

**Prerequisites**

  * RHACM hub cluster is deployed and managing target clusters. For more information, see [Red Hat Advanced Cluster Management for Kubernetes documentation](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/). 
  * Topology Aware Lifecycle Manager (TALM) is installed on the RHACM hub cluster. For more information, see "Installing Topology Aware Lifecycle Manager by using the CLI". 
  * You have a Git repository for storing update policies with appropriate access controls. 
  * You have cluster-admin privileges on the RHACM hub cluster. 
  * The `oc` CLI tool is installed and configured. 



**Procedure**

  1. Prepare your Git repository structure similar to the following example: 

```plaintext
upgrade-policies/
├── policies/
│   ├── zstream/
│   │   └── upgrade-4.20.1-policy.yaml
│   ├── ystream/
│   │   └── upgrade-4.20-policy.yaml
│   └── eus/
│       └── upgrade-4.20-eus-policy.yaml
└── cgu/
    ├── core-zstream-upgrade.yaml
    ├── core-ystream-upgrade.yaml
    └── core-eus-upgrade.yaml
```


Note

If you are using Kustomize for policy management with Argo CD or Flux, you can add a `kustomization.yaml` file to manage policy overlays. This file is optional if you apply policies directly with `oc apply`. 

  2. Create a `Placement` rule so that update policies can be bound to clusters through labels. 

Note

If you use PolicyGenerator with Argo CD or a ZTP pipeline, `Placement` and `PlacementBinding` resources are generated automatically from your PolicyGenerator configuration. The following manual steps are provided for environments that do not use PolicyGenerator or for reference when troubleshooting placement issues. 

The following example uses the label `upgrade-version-to-4-21=""` to bind a policy to a cluster: 

```yaml
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Placement
metadata:
  name: openshift-upgrade-placement
  namespace: openshift-upgrade-policies
  annotations:
    policy.open-cluster-management.io/description: |
      Placement rule for OpenShift upgrade policies. Targets clusters with
      the label "upgrade-version-to-4-21" for 4.20 to 4.21 upgrades.
spec:
  predicates:
    - requiredClusterSelector:
        labelSelector:
          matchLabels:
            upgrade-version-to-4-21: ""
```


  3. Create a `PlacementBinding` resource to connect the policies to the placement rule: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: PlacementBinding
metadata:
  name: openshift-upgrade-placement-binding
  namespace: openshift-upgrade-policies
  annotations:
    policy.open-cluster-management.io/description: |
      Binding that connects OpenShift upgrade policies to their placement rule.
      This binding ensures that both the main upgrade policy and pre-upgrade
      health check policy are applied to the same set of target clusters.
placementRef:
  name: openshift-upgrade-placement
  kind: Placement
  apiGroup: cluster.open-cluster-management.io
subjects:
  - name: openshift-upgrade-4.21-policy
    kind: Policy
    apiGroup: policy.open-cluster-management.io
  - name: pre-upgrade-health-check-policy
    kind: Policy
    apiGroup: policy.open-cluster-management.io
```


A single policy, placement rule, and placement binding set can be bound to multiple clusters by adding the matching label to each cluster. 

  4. Add an update label to your target clusters and verify by running the following commands: 

```shell-session
$ oc label managedcluster <cluster_name> upgrade-version-to-4-21=""
$ oc get managedcluster <cluster_name> -o jsonpath='{.metadata.labels}'
```


The following example shows the output: 

```shell-session
{
  "app.kubernetes.io/instance": "clusters",
  "cluster.open-cluster-management.io/clusterset": "default",
  "name": "test1",
  "ocp-version": "4.20",
  "openshiftVersion": "4.20.15",
  "upgrade-version-to-4-21": "",
  "upgrade-version-to-4-22": "",
  "unpause-worker-mcp": ""
}
```


  5. Optional: Label clusters by site location for topology awareness by running the following command: 

```shell-session
$ oc label managedcluster <cluster_name> site=<site_name>
```


  6. Create and apply a `ManagedClusterSet` resource for update targets: 

```yaml
apiVersion: cluster.open-cluster-management.io/v1beta2
kind: ManagedClusterSet
metadata:
  name: core-bm-clusters
spec:
  clusterSelector:
    selectorType: LabelSelector
    labelSelector:
      matchLabels:
        cluster-type: bare-metal-core
```


Apply the `ManagedClusterSet` resource by running the following command: 

```shell-session
$ oc apply -f managedclusterset.yaml
```


**Verification**

  * Verify that TALM is active, cluster labels are applied, and the `ManagedClusterSet` resource exists by running the following commands: 

```shell-session
$ oc get pods -n openshift-operators | grep cluster-group-upgrades
$ oc get managedclusters --show-labels
$ oc get managedclusterset core-bm-clusters
```


The following example shows the output: 

```shell-session
cluster-group-upgrades-controller-manager-5d7b9c8f7d-abc12   2/2     Running   0          5m
```


### 13.3.2.2. ClusterGroupUpgrade custom resource configuration

You can configure `ClusterGroupUpgrade` custom resources (CRs) to orchestrate cluster updates with Topology Aware Lifecycle Manager (TALM). A `ClusterGroupUpgrade` CR defines which clusters to update, which policies to apply, and how to manage batching and concurrency. 

Important

RHACM policies used for updates must be set to `inform` mode. The `ClusterGroupUpgrade` CR temporarily changes these policies to `enforce` mode at the scheduled update time, applying them to the target clusters. When the `ClusterGroupUpgrade` CR completes or times out, the policies automatically revert to `inform` mode. This ensures that update policies are only enforced at the specific time you intend, rather than immediately when the policy is created. 

#### 13.3.2.2.1. Basic ClusterGroupUpgrade CR

The following example shows a basic `ClusterGroupUpgrade` CR: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: <cgu_name>
  namespace: <namespace>
spec:
  clusters:
  - <cluster_name_1>
  - <cluster_name_2>
  managedPolicies:
  - <policy_name>
  enable: false
  remediationStrategy:
    maxConcurrency: <max_concurrency>
    timeout: <timeout_minutes>
```


Table 13.2. ClusterGroupUpgrade CR fieldsField| Description  
---|---  
`name` |  Specifies a name for your `ClusterGroupUpgrade` CR, for example `core-zstream-upgrade-4.20.1`.   
`namespace` |  Specifies the namespace for the resource, for example `openshift-upgrade-policies`.   
`clusters` |  Specifies the names of your target clusters.   
`managedPolicies` |  Specifies the names of your update policies.   
`enable` |  Set to `false` to create the resource without starting the update. Set to `true` to start the update immediately.   
`maxConcurrency` |  Specifies the number of clusters to update simultaneously. Use `1` for canary testing, `2-5` for production rollouts, or higher for large fleets with proven procedures.   
`timeout` |  Specifies the maximum time in minutes to wait for each cluster update. See the timeout guidelines that follow.   
Show more

#### 13.3.2.2.2. Timeout guidelines

Calculate appropriate timeout values based on your environment: 

  * Base timeout: 60 minutes for z-stream updates, 120 minutes for y-stream updates. 
  * Add 30 minutes for each additional worker node beyond 3. 
  * Add 60 minutes for disconnected environments. 
  * Add 30 minutes for clusters with large image registries. 



#### 13.3.2.2.3. Optional configuration fields

You can add the following optional fields to the `spec` section to customize the update behavior: 

  * Canary cluster testing 
  * Pre-update blocking checks 
  * Post-update label management 



#### 13.3.2.2.4. Canary cluster testing

To test the update on a canary cluster before rolling it out to the full fleet, add a `canaries` list under `remediationStrategy` and use `clusterSelector` instead of `clusters` to target clusters by label: 

```yaml
  clusterSelector:
  - <label_selector>
  remediationStrategy:
    canaries:
    - <canary_cluster_name>
    maxConcurrency: 1
```


where: 

  * `<label_selector>`: Specifies a label selector for the target clusters, for example `upgrade-wave=1`. 
  * `<canary_cluster_name>`: Specifies the name of the canary cluster to update first. TALM updates the canary cluster first, waits for success, and then proceeds with other clusters. 



#### 13.3.2.2.5. Pre-update blocking checks

To require pre-update checks to pass before the update begins, add `blockingCRs` and `beforeEnable` fields: 

```yaml
  beforeEnable:
    addClusterLabels:
      pre-upgrade-check: pending
  blockingCRs:
  - name: <blocking_cr_name>
    namespace: <blocking_cr_namespace>
    kind: ConfigMap
    conditions:
    - type: <condition_type>
      status: "True"
```


where: 

  * `<blocking_cr_name>`: Specifies the name of the blocking custom resource, for example `etcd-backup`. 
  * `<condition_type>`: Specifies the condition that must be met before the update can proceed, for example `BackupComplete`. 



#### 13.3.2.2.6. Post-update label management

To update cluster labels after the update completes, add an `afterCompletion` field: 

```yaml
  afterCompletion:
    addClusterLabels:
      upgraded-to: "<target_version>"
      upgrade-status: complete
    removeClusterLabels:
    - pre-upgrade-check
```


where `<target_version>` is the target version, for example `4.20`. 

#### 13.3.2.2.7. Chained ClusterGroupUpgrade CRs for EUS-to-EUS updates

For Extended Update Support (EUS) to EUS updates, you can create chained `ClusterGroupUpgrade` CRs that use `blockingCRs` and `actions` to orchestrate a multi-step update: 

```yaml
---
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: upgrade-20to21
  namespace: openshift-upgrade-policies
spec:
  actions:
    afterCompletion:
      deleteClusterLabels:
        upgrade-version-to-4-21: ""
      deleteObjects: true
      addClusterLabels:
        unpause-workers-4-22: ""
  backup: false
  clusters:
  - <cluster_name>
  enable: true
  managedPolicies:
    - prep-20to22
    - upgrade-ocp-20to21
    - upgrade-olm-20to21
    - upgrade-validate-21
  preCaching: false
  preCachingConfigRef: {}
  remediationStrategy:
    maxConcurrency: 1
    timeout: 480
---
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: upgrade-21to22
  namespace: openshift-upgrade-policies
spec:
  actions:
    afterCompletion:
      deleteClusterLabels:
        upgrade-version-4-22: ""
        unpause-workers-4-22: ""
      deleteObjects: true
  backup: false
  clusters:
  - <cluster_name>
  enable: true
  managedPolicies:
    - upgrade-ocp-21to22
    - upgrade-olm-21to22
    - upgrade-validate-22
    - upgrade-worker-1
    - upgrade-worker-2
  preCaching: false
  preCachingConfigRef: {}
  remediationStrategy:
    maxConcurrency: 1
    timeout: 480
  blockingCRs:
  - name: upgrade-20to21
    namespace: openshift-upgrade-policies
```


where: 

  * `<cluster_name>`: Specifies the name of the target cluster. 
  * `actions`: Changes cluster labels as each step completes. This removes temporary update labels and unbinds completed update policies from the cluster. 
  * `blockingCRs`: Requires the first `ClusterGroupUpgrade` CR to complete before the second `ClusterGroupUpgrade` CR begins enforcing its policies. 
  * `upgrade-worker-1`, `upgrade-worker-2`: Separate unpause policies for each `MachineConfigPool` resource. Your cluster might have more machine config pools, requiring additional policies. 



#### 13.3.2.2.8. Applying and monitoring a ClusterGroupUpgrade CR

After creating a `ClusterGroupUpgrade` CR, apply and enable it by running the following commands: 

```shell-session
$ oc apply -f <cgu_cr_filename>.yaml
$ oc patch cgu <cgu_name> \
  -n <namespace> \
  --type merge \
  -p '{"spec":{"enable":true}}'
```


Monitor the `ClusterGroupUpgrade` status by running the following commands: 

```shell-session
$ oc get cgu <cgu_name> -n <namespace> -o yaml
$ oc get cgu <cgu_name> -n <namespace> -w
```


Check the `status` section for update progress: 

The following example shows the output: 

\+ 

```yaml
status:
  conditions:
  - message: Upgrade is progressing
    reason: InProgress
    status: "True"
    type: Progressing
  managedPoliciesForUpgrade:
  - name: core-upgrade-4.20.1-policy
    namespace: openshift-upgrade-policies
  remediationPlan:
  - - spoke1
    - spoke2
  status:
    spoke1: complete
    spoke2: inprogress
```


Verify the `ClusterGroupUpgrade` CR entered the expected state by running the following commands: 

```shell-session
$ oc get cgu -n <namespace>
$ oc get cgu <cgu_name> -n <namespace> -o jsonpath='{.status.clusters}'
```


The following example shows the output: 

\+ 

```shell-session
NAME                             AGE   STATE        DETAILS
core-zstream-upgrade-4.20.1     5m    InProgress   Remediating non-compliant policies
```


When the cluster is fully updated and the state of all `ClusterGroupUpgrade` CRs shows `Completed`, verify that all policies show `Compliant` by running the following command: 

```shell-session
$ oc get policies -n <cluster_name>
```


The following example shows the output: 

\+ 

```shell-session
NAME                        REMEDIATION ACTION   COMPLIANCE STATE   AGE
upgrade.upgrade-ocp-21to22  inform               Compliant          1h
upgrade.upgrade-olm-21to22  inform               Compliant          10m
```


Delete the completed `ClusterGroupUpgrade` CRs from the update namespace by running the following command: 

```shell-session
$ oc delete cgu -n <namespace> <cgu_name>
```


#### 13.3.2.2.9. Troubleshooting

  * If the `ClusterGroupUpgrade` CR is stuck in `Preparing` state, verify that all managed policies exist and are bound to target clusters. 
  * If the `ClusterGroupUpgrade` CR fails with a timeout error, increase the `timeout` value in the `remediationStrategy` section. 



### 13.3.2.3. Additional resources

  * [Overview of cluster updates with RHACM and TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-overview "13.3.1. About cluster updates with RHACM and TALM")
  * [Installing Topology Aware Lifecycle Manager by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#installing-topology-aware-lifecycle-manager-using-cli_cnf-topology-aware-lifecycle-manager)
  * [RHACM](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes)
  * [`ClusterGroupUpgrade` samples on GitHub](https://github.com/openshift-kni/cluster-group-upgrades-operator/tree/main/samples)



## 13.3.3. Prepare worker node pools before a cluster update with TALM

You can configure worker node batching to control how many worker nodes update simultaneously and how workloads tolerate disruption during cluster updates by using `MachineConfigPool` and `PodDisruptionBudget` resources. 

### 13.3.3.1. Configuring worker node batching by using machine config pools

You can configure the `MachineConfigPool` resource to control how many worker nodes update simultaneously during a cluster update. Adjusting the `maxUnavailable` setting balances update speed against workload availability. 

**Prerequisites**

  * You have access to the target cluster with cluster-admin privileges. 
  * The `oc` CLI tool is installed and configured. 



**Procedure**

  1. Check the current `maxUnavailable` setting for the worker `MachineConfigPool` resource by running the following command: 

```shell-session
$ oc get mcp worker -o jsonpath='{.spec.maxUnavailable}'
```


  2. Set the required `maxUnavailable` value in the worker `MachineConfigPool` resource by running the following command: 

```shell-session
$ oc patch mcp worker --type merge -p '{"spec":{"maxUnavailable":"<max_unavailable>"}}'
```


where `<max_unavailable>` is one of the following values: 

     * An integer, for example `1`, to specify the exact number of nodes that can be unavailable during the update. 
     * A percentage, for example `"50%"`, to specify the proportion of nodes that can be unavailable. 

Note

The default `maxUnavailable` value is 1 worker node or 33% of worker nodes, whichever is smaller. Setting a higher value accelerates updates but increases the number of nodes unavailable at any given time. Consult your application teams to find the appropriate value for your workloads. 

  3. Verify the updated setting by running the following command: 

```shell-session
$ oc get mcp worker -o yaml
```


**Verification**

  * Verify the `MachineConfigPool` resource reflects the updated `maxUnavailable` value by running the following command: 

```shell-session
$ oc get mcp worker -o jsonpath='{.spec.maxUnavailable}'
```


### 13.3.3.2. Configuring worker node batching by using pod disruption budgets

You can configure `PodDisruptionBudget` resources to control how your workloads tolerate node draining during cluster updates. Pod disruption budgets ensure that a minimum number of pod replicas remain available during worker node updates. 

**Prerequisites**

  * You have access to the target cluster with cluster-admin privileges. 
  * The `oc` CLI tool is installed and configured. 
  * You have identified critical workloads that run with replicas. 



**Procedure**

  1. Create a `PodDisruptionBudget` resource for each critical workload: 

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: <pdb_name>
  namespace: <namespace>
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      app: <app_label>
```


where: 

     * `<pdb_name>`: Specifies a name for the `PodDisruptionBudget` resource, for example `cnf-workload-pdb`. 
     * `<namespace>`: Specifies the namespace where the workload runs, for example `cnf-workload`. 
     * `maxUnavailable`: Specifies the maximum number of pods that can be unavailable during a disruption. Set this value to at least `1` to allow node draining to proceed. 
     * `<app_label>`: Specifies the label selector that matches the pods for this workload. 

  2. Apply the `PodDisruptionBudget` resource by running the following command: 

```shell-session
$ oc apply -f <pdb_filename>.yaml
```


  3. Verify that the pod disruption budget allows at least one disruption by running the following command: 

```shell-session
$ oc get pdb <pdb_name> -n <namespace>
```


The following example shows the output: 

```shell-session
NAME               MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
cnf-workload-pdb   N/A             1                 1                     30s
```


Important

Ensure the `ALLOWED DISRUPTIONS` column shows a value greater than 0. If this value is 0, the pod disruption budget blocks node draining and updates stall. Do not set `minAvailable` to 100% of replicas, as this prevents any disruption. 

  4. Repeat steps 1-3 for all critical workloads in your cluster. 
  5. Verify all pod disruption budgets across the cluster by running the following command: 

```shell-session
$ oc get pdb -A
```


**Verification**

  * Verify that no pod disruption budgets are blocking disruptions by running the following command: 

```shell-session
$ oc get pdb -A -o jsonpath='{range .items[?(@.status.disruptionsAllowed==0)]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```


This command must produce no output. If the output lists any pod disruption budgets, adjust their configuration before updating. 




### 13.3.3.3. Additional resources

  * [Configuring application pods before updating your OpenShift Container Platform cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-cnf-update-prep "13.2.4. Configuring application pods before updating your OpenShift Container Platform cluster")
  * [Kubernetes PodDisruptionBudget documentation](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
  * [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)



## 13.3.4. Perform health checks before a cluster update with TALM

Running pre-update health checks reduces the risk of update failures and identifies problems early. If any checks fail, resolve the issues before proceeding with the cluster update. 

### 13.3.4.1. Performing health checks before cluster updates

You can perform comprehensive health checks before updating clusters to ensure cluster components are ready for the update. These checks validate cluster Operators, etcd health, storage systems, network connectivity, and custom resources specific to your deployment. 

Complete these health checks before starting any cluster update to minimize the risk of update failures. 

**Prerequisites**

  * You have access to target clusters with cluster-admin privileges. 
  * The `oc` CLI tool is installed and configured for the target cluster. 



**Procedure**

  1. Verify control plane node readiness by running the following command: 

```shell-session
$ oc get nodes -l node-role.kubernetes.io/master=
```


The following example shows the output: 

```shell-session
NAME                   STATUS   ROLES                  AGE   VERSION
master-0.example.com   Ready    control-plane,master   30d   v1.33.0
master-1.example.com   Ready    control-plane,master   30d   v1.33.0
master-2.example.com   Ready    control-plane,master   30d   v1.33.0
```


All control plane nodes must show `Ready` status with no `SchedulingDisabled` notation. If any nodes show `NotReady` or `SchedulingDisabled`, investigate and resolve before updating. 

  2. Verify worker node readiness by running the following command: 

```shell-session
$ oc get nodes -l node-role.kubernetes.io/worker=
```


All worker nodes must show `Ready` status. If any nodes show `NotReady` or `SchedulingDisabled`, investigate and resolve before updating. 

  3. Check cluster Operator status by running the following command: 

```shell-session
$ oc get co
```


The following example shows the output: 

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.20.0    True        False         False      30d
cloud-controller-manager                   4.20.0    True        False         False      30d
cluster-autoscaler                         4.20.0    True        False         False      30d
```


All cluster Operators must show the following: 

     * `AVAILABLE`: `True`
     * `PROGRESSING`: `False`
     * `DEGRADED`: `False`

If any Operator is degraded or progressing, resolve the issue before proceeding. 

  4. Verify etcd cluster health by running the following command: 

```shell-session
$ oc get etcd -o=jsonpath='{range .items[0].status.conditions[?(@.type=="EtcdMembersAvailable")]}{.message}{"\n"}{end}'
```


The following example shows the output: 

```shell-session
3 members are available
```


All etcd members must be available. If the output indicates unhealthy members, investigate etcd pod logs before updating. 

  5. Check your backup storage location for an etcd backup created within the past 24 hours. 

If no recent backup exists, create an etcd backup before proceeding. For more information, see "Backing up etcd" in the "Additional resources" section. 

  6. Verify machine config pool status by running the following command: 

```shell-session
$ oc get mcp
```


The following example shows the output: 

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-abc123                             True      False      False      3              3                   3                     0                      30d
worker   rendered-worker-def456                             True      False      False      3              3                   3                     0                      30d
```


All machine config pools must show the following: 

     * `UPDATED`: `True`
     * `UPDATING`: `False`
     * `DEGRADED`: `False`
     * `MACHINECOUNT` must equal `READYMACHINECOUNT` and `UPDATEDMACHINECOUNT`

  7. Verify persistent volume health by running the following command: 

```shell-session
$ oc get pv
```


All persistent volumes must show `Bound` or `Available` status. Persistent volumes must not show `Failed` status. 

  8. Verify that a default storage class exists by running the following command: 

```shell-session
$ oc get storageclass
```


At least one storage class must be marked as `(default)`. 

  9. If your cluster uses SR-IOV, verify network node policies by running the following command: 

```shell-session
$ oc get sriovnetworknodepolicy -n openshift-sriov-network-operator
```


All SR-IOV network node policies must show `Succeeded` or `InProgress` state. 

  10. Verify OLM Operator health by running the following command: 

```shell-session
$ oc get csv -A
```


All `ClusterServiceVersions` must show `Succeeded` phase. If any Operators show `Failed` or `Installing` phase, investigate before updating. 

  11. Verify that no pods are in an unexpected state by running the following command: 

```shell-session
$ oc get pod -A | grep -E -i -v 'complete|running'
```


The command must produce no output. If any pods are listed, review their status before updating. 

  12. Verify that pod disruption budgets (PDBs) are configured for all critical cloud-native network function (CNF) workloads by running the following command: 

```shell-session
$ oc get pdb -A
```


The following example shows the output: 

```shell-session
NAME                    MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
cnf-workload-pdb        2               N/A               1                     30d
```


PDBs must allow at least one disruption. Setting `minAvailable` to 100% of replicas blocks node drains during updates. 

  13. Check `PerformanceProfile` status by running the following command: 

```shell-session
$ oc get performanceprofile
```


The following example shows the output: 

```shell-session
NAME               AGE
core-performance   30d
```


  14. Verify the `PerformanceProfile` shows `Applied` status by running the following command: 

```shell-session
$ oc get performanceprofile core-performance -o jsonpath='{.status.conditions[?(@.type=="Applied")].status}'
```


The output must be `True`. 

  15. Verify API server responsiveness by running the following command: 

```shell-session
$ oc version
```


The command should complete within a few seconds. If the API server is slow to respond, investigate before updating. 

  16. Verify certificate validity by running the following command: 

```shell-session
$ oc -n openshift-kube-apiserver-operator get secret kube-apiserver-to-kubelet-signer -o jsonpath='{.metadata.annotations.auth\.openshift\.io/certificate-not-after}'
```


Certificates that expire within 30 days must be renewed before updating. If `cert-manager` is installed in the cluster, you can also run `oc get certificates -A` to check additional managed certificates. 

  17. Check CPU and memory utilization on nodes by running the following command: 

```shell-session
$ oc adm top nodes
```


The following example shows the output: 

```shell-session
NAME                   CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
master-0.example.com   500m         25%    8Gi             50%
worker-0.example.com   1000m        50%    16Gi            60%
```


Nodes should have sufficient headroom for rolling updates. CPU usage should be below 80%, and memory usage should be below 85%. 




**Troubleshooting**

  * If cluster Operators are degraded, check Operator logs by running the following command: 

```shell-session
$ oc logs -n openshift-<operator_namespace> <operator_pod_name>
```


  * If etcd members are unhealthy, investigate etcd pod logs by running the following command: 

```shell-session
$ oc logs -n openshift-etcd <etcd_pod_name>
```


  * If PDBs block updates, review PDB configuration to ensure they allow sufficient disruptions. 
  * If nodes show `NotReady` status, check the node conditions by running the following command: 

```shell-session
$ oc describe node <node_name> | grep -A 10 Conditions
```


Check kubelet logs by running the following command: 

```shell-session
$ oc debug node/<node_name> -- chroot /host journalctl -u kubelet
```


Common causes for `NotReady` nodes include disk pressure, memory pressure, and network connectivity issues. 




### 13.3.4.2. Additional resources

  * [Checking the cluster health](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#update-checking-cluster-health_update-before-the-update "13.2.5.3. Checking the cluster health")
  * [Backing up etcd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/#backup-etcd)



## 13.3.5. Manage worker nodes during a cluster update with TALM

You can pause and unpause worker nodes during cluster updates to stage control plane and worker node updates separately, minimizing workload disruption. 

### 13.3.5.1. Pausing and unpausing worker nodes by using TALM

You can pause worker nodes before updating the control plane by using Topology Aware Lifecycle Manager (TALM) policies. After the control plane update completes, you can unpause worker nodes to apply the update to compute resources during a separate maintenance window. 

Pausing worker nodes prevents the `MachineConfigPool` resource from updating worker nodes while the control plane updates, minimizing workload disruption. 

**Prerequisites**

  * You have access to clusters with cluster-admin privileges. 
  * Topology Aware Lifecycle Manager (TALM) is installed on the Red Hat Advanced Cluster Management (RHACM) hub cluster. 



**Procedure**

  1. Create a RHACM policy for each `MachineConfigPool` resource that needs to be paused during the update: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: pause-<mcp_name>
  namespace: openshift-upgrade-policies
spec:
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        evaluationInterval:
          compliant: never
        kind: ConfigurationPolicy
        metadata:
          name: pause-<mcp_name>
        spec:
          object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: machineconfiguration.openshift.io/v1
                kind: MachineConfigPool
                metadata:
                  name: <mcp_name>
                spec:
                  paused: true
          remediationAction: inform
          severity: low
  remediationAction: inform
```


where `<mcp_name>` is the name of the machine config pool to pause, for example `mcp-1`. This value is used in both the policy name and the `MachineConfigPool` resource name. 

Important

Create a separate policy for each `MachineConfigPool` resource that you need to pause during the cluster update. If the machine config pool is not paused, any machine configuration change triggers a node reboot. Pausing the machine config pool allows all configuration changes to be applied in a single reboot when the pool is unpaused. 

  2. Apply the policy to RHACM by running the following command: 

```shell-session
$ oc apply -f pause-<mcp_name>-policy.yaml
```


  3. Include the pause policy in your `ClusterGroupUpgrade` custom resource (CR) before the update policy: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: <cgu_name>
  namespace: <namespace>
spec:
  clusters:
  - <cluster_name>
  managedPolicies:
  - pause-<mcp_name>
  - <upgrade_policy_name>
  enable: false
  remediationStrategy:
    maxConcurrency: 1
    timeout: 120
```


TALM applies the pause policy before applying the update policy, ensuring workers remain paused during the control plane update. 

  4. After the control plane update completes and you are ready to update worker nodes, create an unpause policy for each `MachineConfigPool` resource: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: unpause-<mcp_name>
  namespace: openshift-upgrade-policies
spec:
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        evaluationInterval:
          compliant: never
        kind: ConfigurationPolicy
        metadata:
          name: unpause-<mcp_name>
        spec:
          object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: machineconfiguration.openshift.io/v1
                kind: MachineConfigPool
                metadata:
                  name: <mcp_name>
                spec:
                  paused: false
          remediationAction: inform
          severity: low
  remediationAction: inform
```


where `<mcp_name>` is the name of the machine config pool to unpause, for example `mcp-1`. 

The unpause policies for each machine config pool are included as managed policies in the final `ClusterGroupUpgrade` CR. When TALM enforces these policies, the machine config pools unpause and all accumulated configuration changes are applied in a single reboot per node. 

  5. Apply the unpause policy by using a `ClusterGroupUpgrade` CR: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: <cgu_name>
  namespace: <namespace>
spec:
  clusters:
  - <cluster_name>
  managedPolicies:
  - unpause-<mcp_name>
  enable: false
  remediationStrategy:
    maxConcurrency: 1
```


  6. Apply and enable the `ClusterGroupUpgrade` CR to unpause workers by running the following commands: 

```shell-session
$ oc apply -f <unpause_cgu_cr_filename>.yaml
$ oc patch cgu <cgu_name> \
  -n <namespace> \
  --type merge \
  -p '{"spec":{"enable":true}}'
```


  7. Monitor worker node updates after unpausing by running the following command: 

```shell-session
$ oc get mcp <mcp_name> -w
```


The `MachineConfigPool` status shows the rolling update progress. Nodes update in a rolling fashion based on the `maxUnavailable` setting. 




**Verification**

  1. Verify that worker nodes are updated and workloads are healthy by running the following commands: 

```shell-session
$ oc get nodes
$ oc get mcp <mcp_name>
$ oc get pods -A | grep -v Running | grep -v Completed
```


All nodes must show `Ready` status and the expected kubelet version. For the `MachineConfigPool` output, verify that `MACHINECOUNT` = `READYMACHINECOUNT` = `UPDATEDMACHINECOUNT`. The `oc get pods` command must return no unexpected pods. 




**Troubleshooting**

  * If the pause policy does not take effect, verify the policy is enforced in RHACM by running the following command: 

```shell-session
$ oc get policy <pause_policy_name> -n <namespace>
```


  * If workers update despite being paused, check for manual `MachineConfigPool` edits that override the policy. 
  * If a worker node update gets stuck, check the node status by running the following command: 

```shell-session
$ oc describe node <worker_node_name>
```


  * Common issues include pod disruption budgets blocking node draining, pods with local storage that cannot be evicted, or node cordoning preventing new pods from scheduling. 

To identify blocking pod disruption budgets, run the following command: 

```shell-session
$ oc get pdb -A -o jsonpath='{range .items[?(@.status.disruptionsAllowed==0)]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```


### 13.3.5.2. Pausing and unpausing worker nodes by using machine config pools

You can pause and unpause worker nodes directly by patching the `MachineConfigPool` resource on the target cluster. Use this method when you are managing a single cluster or when you do not have Topology Aware Lifecycle Manager (TALM) configured. 

**Prerequisites**

  * You have access to the target cluster with cluster-admin privileges. 
  * The `oc` CLI tool is installed and configured. 



**Procedure**

  1. Pause the worker `MachineConfigPool` resource by running the following command: 

```shell-session
$ oc patch mcp worker --type merge -p '{"spec":{"paused":true}}'
```


  2. Verify the worker `MachineConfigPool` resource is paused and workloads continue running by running the following commands: 

```shell-session
$ oc get mcp worker -o jsonpath='{.spec.paused}'
$ oc get mcp worker
$ oc get pods -A -o wide | grep worker
```


  3. After the control plane update completes and you are ready to update worker nodes, unpause the worker `MachineConfigPool` resource by running the following command: 

```shell-session
$ oc patch mcp worker --type merge -p '{"spec":{"paused":false}}'
```


  4. Monitor worker node updates after unpausing by running the following commands: 

```shell-session
$ oc get mcp worker -w
$ oc get nodes -l node-role.kubernetes.io/worker= -w
```


Nodes progress through the following states: 

     * `Ready,SchedulingDisabled`: Node is being drained 
     * `NotReady,SchedulingDisabled`: Node is rebooting with new configuration 
     * `Ready`: Node update complete 




**Verification**

  * Verify that worker nodes are updated and workloads are healthy by running the following commands: 

```shell-session
$ oc get nodes
$ oc get mcp worker
$ oc get pods -A | grep -v Running | grep -v Completed
```


All nodes must show `Ready` status and the expected kubelet version. For the `MachineConfigPool` output, verify that `MACHINECOUNT` = `READYMACHINECOUNT` = `UPDATEDMACHINECOUNT`. The `oc get pods` command must return no unexpected pods. 




### 13.3.5.3. Additional resources

  * [Complete an EUS-to-EUS cluster update with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-eus "13.3.9. Complete an EUS-to-EUS cluster update with TALM")
  * [Prepare worker node pools before a cluster update with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-worker-batching "13.3.3. Prepare worker node pools before a cluster update with TALM")
  * [Using the Topology Aware Lifecycle Manager for cluster updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-talm-for-cluster-updates)



## 13.3.6. Coordinate OLM-managed Operator updates with TALM

OLM-managed Operators must be compatible with the target OpenShift Container Platform version before you begin a cluster update. Planning Operator updates alongside cluster updates prevents compatibility issues that can block or degrade the update process. 

### 13.3.6.1. Coordinating OLM Operator updates with cluster updates

You can coordinate Operator Lifecycle Manager (OLM) Operator updates with OpenShift Container Platform cluster updates to ensure Operator compatibility. Incompatible Operators can block cluster updates or cause degraded cluster Operators after updates complete. 

**Prerequisites**

  * You have an understanding of OLM concepts including subscriptions, channels, and `ClusterServiceVersions` (CSVs). 
  * You have access to clusters with cluster-admin privileges. 
  * Topology Aware Lifecycle Manager (TALM) is installed on the Red Hat Advanced Cluster Management (RHACM) hub cluster. 
  * A cluster update is planned or in progress. 



**Procedure**

  1. Check installed Operator versions and subscription channels by running the following commands: 

```shell-session
$ oc get csv -A
$ oc get subscription -A
```


The following example shows the output: 

```shell-session
NAMESPACE                              NAME                                          VERSION   PHASE
openshift-sriov-network-operator       sriov-network-operator.v4.20.0                4.20.0    Succeeded
openshift-ptp                          ptp-operator.v4.20.0                          4.20.0    Succeeded
openshift-cluster-node-tuning-operator node-tuning-operator.v4.20.0                  4.20.0    Succeeded
```


The following example shows the output: 

```shell-session
NAMESPACE                              NAME                                PACKAGE                  SOURCE             CHANNEL
openshift-sriov-network-operator       sriov-network-operator-subscription sriov-network-operator   redhat-operators   stable-4.20
openshift-ptp                          ptp-operator-subscription           ptp-operator             redhat-operators   stable-4.20
```


  2. Identify Operators that need channel updates before the cluster update: 

Review Operator compatibility in the OpenShift Container Platform release notes and identify which Operator channels support your target OpenShift Container Platform version. For a cluster updating from 4.20 to 4.21, identify Operators still on 4.20 channels. Refer to the [Red Hat Catalog](https://catalog.redhat.com/en) for compatibility details for each Operator. 

  3. Create an OLM Operator update policy. 

In environments where Operator updates are set to manual approval, use a TALM-managed policy to coordinate Operator updates. When TALM enforces the policy, it automatically approves the Operator `InstallPlan`: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: upgrade-olm-21
  namespace: openshift-upgrade-policies
  annotations:
    ran.openshift.io/soak-seconds: "60"
spec:
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        kind: ConfigurationPolicy
        metadata:
          name: upgrade-olm-21
        spec:
          object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: operators.coreos.com/v1alpha1
                kind: Subscription
                metadata:
                  name: cluster-logging
                  namespace: openshift-logging
                spec:
                  name: cluster-logging
                  channel: stable-6.1
                status:
                  state: AtLatestKnown
```


where: 

     * `ran.openshift.io/soak-seconds`: Specifies the soak-seconds annotation that gives the catalog pod time to restart and OLM time to read version data from the new pod before evaluating the `Subscription` status. This avoids a race condition where the policy evaluates too quickly after a catalog image change. 
     * `channel`: Sets the channel only if it needs to change for the new version. Channels are determined by the Operator development team. Refer to the [Red Hat Catalog](https://catalog.redhat.com/en) for compatibility. 
     * `status.state: AtLatestKnown`: Ensures the Operator update completes before TALM proceeds to the next step. 

You can include multiple Operator subscriptions in the same policy. The following example shows multiple Operators in a single policy: 

```yaml
spec:
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        kind: ConfigurationPolicy
        metadata:
          name: upgrade-olm-20to21
        spec:
          object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: operators.coreos.com/v1alpha1
                kind: Subscription
                metadata:
                  name: sriov-network-operator-subscription
                  namespace: openshift-sriov-network-operator
                spec:
                  name: sriov-network-operator
                  channel: stable
                  installPlanApproval: Manual
                  source: redhat-operators
                  sourceNamespace: openshift-marketplace
                status:
                  state: AtLatestKnown
            - complianceType: musthave
              objectDefinition:
                apiVersion: operators.coreos.com/v1alpha1
                kind: Subscription
                metadata:
                  name: kubernetes-nmstate-operator
                  namespace: openshift-nmstate
                spec:
                  name: kubernetes-nmstate-operator
                  channel: stable
                  installPlanApproval: Manual
                  source: redhat-operators
                  sourceNamespace: openshift-marketplace
                status:
                  state: AtLatestKnown
```


For an example of creating this policy with zero touch provisioning (ZTP), see [Example OLM update policy in the OpenShift KNI reference repository](https://github.com/openshift-kni/telco-reference/blob/main/telco-core/configuration/core-upgrade.yaml#L68-L101). 

  4. Monitor Operator updates and verify the new versions by running the following commands: 

```shell-session
$ oc get csv -n openshift-sriov-network-operator -w
$ oc get csv -n openshift-sriov-network-operator -o jsonpath='{.items[?(@.spec.version=="4.21.0")].status.phase}'
```


The Operator creates a new `ClusterServiceVersion` and transitions to the new version. 

The following example shows the output: 

```shell-session
Succeeded
```


  5. After the control plane update completes, check for pending Operator updates by running the following command: 

```shell-session
$ oc get csv -A
```


Some Operators might not update until after the cluster update completes. 

  6. If Operators are configured with manual approval, list and approve pending install plans by running the following commands: 

```shell-session
$ oc get installplan -A
$ oc patch installplan <install_plan_name> \
  -n <namespace> \
  --type merge \
  -p '{"spec":{"approved":true}}'
```


  7. Verify Operator health after cluster update by running the following command: 

```shell-session
$ oc get csv -A
```


All Operators must show `Succeeded` phase. 

  8. Verify CNF-specific Operator pods and custom resources by running the following commands: 

```shell-session
$ oc get pods -n openshift-sriov-network-operator
$ oc get pods -n openshift-ptp
$ oc get performanceprofile -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.conditions[?(@.type=="Applied")].status}{"\n"}{end}'
$ oc get ptpconfig -n openshift-ptp
$ oc get sriovnetworknodepolicy -n openshift-sriov-network-operator
$ oc get sriovnetworknodepolicy -n openshift-sriov-network-operator -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.syncStatus}{"\n"}{end}'
$ oc get pods -n openshift-ptp -l app=linuxptp-daemon -o wide
```


All custom resources must show expected status. 

Review Operator considerations specific to your deployment: 

     * Node Tuning Operator: The Node Tuning Operator provides performance tuning capabilities through `PerformanceProfile` custom resources. Verify that performance profiles are reconciled after the update. 
     * SR-IOV Network Operator: The SR-IOV Network Operator might require node reboots when updating to new versions. Schedule Operator updates during maintenance windows to avoid unexpected node reboots. 
     * PTP Operator: PTP configurations are sensitive to version changes. Validate PTP synchronization after Operator updates. 




**Verification**

  1. Verify that all Operators and custom resources are healthy by running the following commands: 

```shell-session
$ oc get csv -A
$ oc get pods -A | grep -E "openshift-sriov|openshift-ptp|openshift-performance"
$ oc get performanceprofile,ptpconfig,sriovnetworknodepolicy -A
```


All `ClusterServiceVersion` resources must show `Succeeded` phase. All Operator pods must be `Running` and ready. Custom resources must exist and show the expected configuration. 




**Troubleshooting**

  * If an Operator blocks the cluster update, update the Operator subscription channel before updating the cluster. 
  * If an Operator is stuck in `Installing` phase, check catalog source availability by running the following command: 

```shell-session
$ oc get catalogsource -n openshift-marketplace
```


  * If a custom resource is not reconciling, check Operator logs by running the following command: 

```shell-session
$ oc logs -n <operator_namespace> deployment/<operator_deployment>
```


  * If Operator pods are in `CrashLoopBackOff`, check for compatibility issues with the new cluster version. 



### 13.3.6.2. Additional resources

  * [Prepare RHACM policies and TALM for cluster updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-preparing-policies "13.3.2. Prepare RHACM policies and TALM for cluster updates")
  * [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)



## 13.3.7. Complete a z-stream cluster update with TALM

You can update clusters to z-stream patch releases by using RHACM policies and Topology Aware Lifecycle Manager (TALM). 

### 13.3.7.1. Updating clusters with z-stream releases

You can update clusters to z-stream patch releases by using RHACM policies and Topology Aware Lifecycle Manager (TALM). Z-stream updates apply security fixes and bug fixes with minimal risk and should be performed regularly to maintain cluster security. 

Apply z-stream updates as soon as they become available to address critical vulnerabilities and maintain security compliance. 

Note

The following procedure uses `spoke1` and `spoke2` as example cluster names. Replace these with your actual cluster names throughout. 

**Prerequisites**

  * You have completed the pre-update health check successfully. 
  * TALM is installed and configured on the Red Hat Advanced Cluster Management (RHACM) hub cluster. 
  * A z-stream patch release is available on the Red Hat Customer Portal. 
  * A recent etcd backup exists that was created within the past 24 hours. 



**Procedure**

  1. Verify the current cluster version by running the following command: 

```shell-session
$ oc get clusterversion
```


The following example shows the output: 

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.20.0    True        False         30d     Cluster version is 4.20.0
```


  2. Check for available z-stream updates by running the following command: 

```shell-session
$ oc adm upgrade
```


The following example shows the output: 

```shell-session
Cluster version is 4.20.0

Upstream is unset, so the cluster will use an appropriate default.
Channel: stable-4.20 (available channels: candidate-4.20, eus-4.20, fast-4.20, stable-4.20)

Recommended updates:

  VERSION     IMAGE
  4.20.1      quay.io/openshift-release-dev/ocp-release@sha256:abc123...
  4.20.2      quay.io/openshift-release-dev/ocp-release@sha256:def456...
```


Review the OpenShift Container Platform release notes for the target version to identify security fixes and bug fixes included in the z-stream release. 

  3. Create a RHACM policy for the z-stream update: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: core-upgrade-4.20.1-policy
  namespace: openshift-upgrade-policies
spec:
  remediationAction: inform
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: upgrade-cluster-version
      spec:
        remediationAction: inform
        severity: high
        object-templates:
        - complianceType: musthave
          objectDefinition:
            apiVersion: config.openshift.io/v1
            kind: ClusterVersion
            metadata:
              name: version
            spec:
              channel: stable-4.20
              desiredUpdate:
                version: 4.20.1
```


Replace `4.20.1` with your target z-stream version. The policy is set to `inform` so it does not immediately push the update. The `ClusterGroupUpgrade` custom resource (CR) enforces the policy at the scheduled update time. 

  4. Apply the policy to the RHACM hub cluster by running the following command: 

```shell-session
$ oc apply -f core-upgrade-4.20.1-policy.yaml
```


  5. Verify the policy and placement resources were created by running the following commands: 

```shell-session
$ oc get policy core-upgrade-4.20.1-policy -n openshift-upgrade-policies
$ oc get placementbinding -n openshift-upgrade-policies
$ oc get placement -n openshift-upgrade-policies
```


The following example shows the output: 

```shell-session
NAME                           REMEDIATION ACTION   COMPLIANCE STATE   AGE
core-upgrade-4.20.1-policy    inform               NonCompliant       30s
```


If no `PlacementBinding` or `Placement` exists, the policy will not apply to any clusters. Create appropriate placement resources for your target clusters. 

  6. Create a `ClusterGroupUpgrade` CR for the z-stream update: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: core-zstream-upgrade-4.20.1
  namespace: openshift-upgrade-policies
spec:
  clusters:
  - spoke1
  - spoke2
  managedPolicies:
  - core-upgrade-4.20.1-policy
  enable: false
  remediationStrategy:
    maxConcurrency: 2
    timeout: 60
```


where: 

     * `clusters`: Specifies your target cluster names. 
     * `maxConcurrency`: Specifies the number of clusters to update simultaneously. 
     * `timeout`: Specifies the maximum time in minutes to wait for each cluster update. For example, 60 equals 1 hour per cluster. 

  7. Apply and enable the `ClusterGroupUpgrade` CR to start the update by running the following commands: 

```shell-session
$ oc apply -f core-zstream-cgu.yaml
$ oc patch cgu core-zstream-upgrade-4.20.1 \
  -n openshift-upgrade-policies \
  --type merge \
  -p '{"spec":{"enable":true}}'
```


  8. Monitor the update progress by running the following commands: 

```shell-session
$ oc get cgu core-zstream-upgrade-4.20.1 -n openshift-upgrade-policies -w
$ oc --context=spoke1 get clusterversion -w
$ oc --context=spoke1 get co
```


The `ClusterGroupUpgrade` CR progresses through these states: 

     * `Preparing`: TALM validates cluster readiness 
     * `InProgress`: Clusters are updating 
     * `Complete`: All clusters successfully updated 

Operators update sequentially during the z-stream update. 




**Verification**

  1. Verify the cluster version and Operator health by running the following commands: 

```shell-session
$ oc --context=spoke1 get clusterversion -o jsonpath='{.items[0].status.desired.version}'
$ oc --context=spoke1 get co
```


The cluster version must show the target z-stream version. All Operators must show `AVAILABLE=True`, `PROGRESSING=False`, `DEGRADED=False`. 

  2. Check workload health by running the following command: 

```shell-session
$ oc --context=spoke1 get pods -A | grep -v Running | grep -v Completed
```


Pods must not show unexpected failures or crash loops. 

  3. Verify CNF-specific resources by running the following commands: 

```shell-session
$ oc --context=spoke1 get performanceprofile
$ oc --context=spoke1 get ptpconfig -n openshift-ptp
$ oc --context=spoke1 get sriovnetworknodepolicy -n openshift-sriov-network-operator
```


All custom resources must show expected status. 

  4. Run smoke tests for critical workloads to ensure functionality after the update. 



**Troubleshooting**

  * If the `ClusterGroupUpgrade` CR is stuck in `Preparing` state, check policy compliance in RHACM by running the following command: 

```shell-session
$ oc get policy core-upgrade-4.20.1-policy -n openshift-upgrade-policies
```


  * If a cluster Operator becomes degraded during the update, check Operator logs by running the following command: 

```shell-session
$ oc --context=spoke1 logs -n openshift-<operator_namespace> deployment/<operator_deployment>
```


  * If the update exceeds the timeout, investigate slow nodes or image pull issues by running the following command: 

```shell-session
$ oc --context=spoke1 get events -A --sort-by='.lastTimestamp' | tail -20
```


### 13.3.7.2. Additional resources

  * [Prepare RHACM policies and TALM for cluster updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-preparing-policies "13.3.2. Prepare RHACM policies and TALM for cluster updates")
  * [Perform health checks before a cluster update with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-health-checks "13.3.4. Perform health checks before a cluster update with TALM")
  * [Troubleshoot cluster updates with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-troubleshooting "13.3.10. Troubleshoot cluster updates with TALM")
  * [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)
  * [OpenShift Container Platform update lifecycle and support policy](https://access.redhat.com/support/policy/updates/openshift)



## 13.3.8. Complete a y-stream cluster update with TALM

Y-stream updates move clusters between minor versions. You can update through a single y-stream release or chain multiple sequential updates to reach a target version that is more than one minor release away. 

### 13.3.8.1. Updating clusters through y-stream releases

You can update clusters through minor version, or y-stream, releases by using RHACM policies and Topology Aware Lifecycle Manager (TALM). Y-stream updates introduce new features and might include API deprecations, requiring careful planning and validation. 

You must perform y-stream updates through consecutive versions. You cannot skip versions during y-stream updates. For example, to update from 4.20 to 4.22, you must update from 4.20 to 4.21, and then from 4.21 to 4.22. If you need to move 2 y-stream versions, consider EUS-to-EUS updates instead. 

Note

The following procedure uses `spoke1` as an example cluster name. Replace it with your actual cluster name throughout. 

**Prerequisites**

  * You have completed the pre-update health check successfully. 
  * TALM is installed and configured on the Red Hat Advanced Cluster Management (RHACM) hub cluster. 
  * A y-stream release is available, such as 4.21 when updating from 4.20. 
  * You have reviewed the y-stream release notes for API deprecations and breaking changes. 
  * You have scheduled a maintenance window. Y-stream updates take 1 to 2 hours. 



**Procedure**

  1. Identify deprecated APIs in use on your cluster by running the following command: 

```shell-session
$ oc get apirequestcounts -o jsonpath='{range .items[?(@.status.removedInRelease!="")]}{.status.removedInRelease}{"\t"}{.metadata.name}{"\n"}{end}' | sort -k1
```


This command shows APIs that will be removed in future releases. Review the OpenShift Container Platform release notes for your target version and update any resources that use deprecated or removed APIs before updating. 

  2. Validate OLM Operator compatibility with the target y-stream version by running the following command: 

```shell-session
$ oc get csv -A
```


All Operators must show `Succeeded` status. Investigate any Operators in a failed state before proceeding. 

  3. Review Operator subscription channels to ensure they support the target OpenShift Container Platform version by running the following command: 

```shell-session
$ oc get subscription -A -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.channel}{"\n"}{end}'
```


Update Operator subscriptions if needed before the cluster update. 

  4. Create a RHACM policy to pause worker nodes: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: core-pause-worker-nodes
  namespace: openshift-upgrade-policies
spec:
  remediationAction: inform
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: pause-worker-mcp
      spec:
        remediationAction: inform
        severity: high
        object-templates:
        - complianceType: musthave
          objectDefinition:
            apiVersion: machineconfiguration.openshift.io/v1
            kind: MachineConfigPool
            metadata:
              name: worker
            spec:
              paused: true
```


  5. Create a RHACM policy for the y-stream update: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: core-upgrade-4.21-policy
  namespace: openshift-upgrade-policies
spec:
  remediationAction: inform
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: upgrade-cluster-version
      spec:
        remediationAction: inform
        severity: high
        object-templates:
        - complianceType: musthave
          objectDefinition:
            apiVersion: config.openshift.io/v1
            kind: ClusterVersion
            metadata:
              name: version
            spec:
              channel: stable-4.21
              desiredUpdate:
                version: 4.21.0
```


Replace `4.21.0` with your target y-stream version. Both policies are set to `inform` so they do not immediately push changes. The `ClusterGroupUpgrade` custom resource (CR) enforces these policies at the scheduled update time. 

  6. Apply the policies to RHACM by running the following commands: 

```shell-session
$ oc apply -f core-pause-worker-policy.yaml
$ oc apply -f core-upgrade-4.21-policy.yaml
```


  7. Verify the policies and placement resources were created by running the following commands: 

```shell-session
$ oc get policy -n openshift-upgrade-policies
$ oc get placementbinding -n openshift-upgrade-policies
$ oc get placement -n openshift-upgrade-policies
```


If no `PlacementBinding` or `Placement` exists, the policies will not apply to any clusters. Create appropriate placement resources for your target clusters. 

  8. Create a `ClusterGroupUpgrade` CR for the y-stream update: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: core-ystream-upgrade-4.21
  namespace: openshift-upgrade-policies
spec:
  clusters:
  - spoke1
  managedPolicies:
  - core-pause-worker-nodes
  - core-upgrade-4.21-policy
  enable: false
  remediationStrategy:
    maxConcurrency: 1
    timeout: 120
  actions:
    beforeEnable:
      addClusterLabels:
        upgrade-in-progress: "true"
    afterCompletion:
      addClusterLabels:
        upgraded-to: "4.21"
        control-plane-upgraded: "true"
```


For canary deployments, use a single cluster first before updating additional clusters. 

  9. Apply and enable the `ClusterGroupUpgrade` CR to start the control plane update by running the following commands: 

```shell-session
$ oc apply -f core-ystream-cgu.yaml
$ oc patch cgu core-ystream-upgrade-4.21 \
  -n openshift-upgrade-policies \
  --type merge \
  -p '{"spec":{"enable":true}}'
```


  10. Monitor the control plane update progress by running the following commands: 

```shell-session
$ oc get cgu core-ystream-upgrade-4.21 -n openshift-upgrade-policies -w
$ oc --context=spoke1 get clusterversion -w
$ oc --context=spoke1 get co
```


Cluster Operators update sequentially during the y-stream update. The control plane update typically takes 60 to 120 minutes. 

  11. After the control plane update completes, verify control plane health by running the following commands: 

```shell-session
$ oc --context=spoke1 get nodes -l node-role.kubernetes.io/master=
$ oc --context=spoke1 get co | grep -v "True.*False.*False"
```


All control plane nodes and Operators must be healthy before proceeding. 

  12. Create an OLM Operator update policy that updates Operator subscription channels to versions compatible with the new y-stream: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: core-upgrade-olm-4.21
  namespace: openshift-upgrade-policies
spec:
  remediationAction: inform
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: upgrade-olm-operators
      spec:
        remediationAction: inform
        severity: high
        object-templates:
        - complianceType: musthave
          objectDefinition:
            apiVersion: operators.coreos.com/v1alpha1
            kind: Subscription
            metadata:
              name: sriov-network-operator-subscription
              namespace: openshift-sriov-network-operator
            spec:
              channel: stable-4.21
            status:
              state: AtLatestKnown
```


You can include multiple Operator subscriptions in the same policy. For more details about creating OLM update policies, see "Coordinating OLM Operator updates with cluster updates". 

  13. Create a `ClusterGroupUpgrade` CR to apply the OLM Operator update policy: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: core-olm-upgrade-4.21
  namespace: openshift-upgrade-policies
spec:
  clusters:
  - spoke1
  managedPolicies:
  - core-upgrade-olm-4.21
  enable: true
  remediationStrategy:
    maxConcurrency: 1
    timeout: 60
```


  14. Apply the OLM Operator update policy and `ClusterGroupUpgrade` CR by running the following commands: 

```shell-session
$ oc apply -f core-olm-upgrade-policy.yaml
$ oc apply -f core-olm-cgu.yaml
```


  15. Monitor the OLM Operator update and verify that worker nodes remain at the previous version by running the following commands: 

```shell-session
$ oc get cgu core-olm-upgrade-4.21 -n openshift-upgrade-policies -w
$ oc --context=spoke1 get nodes
```


Worker nodes must still show the previous kubelet version. 

  16. Create a policy to unpause worker nodes: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: core-unpause-worker-nodes
  namespace: openshift-upgrade-policies
spec:
  remediationAction: inform
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: unpause-worker-mcp
      spec:
        remediationAction: inform
        severity: high
        object-templates:
        - complianceType: musthave
          objectDefinition:
            apiVersion: machineconfiguration.openshift.io/v1
            kind: MachineConfigPool
            metadata:
              name: worker
            spec:
              paused: false
```


  17. Create a `ClusterGroupUpgrade` CR to unpause workers: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: core-unpause-workers-4.21
  namespace: openshift-upgrade-policies
spec:
  clusters:
  - spoke1
  managedPolicies:
  - core-unpause-worker-nodes
  enable: false
  remediationStrategy:
    maxConcurrency: 1
```


  18. Apply and enable the unpause `ClusterGroupUpgrade` CR by running the following commands: 

```shell-session
$ oc apply -f core-unpause-workers-cgu.yaml
$ oc patch cgu core-unpause-workers-4.21 \
  -n openshift-upgrade-policies \
  --type merge \
  -p '{"spec":{"enable":true}}'
```


  19. Monitor worker node updates by running the following command: 

```shell-session
$ oc --context=spoke1 get mcp worker -w
```


Worker nodes update in a rolling fashion. The process typically takes 30 to 60 minutes depending on the number of worker nodes. 




**Verification**

  1. Verify all nodes are at the target y-stream version by running the following command: 

```shell-session
$ oc --context=spoke1 get nodes
```


  2. Verify all cluster Operators are healthy by running the following command: 

```shell-session
$ oc --context=spoke1 get co
```


  3. Verify workload health and CNF-specific resources by running the following commands: 

```shell-session
$ oc --context=spoke1 get pods -A | grep -v Running | grep -v Completed
$ oc --context=spoke1 get performanceprofile
$ oc --context=spoke1 get ptpconfig -n openshift-ptp
$ oc --context=spoke1 get sriovnetworknodepolicy -n openshift-sriov-network-operator
```


  4. Run smoke tests for critical workloads. 



**Troubleshooting**

  * If API deprecation warnings appear, update manifests to use new API versions before updating. 
  * If Operator compatibility issues occur, update Operator subscriptions to channels that support the target y-stream. 
  * If worker node updates get stuck, check `MachineConfigPool` resource status and node logs. 



### 13.3.8.2. Updating through sequential y-stream releases

You can update clusters through multiple sequential y-stream releases when you need to move from an older version to a newer version that is more than one minor release away. You must update through each intermediate y-stream version because skipping versions is not supported. 

For example, to update from 4.20 to 4.22, you must first update from 4.20 to 4.21, and then update from 4.21 to 4.22. 

Note

The following procedure uses `spoke1` as an example cluster name. Replace it with your actual cluster name throughout. 

Important

When planning to update clusters through multiple sequential y-stream releases, allow at least 24 hours, and up to 48 hours, between y-stream updates to monitor cluster stability. 

**Prerequisites**

  * You have completed the pre-update health check successfully. 
  * TALM is installed and configured on the Red Hat Advanced Cluster Management (RHACM) hub cluster. 
  * You have access to the target clusters with cluster-admin privileges. 
  * The `oc` CLI tool is installed and configured for the target clusters. 
  * All intermediate y-stream releases are available, such as both 4.21 and 4.22 when updating from 4.20 to 4.22. 
  * You have reviewed the release notes for each intermediate y-stream version for API deprecations and breaking changes. 
  * You have planned maintenance windows for each y-stream update. 



**Procedure**

  1. Determine the complete update path: 

Identify your current version and target version, then map out the required intermediate versions. 

Table 13.3. Example update pathsCurrent version| Update path to 4.22  
---|---  
4.20.20  |  4.20.20  4.21.latest  4.22.0   
4.19.10  |  4.19.10  4.20.latest  4.21.latest  4.22.0   
Show more

  2. Update to the first intermediate y-stream version: 

Follow the procedure in "Updating clusters through y-stream releases" to update to the first intermediate version. 

For example, update from 4.20.20 to 4.21.latest. 

  3. Verify the first y-stream update completed successfully by running the following command: 

```shell-session
$ oc --context=spoke1 get clusterversion
```


Verify all cluster Operators are healthy by running the following command: 

```shell-session
$ oc --context=spoke1 get co | grep -v "True.*False.*False"
```


All cluster Operators must show healthy status before proceeding. 

  4. Wait at least 24 hours, and up to 48 hours, between y-stream updates: 

Allow time to monitor cluster stability after the first update. Extend this period for large production deployments or if any anomalies are observed. 

During this wait period: 

     * Monitor workload health and performance. 
     * Check for unexpected behavior or errors. 
     * Run smoke tests for critical cloud-native network function (CNF) workloads. 
     * Verify all custom resources specific to your deployment are functioning correctly. 
     * Review release notes for the next y-stream version for additional API deprecations or configuration changes. 

  5. Update OLM Operator subscriptions if needed: 

Some Operators might require intermediate channel updates when updating through multiple y-streams. Verify the Operator status by running the following command: 

```shell-session
$ oc --context=spoke1 get csv -A
```


Verify all Operators are at versions compatible with your current cluster version before proceeding. 

  6. Create RHACM policies for the second y-stream update: 

Update the cluster version policy to target the next y-stream: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: core-upgrade-4.22-policy
  namespace: openshift-upgrade-policies
spec:
  remediationAction: inform
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: upgrade-cluster-version
      spec:
        remediationAction: inform
        severity: high
        object-templates:
        - complianceType: musthave
          objectDefinition:
            apiVersion: config.openshift.io/v1
            kind: ClusterVersion
            metadata:
              name: version
            spec:
              channel: stable-4.22
              desiredUpdate:
                version: 4.22.0
```


  7. Apply the updated policy by running the following command: 

```shell-session
$ oc apply -f core-upgrade-4.22-policy.yaml
```


  8. Create a new `ClusterGroupUpgrade` custom resource (CR) for the second y-stream: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: core-ystream-upgrade-4.22
  namespace: openshift-upgrade-policies
spec:
  clusters:
  - spoke1
  managedPolicies:
  - core-pause-worker-nodes
  - core-upgrade-4.22-policy
  enable: false
  remediationStrategy:
    maxConcurrency: 1
    timeout: 120
```


  9. Apply and enable the `ClusterGroupUpgrade` CR by running the following commands: 

```shell-session
$ oc apply -f core-ystream-upgrade-4.22-cgu.yaml
$ oc patch cgu core-ystream-upgrade-4.22 \
  -n openshift-upgrade-policies \
  --type merge \
  -p '{"spec":{"enable":true}}'
```


  10. Monitor the second y-stream update and verify completion by running the following commands: 

```shell-session
$ oc get cgu core-ystream-upgrade-4.22 -n openshift-upgrade-policies -w
$ oc --context=spoke1 get clusterversion
$ oc --context=spoke1 get co
```


  11. Update Operators for the second y-stream by running the following command: 

```shell-session
$ oc --context=spoke1 get csv -A | grep -v Succeeded
```


Update Operator channels as needed for the new cluster version. 

  12. Unpause worker nodes and complete the second y-stream update: 

Follow the worker node unpause procedure from "Pausing and unpausing worker nodes by using TALM". 

  13. Repeat steps 2-12 for any additional intermediate y-stream versions: 

If updating through more than two y-streams, repeat the process for each intermediate version. 




**Verification**

  1. Verify the final cluster version by running the following command: 

```shell-session
$ oc --context=spoke1 get clusterversion -o jsonpath='{.items[0].status.desired.version}'
```


  2. Run comprehensive health checks: 

Follow the procedure in "Performing health checks before cluster updates". 

  3. Verify workload functionality after all updates: 

Run smoke tests and validate that all CNF workloads operate correctly at the final version. 




**Troubleshooting**

  * If the cluster becomes degraded after the first y-stream update, resolve all issues before proceeding to the second y-stream. 
  * If Operator versions are incompatible with an intermediate y-stream, update the Operator subscription before updating the cluster. 
  * If configuration changes are needed between y-streams, apply those changes during the wait period before proceeding. 



### 13.3.8.3. Additional resources

  * [Complete an EUS-to-EUS cluster update with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-eus "13.3.9. Complete an EUS-to-EUS cluster update with TALM")
  * [Prepare RHACM policies and TALM for cluster updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-preparing-policies "13.3.2. Prepare RHACM policies and TALM for cluster updates")
  * [Perform health checks before a cluster update with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-health-checks "13.3.4. Perform health checks before a cluster update with TALM")
  * [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)
  * [OpenShift Container Platform update lifecycle and support policy](https://access.redhat.com/support/policy/updates/openshift)



## 13.3.9. Complete an EUS-to-EUS cluster update with TALM

You can partially skip intermediate odd-numbered releases by using control-plane-only EUS-to-EUS updates with RHACM policies and Topology Aware Lifecycle Manager (TALM). With this approach, you can manage control plane and worker version skew during staged rollouts. 

### 13.3.9.1. Updating with EUS-to-EUS control-plane-only updates

You can update clusters from one Extended Update Support (EUS) release to another using control-plane-only updates. This approach updates the control plane while leaving worker nodes at the previous EUS version, enabling staged rollouts that minimize workload disruption. 

EUS releases provide 18 months of support and include even-numbered minor versions such as 4.18, 4.20, and 4.22. Control plane and worker nodes can be up to two minor versions apart during EUS-to-EUS updates. 

Warning

Control plane and worker version skew is limited to N-2, or two minor versions. For example, if the control plane is at 4.20, workers must be updated before the control plane reaches 4.22, or they will be in an unsupported configuration. Plan worker updates accordingly to avoid exceeding the version skew policy. For more information about version skew policies, see the Kubernetes version and version skew support policy. 

The following procedure demonstrates an EUS-to-EUS update using an example cluster. 

Note

The following procedure uses `spoke1` as an example cluster name. Replace it with your actual cluster name throughout. 

**Prerequisites**

  * You have completed the pre-update health check successfully. 
  * TALM is installed and configured on the Red Hat Advanced Cluster Management (RHACM) hub cluster. 
  * The current cluster is at the latest z-stream of a source EUS version, such as 4.20.latest. 
  * The target EUS version is available, such as 4.22. 
  * You have verified that the EUS-to-EUS update path is supported in the release notes. 
  * You have reviewed the release notes for API deprecations and breaking changes between the source and target EUS versions. 
  * You have scheduled a maintenance window. EUS-to-EUS updates take 2 to 3 hours. 



**Procedure**

  1. Verify the current cluster version is at the latest z-stream of the source EUS by running the following command: 

```shell-session
$ oc --context=spoke1 get clusterversion
```


The following example shows the output: 

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.20.35   True        False         30d     Cluster version is 4.20.35
```


If not at the latest z-stream, update to the latest patch release before proceeding. 

  2. Validate that your cloud-native network function (CNF) workloads tolerate control plane and worker version skew: 

Verify that your CNF workloads can operate with the control plane at 4.22 while workers remain at 4.20. Consult with application teams if needed. 

  3. Create a RHACM policy to pause worker nodes: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: core-pause-worker-nodes
  namespace: openshift-upgrade-policies
spec:
  remediationAction: inform
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: pause-worker-mcp
      spec:
        remediationAction: inform
        severity: high
        object-templates:
        - complianceType: musthave
          objectDefinition:
            apiVersion: machineconfiguration.openshift.io/v1
            kind: MachineConfigPool
            metadata:
              name: worker
            spec:
              paused: true
```


  4. Verify the current cluster channel before creating the update policy by running the following command: 

```shell-session
$ oc --context=spoke1 get clusterversion -o jsonpath='{.items[0].spec.channel}'
```


The following example shows the output: 

```shell-session
eus-4.20
```


If the cluster is on a non-EUS channel, such as `stable-4.20`, changing to an EUS channel and setting the required version simultaneously can cause unexpected update behavior. 

  5. Get the release image reference for the target version. 

The image reference is required for the update policy. Retrieve it by running the following command: 

```shell-session
$ oc adm release info 4.21.5 | head -9
```


The following example shows the output: 

```shell-session
Name:           4.21.5
Digest:         sha256:93879f84b3165c5b5bd1fdf4563a11155dc61ea35cd93e67dc61c2b66e11c8bb
Created:        2025-03-13T09:17:26Z
OS/Arch:        linux/amd64
Manifests:      758
Metadata files: 2

Pull From: quay.io/openshift-release-dev/ocp-release@sha256:93879f84b3165c5b5bd1fdf4563a11155dc61ea35cd93e67dc61c2b66e11c8bb
```


Use the `Pull From` value as the `image` field in the update policy. 

  6. Create a policy for the EUS update. 

For an EUS-to-EUS update, you need a separate policy for each y-stream step. The following example shows a policy for the first y-stream update: 

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: upgrade-ocp-20to21
  namespace: openshift-upgrade-policies
  annotations:
    policy.open-cluster-management.io/categories: CM Configuration Management
    policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
    policy.open-cluster-management.io/standards: NIST SP 800-53
  labels:
    app.kubernetes.io/instance: policies
spec:
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        kind: ConfigurationPolicy
        metadata:
          name: upgrade-ocp-20to21
        spec:
          object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: config.openshift.io/v1
                kind: ClusterVersion
                metadata:
                  name: version
                spec:
                  channel: eus-4.22
                  desiredUpdate:
                    force: true
                    image: quay.io/openshift-release-dev/ocp-release@sha256:df00d64554b9b5d860273f938e0ff3b0c4a7af8356fbd103658ebe6fa2a830c8
                    version: 4.21.29
                status:
                  history:
                    - state: Completed
                      version: 4.21.29
          remediationAction: inform
          severity: low
  remediationAction: inform
```


where: 

     * `channel`: Sets the cluster channel to the target EUS release. Refer to the [update selection tool](https://access.redhat.com/labs/ocpupgradegraph/update_path/) when setting the channel. 
     * `image`: Specifies the release image reference obtained from the `oc adm release info` command. 
     * `version`: Sets the specific y-stream and z-stream release version for the cluster update. The `status.history` section ensures the policy remains noncompliant until the update completes. 
     * `force`: The `force: true` field bypasses the Cincinnati update graph safety checks. Use this field only when the update path has been verified through the update selection tool or release notes. Removing this field or setting it to `false` causes the update to follow the standard update graph, which might not include a direct path for EUS-to-EUS intermediate hops. 

Important

For an EUS-to-EUS update, create a policy for each y-stream step. For example, updating from 4.20 to 4.22 requires one policy for 4.20-to-4.21 and another for 4.21-to-4.22. For a complete example of chaining multiple policies across y-stream steps, see "Configuring ClusterGroupUpgrade custom resources for cluster updates". 

  7. Apply the policies to RHACM by running the following commands: 

```shell-session
$ oc apply -f upgrade-ocp-20to21-policy.yaml
$ oc apply -f core-pause-worker-nodes-policy.yaml
```


  8. Create a `ClusterGroupUpgrade` custom resource (CR) for the EUS update: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: core-eus-upgrade-4.20-to-4.22
  namespace: openshift-upgrade-policies
spec:
  clusters:
  - spoke1
  managedPolicies:
  - core-pause-worker-nodes
  - upgrade-ocp-20to21
  enable: false
  remediationStrategy:
    maxConcurrency: 1
    timeout: 180
```


EUS updates might take longer than single y-stream updates, so the timeout is set to 180 minutes, or 3 hours. 

  9. Apply and enable the `ClusterGroupUpgrade` CR to start the EUS update by running the following commands: 

```shell-session
$ oc apply -f core-eus-upgrade-cgu.yaml
$ oc patch cgu core-eus-upgrade-4.20-to-4.22 \
  -n openshift-upgrade-policies \
  --type merge \
  -p '{"spec":{"enable":true}}'
```


  10. Monitor the EUS control plane update progress by running the following commands: 

```shell-session
$ oc get cgu core-eus-upgrade-4.20-to-4.22 -n openshift-upgrade-policies -w
$ oc --context=spoke1 get clusterversion -w
$ oc --context=spoke1 get co
```


The cluster version progresses through intermediate versions during the EUS update. For example, updating from 4.20 to 4.22 goes through 4.21 internally. Cluster Operators might take longer to stabilize during EUS updates because of the larger version jump. 

  11. After the control plane update completes, verify control plane and worker node status by running the following commands: 

```shell-session
$ oc --context=spoke1 get nodes -l node-role.kubernetes.io/master=
$ oc --context=spoke1 get co | grep -v "True.*False.*False"
$ oc --context=spoke1 get nodes -l node-role.kubernetes.io/worker=
```


The following example shows the output for control plane nodes: 

```shell-session
NAME                   STATUS   ROLES                  AGE   VERSION
master-0.example.com   Ready    control-plane,master   60d   v1.35.0
master-1.example.com   Ready    control-plane,master   60d   v1.35.0
master-2.example.com   Ready    control-plane,master   60d   v1.35.0
```


Control plane nodes must show the new kubelet version, 4.22. All Operators must be healthy before updating worker nodes. 

The following example shows the output for worker nodes: 

```shell-session
NAME                   STATUS   ROLES    AGE   VERSION
worker-0.example.com   Ready    worker   60d   v1.33.0
worker-1.example.com   Ready    worker   60d   v1.33.0
worker-2.example.com   Ready    worker   60d   v1.33.0
```


Worker nodes must still show the previous kubelet version, 4.20. 

  12. Update OLM Operators for the new EUS version: 

Operators might need multiple version jumps for EUS-to-EUS updates. Check the status of OLM Operators by running the following command: 

```shell-session
$ oc --context=spoke1 get csv -A | grep -v Succeeded
```


Update Operator subscriptions to EUS-compatible channels by running the following command: 

```shell-session
$ oc --context=spoke1 patch subscription sriov-network-operator-subscription \
  -n openshift-sriov-network-operator \
  --type merge \
  -p '{"spec":{"channel":"stable-4.22"}}'
```


  13. When ready to update worker nodes, create and apply an unpause policy: 

Determine the timing for worker node updates based on your maintenance schedule. Workers can remain at the previous EUS version for an extended period if needed. 

Follow the procedure in "Pausing and unpausing worker nodes by using TALM" to unpause and update workers. 

  14. Monitor worker node updates to completion by running the following command: 

```shell-session
$ oc --context=spoke1 get mcp worker -w
```


**Verification**

  1. Verify all nodes are at the target EUS version by running the following command: 

```shell-session
$ oc --context=spoke1 get nodes
```


  2. Verify all cluster Operators are healthy by running the following command: 

```shell-session
$ oc --context=spoke1 get co
```


  3. Validate CNF-specific resources by running the following commands: 

```shell-session
$ oc --context=spoke1 get performanceprofile
$ oc --context=spoke1 get ptpconfig -n openshift-ptp
$ oc --context=spoke1 get sriovnetworknodepolicy -n openshift-sriov-network-operator
```


  4. Run comprehensive smoke tests for all CNF workloads. 



**Troubleshooting**

  * If the EUS update path is not available, verify you are at the latest z-stream of the source EUS version. 
  * If the control plane update gets stuck, check for Operator compatibility issues with the target EUS version. 
  * If worker nodes fail to update after unpause, check the `MachineConfigPool` resource status and node logs. 



### 13.3.9.2. Additional resources

  * [Prepare RHACM policies and TALM for cluster updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-preparing-policies "13.3.2. Prepare RHACM policies and TALM for cluster updates")
  * [Manage worker nodes during a cluster update with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-worker-management "13.3.5. Manage worker nodes during a cluster update with TALM")
  * [Perform health checks before a cluster update with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-health-checks "13.3.4. Perform health checks before a cluster update with TALM")
  * [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)
  * [OpenShift Container Platform update lifecycle and support policy](https://access.redhat.com/support/policy/updates/openshift)



## 13.3.10. Troubleshoot cluster updates with TALM

If a cluster update gets stuck, fails, or results in degraded cluster Operators, use the following diagnostic procedures to identify the root cause and take corrective action. 

### 13.3.10.1. Diagnosing a ClusterGroupUpgrade CR stuck in Preparing state

If a `ClusterGroupUpgrade` custom resource (CR) is stuck in the `Preparing` state, the issue is typically related to policy compliance, cluster readiness, or blocking custom resources. 

**Prerequisites**

  * You have a `ClusterGroupUpgrade` CR that is stuck in `Preparing` state. 
  * You have access to the Red Hat Advanced Cluster Management (RHACM) hub cluster with cluster-admin privileges. 



**Procedure**

  1. Check the `ClusterGroupUpgrade` status by running the following command: 

```shell-session
$ oc get cgu <cgu_name> -n <namespace> -o yaml
```


Look for error messages in the `status.conditions` section. Common causes include managed policies that do not exist or are not bound to target clusters, target clusters that are not in a ready state, and blocking custom resources that are not ready. 

  2. Check policy compliance in RHACM by running the following command: 

```shell-session
$ oc get policy <policy_name> -n <namespace>
```


  3. Check policy details for noncompliant policies by running the following command: 

```shell-session
$ oc describe policy <policy_name> -n <namespace>
```


Resolve policy compliance issues before the `ClusterGroupUpgrade` CR can proceed. 




### 13.3.10.2. Diagnosing a ClusterGroupUpgrade CR that failed on some clusters

If a `ClusterGroupUpgrade` custom resource (CR) completes but some clusters show a `failed` status, investigate the failed clusters individually to identify the root cause. 

**Prerequisites**

  * You have a `ClusterGroupUpgrade` CR that shows failed clusters. 
  * You have access to the Red Hat Advanced Cluster Management (RHACM) hub cluster with cluster-admin privileges. 



**Procedure**

  1. Check detailed cluster status in the `ClusterGroupUpgrade` CR by running the following command: 

```shell-session
$ oc get cgu <cgu_name> -n <namespace> -o jsonpath='{.status.clusters}'
```


The following example shows the output: 

```plaintext
{
  "spoke1": "complete",
  "spoke2": "failed",
  "spoke3": "inprogress"
}
```


  2. Check TALM logs for errors related to the failed clusters by running the following command: 

```shell-session
$ oc logs -n openshift-operators deployment/cluster-group-upgrades-controller-manager
```


  3. Check policy violation events on the failed cluster by running the following command: 

```shell-session
$ oc --context=<failed_cluster> get events -A --sort-by='.lastTimestamp' | tail -20
```


### 13.3.10.3. Diagnosing degraded cluster Operators during an update

If a cluster Operator becomes degraded during an update, identify the affected Operator and investigate the root cause. 

Common Operators that degrade during updates include `authentication`, `console`, `monitoring`, and `network`. 

**Prerequisites**

  * You have a cluster update in progress with one or more degraded Operators. 
  * You have access to the target cluster with cluster-admin privileges. 



**Procedure**

  1. Identify degraded Operators by running the following command: 

```shell-session
$ oc get co | grep -v "True.*False.*False"
```


The following example shows the output: 

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.20.0    True        False         True       5m      APIServerDeploymentDegraded: ...
```


  2. Check Operator details by running the following command: 

```shell-session
$ oc describe co authentication
```


Look for error messages in the `status.conditions` section of the output. 

  3. Check Operator pod logs by running the following command: 

```shell-session
$ oc logs -n openshift-authentication deployment/oauth-openshift
```


### 13.3.10.4. Diagnosing an update stuck in Working towards state

If the cluster version shows a "Working towards" message for an extended period, identify which Operators are blocking the update from completing. Updates typically complete within 90 to 180 minutes. 

**Prerequisites**

  * You have a cluster update that appears stuck in the "Working towards" state. 
  * You have access to the target cluster with cluster-admin privileges. 



**Procedure**

  1. Check `ClusterVersion` status by running the following command: 

```shell-session
$ oc get clusterversion -o yaml
```


Look for the `status.conditions` section to identify blocking resources. 

  2. Check which Operators are still progressing by running the following command: 

```shell-session
$ oc get co | grep "True"
```


Any Operator showing `PROGRESSING=True` is still updating. 

  3. Check `ClusterVersion` history by running the following command: 

```shell-session
$ oc get clusterversion -o jsonpath='{.status.history}'
```


A missing or stalled history entry indicates the update has timed out. 




### 13.3.10.5. Diagnosing worker nodes stuck in NotReady state

If worker nodes show `NotReady` status during an update, common causes include disk pressure, memory pressure, network connectivity issues, and PID pressure. 

**Prerequisites**

  * You have worker nodes showing `NotReady` status during a cluster update. 
  * You have access to the target cluster with cluster-admin privileges. 



**Procedure**

  1. Identify `NotReady` nodes by running the following command: 

```shell-session
$ oc get nodes | grep NotReady
```


  2. Check node conditions by running the following command: 

```shell-session
$ oc describe node <node_name> | grep -A 10 Conditions
```


  3. Check kubelet logs by running the following command: 

```shell-session
$ oc debug node/<node_name> -- chroot /host journalctl -u kubelet -n 100
```


### 13.3.10.6. Diagnosing a stuck worker node update

If worker node updates are stuck, the issue is typically related to pod disruption budgets, machine config daemon failures, or node reboot failures. 

**Prerequisites**

  * You have a worker node update that is not progressing. 
  * You have access to the target cluster with cluster-admin privileges. 



**Procedure**

  1. Check the `MachineConfigPool` resource status by running the following command: 

```shell-session
$ oc get mcp worker -o yaml
```


Look for degraded machine configs in the status. 

  2. Check pod disruption budgets by running the following command: 

```shell-session
$ oc get pdb -A
```


If a pod disruption budget (PDB) shows `ALLOWED DISRUPTIONS` of 0, adjust the PDB configuration. 

  3. Check machine-config-daemon logs on the stuck node by running the following command: 

```shell-session
$ oc logs -n openshift-machine-config-operator <machine_config_daemon_pod>
```


### 13.3.10.7. Diagnosing etcd issues during control plane updates

If etcd members become unhealthy during a control plane update, identify the affected members and investigate the root cause before proceeding. 

**Prerequisites**

  * You have a control plane update with suspected etcd issues. 
  * You have access to the target cluster with cluster-admin privileges. 



**Procedure**

  1. Check etcd cluster health by running the following command: 

```shell-session
$ oc get etcd -o yaml
```


Look for the `EtcdMembersAvailable` condition in the output. 

  2. Check etcd pod status by running the following command: 

```shell-session
$ oc get pods -n openshift-etcd -l app=etcd
```


All etcd pods must be running. 

  3. View etcd member status by running the following command: 

```shell-session
$ oc rsh -n openshift-etcd <etcd_pod> etcdctl member list -w table
```


  4. Monitor etcd logs for errors by running the following command: 

```shell-session
$ oc logs -n openshift-etcd <etcd_pod> etcd
```


### 13.3.10.8. Diagnosing image pull failures during updates

If image pull failures occur during an update, common causes include registry connectivity issues, images not mirrored to a disconnected registry, and image pull authentication failures. 

**Prerequisites**

  * You have image pull failures during a cluster update. 
  * You have access to the target cluster with cluster-admin privileges. 



**Procedure**

  1. Check image pull status on nodes by running the following command: 

```shell-session
$ oc get events -A --field-selector reason=Failed --sort-by='.lastTimestamp' | grep -i image
```


  2. For disconnected environments, verify image mirroring by running the following command: 

```shell-session
$ oc get imagedigestmirrorset
```


Note

In OpenShift Container Platform 4.13 and earlier, image mirroring was configured with `ImageContentSourcePolicy` resources. In OpenShift Container Platform 4.14 and later, `ImageDigestMirrorSet` resources replace `ImageContentSourcePolicy`. If your cluster was originally installed on a version earlier than 4.14, check both resource types. 

  3. Test image pull from a node by running the following command: 

```shell-session
$ oc debug node/<node_name> -- chroot /host podman pull <image_url>
```


### 13.3.10.9. Diagnosing update timeout exceeded

If TALM reports that the update timeout was exceeded, investigate cluster resource utilization, image pull speed, and network latency. 

**Prerequisites**

  * You have a `ClusterGroupUpgrade` custom resource (CR) that has timed out. 
  * You have access to the target cluster with cluster-admin privileges. 



**Procedure**

  1. Check cluster resource utilization by running the following command: 

```shell-session
$ oc adm top nodes
```


High CPU or memory usage can slow updates. 

  2. Check for slow image pulls by running the following command: 

```shell-session
$ oc get events -A --sort-by='.lastTimestamp' | grep -i "pull"
```


Slow image pulls can indicate network latency between nodes and registries. 

  3. Increase the `ClusterGroupUpgrade` CR timeout by running the following command if the cluster is healthy but updating slowly: 

```shell-session
$ oc patch cgu <cgu_name> -n <namespace> --type merge -p '{"spec":{"remediationStrategy":{"timeout":240}}}'
```


### 13.3.10.10. Resolving a noncompliant policy hold during an update

During the update, TALM verifies the status of `ClusterVersion` for the OpenShift Container Platform update and `Subscription` for OLM Operators. 

If errors occur during those updates, the status does not change to the expected value and the policies do not become compliant. TALM holds at that point waiting for compliance. 

If you are monitoring the update, you can fix the issue on the target cluster and the update continues automatically when the policy becomes compliant. 

`ClusterGroupUpgrade` custom resource (CR) has timed out
    

Delete the timed-out CR by running the following command: 

```shell-session
$ oc delete cgu <timed_out_cgu_name> -n <namespace>
```


All policies revert to `inform` mode, leaving the cluster at the point where the issue occurred. 

Fix the issue that caused the timeout, then re-create the `ClusterGroupUpgrade` CR to resume the update by running the following command: 

```shell-session
$ oc apply -f <cgu_cr_filename>.yaml
```


Policies or TALM are conflicting with changes you need to make
    

Delete the `ClusterGroupUpgrade` CR to revert all policies to `inform` mode by running the following command: 

```shell-session
$ oc delete cgu <cgu_name> -n <namespace>
```


After the policies revert to `inform` mode, they do not enforce changes on the cluster. 

Fix the issue, then re-create the `ClusterGroupUpgrade` CR to resume the update. 

### 13.3.10.11. Collecting diagnostic information for Red Hat support

If you cannot resolve the update issue, collect diagnostic information and contact Red Hat support for assistance. 

**Prerequisites**

  * You have a cluster update issue that you cannot resolve. 
  * You have access to the target cluster and the Red Hat Advanced Cluster Management (RHACM) hub cluster with cluster-admin privileges. 



**Procedure**

  1. Collect must-gather data by running the following command: 

```shell-session
$ oc adm must-gather
```


  2. Collect RHACM must-gather data for TALM-specific issues by running the following command: 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/rhacm2/must-gather-rhel8
```


  3. Collect `ClusterVersion` history by running the following command: 

```shell-session
$ oc get clusterversion -o jsonpath='{.status.history}' > clusterversion-history.json
```


  4. Collect `ClusterGroupUpgrade` status by running the following command: 

```shell-session
$ oc get cgu <cgu_name> -n <namespace> -o yaml > cgu-status.yaml
```


### 13.3.10.12. Additional resources

  * [Perform health checks before a cluster update with TALM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters#core-cluster-upgrades-health-checks "13.3.4. Perform health checks before a cluster update with TALM")
  * [Using the Topology Aware Lifecycle Manager for cluster updates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-talm-for-cluster-updates)
  * [Contact Red Hat support](https://access.redhat.com/support)
  * [Red Hat Knowledgebase](https://access.redhat.com/solutions)
