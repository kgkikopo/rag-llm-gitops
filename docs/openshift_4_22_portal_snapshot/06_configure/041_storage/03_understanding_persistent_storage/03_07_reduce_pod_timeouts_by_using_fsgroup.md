# 3.7. Reduce pod timeouts by using fsGroup

To reduce pod timeouts when using a storage volume with many files, configure the `fsGroup` field. By specifying this field, you can manage how file ownership and permissions are applied, preventing delays caused by the default recursive permission changes on large volumes. 

This can occur because, by default, OpenShift Container Platform recursively changes ownership and permissions for the contents of each volume to match the `fsGroup` specified in the `securityContext` of the pod when that volume is mounted. For volumes with many files, checking and changing ownership and permissions can be time consuming, slowing pod startup. You can use the `fsGroupChangePolicy` field inside a `securityContext` to control the way that OpenShift Container Platform checks and manages ownership and permissions for a volume. 

`fsGroupChangePolicy` defines behavior for changing ownership and permission of the volume before being exposed inside a pod. This field only applies to volume types that support `fsGroup`-controlled ownership and permissions. This field has two possible values: 

  * `OnRootMismatch`: Only change permissions and ownership if permission and ownership of root directory does not match with expected permissions of the volume. This can help shorten the time it takes to change ownership and permission of a volume to reduce pod timeouts. 
  * `Always`: (Default) Always change permission and ownership of the volume when a volume is mounted. 



Note

The `fsGroupChangePolicy` field has no effect on ephemeral volume types, such as secret, configMap, and emptydir. 

You can set `fsGroupChangePolicy` at either the namespace or pod level. 

## 3.7.1. Changing fsGroup at the namespace level

You can change `fsGroupChangePolicy` at the namespace level to establish a default permission-change behavior for all pods in that namespace, reducing per-pod configuration overhead. 

After applying the desired setting for `fsGroupChangePolicy` at the namespace level, all subsequently created pods in that namespace inherit the setting. However, if desired, you can override the inherited `fsGroupChangePolicy` setting for individual pods. Setting `fsGroupChangePolicy` at the pod level overrides inheritance from the namespace level setting for that pod. 

**Prerequisites**

  * You are logged in to a running OpenShift Container Platform cluster with administrator privileges. 
  * You have access to the OpenShift Container Platform console. 



**Procedure**

  1. Select the desired namespace: 

     1. Click **Administration** > **Namespaces**. 
     2. On the **Namespaces** page, click the desired namespace. The **Namespace details** page appears. 

  2. Add the `fsGroupChangePolicy` label to the namespace: 

     1. On the **Namespace details** page, next to **Labels** , click **Edit**. 
     2. In the **Edit labels** dialog, add the label `storage.openshift.io/fsgroup-change-policy` and set it equal to either: 

        * `OnRootMismatch`: Specifies only changing permissions and ownership if the permission and the ownership of root directory does not match with expected permissions of the volume, thus helping to avoid pod timeout problems. 
        * `Always`: (Default) Specifies always changing permission and ownership of the volume when a volume is mounted. 

     3. Click **Save**. 




**Verification**

  * Start up a pod in the previously edited namespace and observe that the parameter `spec.securityContext.fsGroupChangePolicy` contains the value that you set for the namespace. 

**Example pod YAML file showing`fsGroupChangePolicy` setting**

```yaml
securityContext:
  seLinuxOptions:
    level: 's0:c27,c24'
  runAsNonRoot: true
  fsGroup: 1000750000
  fsGroupChangePolicy: OnRootMismatch
  ...
```


The value for `securityContext.fsGroupChangePolicy` is inherited from the namespace. 




## 3.7.2. Changing fsGroup at the pod level

You can set `fsGroupChangePolicy` parameter in new or existing deployments and stateful sets, and then the pods that it manages will have this parameter value. You cannot edit `fsGroupChangePolicy` on an existing pod; however, you can set this parameter when creating a new pod. 

This procedure describes how to set the `fsGroupChangePolicy` parameter in an existing deployment. 

**Prerequisites**

  * Access to the OpenShift Container Platform console. 



**Procedure**

  1. Click **Workloads** > **Deployments**. 
  2. On the **Deployment** page, click the desired deployment. 
  3. On the **Deployment details** page, click the **YAML** tab. 
  4. Edit the deployment’s YAML file under `spec.template.spec.securityContext` using the following example file: 

**Example deployment YAML file setting`fsGroupChangePolicy`**

```yaml
...
spec:
replicas: 3
selector:
matchLabels:
app: my-app
template:
metadata:
creationTimestamp: null
labels:
app: my-app
spec:
containers:
- name: container
image: 'image-registry.openshift-image-registry.svc:5000/openshift/httpd:latest'
ports:
- containerPort: 8080
protocol: TCP
resources: {}
terminationMessagePath: /dev/termination-log
terminationMessagePolicy: File
imagePullPolicy: Always
restartPolicy: Always
terminationGracePeriodSeconds: 30
dnsPolicy: ClusterFirst
securityContext:
  fsGroupChangePolicy: OnRootMismatch
...
```


`spec.securityContext.fsGroupChangePolicy`, `OnRootMismatch`, specifies skipping recursive permission change, thus helping to avoid pod timeout problems. The default value is `Always`, which always changes permission and ownership of the volume when a volume is mounted. 

  5. Click **Save**.
