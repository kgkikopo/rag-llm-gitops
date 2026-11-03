# 4.6. Security and permissions

KMM security and permissions govern how privileged workloads load kernel modules on OpenShift Container Platform nodes. Review `ServiceAccount`, `SecurityContextConstraint`, and pod security requirements before deploying `Module` resources. 

Important

Loading kernel modules is a highly sensitive operation. After they are loaded, kernel modules have all possible permissions to do any kind of operation on the node. 

## 4.6.1. ServiceAccounts and SecurityContextConstraints

Kernel Module Management (KMM) creates a privileged workload to load the kernel modules on nodes. That workload needs `ServiceAccounts` allowed to use the `privileged` `SecurityContextConstraint` (SCC) resource. 

The authorization model for that workload depends on the namespace of the `Module` resource, as well as its spec. 

  * If the `.spec.moduleLoader.serviceAccountName` or `.spec.devicePlugin.serviceAccountName` fields are set, they are always used. 
  * If those fields are not set, then: 

    * If the `Module` resource is created in the Operator’s namespace (`openshift-kmm` by default), then KMM uses its default, powerful `ServiceAccounts` to run the worker and device plugin pods. 
    * If the `Module` resource is created in any other namespace, then KMM runs the pods with the namespace’s `default` `ServiceAccount`. The `Module` resource cannot run a privileged workload unless you manually enable it to use the `privileged` SCC. 




Important

`openshift-kmm` is a trusted namespace. 

When setting up RBAC permissions, remember that any user or `ServiceAccount` creating a `Module` resource in the `openshift-kmm` namespace results in KMM automatically running privileged workloads on potentially all nodes in the cluster. 

To allow any `ServiceAccount` to use the `privileged` SCC and run worker or device plugin pods, you can use the `oc adm policy` command, as in the following example: 

```shell-session
$ oc adm policy add-scc-to-user privileged -z "${serviceAccountName}" [ -n "${namespace}" ]
```


## 4.6.2. Pod security standards

OpenShift runs a synchronization mechanism that sets the namespace Pod Security level automatically based on the security contexts in use. No action is needed. 

**Additional resources**

  * [Understanding and managing pod security admission](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-and-managing-pod-security-admission)
