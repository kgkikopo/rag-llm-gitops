# 13.5. About the ClusterGroupUpgrade CR

The Topology Aware Lifecycle Manager (TALM) builds the remediation plan from the `ClusterGroupUpgrade` CR for a group of clusters. You can define the following specifications in a `ClusterGroupUpgrade` CR: 

  * Clusters in the group 
  * Blocking `ClusterGroupUpgrade` CRs 
  * Applicable list of managed policies 
  * Number of concurrent updates 
  * Applicable canary updates 
  * Actions to perform before and after the update 
  * Update timing 



You can control the start time of an update using the `enable` field in the `ClusterGroupUpgrade` CR. For example, if you have a scheduled maintenance window of four hours, you can prepare a `ClusterGroupUpgrade` CR with the `enable` field set to `false`. 

You can set the timeout by configuring the `spec.remediationStrategy.timeout` setting as follows: 

```yaml
spec
  remediationStrategy:
          maxConcurrency: 1
          timeout: 240
```


You can use the `batchTimeoutAction` to determine what happens if an update fails for a cluster. You can specify `continue` to skip the failing cluster and continue to upgrade other clusters, or `abort` to stop policy remediation for all clusters. Once the timeout elapses, TALM removes all `enforce` policies to ensure that no further updates are made to clusters. 

To apply the changes, you set the `enabled` field to `true`. 

For more information see the "Applying update policies to managed clusters" section. 

As TALM works through remediation of the policies to the specified clusters, the `ClusterGroupUpgrade` CR can report true or false statuses for a number of conditions. 

Note

After TALM completes a cluster update, the cluster does not update again under the control of the same `ClusterGroupUpgrade` CR. You must create a new `ClusterGroupUpgrade` CR in the following cases: 

  * When you need to update the cluster again 
  * When the cluster changes to non-compliant with the `inform` policy after being updated 



## 13.5.1. Selecting clusters

TALM builds a remediation plan and selects clusters based on the following fields: 

  * The `clusterLabelSelector` field specifies the labels of the clusters that you want to update. This consists of a list of the standard label selectors from `k8s.io/apimachinery/pkg/apis/meta/v1`. Each selector in the list uses either label value pairs or label expressions. Matches from each selector are added to the final list of clusters along with the matches from the `clusterSelector` field and the `cluster` field. 
  * The `clusters` field specifies a list of clusters to update. 
  * The `canaries` field specifies the clusters for canary updates. 
  * The `maxConcurrency` field specifies the number of clusters to update in a batch. 
  * The `actions` field specifies `beforeEnable` actions that TALM takes as it begins the update process, and `afterCompletion` actions that TALM takes as it completes policy remediation for each cluster. 



You can use the `clusters`, `clusterLabelSelector`, and `clusterSelector` fields together to create a combined list of clusters. 

The remediation plan starts with the clusters listed in the `canaries` field. Each canary cluster forms a single-cluster batch. 

**Sample`ClusterGroupUpgrade` CR with the enabled `field` set to `false`**

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  creationTimestamp: '2022-11-18T16:27:15Z'
  finalizers:
    - ran.openshift.io/cleanup-finalizer
  generation: 1
  name: talm-cgu
  namespace: talm-namespace
  resourceVersion: '40451823'
  uid: cca245a5-4bca-45fa-89c0-aa6af81a596c
Spec:
  actions:
    afterCompletion:
      addClusterLabels:
        upgrade-done: ""
      deleteClusterLabels:
        upgrade-running: ""
      deleteObjects: true
    beforeEnable:
      addClusterLabels:
        upgrade-running: ""
  clusters:
    - spoke1
  enable: false
  managedPolicies:
    - talm-policy
  preCaching: false
  remediationStrategy:
    canaries:
        - spoke1
    maxConcurrency: 2
    timeout: 240
  clusterLabelSelectors:
    - matchExpressions:
      - key: label1
      operator: In
      values:
        - value1a
        - value1b
  batchTimeoutAction:
status:
    computedMaxConcurrency: 2
    conditions:
      - lastTransitionTime: '2022-11-18T16:27:15Z'
        message: All selected clusters are valid
        reason: ClusterSelectionCompleted
        status: 'True'
        type: ClustersSelected
      - lastTransitionTime: '2022-11-18T16:27:15Z'
        message: Completed validation
        reason: ValidationCompleted
        status: 'True'
        type: Validated
      - lastTransitionTime: '2022-11-18T16:37:16Z'
        message: Not enabled
        reason: NotEnabled
        status: 'False'
        type: Progressing
    managedPoliciesForUpgrade:
      - name: talm-policy
        namespace: talm-namespace
    managedPoliciesNs:
      talm-policy: talm-namespace
    remediationPlan:
      - - spoke1
      - - spoke2
        - spoke3
    status:
```


  * `Spec.actions.afterCompletion` specifies the action that TALM takes when it completes policy remediation for each cluster. 
  * `Spec.actions.beforeEnable` specifies the action that TALM takes as it begins the update process. 
  * `Spec.clusters` defines the list of clusters to update. 
  * `Spec.enable` the `enable` field is set to `false`. 
  * `Spec.managedPolicies` lists the user-defined set of policies to remediate. 
  * `Spec.remediationStrategy` defines the specifics of the cluster updates. 
  * `Spec.preCaching.canaries` defines the clusters for canary updates. 
  * `Spec.preCaching.maxConcurrency` defines the maximum number of concurrent updates in a batch. The number of remediation batches is the number of canary clusters, plus the number of clusters, except the canary clusters, divided by the `maxConcurrency` value. The clusters that are already compliant with all the managed policies are excluded from the remediation plan. 
  * `Spec.clusterLabelSelectors` displays the parameters for selecting clusters. 
  * `Spec.batchTimeoutAction` controls what happens if a batch times out. Possible values are `abort` or `continue`. If unspecified, the default is `continue`. 
  * `status` displays information about the status of the updates. 
  * `Spec.preCaching.conditions.type` the `ClustersSelected` condition shows that all selected clusters are valid. 
  * `Spec.preCaching.conditions.type` the `Validated` condition shows that all selected clusters have been validated. 



Note

Any failures during the update of a canary cluster stops the update process. 

When the remediation plan is successfully created, you can you set the `enable` field to `true` and TALM starts to update the non-compliant clusters with the specified managed policies. 

Note

You can only make changes to the `spec` fields if the `enable` field of the `ClusterGroupUpgrade` CR is set to `false`. 

## 13.5.2. Validating

TALM checks that all specified managed policies are available and correct, and uses the `Validated` condition to report the status and reasons as follows: 

  * `true`

Validation is completed. 

  * `false`

Policies are missing or invalid, or an invalid platform image has been specified. 




## 13.5.3. Pre-caching

Clusters might have limited bandwidth to access the container image registry, which can cause a timeout before the updates are completed. On single-node OpenShift clusters, you can use pre-caching to avoid this. The container image pre-caching starts when you create a `ClusterGroupUpgrade` CR with the `preCaching` field set to `true`. TALM compares the available disk space with the estimated OpenShift Container Platform image size to ensure that there is enough space. If a cluster has insufficient space, TALM cancels pre-caching for that cluster and does not remediate policies on it. 

TALM uses the `PrecacheSpecValid` condition to report status information as follows: 

  * `true`

The pre-caching spec is valid and consistent. 

  * `false`

The pre-caching spec is incomplete. 




TALM uses the `PrecachingSucceeded` condition to report status information as follows: 

  * `true`

TALM has concluded the pre-caching process. If pre-caching fails for any cluster, the update fails for that cluster but proceeds for all other clusters. A message informs you if pre-caching has failed for any clusters. 

  * `false`

Pre-caching is still in progress for one or more clusters or has failed for all clusters. 




For more information see the "Using the container image pre-cache feature" section. 

## 13.5.4. Updating clusters

TALM enforces the policies following the remediation plan. Enforcing the policies for subsequent batches starts immediately after all the clusters of the current batch are compliant with all the managed policies. If the batch times out, TALM moves on to the next batch. The timeout value of a batch is the `spec.timeout` field divided by the number of batches in the remediation plan. 

TALM uses the `Progressing` condition to report the status and reasons as follows: 

  * `true`

TALM is remediating non-compliant policies. 

  * `false`

The update is not in progress. Possible reasons for this are: 

    * All clusters are compliant with all the managed policies. 
    * The update timed out as policy remediation took too long. 
    * Blocking CRs are missing from the system or have not yet completed. 
    * The `ClusterGroupUpgrade` CR is not enabled. 




Note

The managed policies apply in the order that they are listed in the `managedPolicies` field in the `ClusterGroupUpgrade` CR. One managed policy is applied to the specified clusters at a time. When a cluster complies with the current policy, the next managed policy is applied to it. 

**Sample`ClusterGroupUpgrade` CR in the `Progressing` state**

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  creationTimestamp: '2022-11-18T16:27:15Z'
  finalizers:
    - ran.openshift.io/cleanup-finalizer
  generation: 1
  name: talm-cgu
  namespace: talm-namespace
  resourceVersion: '40451823'
  uid: cca245a5-4bca-45fa-89c0-aa6af81a596c
Spec:
  actions:
    afterCompletion:
      deleteObjects: true
    beforeEnable: {}
  clusters:
    - spoke1
  enable: true
  managedPolicies:
    - talm-policy
  preCaching: true
  remediationStrategy:
    canaries:
        - spoke1
    maxConcurrency: 2
    timeout: 240
  clusterLabelSelectors:
    - matchExpressions:
      - key: label1
      operator: In
      values:
        - value1a
        - value1b
  batchTimeoutAction:
status:
    clusters:
      - name: spoke1
        state: complete
    computedMaxConcurrency: 2
    conditions:
      - lastTransitionTime: '2022-11-18T16:27:15Z'
        message: All selected clusters are valid
        reason: ClusterSelectionCompleted
        status: 'True'
        type: ClustersSelected
      - lastTransitionTime: '2022-11-18T16:27:15Z'
        message: Completed validation
        reason: ValidationCompleted
        status: 'True'
        type: Validated
      - lastTransitionTime: '2022-11-18T16:37:16Z'
        message: Remediating non-compliant policies
        reason: InProgress
        status: 'True'
        type: Progressing
    managedPoliciesForUpgrade:
      - name: talm-policy
        namespace: talm-namespace
    managedPoliciesNs:
      talm-policy: talm-namespace
    remediationPlan:
      - - spoke1
      - - spoke2
        - spoke3
    status:
      currentBatch: 2
      currentBatchRemediationProgress:
        spoke2:
          state: Completed
        spoke3:
          policyIndex: 0
          state: InProgress
      currentBatchStartedAt: '2022-11-18T16:27:16Z'
      startedAt: '2022-11-18T16:27:15Z'
```


The `Progressing` fields show that TALM is in the process of remediating policies. 

## 13.5.5. Update status

TALM uses the `Succeeded` condition to report the status and reasons as follows: 

  * `true`

All clusters are compliant with the specified managed policies. 

  * `false`

Policy remediation failed as there were no clusters available for remediation, or because policy remediation took too long for one of the following reasons: 

    * The current batch contains canary updates and the cluster in the batch does not comply with all the managed policies within the batch timeout. 
    * Clusters did not comply with the managed policies within the `timeout` value specified in the `remediationStrategy` field. 




**Sample`ClusterGroupUpgrade` CR in the `Succeeded` state**

```yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: cgu-upgrade-complete
      namespace: default
    spec:
      clusters:
      - spoke1
      - spoke4
      enable: true
      managedPolicies:
      - policy1-common-cluster-version-policy
      - policy2-common-pao-sub-policy
      remediationStrategy:
        maxConcurrency: 1
        timeout: 240
    status:
      clusters:
        - name: spoke1
          state: complete
        - name: spoke4
          state: complete
      conditions:
      - message: All selected clusters are valid
        reason: ClusterSelectionCompleted
        status: "True"
        type: ClustersSelected
      - message: Completed validation
        reason: ValidationCompleted
        status: "True"
        type: Validated
      - message: All clusters are compliant with all the managed policies
        reason: Completed
        status: "False"
        type: Progressing
      - message: All clusters are compliant with all the managed policies
        reason: Completed
        status: "True"
        type: Succeeded
      managedPoliciesForUpgrade:
      - name: policy1-common-cluster-version-policy
        namespace: default
      - name: policy2-common-pao-sub-policy
        namespace: default
      remediationPlan:
      - - spoke1
      - - spoke4
      status:
        completedAt: '2022-11-18T16:27:16Z'
        startedAt: '2022-11-18T16:27:15Z'
```


  * `spec.conditions.type` in the `Progressing` fields, the status is `false` as the update has completed; clusters are compliant with all the managed policies. 
  * `spec.conditions.type` the `Succeeded` fields show that the validations completed successfully. 
  * `status` the `status` field includes a list of clusters and their respective statuses. The status of a cluster can be `complete` or `timedout`. 



**Sample`ClusterGroupUpgrade` CR in the `timedout` state**

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  creationTimestamp: '2022-11-18T16:27:15Z'
  finalizers:
    - ran.openshift.io/cleanup-finalizer
  generation: 1
  name: talm-cgu
  namespace: talm-namespace
  resourceVersion: '40451823'
  uid: cca245a5-4bca-45fa-89c0-aa6af81a596c
spec:
  actions:
    afterCompletion:
      deleteObjects: true
    beforeEnable: {}
  clusters:
    - spoke1
    - spoke2
  enable: true
  managedPolicies:
    - talm-policy
  preCaching: false
  remediationStrategy:
    maxConcurrency: 2
    timeout: 240
status:
  clusters:
    - name: spoke1
      state: complete
    - currentPolicy:
        name: talm-policy
        status: NonCompliant
      name: spoke2
      state: timedout
  computedMaxConcurrency: 2
  conditions:
    - lastTransitionTime: '2022-11-18T16:27:15Z'
      message: All selected clusters are valid
      reason: ClusterSelectionCompleted
      status: 'True'
      type: ClustersSelected
    - lastTransitionTime: '2022-11-18T16:27:15Z'
      message: Completed validation
      reason: ValidationCompleted
      status: 'True'
      type: Validated
    - lastTransitionTime: '2022-11-18T16:37:16Z'
      message: Policy remediation took too long
      reason: TimedOut
      status: 'False'
      type: Progressing
    - lastTransitionTime: '2022-11-18T16:37:16Z'
      message: Policy remediation took too long
      reason: TimedOut
      status: 'False'
      type: Succeeded
  managedPoliciesForUpgrade:
    - name: talm-policy
      namespace: talm-namespace
  managedPoliciesNs:
    talm-policy: talm-namespace
  remediationPlan:
    - - spoke1
      - spoke2
  status:
        startedAt: '2022-11-18T16:27:15Z'
        completedAt: '2022-11-18T20:27:15Z'
```


  * `status.clusters.currentPolicy` if a cluster’s state is `timedout`, the `currentPolicy` field shows the name of the policy and the policy status. 
  * `status.conditions.type` the status for `succeeded` is `false` and the message indicates that policy remediation took too long. 



## 13.5.6. Blocking ClusterGroupUpgrade CRs

You can create multiple `ClusterGroupUpgrade` CRs and control their order of application. 

For example, if you create `ClusterGroupUpgrade` CR C that blocks the start of `ClusterGroupUpgrade` CR A, then `ClusterGroupUpgrade` CR A cannot start until the status of `ClusterGroupUpgrade` CR C becomes `UpgradeComplete`. 

One `ClusterGroupUpgrade` CR can have multiple blocking CRs. In this case, all the blocking CRs must complete before the upgrade for the current CR can start. 

**Prerequisites**

  * Install the Topology Aware Lifecycle Manager (TALM). 
  * Provision one or more managed clusters. 
  * Log in as a user with `cluster-admin` privileges. 
  * Create RHACM policies in the hub cluster. 



**Procedure**

  1. Save the content of the `ClusterGroupUpgrade` CRs in the `cgu-a.yaml`, `cgu-b.yaml`, and `cgu-c.yaml` files. 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-a
  namespace: default
spec:
  blockingCRs:
  - name: cgu-c
    namespace: default
  clusters:
  - spoke1
  - spoke2
  - spoke3
  enable: false
  managedPolicies:
  - policy1-common-cluster-version-policy
  - policy2-common-pao-sub-policy
  - policy3-common-ptp-sub-policy
  remediationStrategy:
    canaries:
    - spoke1
    maxConcurrency: 2
    timeout: 240
status:
  conditions:
  - message: The ClusterGroupUpgrade CR is not enabled
    reason: UpgradeNotStarted
    status: "False"
    type: Ready
  managedPoliciesForUpgrade:
  - name: policy1-common-cluster-version-policy
    namespace: default
  - name: policy2-common-pao-sub-policy
    namespace: default
  - name: policy3-common-ptp-sub-policy
    namespace: default
  placementBindings:
  - cgu-a-policy1-common-cluster-version-policy
  - cgu-a-policy2-common-pao-sub-policy
  - cgu-a-policy3-common-ptp-sub-policy
  placementRules:
  - cgu-a-policy1-common-cluster-version-policy
  - cgu-a-policy2-common-pao-sub-policy
  - cgu-a-policy3-common-ptp-sub-policy
  remediationPlan:
  - - spoke1
  - - spoke2
```


     * `spec.blockingCRs.name` defines the blocking CRs. The `cgu-a` update cannot start until `cgu-c` is complete. 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-b
  namespace: default
spec:
  blockingCRs:
  - name: cgu-a
    namespace: default
  clusters:
  - spoke4
  - spoke5
  enable: false
  managedPolicies:
  - policy1-common-cluster-version-policy
  - policy2-common-pao-sub-policy
  - policy3-common-ptp-sub-policy
  - policy4-common-sriov-sub-policy
  remediationStrategy:
    maxConcurrency: 1
    timeout: 240
status:
  conditions:
  - message: The ClusterGroupUpgrade CR is not enabled
    reason: UpgradeNotStarted
    status: "False"
    type: Ready
  managedPoliciesForUpgrade:
  - name: policy1-common-cluster-version-policy
    namespace: default
  - name: policy2-common-pao-sub-policy
    namespace: default
  - name: policy3-common-ptp-sub-policy
    namespace: default
  - name: policy4-common-sriov-sub-policy
    namespace: default
  placementBindings:
  - cgu-b-policy1-common-cluster-version-policy
  - cgu-b-policy2-common-pao-sub-policy
  - cgu-b-policy3-common-ptp-sub-policy
  - cgu-b-policy4-common-sriov-sub-policy
  placementRules:
  - cgu-b-policy1-common-cluster-version-policy
  - cgu-b-policy2-common-pao-sub-policy
  - cgu-b-policy3-common-ptp-sub-policy
  - cgu-b-policy4-common-sriov-sub-policy
  remediationPlan:
  - - spoke4
  - - spoke5
  status: {}
```


The `cgu-b` update cannot start until `cgu-a` is complete. 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-c
  namespace: default
spec:
  clusters:
  - spoke6
  enable: false
  managedPolicies:
  - policy1-common-cluster-version-policy
  - policy2-common-pao-sub-policy
  - policy3-common-ptp-sub-policy
  - policy4-common-sriov-sub-policy
  remediationStrategy:
    maxConcurrency: 1
    timeout: 240
status:
  conditions:
  - message: The ClusterGroupUpgrade CR is not enabled
    reason: UpgradeNotStarted
    status: "False"
    type: Ready
  managedPoliciesCompliantBeforeUpgrade:
  - policy2-common-pao-sub-policy
  - policy3-common-ptp-sub-policy
  managedPoliciesForUpgrade:
  - name: policy1-common-cluster-version-policy
    namespace: default
  - name: policy4-common-sriov-sub-policy
    namespace: default
  placementBindings:
  - cgu-c-policy1-common-cluster-version-policy
  - cgu-c-policy4-common-sriov-sub-policy
  placementRules:
  - cgu-c-policy1-common-cluster-version-policy
  - cgu-c-policy4-common-sriov-sub-policy
  remediationPlan:
  - - spoke6
  status: {}
```


The `cgu-c` update does not have any blocking CRs. TALM starts the `cgu-c` update when the `enable` field is set to `true`. 

  2. Create the `ClusterGroupUpgrade` CRs by running the following command for each relevant CR: 

```shell-session
$ oc apply -f <name>.yaml
```


  3. Start the update process by running the following command for each relevant CR: 

```shell-session
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/<name> \
--type merge -p '{"spec":{"enable":true}}'
```


The following examples show `ClusterGroupUpgrade` CRs where the `enable` field is set to `true`: 

Example for `cgu-a` with blocking CRs: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-a
  namespace: default
spec:
  blockingCRs:
  - name: cgu-c
    namespace: default
  clusters:
  - spoke1
  - spoke2
  - spoke3
  enable: true
  managedPolicies:
  - policy1-common-cluster-version-policy
  - policy2-common-pao-sub-policy
  - policy3-common-ptp-sub-policy
  remediationStrategy:
    canaries:
    - spoke1
    maxConcurrency: 2
    timeout: 240
status:
  conditions:
  - message: 'The ClusterGroupUpgrade CR is blocked by other CRs that have not yet
      completed: [cgu-c]'
    reason: UpgradeCannotStart
    status: "False"
    type: Ready
  managedPoliciesForUpgrade:
  - name: policy1-common-cluster-version-policy
    namespace: default
  - name: policy2-common-pao-sub-policy
    namespace: default
  - name: policy3-common-ptp-sub-policy
    namespace: default
  placementBindings:
  - cgu-a-policy1-common-cluster-version-policy
  - cgu-a-policy2-common-pao-sub-policy
  - cgu-a-policy3-common-ptp-sub-policy
  placementRules:
  - cgu-a-policy1-common-cluster-version-policy
  - cgu-a-policy2-common-pao-sub-policy
  - cgu-a-policy3-common-ptp-sub-policy
  remediationPlan:
  - - spoke1
  - - spoke2
  status: {}
```


Shows the list of blocking CRs. 

Example for `cgu-b` with blocking CRs: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-b
  namespace: default
spec:
  blockingCRs:
  - name: cgu-a
    namespace: default
  clusters:
  - spoke4
  - spoke5
  enable: true
  managedPolicies:
  - policy1-common-cluster-version-policy
  - policy2-common-pao-sub-policy
  - policy3-common-ptp-sub-policy
  - policy4-common-sriov-sub-policy
  remediationStrategy:
    maxConcurrency: 1
    timeout: 240
status:
  conditions:
  - message: 'The ClusterGroupUpgrade CR is blocked by other CRs that have not yet
      completed: [cgu-a]'
    reason: UpgradeCannotStart
    status: "False"
    type: Ready
  managedPoliciesForUpgrade:
  - name: policy1-common-cluster-version-policy
    namespace: default
  - name: policy2-common-pao-sub-policy
    namespace: default
  - name: policy3-common-ptp-sub-policy
    namespace: default
  - name: policy4-common-sriov-sub-policy
    namespace: default
  placementBindings:
  - cgu-b-policy1-common-cluster-version-policy
  - cgu-b-policy2-common-pao-sub-policy
  - cgu-b-policy3-common-ptp-sub-policy
  - cgu-b-policy4-common-sriov-sub-policy
  placementRules:
  - cgu-b-policy1-common-cluster-version-policy
  - cgu-b-policy2-common-pao-sub-policy
  - cgu-b-policy3-common-ptp-sub-policy
  - cgu-b-policy4-common-sriov-sub-policy
  remediationPlan:
  - - spoke4
  - - spoke5
  status: {}
```


Shows the list of blocking CRs. 

Example for `cgu-c` with blocking CRs: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-c
  namespace: default
spec:
  clusters:
  - spoke6
  enable: true
  managedPolicies:
  - policy1-common-cluster-version-policy
  - policy2-common-pao-sub-policy
  - policy3-common-ptp-sub-policy
  - policy4-common-sriov-sub-policy
  remediationStrategy:
    maxConcurrency: 1
    timeout: 240
status:
  conditions:
  - message: The ClusterGroupUpgrade CR has upgrade policies that are still non compliant
    reason: UpgradeNotCompleted
    status: "False"
    type: Ready
  managedPoliciesCompliantBeforeUpgrade:
  - policy2-common-pao-sub-policy
  - policy3-common-ptp-sub-policy
  managedPoliciesForUpgrade:
  - name: policy1-common-cluster-version-policy
    namespace: default
  - name: policy4-common-sriov-sub-policy
    namespace: default
  placementBindings:
  - cgu-c-policy1-common-cluster-version-policy
  - cgu-c-policy4-common-sriov-sub-policy
  placementRules:
  - cgu-c-policy1-common-cluster-version-policy
  - cgu-c-policy4-common-sriov-sub-policy
  remediationPlan:
  - - spoke6
  status:
    currentBatch: 1
    remediationPlanForBatch:
      spoke6: 0
```


The `cgu-c` update does not have any blocking CRs.
