# 4.7. Managing host firmware settings with GitOps ZTP

Hosts require the correct firmware configuration to ensure high performance and optimal efficiency. You can deploy custom host firmware configurations for managed clusters with GitOps ZTP. 

Tune hosts with specific hardware profiles in your lab and ensure they are optimized for your requirements. When you have completed host tuning to your satisfaction, you extract the host profile and save it in your GitOps ZTP repository. Then, you use the host profile to configure firmware settings in the managed cluster hosts that you deploy with GitOps ZTP. 

You specify the required hardware profiles by creating `HostFirmwareSettings` CRs, packaging them in `ConfigMap` resources, and referencing them in the `templateRefs` field of your `ClusterInstance` CR. The SiteConfig Operator generates the required `HostFirmwareSettings` and `BareMetalHost` CRs that are applied to the hub cluster. 

Use the following best practices to manage your host firmware profiles. 

Identify critical firmware settings with hardware vendors
     Work with hardware vendors to identify and document critical host firmware settings required for optimal performance and compatibility with the deployed host platform. 
Use common firmware configurations across similar hardware platforms
     Where possible, use a standardized host firmware configuration across similar hardware platforms to reduce complexity and potential errors during deployment. 
Test firmware configurations in a lab environment
     Test host firmware configurations in a controlled lab environment before deploying in production to ensure that settings are compatible with hardware, firmware, and software. 
Manage firmware profiles in source control
     Manage host firmware profiles in Git repositories to track changes, ensure consistency, and facilitate collaboration with vendors. 

**Additional resources**

  * [Recommended firmware configuration for vDU cluster hosts](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-vdu-configuration-reference#ztp-du-firmware-config-reference_vdu-config-ref "8.1. Recommended firmware configuration for vDU cluster hosts")



## 4.7.1. Retrieving the host firmware schema for a managed cluster

You can discover the host firmware schema for managed clusters. The host firmware schema for bare-metal hosts is populated with information that the Ironic API returns. The API returns information about host firmware interfaces, including firmware setting types, allowable values, ranges, and flags. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have installed Red Hat Advanced Cluster Management (RHACM) and logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have provisioned a cluster that is managed by RHACM. 



**Procedure**

  * Discover the host firmware schema for the managed cluster. Run the following command: 

```shell-session
$ oc get firmwareschema -n <managed_cluster_namespace> -o yaml
```


The following example output shows the host firmware schema: 

```shell-session
apiVersion: v1
items:
- apiVersion: metal3.io/v1alpha1
  kind: FirmwareSchema
  metadata:
    creationTimestamp: "2024-09-11T10:29:43Z"
    generation: 1
    name: schema-40562318
    namespace: compute-1
    ownerReferences:
    - apiVersion: metal3.io/v1alpha1
      kind: HostFirmwareSettings
      name: compute-1.example.com
      uid: 65d0e89b-1cd8-4317-966d-2fbbbe033fe9
    resourceVersion: "280057624"
    uid: 511ad25d-f1c9-457b-9a96-776605c7b887
  spec:
    schema:
      AccessControlService:
        allowable_values:
        - Enabled
        - Disabled
        attribute_type: Enumeration
        read_only: false
      # ...
```


## 4.7.2. Retrieving the host firmware settings for a managed cluster

You can retrieve the host firmware settings for managed clusters. This is useful when you have deployed changes to the host firmware and you want to monitor the changes and ensure that they are applied successfully. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have installed Red Hat Advanced Cluster Management (RHACM) and logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have provisioned a cluster that is managed by RHACM. 



**Procedure**

  1. Retrieve the host firmware settings for the managed cluster. Run the following command: 

```shell-session
$ oc get hostfirmwaresettings -n <cluster_namespace> <node_name> -o yaml
```


The following example output shows the host firmware settings: 

```shell-session
apiVersion: v1
items:
- apiVersion: metal3.io/v1alpha1
  kind: HostFirmwareSettings
  metadata:
    creationTimestamp: "2024-09-11T10:29:43Z"
    generation: 1
    name: compute-1.example.com
    namespace: kni-qe-24
    ownerReferences:
    - apiVersion: metal3.io/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: BareMetalHost
      name: compute-1.example.com
      uid: 0baddbb7-bb34-4224-8427-3d01d91c9287
    resourceVersion: "280057626"
    uid: 65d0e89b-1cd8-4317-966d-2fbbbe033fe9
  spec:
    settings: {}
  status:
    conditions:
    - lastTransitionTime: "2024-09-11T10:29:43Z"
      message: ""
      observedGeneration: 1
      reason: Success
      # Indicates that a change in the host firmware settings has been detected.
      status: "True"
      type: ChangeDetected
    - lastTransitionTime: "2024-09-11T10:29:43Z"
      message: Invalid BIOS setting
      observedGeneration: 1
      reason: ConfigurationError
      # Indicates that the host has an invalid firmware setting.
      status: "False"
      type: Valid
    lastUpdated: "2024-09-11T10:29:43Z"
    schema:
      name: schema-40562318
      namespace: compute-1
    # Contains the complete list of configured host firmware settings returned under the `status.settings` field.
    settings:
      AccessControlService: Enabled
      AcpiHpet: Enabled
      AcpiRootBridgePxm: Enabled
      # ...
```


  2. Optional: Check the status of the `HostFirmwareSettings` (`hfs`) custom resource in the cluster: 

```shell-session
$ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="ChangeDetected")].status}'
```


The following example output shows a detected change: 

```shell-session
True
```


  3. Optional: Check for invalid firmware settings in the cluster host by running the following command: 

```shell-session
$ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="Valid")].status}'
```


The following example output shows an invalid firmware setting: 

```shell-session
False
```


## 4.7.3. Deploying user-defined firmware to cluster hosts with GitOps ZTP

You can deploy user-defined firmware settings to cluster hosts by creating custom node templates that include `HostFirmwareSettings` CRs, and referencing them in the `ClusterInstance` CR. You can configure hardware profiles to apply to hosts in the following scenarios: 

  * All hosts in the cluster 
  * Individual hosts in the cluster 



Important

You can configure host hardware profiles to be applied in a hierarchy. Node-level profiles override cluster-wide settings. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have installed Red Hat Advanced Cluster Management (RHACM) version 2.12 or later and logged in to the hub cluster as a user with `cluster-admin` privileges. 
  * You have installed the SiteConfig Operator in the hub cluster. 
  * You created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application. 



**Procedure**

  1. Create the `HostFirmwareSettings` CR that contains the firmware settings you want to apply. For example, create the following YAML file: 

**host-firmware-settings.yaml**

```yaml
apiVersion: metal3.io/v1alpha1
kind: HostFirmwareSettings
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  settings:
    BootMode: "Uefi"
    LogicalProc: "Enabled"
    ProcVirtualization: "Enabled"
```


  2. Save the `HostFirmwareSettings` CR file relative to the `kustomization.yaml` file that you use to provision the cluster. For example: 

```shell-session
site-configs/
  └── site1-sno-du/
        ├── clusterinstance-site1-sno-du.yaml
        ├── kustomization.yaml
        └── host-firmware-settings.yaml
```


  3. Create a `ConfigMap` to store the `HostFirmwareSettings` CR. You can use a `kustomization.yaml` file with `configMapGenerator` to create the `ConfigMap`. For example: 

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - clusterinstance-site1-sno-du.yaml
configMapGenerator:
  - name: host-firmware-settings-cm
    namespace: site1-sno-du
    files:
      - host-firmware-settings.yaml
generatorOptions:
  disableNameSuffixHash: true
```


     * `namespace` must match the `ClusterInstance` namespace. 
     * `host-firmware-settings.yaml` is the name of the `HostFirmwareSettings` CR. 

  4. To apply a hardware profile to all hosts in the cluster, reference the `ConfigMap` in the `spec.templateRefs` field of your `ClusterInstance` CR. For example: 

```yaml
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  clusterName: "site1-sno-du"
  # ...
  templateRefs:
    - name: host-firmware-settings-cm
      namespace: site1-sno-du
  nodes:
    - hostName: "node1.example.com"
      # ...
```


     * `templateRefs` applies the firmware profile to all hosts in the cluster. 

  5. Optional: To apply a hardware profile to a specific host in the cluster, reference the `ConfigMap` in the `spec.nodes[].templateRefs` field. For example: 

```yaml
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  clusterName: "site1-sno-du"
  # ...
  nodes:
    - hostName: "node1.example.com"
      # ...
      templateRefs:
        - name: host-firmware-node1-cm
          namespace: site1-sno-du
    - hostName: "node2.example.com"
      # ...
```


     * `nodes[].templateRefs` applies the firmware profile only to the `node1.example.com` host. 

Note

Node-level `templateRefs` settings override cluster-level `templateRefs` settings. 

  6. Commit the `ClusterInstance` CR, `ConfigMap`, and associated `kustomization.yaml` changes in your Git repository and push the changes. 

The Argo CD pipeline detects the changes and begins the managed cluster deployment. 

Note

Cluster deployment proceeds even if an invalid firmware setting is detected. To apply a correction using GitOps ZTP, re-deploy the cluster with the corrected hardware profile. 




**Verification**

  * Check that the firmware settings have been applied in the managed cluster host. For example, run the following command: 

```shell-session
$ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="Valid")].status}'
```


  * `<managed_cluster_namespace>` is the namespace of the managed cluster and `<managed_cluster_name>` is the name of the managed cluster. 

The following example output shows valid firmware settings: 

```shell-session
True
```
