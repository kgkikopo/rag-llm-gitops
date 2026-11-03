# 18.1. About pod security admission

You can use pod security admission modes, such as `enforce`, `warn`, or `audit`, along with security profiles to restrict which pods run in your cluster. You can apply this control at both the global and namespace levels. 

Globally, the `privileged` profile is enforced, and the `restricted` profile is used for warnings and audits. 

You can also configure the pod security admission settings at the namespace level. 

Important

Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components. 

The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects. 

## 18.1.1. Pod security admission modes

You can configure the following pod security admission modes for a namespace: 

Table 18.1. Pod security admission modesMode| Label| Description  
---|---|---  
`enforce` |  `pod-security.kubernetes.io/enforce` |  Rejects a pod from admission if it does not comply with the set profile   
`audit` |  `pod-security.kubernetes.io/audit` |  Logs audit events if a pod does not comply with the set profile   
`warn` |  `pod-security.kubernetes.io/warn` |  Displays warnings if a pod does not comply with the set profile   
Show more

## 18.1.2. Pod security admission profiles

You can set each of the pod security admission modes to one of the following profiles: 

Table 18.2. Pod security admission profilesProfile| Description  
---|---  
`privileged` |  Least restrictive policy; allows for known privilege escalation   
`baseline` |  Minimally restrictive policy; prevents known privilege escalations   
`restricted` |  Most restrictive policy; follows current pod hardening best practices   
Show more

## 18.1.3. Privileged namespaces

The following system namespaces are always set to the `privileged` pod security admission profile: 

  * `default`
  * `kube-public`
  * `kube-system`



You cannot change the pod security profile for these privileged namespaces. 

**Example privileged namespace configuration**

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/warn: privileged
  name: "<mig_namespace>"
# ...
```


## 18.1.4. Pod security admission and security context constraints

Pod security admission and security context constraints operate as two independent mechanisms in OpenShift Container Platform. You must ensure your workloads comply with both to avoid unexpected pod rejections. 

The two controllers independently enforce security policies by using the following processes: 

  1. The security context constraint controller may mutate some security context fields per the pod’s assigned SCC. For example, if the seccomp profile is empty or not set and if the pod’s assigned SCC enforces `seccompProfiles` field to be `runtime/default`, the controller sets the default type to `RuntimeDefault`. 
  2. The security context constraint controller validates the pod’s security context against the matching SCC. 
  3. The pod security admission controller validates the pod’s security context against the pod security standard assigned to the namespace.
