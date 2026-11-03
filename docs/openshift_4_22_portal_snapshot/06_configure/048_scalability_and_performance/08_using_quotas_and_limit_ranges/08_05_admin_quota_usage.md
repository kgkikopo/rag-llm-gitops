# 8.5. Admin quota usage

To ensure projects remain within defined constraints, monitor admin quota usage. After a resource quota for a project is first created, the project restricts the ability to create any new resources that can violate a quota constraint until it has calculated updated usage statistics. 

Quota enforcement
    

After a resource quota for a project is first created, the project restricts the ability to create any new resources that can violate a quota constraint until the quota has calculated updated usage statistics. 

After a quota is created and usage statistics are updated, the project accepts the creation of new content. When you create or modify resources, your quota usage is incremented immediately upon the request to create or modify the resource. 

When you delete a resource, your quota use is decremented during the next full recalculation of quota statistics for the project. 

A configurable amount of time determines how long the quota takes to reduce quota usage statistics to their current observed system value. 

If project modifications exceed a quota usage limit, the server denies the action and returns an appropriate error message to the user. The error message explains the quota constraint violated and what their currently observed usage statistics are in the system. 

Requests compared to limits
    

When allocating compute resources by quota, each container can specify a request and a limit value each for CPU, memory, and ephemeral storage. Quotas can restrict any of these values. 

If the quota has a value specified for `requests.cpu` or `requests.memory`, then the quota requires that every incoming container makes an explicit request for those resources. If the quota has a value specified for `limits.cpu` or `limits.memory`, the quota requires that every incoming container specify an explicit limit for those resources. 

## 8.5.1. Sample resource quota definitions

To properly structure your quota configurations, reference these sample `ResourceQuota` definitions. These YAML examples demonstrate how to specify hard limits for compute resources, storage, and object counts to ensure your project complies with cluster policies. 

**Example core-object-counts.yaml**

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: core-object-counts
spec:
  hard:
    configmaps: "10"
    persistentvolumeclaims: "4"
    replicationcontrollers: "20"
    secrets: "10"
    services: "10"
# ...
```


where: 

`configmaps`
     Specifies the total number of `ConfigMap` objects that can exist in the project. 
`persistentvolumeclaims`
     Specifies the total number of persistent volume claims (PVCs) that can exist in the project. 
`replicationcontrollers`
     Specifies the total number of replication controllers that can exist in the project. 
`secrets`
     Specifies the total number of secrets that can exist in the project. 
`services`
     Specifies the total number of services that can exist in the project. 

**Example openshift-object-counts.yaml**

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: openshift-object-counts
spec:
  hard:
    openshift.io/imagestreams: "10"
# ...
```


where: 

`openshift.io/imagestreams`
     Specifies the total number of image streams that can exist in the project. 

**Example compute-resources.yaml**

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    pods: "4"
    requests.cpu: "1"
    requests.memory: 1Gi
    requests.ephemeral-storage: 2Gi
    limits.cpu: "2"
    limits.memory: 2Gi
    limits.ephemeral-storage: 4Gi
# ...
```


where: 

`pods`
     Specifies the total number of pods in a non-terminal state that can exist in the project. 
`requests.cpu`
     Specifies that across all pods in a non-terminal state, the sum of CPU requests cannot exceed 1 core. 
`requests.memory`
     Specifies that across all pods in a non-terminal state, the sum of memory requests cannot exceed 1 Gi. 
`requests.ephemeral-storage`
     Specifies that across all pods in a non-terminal state, the sum of ephemeral storage requests cannot exceed 2 Gi. 
`limits.cpu`
     Specifies that across all pods in a non-terminal state, the sum of CPU limits cannot exceed 2 cores. 
`limits.memory`
     Specifies that across all pods in a non-terminal state, the sum of memory limits cannot exceed 2 Gi. 
`limits.ephemeral-storage`
     Specifies that across all pods in a non-terminal state, the sum of ephemeral storage limits cannot exceed 4 Gi. 

**Example besteffort.yaml**

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: besteffort
spec:
  hard:
    pods: "1"
  scopes:
  - BestEffort
# ...
```


where: 

`pods`
     Specifies the total number of pods in a non-terminal state with `BestEffort` quality of service that can exist in the project. 
`scopes`
     Specifies a restriction on the quota to only match pods that have `BestEffort` quality of service for either memory or CPU. 

**Example compute-resources-long-running.yaml**

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources-long-running
spec:
  hard:
    pods: "4"
    limits.cpu: "4"
    limits.memory: "2Gi"
    limits.ephemeral-storage: "4Gi"
  scopes:
  - NotTerminating
# ...
```


where: 

`pods`
     Specifies the total number of pods in a non-terminal state. 
`limits.cpu`
     Specifies that across all pods in a non-terminal state, the sum of CPU limits cannot exceed this value. 
`limits.memory`
     Specifies that across all pods in a non-terminal state, the sum of memory limits cannot exceed this value. 
`limits.ephemeral-storage`
     Specifies that across all pods in a non-terminal state, the sum of ephemeral storage limits cannot exceed this value. 
`scopes`
     Specifies a restriction on the quota that only matches pods where `spec.activeDeadlineSeconds` is set to `nil`. Build pods fall under `NotTerminating` unless the `RestartNever` policy is applied. 

**Example compute-resources-time-bound.yaml**

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources-time-bound
spec:
  hard:
    pods: "2"
    limits.cpu: "1"
    limits.memory: "1Gi"
    limits.ephemeral-storage: "1Gi"
  scopes:
  - Terminating
# ...
```


where: 

`pods`
     Specifies the total number of pods in a non-terminal state. 
`limits.cpu`
     Specifies that across all pods in a non-terminal state, the sum of CPU limits cannot exceed this value. 
`limits.memory`
     Specifies that across all pods in a non-terminal state, the sum of memory limits cannot exceed this value. 
`limits.ephemeral-storage`
     Specifies that across all pods in a non-terminal state, the sum of ephemeral storage limits cannot exceed this value. 
`scopes`
     Specifies a restriction on the quota that only matches pods where `spec.activeDeadlineSeconds>=0`. For example, this quota would charge for build pods, but not long running pods such as a web server or database. 

**Example storage-consumption.yaml**

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: storage-consumption
spec:
  hard:
    persistentvolumeclaims: "10"
    requests.storage: "50Gi"
    gold.storageclass.storage.k8s.io/requests.storage: "10Gi"
    silver.storageclass.storage.k8s.io/requests.storage: "20Gi"
    silver.storageclass.storage.k8s.io/persistentvolumeclaims: "5"
    bronze.storageclass.storage.k8s.io/requests.storage: "0"
    bronze.storageclass.storage.k8s.io/persistentvolumeclaims: "0"
# ...
```


where: 

`persistentvolumeclaims`
     Specifies the total number of PVCs in a project. 
`requests.storage`
     Specifies that across all PVCs in a project, the sum of storage requested cannot exceed this value. 
`gold.storageclass.storage.k8s.io/requests.storage`
     Specifies that across all PVCs in a project, the sum of storage requested in the gold storage class cannot exceed this value. 
`silver.storageclass.storage.k8s.io/requests.storage`
     Specifies that across all PVCs in a project, the sum of storage requested in the silver storage class cannot exceed this value. 
`silver.storageclass.storage.k8s.io/persistentvolumeclaims`
     Specifies that across PVCs in a project, the total number of claims in the silver storage class cannot exceed this value. 
`bronze.storageclass.storage.k8s.io/requests.storage`
     Specifies that across all PVCs in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this is set to `0`, the bronze storage class cannot request storage. 
`bronze.storageclass.storage.k8s.io/persistentvolumeclaims`
     Specifies that across all PVCs in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this is set to `0`, the bronze storage class cannot create claims. 

## 8.5.2. Creating a quota

To create a quota, define a `ResourceQuota` object in a file and apply the file to a project. By doing this task, you can restrict aggregate resource consumption and object counts within the project to ensure the project complies with cluster policies. 

**Procedure**

  * To apply resource constraints to a specific project, create a `ResourceQuota` object by using the OpenShift CLI (`oc`). Run the following `oc create` command with your definition file to enforce the limits on aggregate resource consumption and object counts specified for that namespace: 

```shell-session
$ oc create -f <resource_quota_definition> [-n <project_name>]
```


**Example command to create a ResourceQuota object**

```shell-session
$ oc create -f core-object-counts.yaml -n demoproject
```


## 8.5.3. Creating object count quotas

To manage the consumption of standard namespaced resource types, create an object count quota. By creating an object count quota within a OpenShift Container Platform project, you can set defined limits on the number of objects, such as `BuildConfig` and `DeploymentConfig` objects. 

When you use a resource quota, OpenShift Container Platform charges an object against the quota if the object exists in server storage. These quotas protect against exhaustion of storage resources. 

**Procedure**

  1. To configure an object count quota for a resource, run the following command: 

```shell-session
$ oc create quota <name> --hard=count/<resource>.<group>=<quota>,count/<resource>.<group>=<quota>
```


**Example showing object count quota**

```shell-session
$ oc create quota test --hard=count/deployments.extensions=2,count/replicasets.extensions=4,count/pods=3,count/secrets=4
resourcequota "test" created
```


  2. To inspect the detailed status of the object count quota, use the following `oc describe` command: 

```shell-session
$ oc describe quota test
```


**Example output**

```shell-session
Name:                         test
Namespace:                    quota
Resource                      Used  Hard
--------                      ----  ----
count/deployments.extensions  0     2
count/pods                    0     3
count/replicasets.extensions  0     4
count/secrets                 0     4
```


This example limits the listed resources to the hard limit in each project in the cluster. 




## 8.5.4. Viewing a quota

To monitor usage statistics against defined hard limits, navigate to the **Quota** page in the web console. Alternatively, you can use the CLI to view detailed quota information for the project. 

**Procedure**

  1. Get the list of quotas defined in the project by entering the following command: 

**Example command with a project called demoproject**

```shell-session
$ oc get quota -n demoproject
```


**Example output**

```shell-session
NAME                AGE
besteffort          11m
compute-resources   2m
core-object-counts  29m
```


  2. Describe the target quota by entering the following command: 

**Example command for the core-object-counts quota**

```shell-session
$ oc describe quota core-object-counts -n demoproject
```


**Example output**

```shell-session
Name:			core-object-counts
Namespace:		demoproject
Resource		Used	Hard
--------		----	----
configmaps		3	10
persistentvolumeclaims	0	4
replicationcontrollers	3	20
secrets			9	10
services		2	10
```


## 8.5.5. Configuring quota synchronization period

When a set of resources are deleted, the synchronization time frame of resources is determined by the `resource-quota-sync-period` setting in the `/etc/origin/master/master-config.yaml` file. 

You can change the `resource-quota-sync-period` setting to have the set of resources regenerate in the needed amount of time (in seconds) for the resources to be once again available. 

Note

Before quota usage is restored, you might encounter problems when attempting to reuse the resources. 

Adjusting the regeneration time can be helpful for creating resources and determining resource usage when automation is used. 

Note

The `resource-quota-sync-period` setting balances system performance. Reducing the sync period can result in a heavy load on the controller. 

**Procedure**

  1. To specify the time required for resources to regenerate and become available again, edit the `resource-quota-sync-period` setting. With this configuration, you can set the synchronization interval in seconds. 

**Example of the`resource-quota-sync-period` setting**

```yaml
kubernetesMasterConfig:
  apiLevels:
  - v1beta3
  - v1
  apiServerArguments: null
  controllerArguments:
    resource-quota-sync-period:
      - "10s"
# ...
```


  2. Restart the controller services to apply them to your cluster by entering the following commands: 

```shell-session
$ master-restart api
```


```shell-session
$ master-restart controllers
```


## 8.5.6. Setting a quota to consume a resource

To restrict the amount of a resource that a user can consume, set a quota. By doing this task, you can prevent unbounded usage of resources, such as storage classes, ensuring that project consumption remains within defined limits. 

If a quota does not manage a resource, a user has no restriction on the amount of that resource that can be consumed. For example, if there is no quota on storage related to the gold storage class, the amount of gold storage a project can create is unbounded. 

For high-cost compute or storage resources, administrators can require an explicit quota be granted to consume a resource. For example, if a project was not explicitly given quota for storage related to the gold storage class, users of that project would not be able to create any storage of that type. 

The example in the procedure shows how the quota system intercepts every operation that creates or updates a `PersistentVolumeClaim` resource. The quota system checks what resources controlled by quota would be consumed. If there is no covering quota for those resources in the project, the request is denied. In this example, if a user creates a `PersistentVolumeClaim` resource that uses storage associated with the gold storage class and there is no matching quota in the project, the request is denied. 

**Procedure**

  * Add the following stanza to the `master-config.yaml` file. This stanza requires explicit quota to consume a particular resource. 

```yaml
admissionConfig:
  pluginConfig:
    ResourceQuota:
      configuration:
        apiVersion: resourcequota.admission.k8s.io/v1alpha1
        kind: Configuration
        limitedResources:
        - resource: persistentvolumeclaims
        matchContains:
        - gold.storageclass.storage.k8s.io/requests.storage
# ...
```


where: 

`configuration.resource`
     Specifies the group or resource whose consumption is limited by default. 
`configuration.matchContains`
     Specifies the name of the resource tracked by quota associated with the group or resource to limit by default.
