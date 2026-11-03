# 4.3. Configuring the Kernel Module Management Operator

To adapt the Kernel Module Management (KMM) Operator to your OpenShift Container Platform environment, you can create a `ConfigMap` with custom settings and restart the controller. 

**Procedure**

  * To modify any setting, create a `ConfigMap` with the name `kmm-operator-manager-config` in the Operator namespace with the relevant data and restart the controller using the following command: 

```shell-session
$ oc rollout restart -n "$namespace" deployment/kmm-operator-controller
```


The value of `$namespace` depends on your installation method. For example: 

```yaml
apiVersion: v1
data:
  controller_config.yaml: |
    worker:
      firmwareHostPath: /example/different/firmware/path
kind: ConfigMap
metadata:
  name: kmm-operator-manager-config
  namespace: openshift-kmm
```


Note

If you want to configure `KMM Hub`, create the `ConfigMap` using the name `kmm-operator-hub-manager-config` in the KMM Hub controller’s namespace. 

Table 4.1. Operator configuration parametersParameter| Description  
---|---  
`healthProbeBindAddress` |  Defines the address on which the Operator monitors for kubelet health probes. The recommended value is `:8081`.   
`job.gcDelay` |  Defines the duration for which successful build pods should be preserved before they are deleted. For information about the valid values for this setting, see [ParseDuration](https://pkg.go.dev/time#ParseDuration). The default value is `0s`.   
`leaderElection.enabled` |  Determines whether leader election is used to ensure that only one replica of the KMM Operator is running at any time. For more information, see [Leases](https://kubernetes.io/docs/concepts/architecture/leases/). The default value is `true`.   
`leaderElection.resourceID` |  Determines the name of the resource that leader election uses for holding the leader lock. The default value for KMM is `kmm.sigs.x-k8s.io`. The default value for KMM-hub is `kmm-hub.sigs.x-k8s.io`.   
`metrics.bindAddress` |  Determines the bind address for the metrics server. Set this to "0" to disable the metrics server. The default value is `0.0.0.0:8443`.   
`metrics.disableHTTP2` |  If `true`, disables HTTP/2 for the metrics server as a mitigation for [CVE-2023-44487](https://access.redhat.com/security/cve/cve-2023-44487). The default value is `true`.   
`metrics.enableAuthnAuthz` |  Determines if metrics are authenticated using `TokenReviews` and authorized using `SubjectAccessReviews` with the kube-apiserver.  For authentication and authorization, the controller needs a `ClusterRole` with the following rules: 
    * `apiGroups: authentication.k8s.io, resources: tokenreviews, verbs: create`
    * `apiGroups: authorization.k8s.io, resources: subjectaccessreviews, verbs: create`
To scrape metrics, for example, using Prometheus, the client needs a `ClusterRole` with the following rule: 
    * `nonResourceURLs: "/metrics", verbs: get`
The default value is `true`.   
`metrics.secureServing` |  Determines whether the metrics are served over HTTPS instead of HTTP. The default value is `true`.   
`webhook.disableHTTP2` |  If `true`, disables HTTP/2 for the webhook server, as a mitigation for [CVE-2023-44487](https://access.redhat.com/security/cve/cve-2023-44487). The default value is `true`.   
`webhook.port` |  Defines the port on which the Operator monitors webhook requests. The default value is `9443`.   
`worker.runAsUser` |  Determines the value of the `runAsUser` field of the worker container’s security context. For more information, see [SecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/). The default value is `9443`.   
`worker.seLinuxType` |  Determines the value of the `seLinuxOptions.type` field of the worker container’s security context. For more information, see [SecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/). The default value is `spc_t`.   
`worker.firmwareHostPath` |  If set, the value of this field is written by the worker container into the /sys/module/firmware_class/parameters/path file on the node. For more information see [Setting the kernel’s firmware search path](https://openshift-kmm.netlify.app/documentation/firmwares/#setting-the-kernels-firmware-search-path). The default value is `/var/lib/firmware`.   
Show more




**Additional resources**

  * [Installing the Kernel Module Management Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/kernel-module-management-operator#kmm-install_kernel-module-management-operator "4.2. Install the Kernel Module Management Operator")



## 4.3.1. Unloading the kernel module

To unload a kernel module deployed with KMM on OpenShift Container Platform, you can delete the corresponding `Module` resource. KMM creates worker pods that run `modprobe -r` on eligible nodes. 

You must unload the kernel modules when moving to a newer version or if they introduce some undesirable side effect on the node. 

**Procedure**

  * To unload a module loaded with KMM from nodes, delete the corresponding `Module` resource. KMM then creates worker pods, where required, to run `modprobe -r` and unload the kernel module from the nodes. 

Warning

When unloading worker pods, KMM needs all the resources it uses when loading the kernel module. This includes the `ServiceAccount` referenced in the `Module` as well as any RBAC defined to allow privileged KMM worker Pods to run. It also includes any pull secret referenced in `.spec.imageRepoSecret`. 

To avoid situations where KMM is unable to unload the kernel module from nodes, make sure those resources are not deleted while the `Module` resource is still present in the cluster in any state, including `Terminating`. KMM includes a validating admission webhook that rejects the deletion of namespaces that contain at least one `Module` resource. 




## 4.3.2. Setting the kernel firmware search path

To configure where KMM worker pods search for firmware on OpenShift Container Platform nodes, you can set the `worker.setFirmwareClassPath` parameter in the Operator configuration. 

The Linux kernel accepts the `firmware_class.path` parameter as a search path for firmware, as explained in [Firmware search paths](https://www.kernel.org/doc/html/latest/driver-api/firmware/fw_search_path.html). 

**Procedure**

  * To define a firmware search path, set `worker.setFirmwareClassPath` to `/var/lib/firmware` in the Operator configuration. 



**Additional resources**

  * [Configuring the Kernel Module Management Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/kernel-module-management-operator#kmm-configuring-kmmo_kernel-module-management-operator "4.3. Configuring the Kernel Module Management Operator")
