# 17.1. Verify the default seccomp profile applied to a pod

OpenShift Container Platform ships with a default seccomp profile that is referenced as `runtime/default`. In 4.22, newly created pods have the Security Context Constraint (SCC) set to `restricted-v2` and the default seccomp profile applies to the pod. 

**Procedure**

  1. You can verify the Security Context Constraint (SCC) and the default seccomp profile set on a pod by running the following commands: 

     1. Verify what pods are running in the namespace: 

```shell-session
$ oc get pods -n <namespace>
```


For example, to verify what pods are running in the `workshop` namespace run the following: 

```shell-session
$ oc get pods -n workshop
```


**Example output**

```shell-session
NAME                READY   STATUS      RESTARTS   AGE
parksmap-1-4xkwf    1/1     Running     0          2m17s
parksmap-1-deploy   0/1     Completed   0          2m22s
```


     2. Inspect the pods: 

```shell-session
$ oc get pod parksmap-1-4xkwf -n workshop -o yaml
```


**Example output**

```shell-session
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "ovn-kubernetes",
          "interface": "eth0",
          "ips": [
              "10.131.0.18"
          ],
          "default": true,
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "ovn-kubernetes",
          "interface": "eth0",
          "ips": [
              "10.131.0.18"
          ],
          "default": true,
          "dns": {}
      }]
    openshift.io/deployment-config.latest-version: "1"
    openshift.io/deployment-config.name: parksmap
    openshift.io/deployment.name: parksmap-1
    openshift.io/generated-by: OpenShiftWebConsole
    openshift.io/scc: restricted-v2
    seccomp.security.alpha.kubernetes.io/pod: runtime/default
```


where: 

`restricted-v2`
     Specifies the SCC that is added by default if your workload does not have access to a different SCC. 
`runtime/default`
     Specifies that newly created pods in 4.22 have the seccomp profile configured to `runtime/default` as mandated by the SCC. 




## 17.1.1. Upgraded cluster

In clusters upgraded to 4.22, all authenticated users have access to the `restricted` and `restricted-v2` SCC. 

A workload admitted by the SCC `restricted` for example, on a OpenShift Container Platform v4.10 cluster when upgraded may get admitted by `restricted-v2`. This is because `restricted-v2` is the more restrictive SCC between `restricted` and `restricted-v2`. 

Note

The workload must be able to run with `retricted-v2`. 

Conversely with a workload that requires `privilegeEscalation: true` this workload will continue to have the `restricted` SCC available for any authenticated user. This is because `restricted-v2` does not allow `privilegeEscalation`. 

## 17.1.2. Newly installed cluster

For newly installed OpenShift Container Platform 4.11 or later clusters, the `restricted-v2` replaces the `restricted` SCC as an SCC that is available to be used by any authenticated user. A workload with `privilegeEscalation: true`, is not admitted into the cluster since `restricted-v2` is the only SCC available for authenticated users by default. 

The feature `privilegeEscalation` is allowed by `restricted` but not by `restricted-v2`. More features are denied by `restricted-v2` than were allowed by `restricted` SCC. 

A workload with `privilegeEscalation: true` may be admitted into a newly installed OpenShift Container Platform 4.11 or later cluster. To give access to the `restricted` SCC to the ServiceAccount running the workload (or any other SCC that can admit this workload) using a RoleBinding run the following command: 

```shell-session
$ oc -n <workload-namespace> adm policy add-scc-to-user <scc-name> -z <serviceaccount_name>
```


In OpenShift Container Platform 4.22 the ability to add the pod annotations `seccomp.security.alpha.kubernetes.io/pod: runtime/default` and `container.seccomp.security.alpha.kubernetes.io/<container_name>: runtime/default` is deprecated.
