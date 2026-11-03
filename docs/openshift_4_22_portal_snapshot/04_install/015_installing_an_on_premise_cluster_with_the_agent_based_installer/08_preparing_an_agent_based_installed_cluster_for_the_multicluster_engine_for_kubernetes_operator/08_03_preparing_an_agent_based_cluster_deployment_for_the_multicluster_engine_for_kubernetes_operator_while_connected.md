# 8.3. Preparing an Agent-based cluster deployment for the multicluster engine for Kubernetes Operator while connected

Create the required manifests for the multicluster engine Operator, the Local Storage Operator (LSO), and to deploy an agent-based OpenShift Container Platform cluster as a hub cluster. 

**Procedure**

  1. Create a sub-folder named `openshift` in the `<assets_directory>` folder. This sub-folder is used to store the extra manifests that will be applied during the installation to further customize the deployed cluster. The `<assets_directory>` folder contains all the assets including the `install-config.yaml` and `agent-config.yaml` files. 

Note

The installer does not validate extra manifests. 

  2. For the multicluster engine, create the following manifests and save them in the `<assets_directory>/openshift` folder: 

**Example`mce_namespace.yaml`**

```yaml
  apiVersion: v1
  kind: Namespace
  metadata:
    labels:
      openshift.io/cluster-monitoring: "true"
    name: multicluster-engine
```


**Example`mce_operatorgroup.yaml`**

```yaml
  apiVersion: operators.coreos.com/v1
  kind: OperatorGroup
  metadata:
    name: multicluster-engine-operatorgroup
    namespace: multicluster-engine
  spec:
    targetNamespaces:
    - multicluster-engine
```


**Example`mce_subscription.yaml`**

```yaml
  apiVersion: operators.coreos.com/v1alpha1
  kind: Subscription
  metadata:
    name: multicluster-engine
    namespace: multicluster-engine
  spec:
    channel: "stable-2.3"
    name: multicluster-engine
    source: redhat-operators
    sourceNamespace: openshift-marketplace
```


Note

You can install a distributed unit (DU) at scale with the Red Hat Advanced Cluster Management (RHACM) using the assisted installer (AI). These distributed units must be enabled in the hub cluster. The AI service requires persistent volumes (PVs), which are manually created. 

  3. For the AI service, create the following manifests and save them in the `<assets_directory>/openshift` folder: 

**Example`lso_namespace.yaml`**

```yaml
  apiVersion: v1
  kind: Namespace
  metadata:
    annotations:
      openshift.io/cluster-monitoring: "true"
    name: openshift-local-storage
```


**Example`lso_operatorgroup.yaml`**

```yaml
  apiVersion: operators.coreos.com/v1
  kind: OperatorGroup
  metadata:
    name: local-operator-group
    namespace: openshift-local-storage
  spec:
    targetNamespaces:
      - openshift-local-storage
```


**Example`lso_subscription.yaml`**

```yaml
  apiVersion: operators.coreos.com/v1alpha1
  kind: Subscription
  metadata:
    name: local-storage-operator
    namespace: openshift-local-storage
  spec:
    installPlanApproval: Automatic
    name: local-storage-operator
    source: redhat-operators
    sourceNamespace: openshift-marketplace
```


Note

After creating all the manifests, your filesystem must display as follows: 

**Example Filesystem**

```shell-session
<assets_directory>
    ├─ install-config.yaml
    ├─ agent-config.yaml
    └─ /openshift
        ├─ mce_namespace.yaml
        ├─ mce_operatorgroup.yaml
        ├─ mce_subscription.yaml
        ├─ lso_namespace.yaml
        ├─ lso_operatorgroup.yaml
        └─ lso_subscription.yaml
```


  4. Create the agent ISO image by running the following command: 

```shell-session
$ openshift-install agent create image --dir <assets_directory>
```


  5. When the image is ready, boot the target machine and wait for the installation to complete. 
  6. To monitor the installation, run the following command: 

```shell-session
$ openshift-install agent wait-for install-complete --dir <assets_directory>
```


Note

To configure a fully functional hub cluster, you must create the following manifests and manually apply them by running the command `$ oc apply -f <manifest-name>`. The order of the manifest creation is important and where required, the waiting condition is displayed. 

  7. For the PVs that are required by the AI service, create the following manifests: 

```yaml
  apiVersion: local.storage.openshift.io/v1
  kind: LocalVolume
  metadata:
   name: assisted-service
   namespace: openshift-local-storage
  spec:
   logLevel: Normal
   managementState: Managed
   storageClassDevices:
     - devicePaths:
         - /dev/vda
         - /dev/vdb
       storageClassName: assisted-service
       volumeMode: Filesystem
```


  8. Use the following command to wait for the availability of the PVs, before applying the subsequent manifests: 

```shell-session
$ oc wait localvolume -n openshift-local-storage assisted-service --for condition=Available --timeout 10m
```


Note

```plaintext
The `devicePath` is an example and may vary depending on the actual hardware configuration used.
```


  9. Create a manifest for a multicluster engine instance. 

**Example`MultiClusterEngine.yaml`**

```yaml
  apiVersion: multicluster.openshift.io/v1
  kind: MultiClusterEngine
  metadata:
    name: multiclusterengine
  spec: {}
```


  10. Create a manifest to enable the AI service. 

**Example`agentserviceconfig.yaml`**

```yaml
  apiVersion: agent-install.openshift.io/v1beta1
  kind: AgentServiceConfig
  metadata:
    name: agent
    namespace: assisted-installer
  spec:
   databaseStorage:
    storageClassName: assisted-service
    accessModes:
    - ReadWriteOnce
    resources:
     requests:
      storage: 10Gi
   filesystemStorage:
    storageClassName: assisted-service
    accessModes:
    - ReadWriteOnce
    resources:
     requests:
      storage: 10Gi
```


  11. Create a manifest to deploy subsequently spoke clusters. 

**Example`clusterimageset.yaml`**

```yaml
  apiVersion: hive.openshift.io/v1
  kind: ClusterImageSet
  metadata:
    name: "4.22"
  spec:
    releaseImage: quay.io/openshift-release-dev/ocp-release:4.22.0-x86_64
```


  12. Create a manifest to import the agent installed cluster (that hosts the multicluster engine and the Assisted Service) as the hub cluster. 

**Example`autoimport.yaml`**

```yaml
  apiVersion: cluster.open-cluster-management.io/v1
  kind: ManagedCluster
  metadata:
   labels:
     local-cluster: "true"
     cloud: auto-detect
     vendor: auto-detect
   name: local-cluster
  spec:
   hubAcceptsClient: true
```


  13. Wait for the managed cluster to be created. 

```shell-session
$ oc wait -n multicluster-engine managedclusters local-cluster --for condition=ManagedClusterJoined=True --timeout 10m
```


**Verification**

  * To confirm that the managed cluster installation is successful, run the following command: 

```shell-session
$ oc get managedcluster
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS             JOINED   AVAILABLE  AGE
local-cluster   true           https://<your cluster url>:6443   True     True       77m
```


**Additional resources**

  * [The Local Storage Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-local-volume)
