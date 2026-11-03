# 1.17. Initial Operator configuration

After the control plane initializes, you must immediately configure some Operators so that they all become available. 

**Prerequisites**

  * Your control plane has initialized. 



**Procedure**

  1. Watch the cluster components come online: 

```shell-session
$ watch -n5 oc get clusteroperators
```


**Example output**

```shell-session
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
authentication                             4.22.0    True        False         False      19m
baremetal                                  4.22.0    True        False         False      37m
cloud-credential                           4.22.0    True        False         False      40m
cluster-autoscaler                         4.22.0    True        False         False      37m
config-operator                            4.22.0    True        False         False      38m
console                                    4.22.0    True        False         False      26m
csi-snapshot-controller                    4.22.0    True        False         False      37m
dns                                        4.22.0    True        False         False      37m
etcd                                       4.22.0    True        False         False      36m
image-registry                             4.22.0    True        False         False      31m
ingress                                    4.22.0    True        False         False      30m
insights                                   4.22.0    True        False         False      31m
kube-apiserver                             4.22.0    True        False         False      26m
kube-controller-manager                    4.22.0    True        False         False      36m
kube-scheduler                             4.22.0    True        False         False      36m
kube-storage-version-migrator              4.22.0    True        False         False      37m
machine-api                                4.22.0    True        False         False      29m
machine-approver                           4.22.0    True        False         False      37m
machine-config                             4.22.0    True        False         False      36m
marketplace                                4.22.0    True        False         False      37m
monitoring                                 4.22.0    True        False         False      29m
network                                    4.22.0    True        False         False      38m
node-tuning                                4.22.0    True        False         False      37m
openshift-apiserver                        4.22.0    True        False         False      32m
openshift-controller-manager               4.22.0    True        False         False      30m
openshift-samples                          4.22.0    True        False         False      32m
operator-lifecycle-manager                 4.22.0    True        False         False      37m
operator-lifecycle-manager-catalog         4.22.0    True        False         False      37m
operator-lifecycle-manager-packageserver   4.22.0    True        False         False      32m
service-ca                                 4.22.0    True        False         False      38m
storage                                    4.22.0    True        False         False      37m
```


  2. Configure the Operators that are not available. 



## 1.17.1. Disabling the default software catalog sources

To use only trusted or locally available Operator catalogs, disable the default software catalog sources that OpenShift Container Platform configures during installation. In a restricted network environment, you must disable the default catalogs as a cluster administrator. 

**Procedure**

  * Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object: 

```shell-session
$ oc patch OperatorHub cluster --type json \
    -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
```


Tip

Or, you can use the web console to manage catalog sources. From the **Administration** **Cluster Settings** **Configuration** **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources. 




## 1.17.2. Image registry removed during installation

On platforms that do not provide shareable object storage, the OpenShift Image Registry Operator bootstraps itself as `Removed`. This allows `openshift-installer` to complete installations on these platform types. 

After installation, you must edit the Image Registry Operator configuration to switch the `managementState` from `Removed` to `Managed`. When this has completed, you must configure storage. 

## 1.17.3. Image registry storage configuration

The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available. 

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters. 

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades. 

### 1.17.3.1. Configure registry storage for bare metal and other manual installations

As a cluster administrator, following installation you must configure your registry to use storage. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have a cluster that uses manually-provisioned Red Hat Enterprise Linux CoreOS (RHCOS) nodes, such as bare metal. 
  * You have provisioned persistent storage for your cluster, such as Red Hat OpenShift Data Foundation. 

Important

OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required. 

  * You must have a system with at least 100Gi capacity. 



**Procedure**

  1. To configure your registry to use storage, change the `spec.storage.pvc` in the `configs.imageregistry/cluster` resource. 

Note

When you use shared storage, review your security settings to prevent outside access. 

  2. Verify that you do not have a registry pod: 

```shell-session
$ oc get pod -n openshift-image-registry -l docker-registry=default
```


**Example output**

```shell-session
No resources found in openshift-image-registry namespace
```


Note

If you do have a registry pod in your output, you do not need to continue with this procedure. 

  3. Check the registry configuration: 

```shell-session
$ oc edit configs.imageregistry.operator.openshift.io
```


**Example output**

```yaml
storage:
  pvc:
    claim:
```


Leave the `claim` field blank to allow the automatic creation of an `image-registry-storage` PVC. 

  4. Check the `clusteroperator` status: 

```shell-session
$ oc get clusteroperator image-registry
```


**Example output**

```shell-session
NAME             VERSION              AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
image-registry   4.22                 True        False         False      6h50m
```


  5. Ensure that your registry is set to managed to enable building and pushing of images. 

     * Run: 

```plaintext
$ oc edit configs.imageregistry/cluster
```


Then, change the line 

```plaintext
managementState: Removed
```


to 

```plaintext
managementState: Managed
```


### 1.17.3.2. Configure storage for the image registry in non-production clusters

You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory, but you lose all images if you restart the registry. 

**Procedure**

  * To set the image registry storage to an empty directory: 

```shell-session
$ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
```


Warning

Configure this option only for non-production clusters. 

If you run this command before the Image Registry Operator initializes its components, the `oc patch` command fails with the following error: 

**Example output**

```shell-session
Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
```


Wait a few minutes and run the command again. 




### 1.17.3.3. Configure block registry storage for bare metal

To allow the image registry to use block storage types during upgrades as a cluster administrator, you can use the `Recreate` rollout strategy. 

Important

Block storage volumes, or block persistent volumes, are supported but not recommended for use with the image registry on production clusters. An installation where the registry is configured on block storage is not highly available because the registry cannot have more than one replica. 

If you choose to use a block storage volume with the image registry, you must use a filesystem persistent volume claim (PVC). 

**Procedure**

  1. Enter the following command to set the image registry storage as a block storage type, patch the registry so that it uses the `Recreate` rollout strategy, and runs with only one (`1`) replica: 

```shell-session
$ oc patch config.imageregistry.operator.openshift.io/cluster --type=merge -p '{"spec":{"rolloutStrategy":"Recreate","replicas":1}}'
```


  2. Provision the PV for the block storage device, and create a PVC for that volume. The requested block volume uses the ReadWriteOnce (RWO) access mode. 

     1. Create a `pvc.yaml` file with the following contents to define a VMware vSphere `PersistentVolumeClaim` object: 

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: image-registry-storage
  namespace: openshift-image-registry
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 100Gi
```


where: 

`metadata.name`
     Specifies a unique name that represents the `PersistentVolumeClaim` object. 
`metadata.namespace`
     Specifies the `namespace` for the `PersistentVolumeClaim` object, which is `openshift-image-registry`. 
`spec.accessModes`
     Specifies the access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node. 
`spec.resources.requests.storage`
     The size of the persistent volume claim. 

     2. Enter the following command to create the `PersistentVolumeClaim` object from the file: 

```shell-session
$ oc create -f pvc.yaml -n openshift-image-registry
```


  3. Enter the following command to edit the registry configuration so that it references the correct PVC: 

```shell-session
$ oc edit config.imageregistry.operator.openshift.io -o yaml
```


**Example output**

```yaml
storage:
  pvc:
    claim:
```


By creating a custom PVC, you can leave the `claim` field blank for the default automatic creation of an `image-registry-storage` PVC.
