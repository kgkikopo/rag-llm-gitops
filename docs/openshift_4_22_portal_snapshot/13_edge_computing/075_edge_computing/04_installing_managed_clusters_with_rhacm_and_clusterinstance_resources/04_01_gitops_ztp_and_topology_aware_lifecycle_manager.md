# 4.1. GitOps ZTP and Topology Aware Lifecycle Manager

GitOps Zero Touch Provisioning (ZTP) generates installation and configuration CRs from Git manifests and applies them to a hub cluster where Red Hat Advanced Cluster Management (RHACM), the assisted service, and the Topology Aware Lifecycle Manager (TALM) manage the cluster lifecycle. 

The configuration phase of the GitOps ZTP pipeline uses the TALM to orchestrate the application of configuration CRs to the cluster. 

Inform policies
     By default, GitOps ZTP creates all policies with a remediation action of `inform`. These policies cause RHACM to report on compliance status of clusters relevant to the policies but does not apply the desired configuration. During the GitOps ZTP process, after OpenShift installation, the TALM steps through the created `inform` policies and enforces them on the target managed cluster(s). This applies the configuration to the managed cluster. Outside of the GitOps ZTP phase of the cluster lifecycle, this allows you to change policies without the risk of immediately rolling those changes out to affected managed clusters. You can control the timing and the set of remediated clusters by using TALM. 
Automatic creation of ClusterGroupUpgrade CRs
    

To automate the initial configuration of newly deployed clusters, TALM monitors the state of all `ManagedCluster` CRs on the hub cluster. Any `ManagedCluster` CR that does not have a `ztp-done` label applied, including newly created `ManagedCluster` CRs, causes the TALM to automatically create a `ClusterGroupUpgrade` CR with the following characteristics: 

  * The `ClusterGroupUpgrade` CR is created and enabled in the `ztp-install` namespace. 
  * `ClusterGroupUpgrade` CR has the same name as the `ManagedCluster` CR. 
  * The cluster selector includes only the cluster associated with that `ManagedCluster` CR. 
  * The set of managed policies includes all policies that RHACM has bound to the cluster at the time the `ClusterGroupUpgrade` is created. 
  * Pre-caching is disabled. 
  * Timeout set to 4 hours (240 minutes). 



The automatic creation of an enabled `ClusterGroupUpgrade` ensures that initial zero-touch deployment of clusters proceeds without the need for user intervention. Additionally, the automatic creation of a `ClusterGroupUpgrade` CR for any `ManagedCluster` without the `ztp-done` label allows a failed GitOps ZTP installation to be restarted by simply deleting the `ClusterGroupUpgrade` CR for the cluster. 

Waves
    

Each policy generated from a `PolicyGenerator` or `PolicyGentemplate` CR includes a `ztp-deploy-wave` annotation. This annotation is based on the same annotation from each CR which is included in that policy. The wave annotation is used to order the policies in the auto-generated `ClusterGroupUpgrade` CR. The wave annotation is not used other than for the auto-generated `ClusterGroupUpgrade` CR. 

Note

All CRs in the same policy must have the same setting for the `ztp-deploy-wave` annotation. The default value of this annotation for each CR can be overridden in the `PolicyGenerator` or `PolicyGentemplate`. The wave annotation in the source CR is used for determining and setting the policy wave annotation. This annotation is removed from each built CR which is included in the generated policy at runtime. 

The TALM applies the configuration policies in the order specified by the wave annotations. The TALM waits for each policy to be compliant before moving to the next policy. It is important to ensure that the wave annotation for each CR takes into account any prerequisites for those CRs to be applied to the cluster. For example, an Operator must be installed before or concurrently with the configuration for the Operator. Similarly, the `CatalogSource` for an Operator must be installed in a wave before or concurrently with the Operator Subscription. The default wave value for each CR takes these prerequisites into account. 

Note

Multiple CRs and policies can share the same wave number. Having fewer policies can result in faster deployments and lower CPU usage. It is a best practice to group many CRs into relatively few waves. 

To check the default wave value in each source CR, run the following command against the `out/source-crs` directory that is extracted from the `ztp-site-generate` container image: 

```shell-session
$ grep -r "ztp-deploy-wave" out/source-crs
```


Phase labels
    

The `ClusterGroupUpgrade` CR is automatically created and includes directives to annotate the `ManagedCluster` CR with labels at the start and end of the GitOps ZTP process. 

When GitOps ZTP configuration postinstallation commences, the `ManagedCluster` has the `ztp-running` label applied. When all policies are remediated to the cluster and are fully compliant, these directives cause the TALM to remove the `ztp-running` label and apply the `ztp-done` label. 

For deployments that make use of the `informDuValidator` policy, the `ztp-done` label is applied when the cluster is fully ready for deployment of applications. This includes all reconciliation and resulting effects of the GitOps ZTP applied configuration CRs. The `ztp-done` label affects automatic `ClusterGroupUpgrade` CR creation by TALM. Do not manipulate this label after the initial GitOps ZTP installation of the cluster. 

Linked CRs
     The automatically created `ClusterGroupUpgrade` CR has the owner reference set as the `ManagedCluster` from which it was derived. This reference ensures that deleting the `ManagedCluster` CR causes the instance of the `ClusterGroupUpgrade` to be deleted along with any supporting resources.
