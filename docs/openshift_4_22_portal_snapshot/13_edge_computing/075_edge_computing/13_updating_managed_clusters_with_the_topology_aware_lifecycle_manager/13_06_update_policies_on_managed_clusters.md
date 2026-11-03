# 13.6. Update policies on managed clusters

The Topology Aware Lifecycle Manager (TALM) remediates a set of `inform` policies for the clusters specified in the `ClusterGroupUpgrade` custom resource (CR). 

TALM remediates `inform` policies by controlling the `remediationAction` specification in a `Policy` CR through the `bindingOverrides.remediationAction` and `subFilter` specifications in the `PlacementBinding` CR. Each policy has its own corresponding RHACM placement rule and RHACM placement binding. 

One by one, TALM adds each cluster from the current batch to the placement rule that corresponds with the applicable managed policy. If a cluster is already compliant with a policy, TALM skips applying that policy on the compliant cluster. TALM then moves on to applying the next policy to the non-compliant cluster. After TALM completes the updates in a batch, all clusters are removed from the placement rules associated with the policies. Then, the update of the next batch starts. 

If a spoke cluster does not report any compliant state to RHACM, the managed policies on the hub cluster can be missing status information that TALM needs. TALM handles these cases in the following ways: 

  * If a policy’s `status.compliant` field is missing, TALM ignores the policy and adds a log entry. Then, TALM continues looking at the policy’s `status.status` field. 
  * If a policy’s `status.status` is missing, TALM produces an error. 
  * If a cluster’s compliance status is missing in the policy’s `status.status` field, TALM considers that cluster to be non-compliant with that policy. 



The `ClusterGroupUpgrade` CR’s `batchTimeoutAction` determines what happens if an upgrade fails for a cluster. You can specify `continue` to skip the failing cluster and continue to upgrade other clusters, or specify `abort` to stop the policy remediation for all clusters. Once the timeout elapses, TALM removes all the resources it created to ensure that no further updates are made to clusters. 

**Example upgrade policy**

```yaml
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: ocp-4.4.22.4
  namespace: platform-upgrade
spec:
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: upgrade
      spec:
        namespaceselector:
          exclude:
          - kube-*
          include:
          - '*'
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
                version: 4.4.22.4
              upstream: https://api.openshift.com/api/upgrades_info/v1/graph
            status:
              history:
                - state: Completed
                  version: 4.4.22.4
        remediationAction: inform
        severity: low
  remediationAction: inform
```


For more information about RHACM policies, see "Policy overview" in the RHACM documentation. 

**Additional resources**

  * [Policy overview](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#policy-overview)



**Additional resources**

  * [About the PolicyGenerator CRD](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-the-policygentemplate_ztp-configuring-managed-clusters-policygenerator "10.1.2. About the PolicyGenerator CRD")



## 13.6.1. Configuring Operator subscriptions for managed clusters that you install with TALM

Topology Aware Lifecycle Manager (TALM) can only approve the install plan for an Operator if the `Subscription` custom resource (CR) of the Operator contains the `status.state.AtLatestKnown` field. 

**Procedure**

  1. Add the `status.state.AtLatestKnown` field to the `Subscription` CR of the Operator: 

**Example Subscription CR**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: cluster-logging
  namespace: openshift-logging
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
spec:
  channel: "stable-6.2"
  name: cluster-logging
  source: redhat-operators-disconnected
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
status:
  state: AtLatestKnown
```


The `status.state: AtLatestKnown` field is used for the latest Operator version available from the Operator catalog. 

Note

When a new version of the Operator is available in the registry, the associated policy becomes non-compliant. 

  2. Apply the changed `Subscription` policy to your managed clusters with a `ClusterGroupUpgrade` CR. 



## 13.6.2. Applying update policies to managed clusters

You can update your managed clusters by applying your policies. 

**Prerequisites**

  * Install the Topology Aware Lifecycle Manager (TALM). 
  * TALM requires RHACM 2.9 or later. 
  * Provision one or more managed clusters. 
  * Log in as a user with `cluster-admin` privileges. 
  * Create RHACM policies in the hub cluster. 



**Procedure**

  1. Save the contents of the `ClusterGroupUpgrade` CR in the `cgu-1.yaml` file. 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu-1
  namespace: default
spec:
  managedPolicies:
    - policy1-common-cluster-version-policy
    - policy2-common-nto-sub-policy
    - policy3-common-ptp-sub-policy
    - policy4-common-sriov-sub-policy
  enable: false
  clusters:
  - spoke1
  - spoke2
  - spoke5
  - spoke6
  remediationStrategy:
    maxConcurrency: 2
    timeout: 240
  batchTimeoutAction:
```


     * `spec.managedPolicies` the name of the policies to apply. 
     * `spec.clusters` the list of clusters to update. 
     * `spec.remediationStrategy.maxConcurrency` the `maxConcurrency` field signifies the number of clusters updated at the same time. 
     * `spec.remediationStrategy.timeout` the update timeout in minutes. 
     * `spec.batchTimeoutAction` controls what happens if a batch times out. Possible values are `abort` or `continue`. If unspecified, the default is `continue`. 

  2. Create the `ClusterGroupUpgrade` CR by running the following command: 

```shell-session
$ oc create -f cgu-1.yaml
```


     1. Check if the `ClusterGroupUpgrade` CR was created in the hub cluster by running the following command: 

```shell-session
$ oc get cgu --all-namespaces
```


**Example output**

```shell-session
NAMESPACE   NAME  AGE  STATE      DETAILS
default     cgu-1 8m55 NotEnabled Not Enabled
```


     2. Check the status of the update by running the following command: 

```shell-session
$ oc get cgu -n default cgu-1 -ojsonpath='{.status}' | jq
```


**Example output**

```plaintext
{
  "computedMaxConcurrency": 2,
  "conditions": [
    {
      "lastTransitionTime": "2022-02-25T15:34:07Z",
      "message": "Not enabled",
      "reason": "NotEnabled",
      "status": "False",
      "type": "Progressing"
    }
  ],
  "managedPoliciesContent": {
    "policy1-common-cluster-version-policy": "null",
    "policy2-common-nto-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"node-tuning-operator\",\"namespace\":\"openshift-cluster-node-tuning-operator\"}]",
    "policy3-common-ptp-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"ptp-operator-subscription\",\"namespace\":\"openshift-ptp\"}]",
    "policy4-common-sriov-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"sriov-network-operator-subscription\",\"namespace\":\"openshift-sriov-network-operator\"}]"
  },
  "managedPoliciesForUpgrade": [
    {
      "name": "policy1-common-cluster-version-policy",
      "namespace": "default"
    },
    {
      "name": "policy2-common-nto-sub-policy",
      "namespace": "default"
    },
    {
      "name": "policy3-common-ptp-sub-policy",
      "namespace": "default"
    },
    {
      "name": "policy4-common-sriov-sub-policy",
      "namespace": "default"
    }
  ],
  "managedPoliciesNs": {
    "policy1-common-cluster-version-policy": "default",
    "policy2-common-nto-sub-policy": "default",
    "policy3-common-ptp-sub-policy": "default",
    "policy4-common-sriov-sub-policy": "default"
  },
  "placementBindings": [
    "cgu-policy1-common-cluster-version-policy",
    "cgu-policy2-common-nto-sub-policy",
    "cgu-policy3-common-ptp-sub-policy",
    "cgu-policy4-common-sriov-sub-policy"
  ],
  "placementRules": [
    "cgu-policy1-common-cluster-version-policy",
    "cgu-policy2-common-nto-sub-policy",
    "cgu-policy3-common-ptp-sub-policy",
    "cgu-policy4-common-sriov-sub-policy"
  ],
  "remediationPlan": [
    [
      "spoke1",
      "spoke2"
    ],
    [
      "spoke5",
      "spoke6"
    ]
  ],
  "status": {}
}
```


The `spec.enable` field in the `ClusterGroupUpgrade` CR is set to `false`. 

  3. Change the value of the `spec.enable` field to `true` by running the following command: 

```shell-session
$ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-1 \
--patch '{"spec":{"enable":true}}' --type=merge
```


**Verification**

  1. Check the status of the update by running the following command: 

```shell-session
$ oc get cgu -n default cgu-1 -ojsonpath='{.status}' | jq
```


**Example output**

```plaintext
{
  "computedMaxConcurrency": 2,
  "conditions": [
    {
      "lastTransitionTime": "2022-02-25T15:33:07Z",
      "message": "All selected clusters are valid",
      "reason": "ClusterSelectionCompleted",
      "status": "True",
      "type": "ClustersSelected"
    },
    {
      "lastTransitionTime": "2022-02-25T15:33:07Z",
      "message": "Completed validation",
      "reason": "ValidationCompleted",
      "status": "True",
      "type": "Validated"
    },
    {
      "lastTransitionTime": "2022-02-25T15:34:07Z",
      "message": "Remediating non-compliant policies",
      "reason": "InProgress",
      "status": "True",
      "type": "Progressing"
    }
  ],
  "managedPoliciesContent": {
    "policy1-common-cluster-version-policy": "null",
    "policy2-common-nto-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"node-tuning-operator\",\"namespace\":\"openshift-cluster-node-tuning-operator\"}]",
    "policy3-common-ptp-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"ptp-operator-subscription\",\"namespace\":\"openshift-ptp\"}]",
    "policy4-common-sriov-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"sriov-network-operator-subscription\",\"namespace\":\"openshift-sriov-network-operator\"}]"
  },
  "managedPoliciesForUpgrade": [
    {
      "name": "policy1-common-cluster-version-policy",
      "namespace": "default"
    },
    {
      "name": "policy2-common-nto-sub-policy",
      "namespace": "default"
    },
    {
      "name": "policy3-common-ptp-sub-policy",
      "namespace": "default"
    },
    {
      "name": "policy4-common-sriov-sub-policy",
      "namespace": "default"
    }
  ],
  "managedPoliciesNs": {
    "policy1-common-cluster-version-policy": "default",
    "policy2-common-nto-sub-policy": "default",
    "policy3-common-ptp-sub-policy": "default",
    "policy4-common-sriov-sub-policy": "default"
  },
  "placementBindings": [
    "cgu-policy1-common-cluster-version-policy",
    "cgu-policy2-common-nto-sub-policy",
    "cgu-policy3-common-ptp-sub-policy",
    "cgu-policy4-common-sriov-sub-policy"
  ],
  "placementRules": [
    "cgu-policy1-common-cluster-version-policy",
    "cgu-policy2-common-nto-sub-policy",
    "cgu-policy3-common-ptp-sub-policy",
    "cgu-policy4-common-sriov-sub-policy"
  ],
  "remediationPlan": [
    [
      "spoke1",
      "spoke2"
    ],
    [
      "spoke5",
      "spoke6"
    ]
  ],
  "status": {
    "currentBatch": 1,
    "currentBatchRemediationProgress": {
       "spoke1": {
          "policyIndex": 1,
          "state": "InProgress"
       },
       "spoke2": {
          "policyIndex": 1,
          "state": "InProgress"
       }
    },
    "currentBatchStartedAt": "2022-02-25T15:54:16Z",
    "startedAt": "2022-02-25T15:54:16Z"
  }
}
```


Reflects the update progress of the current batch. Run this command again to receive updated information about the progress. 

  2. Check the status of the policies by running the following command: 

```shell-session
oc get policies -A
```


**Example output**

```shell-session
NAMESPACE   NAME                                        REMEDIATION ACTION    COMPLIANCE STATE     AGE
spoke1    default.policy1-common-cluster-version-policy enforce               Compliant            18m
spoke1    default.policy2-common-nto-sub-policy         enforce               NonCompliant         18m
spoke2    default.policy1-common-cluster-version-policy enforce               Compliant            18m
spoke2    default.policy2-common-nto-sub-policy         enforce               NonCompliant         18m
spoke5    default.policy3-common-ptp-sub-policy         inform                NonCompliant         18m
spoke5    default.policy4-common-sriov-sub-policy       inform                NonCompliant         18m
spoke6    default.policy3-common-ptp-sub-policy         inform                NonCompliant         18m
spoke6    default.policy4-common-sriov-sub-policy       inform                NonCompliant         18m
default   policy1-common-ptp-sub-policy                 inform                Compliant            18m
default   policy2-common-sriov-sub-policy               inform                NonCompliant         18m
default   policy3-common-ptp-sub-policy                 inform                NonCompliant         18m
default   policy4-common-sriov-sub-policy               inform                NonCompliant         18m
```


     * The `spec.remediationAction` value changes to `enforce` for the child policies applied to the clusters from the current batch. 
     * The `spec.remedationAction` value remains `inform` for the child policies in the rest of the clusters. 
     * After the batch is complete, the `spec.remediationAction` value changes back to `inform` for the enforced child policies. 

  3. If the policies include Operator subscriptions, you can check the installation progress directly on the single-node cluster. 

     1. Export the `KUBECONFIG` file of the single-node cluster you want to check the installation progress for by running the following command: 

```shell-session
$ export KUBECONFIG=<cluster_kubeconfig_absolute_path>
```


     2. Check all the subscriptions present on the single-node cluster and look for the one in the policy you are trying to install through the `ClusterGroupUpgrade` CR by running the following command: 

```shell-session
$ oc get subs -A | grep -i <subscription_name>
```


**Example output for`cluster-logging` policy**

```shell-session
NAMESPACE                              NAME                         PACKAGE                      SOURCE             CHANNEL
openshift-logging                      cluster-logging              cluster-logging              redhat-operators   stable
```


  4. If one of the managed policies includes a `ClusterVersion` CR, check the status of platform updates in the current batch by running the following command against the spoke cluster: 

```shell-session
$ oc get clusterversion
```


**Example output**

```shell-session
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.4.22.5     True        True          43s     Working towards 4.4.22.7: 71 of 735 done (9% complete)
```


  5. Check the Operator subscription by running the following command: 

```shell-session
$ oc get subs -n <operator-namespace> <operator-subscription> -ojsonpath="{.status}"
```


  6. Check the install plans present on the single-node cluster that is associated with the desired subscription by running the following command: 

```shell-session
$ oc get installplan -n <subscription_namespace>
```


**Example output for`cluster-logging` Operator**

```shell-session
NAMESPACE                              NAME            CSV                                 APPROVAL   APPROVED
openshift-logging                      install-6khtw   cluster-logging.5.3.3-4             Manual     true
```


The install plans have their `Approval` field set to `Manual` and their `Approved` field changes from `false` to `true` after TALM approves the install plan. 

Note

When TALM is remediating a policy containing a subscription, it automatically approves any install plans attached to that subscription. Where multiple install plans are needed to get the operator to the latest known version, TALM might approve multiple install plans, upgrading through one or more intermediate versions to get to the final version. 

  7. Check if the cluster service version for the Operator of the policy that the `ClusterGroupUpgrade` is installing reached the `Succeeded` phase by running the following command: 

```shell-session
$ oc get csv -n <operator_namespace>
```


**Example output for OpenShift Logging Operator**

```shell-session
NAME                    DISPLAY                     VERSION   REPLACES   PHASE
cluster-logging.v6.2.1  Red Hat OpenShift Logging   6.2.1                Succeeded
```
