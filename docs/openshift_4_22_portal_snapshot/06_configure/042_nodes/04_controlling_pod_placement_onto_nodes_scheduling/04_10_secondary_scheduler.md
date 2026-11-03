# 4.10. Secondary scheduler

## 4.10.1. Secondary scheduler overview

You can install the Secondary Scheduler Operator to run a custom secondary scheduler alongside the default scheduler to schedule pods. 

### 4.10.1.1. Extend scheduling behavior with a secondary scheduler

The Secondary Scheduler Operator for Red Hat OpenShift provides a way to deploy a custom secondary scheduler in OpenShift Container Platform. The secondary scheduler runs alongside the default scheduler to schedule pods. Pod configurations can specify which scheduler to use. 

The custom scheduler must have the `/bin/kube-scheduler` binary and be based on the upstream Kubernetes scheduling framework. 

Important

You can use the Secondary Scheduler Operator to deploy a custom secondary scheduler in OpenShift Container Platform, but Red Hat does not directly support the functionality of the custom secondary scheduler. 

The Secondary Scheduler Operator creates the default roles and role bindings required by the secondary scheduler. You can specify which scheduling plugins to enable or disable by configuring the `KubeSchedulerConfiguration` resource for the secondary scheduler. 

You can optionally configure high availability for the secondary scheduler to ensure continuous pod scheduling during scheduler pod failures or maintenance. When high availability is enabled, the Operator deploys multiple secondary scheduler replicas distributed across nodes, eliminating the scheduler as a single point of failure in production environments. 

The Secondary Scheduler Operator publishes secondary scheduler metrics to Prometheus by default, enabling monitoring and observability of scheduler performance. 

**Additional resources**

  * [Kubernetes scheduling framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/)



## 4.10.2. Secondary Scheduler Operator for Red Hat OpenShift release notes

Review the Secondary Scheduler Operator for Red Hat OpenShift release notes to track its development and learn what is new and changed with each release. 

The Secondary Scheduler Operator allows you to deploy a custom secondary scheduler in your OpenShift Container Platform cluster. 

For more information, see [About the Secondary Scheduler Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-secondary-scheduler-about_nodes-secondary-scheduler-about "4.10.1.1. Extend scheduling behavior with a secondary scheduler"). 

### 4.10.2.1. Release notes for Secondary Scheduler Operator for Red Hat OpenShift 1.6.0

Review the release notes for Secondary Scheduler Operator 1.6.0 to learn what is new and updated with this release. 

Issued: 24 June 2026 

The following advisory is available for the Secondary Scheduler Operator for Red Hat OpenShift 1.6.0: 

  * [RHBA-2026:28915](https://access.redhat.com/errata/RHBA-2026:28915)



#### 4.10.2.1.1. New features and enhancements

  * You can now configure high availability for the Secondary Scheduler Operator, ensuring continuous pod scheduling for specialized workloads during scheduler pod failures or maintenance. High availability eliminates the secondary scheduler as a single point of failure in production environments. 

To enable high availability, set the topology mode to `HighlyAvailable` in the `SecondaryScheduler` custom resource (CR). In this mode, the Operator deploys multiple secondary scheduler replicas distributed across nodes, up to a configurable maximum. You can optionally set a node selector to target specific nodes or set tolerations for tainted nodes. 

For more information, see [Deploying a secondary scheduler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-secondary-scheduler-configuring-console_secondary-scheduler-configuring "4.10.3.2. Deploy a secondary scheduler"). 

  * The Secondary Scheduler Operator now publishes secondary scheduler metrics to Prometheus by default. 
  * This release of the Secondary Scheduler Operator updates the Kubernetes version to 1.35. 



#### 4.10.2.1.2. Bug fixes

  * This release of the Secondary Scheduler Operator addresses Common Vulnerabilities and Exposures (CVEs). 



#### 4.10.2.1.3. Known issues

  * Currently, you cannot deploy additional resources, such as config maps, CRDs, or RBAC policies through the Secondary Scheduler Operator. Any resources other than roles and role bindings that are required by your custom secondary scheduler must be applied externally. ([WRKLDS-645](https://issues.redhat.com/browse/WRKLDS-645)) 



## 4.10.3. Scheduling pods using a secondary scheduler

You can run a custom secondary scheduler in OpenShift Container Platform by installing the Secondary Scheduler Operator, deploying the secondary scheduler, and setting the secondary scheduler in the pod definition. 

### 4.10.3.1. Install the Secondary Scheduler Operator

You can install the Secondary Scheduler Operator for Red Hat OpenShift through the OpenShift Container Platform web console to configure a secondary scheduler. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Create the required namespace for the Secondary Scheduler Operator for Red Hat OpenShift. 

     1. Navigate to **Administration** **Namespaces** and click **Create Namespace**. 
     2. Enter `openshift-secondary-scheduler-operator` in the **Name** field and click **Create**. 

  3. Install the Secondary Scheduler Operator for Red Hat OpenShift. 

     1. Navigate to **Ecosystem** **Software Catalog**. 
     2. Enter **Secondary Scheduler Operator for Red Hat OpenShift** into the filter box. 
     3. Select the **Secondary Scheduler Operator for Red Hat OpenShift** and click **Install**. 
     4. On the **Install Operator** page: 

        1. The **Update channel** is set to **stable** , which installs the latest stable release of the Secondary Scheduler Operator for Red Hat OpenShift. 
        2. Select **A specific namespace on the cluster** and select **openshift-secondary-scheduler-operator** from the drop-down menu. 
        3. Select an **Update approval** strategy. 

           * The **Automatic** strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available. 
           * The **Manual** strategy requires a user with appropriate credentials to approve the Operator update. 

        4. Click **Install**. 




**Verification**

  1. Navigate to **Ecosystem** **Installed Operators**. 
  2. Verify that **Secondary Scheduler Operator for Red Hat OpenShift** is listed with a **Status** of **Succeeded**. 



### 4.10.3.2. Deploy a secondary scheduler

After you have installed the Secondary Scheduler Operator, you can deploy a secondary scheduler to apply custom placement logic for specific pods. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * You have access to the OpenShift Container Platform web console. 
  * The Secondary Scheduler Operator for Red Hat OpenShift is installed. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Create config map to hold the configuration for the secondary scheduler. 

     1. Navigate to **Workloads** **ConfigMaps**. 
     2. Click **Create ConfigMap**. 
     3. In the YAML editor, enter the config map definition that contains the necessary `KubeSchedulerConfiguration` configuration. For example: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: "secondary-scheduler-config"
  namespace: "openshift-secondary-scheduler-operator"
data:
  "config.yaml": |
    apiVersion: kubescheduler.config.k8s.io/v1
    kind: KubeSchedulerConfiguration
    leaderElection:
      leaderElect: false
    profiles:
      - schedulerName: secondary-scheduler
        plugins:
          score:
            disabled:
              - name: NodeResourcesBalancedAllocation
              - name: NodeResourcesLeastAllocated
```


where: 

`metadata.name`
     Specifies the name of the config map. This is used in the **Scheduler Config** field when creating the `SecondaryScheduler` CR. 
`metadata.namespace`
     Specifies the namespace to create the config map in. The namespace must be `openshift-secondary-scheduler-operator`. 
`data."config.yaml".kind`
     Specifies the `KubeSchedulerConfiguration` resource for the secondary scheduler. For more information, see [`KubeSchedulerConfiguration`](https://kubernetes.io/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration) in the Kubernetes API documentation. 
`data."config.yaml".profiles.schedulerName`
     Specifies the name of the secondary scheduler. Pods that set their `spec.schedulerName` field to this value are scheduled with this secondary scheduler. 
`data."config.yaml".profiles.plugins`
     Specifies the plugins to enable or disable for the secondary scheduler. For a list default scheduling plugins, see [Scheduling plugins](https://kubernetes.io/docs/reference/scheduling/config/#scheduling-plugins) in the Kubernetes documentation. 

     4. Click **Create**. 

  3. Create the `SecondaryScheduler` CR: 

     1. Navigate to **Ecosystem** **Installed Operators**. 
     2. Select **Secondary Scheduler Operator for Red Hat OpenShift**. 
     3. Select the **Secondary Scheduler** tab and click **Create SecondaryScheduler**. 
     4. The **Name** field defaults to `cluster`; do not change this name. 
     5. The **schedulerConfig** field defaults to `secondary-scheduler-config`. Ensure that this value matches the name of the config map created earlier in this procedure. 
     6. In the **schedulerImage** field, enter the image name for your custom scheduler. 

Important

Red Hat does not directly support the functionality of your custom secondary scheduler. 

     7. Optional: To enable high availability for the secondary scheduler, configure the following settings: 

        1. Expand the **topology** section. 
        2. In the **mode** field, select **HighlyAvailable**. 
        3. In the **maxReplicas** field, enter the maximum number of secondary scheduler replicas to deploy. If unset, the maximum number of replicas is `3`. 
        4. In the **tolerations** field, enter tolerations to allow scheduler replicas on tainted nodes. If unset, no taints are tolerated. 

Note

To configure node selectors, use the **YAML view** option. Add the `spec.topology.highlyAvailableTopology.nodeSelector` field and enter the necessary node labels to target a specific group of nodes for scheduler replica placement. If unset, all nodes are considered. 

     8. Click **Create**. 




### 4.10.3.3. Schedule a pod using the secondary scheduler

To schedule a pod by using the secondary scheduler, set the `schedulerName` field in the pod definition. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * You have access to the OpenShift Container Platform web console. 
  * The Secondary Scheduler Operator for Red Hat OpenShift is installed. 
  * A secondary scheduler is configured. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Navigate to **Workloads** **Pods**. 
  3. Click **Create Pod**. 
  4. In the YAML editor, enter the desired pod configuration and add the `schedulerName` field: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: default
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: nginx
      image: nginx:1.14.2
      ports:
        - containerPort: 80
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  schedulerName: secondary-scheduler
```


The `spec.schedulerName` field must match the name that is defined in the config map when you configured the secondary scheduler. 

  5. Click **Create**. 



**Verification**

  1. Log in to the OpenShift CLI. 
  2. Describe the pod using the following command: 

```shell-session
$ oc describe pod nginx -n default
```


**Example output**

```plaintext
Name:         nginx
Namespace:    default
Priority:     0
Node:         ci-ln-t0w4r1k-72292-xkqs4-worker-b-xqkxp/10.0.128.3
...
Events:
  Type    Reason          Age   From                 Message
  ----    ------          ----  ----                 -------
  Normal  Scheduled       12s   secondary-scheduler  Successfully assigned default/nginx to ci-ln-t0w4r1k-72292-xkqs4-worker-b-xqkxp
...
```


  3. In the events table, find the event with a message similar to `Successfully assigned <namespace>/<pod_name> to <node_name>`. 
  4. In the "From" column, verify that the event was generated from the secondary scheduler and not the default scheduler. 

Note

You can also check the `secondary-scheduler-*` pod logs in the `openshift-secondary-scheduler-namespace` to verify that the pod was scheduled by the secondary scheduler. 




## 4.10.4. Uninstalling the Secondary Scheduler Operator

If you no longer need the Secondary Scheduler Operator for Red Hat OpenShift in your cluster, you can uninstall the Operator and remove its related resources. 

### 4.10.4.1. Uninstall the Secondary Scheduler Operator

You can use the web console to uninstall the Secondary Scheduler Operator for Red Hat OpenShift if you no longer need the Operator in your cluster. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * You have access to the OpenShift Container Platform web console. 
  * The Secondary Scheduler Operator for Red Hat OpenShift is installed. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Uninstall the Secondary Scheduler Operator for Red Hat OpenShift Operator. 

     1. Navigate to **Ecosystem** **Installed Operators**. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **Secondary Scheduler Operator** entry and click **Uninstall Operator**. 
     3. In the confirmation dialog, click **Uninstall**. 




### 4.10.4.2. Remove Secondary Scheduler Operator resources

Optionally, remove the custom resource definition (CRD) and associated namespace after the Secondary Scheduler Operator for Red Hat OpenShift is uninstalled. This cleans up all remaining secondary scheduler artifacts. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Remove the CRD that was installed by the Secondary Scheduler Operator: 

     1. Navigate to **Administration** **CustomResourceDefinitions**. 
     2. Enter `SecondaryScheduler` in the **Name** field to filter the CRDs. 
     3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **SecondaryScheduler** CRD and select **Delete Custom Resource Definition** : 

  3. Remove the `openshift-secondary-scheduler-operator` namespace. 

     1. Navigate to **Administration** **Namespaces**. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **openshift-secondary-scheduler-operator** and select **Delete Namespace**. 
     3. In the confirmation dialog, enter `openshift-secondary-scheduler-operator` in the field and click **Delete**.
