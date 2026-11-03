# 3.5. Enable the cluster capabilities by setting additional enabled capabilities

As a cluster administrator, you can enable cluster capabilities any time after a OpenShift Container Platform installation by setting the `additionalEnabledCapabilities` configuration parameter. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. View the additional enabled capabilities by running the following command: 

```shell-session
$ oc get clusterversion version -o jsonpath='{.spec.capabilities.additionalEnabledCapabilities}{"\n"}'
```


**Example output**

```shell-session
["openshift-samples"]
```


  2. To set the `additionalEnabledCapabilities` configuration parameter, run the following command: 

```shell-session
$ oc patch clusterversion/version --type merge -p '{"spec":{"capabilities":{"additionalEnabledCapabilities":["openshift-samples", "marketplace"]}}}'
```


Important

You cannot disable a capability that is already enabled in a cluster. The cluster version Operator (CVO) continues to reconcile the capability which is already enabled in the cluster. 

If you try to disable a capability, then CVO shows the divergent spec: 

```shell-session
$ oc get clusterversion version -o jsonpath='{.status.conditions[?(@.type=="ImplicitlyEnabledCapabilities")]}{"\n"}'
```


**Example output**

```shell-session
{"lastTransitionTime":"2022-07-22T03:14:35Z","message":"The following capabilities could not be disabled: openshift-samples","reason":"CapabilitiesImplicitlyEnabled","status":"True","type":"ImplicitlyEnabledCapabilities"}
```


Note

During the cluster upgrades, it is possible that a given capability could be implicitly enabled. If a resource was already running on the cluster before the upgrade, then any capabilities that is part of the resource will be enabled. For example, during a cluster upgrade, a resource that is already running on the cluster has been changed to be part of the `marketplace` capability by the system. Even if a cluster administrator does not explicitly enabled the `marketplace` capability, it is implicitly enabled by the system.
