# 13.8. Troubleshooting the Topology Aware Lifecycle Manager

The Topology Aware Lifecycle Manager (TALM) is an OpenShift Container Platform Operator that remediates RHACM policies. When issues occur, use the `oc adm must-gather` command to gather details and logs and to take steps in debugging the issues. 

For more information about related topics, see the following documentation: 

  * [Red Hat Advanced Cluster Management for Kubernetes 2.4 Support Matrix](https://access.redhat.com/articles/6218901)
  * [Red Hat Advanced Cluster Management Troubleshooting](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.0/html/troubleshooting/troubleshooting)
  * The "Troubleshooting Operator issues" section 



**General troubleshooting**

You can determine the cause of the problem by reviewing the following questions: 

  * Is the configuration that you are applying supported? 

    * Are the RHACM and the OpenShift Container Platform versions compatible? 
    * Are the TALM and RHACM versions compatible? 

  * Which of the following components is causing the problem? 

    * [Cannot modify the ClusterUpgradeGroup CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-talm-for-cluster-updates#talo-troubleshooting-modify-cgu_cnf-topology-aware-lifecycle-manager)
    * [Managed policies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-talm-for-cluster-updates#talo-troubleshooting-managed-policies_cnf-topology-aware-lifecycle-manager)
    * [Clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-talm-for-cluster-updates#talo-troubleshooting-clusters_cnf-topology-aware-lifecycle-manager)
    * [Remediation Strategy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-talm-for-cluster-updates#talo-troubleshooting-remediation-strategy_cnf-topology-aware-lifecycle-manager)
    * [Topology Aware Lifecycle Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-talm-for-cluster-updates#talo-troubleshooting-remediation-talo_cnf-topology-aware-lifecycle-manager)




**Cannot modify the ClusterUpgradeGroup CR**

Issue
     You cannot edit the `ClusterUpgradeGroup` CR after enabling the update. 
Resolution
    

Restart the procedure by performing the following steps: 

  1. Remove the old `ClusterGroupUpgrade` CR by running the following command: 

```shell-session
$ oc delete cgu -n <ClusterGroupUpgradeCR_namespace> <ClusterGroupUpgradeCR_name>
```


  2. Check and fix the existing issues with the managed clusters and policies. 

     1. Ensure that all the clusters are managed clusters and available. 
     2. Ensure that all the policies exist and have the `spec.remediationAction` field set to `inform`. 

  3. Create a new `ClusterGroupUpgrade` CR with the correct configurations. 

```shell-session
$ oc apply -f <ClusterGroupUpgradeCR_YAML>
```


**Managed policies**

**Checking managed policies on the system**

Issue
     You want to check if you have the correct managed policies on the system. 
Resolution
    

Run the following command: 

```shell-session
$ oc get cgu lab-upgrade -ojsonpath='{.spec.managedPolicies}'
```


Example output: 

```plaintext
["group-du-sno-validator-du-validator-policy", "policy2-common-nto-sub-policy", "policy3-common-ptp-sub-policy"]
```


**Checking remediationAction mode**

Issue
     You want to check if the `remediationAction` field is set to `inform` in the `spec` of the managed policies. 
Resolution
    

Run the following command: 

```shell-session
$ oc get policies --all-namespaces
```


Example output: 

```shell-session
NAMESPACE   NAME                                                 REMEDIATION ACTION   COMPLIANCE STATE   AGE
default     policy1-common-cluster-version-policy                inform               NonCompliant       5d21h
default     policy2-common-nto-sub-policy                        inform               Compliant          5d21h
default     policy3-common-ptp-sub-policy                        inform               NonCompliant       5d21h
default     policy4-common-sriov-sub-policy                      inform               NonCompliant       5d21h
```


**Checking policy compliance state**

Issue
     You want to check the compliance state of policies. 
Resolution
    

Run the following command: 

```shell-session
$ oc get policies --all-namespaces
```


Example output: 

```shell-session
NAMESPACE   NAME                                                 REMEDIATION ACTION   COMPLIANCE STATE   AGE
default     policy1-common-cluster-version-policy                inform               NonCompliant       5d21h
default     policy2-common-nto-sub-policy                        inform               Compliant          5d21h
default     policy3-common-ptp-sub-policy                        inform               NonCompliant       5d21h
default     policy4-common-sriov-sub-policy                      inform               NonCompliant       5d21h
```


**Clusters**

**Checking if managed clusters are present**

Issue
     You want to check if the clusters in the `ClusterGroupUpgrade` CR are managed clusters. 
Resolution
    

Run the following command: 

```shell-session
$ oc get managedclusters
```


Example output: 

```shell-session
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS                    JOINED   AVAILABLE   AGE
local-cluster   true           https://api.hub.example.com:6443        True     Unknown     13d
spoke1          true           https://api.spoke1.example.com:6443     True     True        13d
spoke3          true           https://api.spoke3.example.com:6443     True     True        27h
```


  1. Alternatively, check the TALM manager logs: 

     1. Get the name of the TALM manager by running the following command: 

```shell-session
$ oc get pod -n openshift-operators
```


Example output: 

```shell-session
NAME                                                         READY   STATUS    RESTARTS   AGE
cluster-group-upgrades-controller-manager-75bcc7484d-8k8xp   2/2     Running   0          45m
```


     2. Check the TALM manager logs by running the following command: 

```shell-session
$ oc logs -n openshift-operators \
cluster-group-upgrades-controller-manager-75bcc7484d-8k8xp -c manager
```


Example output: 

```shell-session
ERROR	controller-runtime.manager.controller.clustergroupupgrade	Reconciler error	{"reconciler group": "ran.openshift.io", "reconciler kind": "ClusterGroupUpgrade", "name": "lab-upgrade", "namespace": "default", "error": "Cluster spoke5555 is not a ManagedCluster"}
sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
```


The error message shows that the cluster is not a managed cluster. 

**Checking if managed clusters are available**

Issue
     You want to check if the managed clusters specified in the `ClusterGroupUpgrade` CR are available. 
Resolution
    

Run the following command: 

```shell-session
$ oc get managedclusters
```


Example output: 

```shell-session
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS                    JOINED   AVAILABLE   AGE
local-cluster   true           https://api.hub.testlab.com:6443        True     Unknown     13d
spoke1          true           https://api.spoke1.testlab.com:6443     True     True        13d
spoke3          true           https://api.spoke3.testlab.com:6443     True     True        27h
```


The value of the `AVAILABLE` field is `True` for the managed clusters. 

**Checking clusterLabelSelector**

Issue
     You want to check if the `clusterLabelSelector` field specified in the `ClusterGroupUpgrade` CR matches at least one of the managed clusters. 
Resolution
    

Run the following command: 

```shell-session
$ oc get managedcluster --selector=upgrade=true
```


The label for the clusters you want to update is `upgrade:true`. 

Example output: 

```shell-session
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS                     JOINED    AVAILABLE   AGE
spoke1          true           https://api.spoke1.testlab.com:6443      True     True        13d
spoke3          true           https://api.spoke3.testlab.com:6443      True     True        27h
```


**Checking if canary clusters are present**

Issue
    

You want to check if the canary clusters are present in the list of clusters. 

Example `ClusterGroupUpgrade` CR: 

```yaml
spec:
    remediationStrategy:
        canaries:
        - spoke3
        maxConcurrency: 2
        timeout: 240
    clusterLabelSelectors:
      - matchLabels:
          upgrade: true
```


Resolution
    

Run the following commands: 

```shell-session
$ oc get cgu lab-upgrade -ojsonpath='{.spec.clusters}'
```


Example output: 

```plaintext
["spoke1", "spoke3"]
```


  1. Check if the canary clusters are present in the list of clusters that match `clusterLabelSelector` labels by running the following command: 

```shell-session
$ oc get managedcluster --selector=upgrade=true
```


Example output: 

```shell-session
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED    AVAILABLE   AGE
spoke1          true           https://api.spoke1.testlab.com:6443   True     True        13d
spoke3          true           https://api.spoke3.testlab.com:6443   True     True        27h
```


Note

A cluster can be present in `spec.clusters` and also be matched by the `spec.clusterLabelSelector` label. 

**Checking the pre-caching status on spoke clusters**

  1. Check the status of pre-caching by running the following command on the spoke cluster: 

```shell-session
$ oc get jobs,pods -n openshift-talo-pre-cache
```


**Remediation Strategy**

**Checking if remediationStrategy is present in the ClusterGroupUpgrade CR**

Issue
     You want to check if the `remediationStrategy` is present in the `ClusterGroupUpgrade` CR. 
Resolution
    

Run the following command: 

```shell-session
$ oc get cgu lab-upgrade -ojsonpath='{.spec.remediationStrategy}'
```


Example output: 

```plaintext
{"maxConcurrency":2, "timeout":240}
```


**Checking if maxConcurrency is specified in the ClusterGroupUpgrade CR**

Issue
     You want to check if the `maxConcurrency` is specified in the `ClusterGroupUpgrade` CR. 
Resolution
    

Run the following command: 

```shell-session
$ oc get cgu lab-upgrade -ojsonpath='{.spec.remediationStrategy.maxConcurrency}'
```


Example output: 

```shell-session
2
```


**Topology Aware Lifecycle Manager**

**Checking condition message and status in the ClusterGroupUpgrade CR**

Issue
     You want to check the value of the `status.conditions` field in the `ClusterGroupUpgrade` CR. 
Resolution
    

Run the following command: 

```shell-session
$ oc get cgu lab-upgrade -ojsonpath='{.status.conditions}'
```


Example output: 

```plaintext
{"lastTransitionTime":"2022-02-17T22:25:28Z", "message":"Missing managed policies:[policyList]", "reason":"NotAllManagedPoliciesExist", "status":"False", "type":"Validated"}
```


**Checking if status.remediationPlan was computed**

Issue
     You want to check if `status.remediationPlan` is computed. 
Resolution
    

Run the following command: 

```shell-session
$ oc get cgu lab-upgrade -ojsonpath='{.status.remediationPlan}'
```


Example output: 

```plaintext
[["spoke2", "spoke3"]]
```


**Errors in the TALM manager container**

Issue
     You want to check the logs of the manager container of TALM. 
Resolution
    

Run the following command: 

```shell-session
$ oc logs -n openshift-operators \
cluster-group-upgrades-controller-manager-75bcc7484d-8k8xp -c manager
```


Example output: 

```shell-session
ERROR	controller-runtime.manager.controller.clustergroupupgrade	Reconciler error	{"reconciler group": "ran.openshift.io", "reconciler kind": "ClusterGroupUpgrade", "name": "lab-upgrade", "namespace": "default", "error": "Cluster spoke5555 is not a ManagedCluster"}
sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
```


Displays the error. 

**Clusters are not compliant to some policies after a`ClusterGroupUpgrade` CR has completed**

Issue
    

The policy compliance status that TALM uses to decide if remediation is needed has not yet fully updated for all clusters. This may be because: 

  * The CGU was run too soon after a policy was created or updated. 
  * The remediation of a policy affects the compliance of subsequent policies in the `ClusterGroupUpgrade` CR. 



Resolution
     Create and apply a new `ClusterGroupUpdate` CR with the same specification. 

**Auto-created`ClusterGroupUpgrade` CR in the GitOps ZTP workflow has no managed policies**

Issue
     If there are no policies for the managed cluster when the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR with no policies is auto-created. Upon completion of the `ClusterGroupUpgrade` CR, the managed cluster is labeled as `ztp-done`. If the `PolicyGenerator` or `PolicyGenTemplate` CRs were not pushed to the Git repository within the required time after `ClusterInstance` resources were pushed, this might result in no policies being available for the target cluster when the cluster became `Ready`. 
Resolution
     Verify that the policies you want to apply are available on the hub cluster, then create a `ClusterGroupUpgrade` CR with the required policies. 

You can either manually create the `ClusterGroupUpgrade` CR or trigger auto-creation again. To trigger auto-creation of the `ClusterGroupUpgrade` CR, remove the `ztp-done` label from the cluster and delete the empty `ClusterGroupUpgrade` CR that was previously created in the `zip-install` namespace. 

**Pre-caching has failed**

Issue
    

Pre-caching might fail for one of the following reasons: 

  * There is not enough free space on the node. 
  * For a disconnected environment, the pre-cache image has not been properly mirrored. 
  * There was an issue when creating the pod. 



Resolution
    

  1. To check if pre-caching has failed due to insufficient space, check the log of the pre-caching pod in the node. 

     1. Find the name of the pod using the following command: 

```shell-session
$ oc get pods -n openshift-talo-pre-cache
```


     2. Check the logs to see if the error is related to insufficient space using the following command: 

```shell-session
$ oc logs -n openshift-talo-pre-cache <pod name>
```


  2. If there is no log, check the pod status using the following command: 

```shell-session
$ oc describe pod -n openshift-talo-pre-cache <pod name>
```


  3. If the pod does not exist, check the job status to see why it could not create a pod using the following command: 

```shell-session
$ oc describe job -n openshift-talo-pre-cache pre-cache
```


**Matching policies and`ManagedCluster` CRs before the managed cluster is available**

Issue
     You want RHACM to match policies and managed clusters before the managed clusters become available. 
Resolution
    

To ensure that TALM correctly applies the RHACM policies specified in the `spec.managedPolicies` field of the `ClusterGroupUpgrade` (CGU) CR, TALM needs to match these policies to the managed cluster before the managed cluster is available. The RHACM `PolicyGenerator` uses the generated `Placement` CR to do this automatically. By default, this `Placement` CR includes the necessary tolerations to ensure proper TALM behavior. 

The expected `spec.tolerations` settings in the `Placement` CR are as follows: 

```yaml
#…​
  tolerations:
    - key: cluster.open-cluster-management.io/unavailable
     operator: Exists
    - key: cluster.open-cluster-management.io/unreachable
     operator: Exists
#…​
```


If you use a custom `Placement` CR instead of the one generated by the RHACM `PolicyGenerator`, include these tolerations in that `Placement` CR. 

For more information on placements in RHACM, see [Placement overview](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.13/html-single/clusters/index#placement-overview). 

For more information on tolerations in RHACM, see [Placing managed clusters by using taints and tolerations](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html-single/clusters/index#taints-tolerations-managed). 

To ensure that the `ClusterGroupUpgrade` configuration is functional, you can do the following: 

**Procedure**

  1. Create the `ClusterGroupUpgrade` CR with the `spec.enable` field set to `false`. 
  2. Wait for the status to be updated and go through the troubleshooting questions. 
  3. If everything looks as expected, set the `spec.enable` field to `true` in the `ClusterGroupUpgrade` CR. 

Warning

After you set the `spec.enable` field to `true` in the `ClusterUpgradeGroup` CR, the update procedure starts and you cannot edit the CR’s `spec` fields anymore. 




**Additional resources**

  * [OpenShift Container Platform Troubleshooting Operator Issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#troubleshooting-operator-issues)
  * [Updating managed policies with Topology Aware Lifecycle Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygentemplate-resources#ztp-topology-aware-lifecycle-manager "11.3. Updating managed clusters in a disconnected environment with PolicyGenTemplate resources and TALM")
  * [About the PolicyGenerator CRD](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/managing-cluster-policies-with-policygenerator-resources#ztp-the-policygentemplate_ztp-configuring-managed-clusters-policygenerator "10.1.2. About the PolicyGenerator CRD")
