# 18.2. About pod security admission synchronization

Pod security admission `warn` and `audit` labels are automatically synchronized on your namespaces. This synchronization maps security context constraints to pod security profiles based on the service account permissions in each namespace. 

The controller examines `ServiceAccount` object permissions to use security context constraints in each namespace. Security context constraints (SCCs) are mapped to pod security profiles based on their field values; the controller uses these translated profiles. Pod security admission `warn` and `audit` labels are set to the most privileged pod security profile in the namespace to prevent displaying warnings and logging audit events when pods are created. 

Namespace labeling is based on consideration of namespace-local service account privileges. 

Applying pods directly might use the SCC privileges of the user who runs the pod. However, user privileges are not considered during automatic labeling. 

## 18.2.1. Pod security admission synchronization namespace exclusions

If you use pod security admission synchronization, the system-created namespaces are permanently disabled from synchronization. 

User-created `openshift-*` prefixed namespaces are also initially disabled, but you can enable synchronization on them later. 

Important

If a pod security admission label (`pod-security.kubernetes.io/<mode>`) is manually modified from the automatically labeled value on a label-synchronized namespace, synchronization is disabled for that label. 

If necessary, you can enable synchronization again by using one of the following methods: 

  * By removing the modified pod security admission label from the namespace 
  * By setting the `security.openshift.io/scc.podSecurityLabelSync` label to `true`

If you force synchronization by adding this label, then any modified pod security admission labels will be overwritten. 




### 18.2.1.1. Permanently disabled namespaces

Namespaces that are defined as part of the cluster payload have pod security admission synchronization disabled permanently. The following namespaces are permanently disabled: 

  * `default`
  * `kube-node-lease`
  * `kube-system`
  * `kube-public`
  * `openshift`
  * All system-created namespaces that are prefixed with `openshift-` , except for `openshift-operators`



### 18.2.1.2. Initially disabled namespaces

By default, all namespaces that have an `openshift-` prefix have pod security admission synchronization disabled initially. You can enable synchronization for user-created `openshift-*` namespaces and for the `openshift-operators` namespace. 

Note

You cannot enable synchronization for any system-created `openshift-*` namespaces, except for `openshift-operators`. 

If an Operator is installed in a user-created `openshift-*` namespace, synchronization is enabled automatically after a cluster service version (CSV) is created in the namespace. The synchronized label is derived from the permissions of the service accounts in the namespace.
