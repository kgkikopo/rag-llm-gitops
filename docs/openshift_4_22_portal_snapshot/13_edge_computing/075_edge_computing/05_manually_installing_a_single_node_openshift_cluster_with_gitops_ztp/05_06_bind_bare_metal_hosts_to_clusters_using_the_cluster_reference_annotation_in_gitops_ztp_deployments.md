# 5.6. Bind bare-metal hosts to clusters using the cluster-reference annotation in GitOps ZTP deployments

In GitOps ZTP deployments, you can declaratively bind individual `BareMetalHost` resources from a shared `InfraEnv` pool to specific `ClusterDeployment` CRs by using the `bmac.agent-install.openshift.io/cluster-reference` annotation. 

This approach is compatible with GitOps workflows because the binding is managed through annotations on the `BareMetalHost` resource rather than by patching `Agent` CRs directly. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have created an `InfraEnv` CR without a `clusterRef` field. If you use the SiteConfig Operator, verify that the generated `InfraEnv` does not include a `clusterRef` field. 
  * You have `BareMetalHost` resources that reference the shared `InfraEnv`. These resources are either generated automatically by the SiteConfig Operator from a `ClusterInstance` CR, or created manually with the `infraenvs.agent-install.openshift.io` label set to the name of the `InfraEnv` CR. 
  * You have booted the hosts from the discovery ISO and `Agent` CRs have been created automatically for the discovered hosts. 
  * You have created the target `ClusterDeployment` and `AgentClusterInstall` CRs for the cluster that you want to bind hosts to. 



**Procedure**

  1. Verify that the `InfraEnv` CR does not have a `clusterRef` field set: 

```shell-session
$ oc get infraenv <infraenv_name> -n <namespace> -o jsonpath='{.spec.clusterRef}'
```


If the command returns an empty result, the `InfraEnv` is configured for late binding. If a `clusterRef` value is returned, the `BareMetalHost` cluster-reference annotation is ignored and you must use the standard binding flow. 

  2. Verify that the `Agent` CRs exist and are not bound to a cluster: 

```shell-session
$ oc get agents -n <namespace>
```


**Example output**

```shell-session
NAME                                   CLUSTER   APPROVED   ROLE          STAGE
aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb             false      auto-assign
cccccccc-4444-5555-6666-dddddddddddd             false      auto-assign
```


Agents that are not bound to a cluster have an empty `CLUSTER` column. 

  3. Add the `bmac.agent-install.openshift.io/cluster-reference` annotation to the `BareMetalHost` resource to bind it to the target `ClusterDeployment` CR: 

```shell-session
$ oc annotate bmh <bmh_name> -n <namespace> \
    bmac.agent-install.openshift.io/cluster-reference=<cluster_namespace>/<cluster_name>
```


Replace `<cluster_namespace>/<cluster_name>` with the namespace and name of the target `ClusterDeployment` CR. 

Alternatively, you can set the annotation declaratively in the `BareMetalHost` YAML manifest: 

```yaml
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: worker-01
  namespace: my-infraenv-ns
  annotations:
    bmac.agent-install.openshift.io/cluster-reference: my-cluster-ns/my-cluster
  labels:
    infraenvs.agent-install.openshift.io: my-infraenv
spec:
  online: true
  bootMACAddress: 00:00:5E:00:53:01
  bmc:
    address: redfish-virtualmedia://192.0.2.10/redfish/v1/Systems/1
    credentialsName: worker-01-bmc-secret
```


The `bmac.agent-install.openshift.io/cluster-reference` annotation value uses the format `<namespace>/<name>`, referencing the target `ClusterDeployment`. 

  4. Verify that the `Agent` CR is bound to the correct `ClusterDeployment` CR by running the following command: 

```shell-session
$ oc get agents -n <namespace>
```


**Example output**

```shell-session
NAME                                   CLUSTER      APPROVED   ROLE          STAGE
aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb   my-cluster   false      auto-assign
```


The `CLUSTER` column shows the name of the target `ClusterDeployment`. 

  5. Verify the `Bound` condition on the `Agent` CR: 

```shell-session
$ oc get agent <agent_name> -n <namespace> \
    -o jsonpath='{.status.conditions[?(@.type=="Bound")]}'
```


A successfully bound agent shows `status: "True"` and `reason: "Bound"` in the output. 

Note

Agents discovered by using a `BareMetalHost` resource are automatically approved for installation when the `bootMACAddress` in the `BareMetalHost` matches a NIC in the inventory of the discovered host. You do not need to manually approve these agents. 

  6. Optional: To unbind a host from a cluster before installation starts, set the annotation value to an empty string: 

```shell-session
$ oc annotate bmh <bmh_name> -n <namespace> \
    bmac.agent-install.openshift.io/cluster-reference="" --overwrite
```


The bare metal agent controller (BMAC) clears the `spec.clusterDeploymentName` field on the corresponding `Agent` CR, and the host returns to the unbound pool. 

Important

You cannot unbind a host after cluster installation has started. If you try to unbind a host that is already installed or in an `error` or `canceled` state, the `Agent` CR `Bound` condition is set to `False` with the reason `UnbindingPendingUserAction`. For hosts discovered by using a `BareMetalHost` resource, the assisted controllers automatically use the `BareMetalHost` to boot the host back into the discovery ISO to complete the unbinding process. For hosts discovered without a `BareMetalHost` resource, you must manually reboot the host with the discovery ISO. 




**Verification**

  * Verify that all agents are approved and bound to the correct cluster: 

```shell-session
$ oc get agents -n <namespace> -o custom-columns=NAME:.metadata.name,CLUSTER:.spec.clusterDeploymentName.name,APPROVED:.spec.approved
```


**Additional resources**

  * [Late binding for bare-metal host pools in GitOps ZTP deployments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-manual-install#ztp-late-binding-bare-metal-host-pools_ztp-manual-install "5.5. Late binding for bare-metal host pools in GitOps ZTP deployments")
  * [`BareMetalHost` cluster-reference annotation reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-manual-install#ztp-bmh-cluster-reference-annotation-ref_ztp-manual-install "5.7. BareMetalHost cluster-reference annotation")
  * [Binding and unbinding hosts in the RHACM documentation](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16/html/clusters/cluster_mce_overview#binding-and-unbinding-hosts)
