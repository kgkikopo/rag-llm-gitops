# 12.2. Syncing new ConfigMap changes to existing PolicyGenerator or PolicyGentemplate CRs

You can sync updated `ConfigMap` CR changes to existing `PolicyGenerator` or `PolicyGentemplate` CRs deployed on the hub cluster. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have created a `PolicyGenerator` or `PolicyGentemplate` CR that pulls information from a `ConfigMap` CR using hub cluster templates. 



**Procedure**

  1. Update the contents of your `ConfigMap` CR, and apply the changes in the hub cluster. 
  2. To sync the contents of the updated `ConfigMap` CR to the deployed policy, do either of the following: 

     1. Option 1: Delete the existing policy. ArgoCD uses the `PolicyGenerator` or `PolicyGentemplate` CR to immediately recreate the deleted policy. For example, run the following command: 

```shell-session
$ oc delete policy <policy_name> -n <policy_namespace>
```


     2. Option 2: Apply a special annotation `policy.open-cluster-management.io/trigger-update` to the policy with a different value every time when you update the `ConfigMap`. For example: 

```shell-session
$ oc annotate policy <policy_name> -n <policy_namespace> policy.open-cluster-management.io/trigger-update="1"
```


Note

You must apply the updated policy for the changes to take effect. For more information, see [Special annotation for reprocessing](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.6/html-single/governance/index#special-annotation-processing). 

  3. Optional: If it exists, delete the `ClusterGroupUpdate` CR that contains the policy. For example: 

```shell-session
$ oc delete clustergroupupgrade <cgu_name> -n <cgu_namespace>
```


     1. Create a new `ClusterGroupUpdate` CR that includes the policy to apply with the updated `ConfigMap` changes. For example, add the following YAML to the file `cgr-example.yaml`: 

```yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: <cgr_name>
  namespace: <policy_namespace>
spec:
  managedPolicies:
    - <managed_policy>
  enable: true
  clusters:
  - <managed_cluster_1>
  - <managed_cluster_2>
  remediationStrategy:
    maxConcurrency: 2
    timeout: 240
```


     2. Apply the updated policy: 

```shell-session
$ oc apply -f cgr-example.yaml
```
