# 17.1. About security context constraints

You can use security context constraints (SCCs) to control permissions for pods by defining what actions a pod can perform, what resources it can access, and what conditions it must meet to be accepted into the system. 

Security context constraints allow an administrator to control: 

  * Whether a pod can run privileged containers with the `allowPrivilegedContainer` flag 
  * Whether a pod is constrained with the `allowPrivilegeEscalation` flag 
  * The capabilities that a container can request 
  * The use of host directories as volumes 
  * The SELinux context of the container 
  * The container user ID 
  * The use of host namespaces and networking 
  * The allocation of an `FSGroup` that owns the pod volumes 
  * The configuration of allowable supplemental groups 
  * Whether a container requires write access to its root file system 
  * The usage of volume types 
  * The configuration of allowable `seccomp` profiles 



Important

Do not set the `openshift.io/run-level` label on any namespaces in OpenShift Container Platform. This label is for use by internal OpenShift Container Platform components to manage the startup of major API groups, such as the Kubernetes API server and OpenShift API server. If the `openshift.io/run-level` label is set, no SCCs are applied to pods in that namespace, causing any workloads running in that namespace to be highly privileged. 

## 17.1.1. Default security context constraints

The cluster contains several default security context constraints (SCCs) as described in the table below. Additional SCCs might be installed when you install Operators or other components to OpenShift Container Platform. 

Important

Do not modify the default SCCs. Customizing the default SCCs can lead to issues when some of the platform pods deploy or OpenShift Container Platform is upgraded. Additionally, the default SCC values are reset to the defaults during some cluster upgrades, which discards all customizations to those SCCs. 

Instead of modifying the default SCCs, create and modify your own SCCs as needed. For detailed steps, see _Creating security context constraints_. 

The following table describes the default SCCs that are available in OpenShift Container Platform. 

Security context constraint| Description  
---|---  
`anyuid` |  Provides all features of the `restricted` SCC, but allows users to run with any UID and any GID.   
`hostaccess` |  Allows access to all host namespaces but still requires pods to be run with a UID and SELinux context that are allocated to the namespace.  Warning This SCC allows host access to namespaces, file systems, and PIDs. It should only be used by trusted pods. Grant with caution.   
`hostmount-anyuid` |  Provides all the features of the `restricted` SCC, but allows host mounts and running as any UID and any GID on the system.  Warning This SCC allows host file system access as any UID, including UID 0. Grant with caution.   
`hostnetwork` |  Allows using host networking and host ports but still requires pods to be run with a UID and SELinux context that are allocated to the namespace.  Warning If additional workloads are run on control plane hosts, use caution when providing access to `hostnetwork`. A workload that runs `hostnetwork` on a control plane host is effectively root on the cluster and must be trusted accordingly.   
`hostnetwork-v2` |  Like the `hostnetwork` SCC, but with the following differences: 

  * `ALL` capabilities are dropped from containers. 
  * The `NET_BIND_SERVICE` capability can be added explicitly. 
  * `seccompProfile` is set to `runtime/default` by default. 
  * `allowPrivilegeEscalation` must be unset or set to `false` in security contexts. 

  
`nested-container` |  Like the `restricted-v2` SCC, but with the following differences: 

  * `seLinuxContext` is set to `MustRunAs` and `seLinuxOptions.type` is `container_engine_t`. 
  * `runAsUser` is set to `MustRunAsRange`. 
  * `requiredDropCapabilities` is set to `null`. 
  * `userNamespaceLevel` is set to `RequirePodLevel`, which forces pods to be in a Linux user namespace (`hostUsers: false`). 

This SCC allows a user to run a container engine inside of an OpenShift Container Platform pod.   
`node-exporter` |  Used for the Prometheus node exporter.  Warning This SCC allows host file system access as any UID, including UID 0. Grant with caution.   
`nonroot` |  Provides all features of the `restricted` SCC, but allows users to run with any non-root UID. The user must specify the UID or it must be specified in the manifest of the container runtime.   
`nonroot-v2` |  Like the `nonroot` SCC, but with the following differences: 

  * `ALL` capabilities are dropped from containers. 
  * The `NET_BIND_SERVICE` capability can be added explicitly. 
  * `seccompProfile` is set to `runtime/default` by default. 
  * `allowPrivilegeEscalation` must be unset or set to `false` in security contexts. 

  
`privileged` |  Allows access to all privileged and host features and the ability to run as any user, any group, any FSGroup, and with any SELinux context.  Warning This is the most relaxed SCC and should be used only for cluster administration. Grant with caution.  The `privileged` SCC allows: 

  * Users to run privileged pods 
  * Pods to mount host directories as volumes 
  * Pods to run as any user 
  * Pods to run with any MCS label 
  * Pods to use the host’s IPC namespace 
  * Pods to use the host’s PID namespace 
  * Pods to use any FSGroup 
  * Pods to use any supplemental group 
  * Pods to use any seccomp profiles 
  * Pods to request any capabilities 

Note Setting `privileged: true` in the pod specification does not necessarily select the `privileged` SCC. The SCC that has `allowPrivilegedContainer: true` and has the highest prioritization will be chosen if the user has the permissions to use it.   
`restricted` |  Denies access to all host features and requires pods to be run with a UID, and SELinux context that are allocated to the namespace.  The `restricted` SCC: 

  * Ensures that pods cannot run as privileged 
  * Ensures that pods cannot mount host directory volumes 
  * Requires that a pod is run as a user in a pre-allocated range of UIDs 
  * Requires that a pod is run with a pre-allocated MCS label 
  * Requires that a pod is run with a preallocated FSGroup 
  * Allows pods to use any supplemental group 

In clusters that were upgraded from OpenShift Container Platform 4.10 or earlier, this SCC is available for use by any authenticated user. The `restricted` SCC is no longer available to users of new OpenShift Container Platform 4.11 or later installations, unless the access is explicitly granted.   
`restricted-v2` |  Like the `restricted` SCC, but with the following differences: 

  * `ALL` capabilities are dropped from containers. 
  * The `NET_BIND_SERVICE` capability can be added explicitly. 
  * `seccompProfile` is set to `runtime/default` by default. 
  * `allowPrivilegeEscalation` must be unset or set to `false` in security contexts. 

This SCC is used by default for authenticated users.   
`restricted-v3` |  Like the `restricted-v2` SCC, but with the following differences: 

  * `UserNamespaceLevel` is set to `RequirePodLevel`, which forces pods to be in a Linux user namespace (`hostUsers: false`). 

This is the most restrictive SCC provided by a new installation and will be used by default for authenticated users.  Note The `restricted-v3` SCC is the most restrictive of the SCCs that is included by default with the system. However, you can create a custom SCC that is even more restrictive. For example, you can create an SCC that restricts `readOnlyRootFilesystem` to `true`.   
Show more

## 17.1.2. Security context constraints settings

Security context constraints (SCCs) are composed of settings and strategies that control the security features a pod has access to. These settings fall into three categories: 

Category| Description  
---|---  
Controlled by a boolean  |  Fields of this type default to the most restrictive value. For example, `AllowPrivilegedContainer` is always set to `false` if unspecified.   
Controlled by an allowable set  |  Fields of this type are checked against the set to ensure their value is allowed.   
Controlled by a strategy  |  Items that have a strategy to generate a value provide: 

  * A mechanism to generate the value, and 
  * A mechanism to ensure that a specified value falls into the set of allowable values. 

  
Show more

CRI-O has the following default list of capabilities that are allowed for each container of a pod: 

  * `CHOWN`
  * `DAC_OVERRIDE`
  * `FSETID`
  * `FOWNER`
  * `SETGID`
  * `SETUID`
  * `SETPCAP`
  * `NET_BIND_SERVICE`
  * `KILL`



The containers use the capabilities from this default list, but pod manifest authors can alter the list by requesting additional capabilities or removing some of the default behaviors. Use the `allowedCapabilities`, `defaultAddCapabilities`, and `requiredDropCapabilities` parameters to control such requests from the pods. With these parameters you can specify which capabilities can be requested, which ones must be added to each container, and which ones must be forbidden, or dropped, from each container. 

Note

You can drop all capabilites from containers by setting the `requiredDropCapabilities` parameter to `ALL`. This is what the `restricted-v2` SCC does. 

## 17.1.3. Security context constraints strategies

The following example shows the strategies that are available for the `RunAsUser` field. 

  * `MustRunAs` \- Requires a `runAsUser` to be configured. Uses the configured `runAsUser` as the default. Validates against the configured `runAsUser`. 

**Example`MustRunAs` snippet**

```yaml
...
runAsUser:
  type: MustRunAs
  uid: <id>
...
```


  * `MustRunAsRange` \- Requires minimum and maximum values to be defined if not using pre-allocated values. Uses the minimum as the default. Validates against the entire allowable range. 

**Example`MustRunAsRange` snippet**

```yaml
...
runAsUser:
  type: MustRunAsRange
  uidRangeMax: <maxvalue>
  uidRangeMin: <minvalue>
...
```


  * `MustRunAsNonRoot` \- Requires that the pod be submitted with a non-zero `runAsUser` or have the `USER` directive defined in the image. No default provided. 

**Example`MustRunAsNonRoot` snippet**

```yaml
...
runAsUser:
  type: MustRunAsNonRoot
...
```


  * `RunAsAny` \- No default provided. Allows any `runAsUser` to be specified. 

**Example`RunAsAny` snippet**

```yaml
...
runAsUser:
  type: RunAsAny
...
```


The following example shows the strategies that are available for the `seLinuxOptions` field. 

  * `MustRunAs` \- Requires `seLinuxOptions` to be configured if not using pre-allocated values. Uses `seLinuxOptions` as the default. Validates against `seLinuxOptions`. 
  * `RunAsAny` \- No default provided. Allows any `seLinuxOptions` to be specified. 



The following example shows the strategies that are available for the `supplementalGroups` field. 

  * `MustRunAs` \- Requires at least one range to be specified if not using pre-allocated values. Uses the minimum value of the first range as the default. Validates against all ranges. 
  * `RunAsAny` \- No default provided. Allows any `supplementalGroups` to be specified. 



The following example shows the strategies that are available for the `fsGroup` field. 

  * `MustRunAs` \- Requires at least one range to be specified if not using pre-allocated values. Uses the minimum value of the first range as the default. Validates against the first ID in the first range. 
  * `RunAsAny` \- No default provided. Allows any `fsGroup` ID to be specified. 



## 17.1.4. Controlling volumes

The usage of specific volume types can be controlled by setting the `volumes` field of the SCC. 

The allowable values of this field correspond to the volume sources that are defined when creating a volume: 

  * [`awsElasticBlockStore`](https://kubernetes.io/docs/concepts/storage/volumes/#awselasticblockstore)
  * [`azureDisk`](https://kubernetes.io/docs/concepts/storage/volumes/#azuredisk)
  * [`azureFile`](https://kubernetes.io/docs/concepts/storage/volumes/#azurefile)
  * [`cephFS`](https://kubernetes.io/docs/concepts/storage/volumes/#cephfs)
  * [`cinder`](https://kubernetes.io/docs/concepts/storage/volumes/#cinder)
  * [`configMap`](https://kubernetes.io/docs/concepts/storage/volumes/#configmap)
  * [`csi`](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes)
  * [`downwardAPI`](https://kubernetes.io/docs/concepts/storage/volumes/#downwardapi)
  * [`emptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir)
  * [`fc`](https://kubernetes.io/docs/concepts/storage/volumes/#fc)
  * [`flexVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#flexvolume)
  * [`flocker`](https://kubernetes.io/docs/concepts/storage/volumes/#flocker)
  * [`gcePersistentDisk`](https://kubernetes.io/docs/concepts/storage/volumes/#gcepersistentdisk)
  * [`ephemeral`](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes)
  * [`gitRepo`](https://kubernetes.io/docs/concepts/storage/volumes/#gitrepo)
  * [`glusterfs`](https://kubernetes.io/docs/concepts/storage/volumes/#glusterfs)
  * [`hostPath`](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath)
  * [`iscsi`](https://kubernetes.io/docs/concepts/storage/volumes/#iscsi)
  * [`nfs`](https://kubernetes.io/docs/concepts/storage/volumes/#nfs)
  * [`persistentVolumeClaim`](https://kubernetes.io/docs/concepts/storage/volumes/#persistentvolumeclaim)
  * `photonPersistentDisk`
  * [`portworxVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#portworxvolume)
  * [`projected`](https://kubernetes.io/docs/concepts/storage/volumes/#projected)
  * [`quobyte`](https://kubernetes.io/docs/concepts/storage/volumes/#quobyte)
  * [`rbd`](https://kubernetes.io/docs/concepts/storage/volumes/#rbd)
  * [`scaleIO`](https://kubernetes.io/docs/concepts/storage/volumes/#scaleio)
  * [`secret`](https://kubernetes.io/docs/concepts/storage/volumes/#secret)
  * [`storageos`](https://kubernetes.io/docs/concepts/storage/volumes/#storageos)
  * [`vsphereVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#vspherevolume)
  * ***** (A special value to allow the use of all volume types.) 
  * `none` (A special value to disallow the use of all volumes types. Exists only for backwards compatibility.) 



The recommended minimum set of allowed volumes for new SCCs are `configMap`, `downwardAPI`, `emptyDir`, `persistentVolumeClaim`, `secret`, and `projected`. 

Note

This list of allowable volume types is not exhaustive because new types are added with each release of OpenShift Container Platform. 

Note

For backwards compatibility, the usage of `allowHostDirVolumePlugin` overrides settings in the `volumes` field. For example, if `allowHostDirVolumePlugin` is set to false but allowed in the `volumes` field, then the `hostPath` value will be removed from `volumes`. 

## 17.1.5. Admission control

_Admission control_ with SCCs allows for control over the creation of resources based on the capabilities granted to a user. 

In terms of the SCCs, this means that an admission controller can inspect the user information made available in the context to retrieve an appropriate set of SCCs. Doing so ensures the pod is authorized to make requests about its operating environment or to generate a set of constraints to apply to the pod. 

The set of SCCs that admission uses to authorize a pod are determined by the user identity and groups that the user belongs to. Additionally, if the pod specifies a service account, the set of allowable SCCs includes any constraints accessible to the service account. 

Note

When you create a workload resource, such as deployment, only the service account is used to find the SCCs and admit the pods when they are created. 

Admission uses the following approach to create the final security context for the pod: 

  1. Retrieve all SCCs available for use. 
  2. Generate field values for security context settings that were not specified on the request. 
  3. Validate the final settings against the available constraints. 



If a matching set of constraints is found, then the pod is accepted. If the request cannot be matched to an SCC, the pod is rejected. 

A pod must validate every field against the SCC. The following are examples for just two of the fields that must be validated: 

Note

These examples are in the context of a strategy using the pre-allocated values. 

**An FSGroup SCC strategy of`MustRunAs`**

If the pod defines a `fsGroup` ID, then that ID must equal the default `fsGroup` ID. Otherwise, the pod is not validated by that SCC and the next SCC is evaluated. 

If the `SecurityContextConstraints.fsGroup` field has value `RunAsAny` and the pod specification omits the `Pod.spec.securityContext.fsGroup`, then this field is considered valid. Note that it is possible that during validation, other SCC settings will reject other pod fields and thus cause the pod to fail. 

**A`SupplementalGroups` SCC strategy of `MustRunAs`**

If the pod specification defines one or more `supplementalGroups` IDs, then the pod’s IDs must equal one of the IDs in the namespace’s `openshift.io/sa.scc.supplemental-groups` annotation. Otherwise, the pod is not validated by that SCC and the next SCC is evaluated. 

If the `SecurityContextConstraints.supplementalGroups` field has value `RunAsAny` and the pod specification omits the `Pod.spec.securityContext.supplementalGroups`, then this field is considered valid. Note that it is possible that during validation, other SCC settings will reject other pod fields and thus cause the pod to fail. 

## 17.1.6. Security context constraints prioritization

Security context constraints (SCCs) have a priority field that affects the ordering when attempting to validate a request by the admission controller. 

Warning

Setting an SCC priority greater than 0 for the default OpenShift Container Platform SCCs can cause critical cluster instability. 

A priority value of `0` is the lowest possible priority. A nil priority is considered a `0`, or lowest, priority. Higher priority SCCs are moved to the front of the set when sorting. 

When the complete set of available SCCs is determined, the SCCs are ordered in the following manner: 

  1. The highest priority SCCs are ordered first. 
  2. If the priorities are equal, the SCCs are sorted from most restrictive to least restrictive. 
  3. If both the priorities and restrictions are equal, the SCCs are sorted by name. 



By default, the `anyuid` SCC granted to cluster administrators is given priority in their SCC set. This allows cluster administrators to run pods as any user by specifying `RunAsUser` in the pod’s `SecurityContext`.
