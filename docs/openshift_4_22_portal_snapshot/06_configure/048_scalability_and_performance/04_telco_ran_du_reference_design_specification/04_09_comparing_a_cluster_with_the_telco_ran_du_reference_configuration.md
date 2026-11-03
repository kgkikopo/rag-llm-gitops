# 4.9. Comparing a cluster with the telco RAN DU reference configuration

After you deploy a telco RAN DU cluster, you can use the `cluster-compare` plugin to assess the cluster’s compliance with the telco RAN DU reference design specifications (RDS). 

The `cluster-compare` plugin is an OpenShift CLI (`oc`) plugin. The plugin uses a telco RAN DU reference configuration to validate the cluster with the telco RAN DU custom resources (CRs). 

The plugin-specific reference configuration for telco RAN DU is packaged in a container image with the telco RAN DU CRs. 

For further information about the `cluster-compare` plugin, see "Understanding the cluster-compare plugin". 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have credentials to access the `registry.redhat.io` container image registry. 
  * You installed the `cluster-compare` plugin. 



**Procedure**

  1. Log on to the container image registry with your credentials by running the following command: 

```shell-session
$ podman login registry.redhat.io
```


  2. Extract the content from the `ztp-site-generate-rhel8` container image by running the following commands:: 

```shell-session
$ podman pull registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22
```


```shell-session
$ mkdir -p ./out
```


```shell-session
$ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 extract /home/ztp --tar | tar x -C ./out
```


  3. Compare the configuration for your cluster to the reference configuration by running the following command: 

```shell-session
$ oc cluster-compare -r out/reference/metadata.yaml
```


**Example output**

```shell-session
...

**********************************

Cluster CR: config.openshift.io/v1_OperatorHub_cluster
Reference File: required/other/operator-hub.yaml
Diff Output: diff -u -N /tmp/MERGED-2801470219/config-openshift-io-v1_operatorhub_cluster /tmp/LIVE-2569768241/config-openshift-io-v1_operatorhub_cluster
--- /tmp/MERGED-2801470219/config-openshift-io-v1_operatorhub_cluster	2024-12-12 14:13:22.898756462 +0000
+++ /tmp/LIVE-2569768241/config-openshift-io-v1_operatorhub_cluster	2024-12-12 14:13:22.898756462 +0000
@@ -1,6 +1,6 @@
 apiVersion: config.openshift.io/v1
 kind: OperatorHub
 metadata:
+  annotations:
+    include.release.openshift.io/hypershift: "true"
   name: cluster
-spec:
-  disableAllDefaultSources: true

**********************************

Summary
CRs with diffs: 11/12
CRs in reference missing from the cluster: 40
optional-image-registry:
  image-registry:
    Missing CRs:
    - optional/image-registry/ImageRegistryPV.yaml
optional-ptp-config:
  ptp-config:
    One of the following is required:
    - optional/ptp-config/PtpConfigBoundary.yaml
    - optional/ptp-config/PtpConfigGmWpc.yaml
    - optional/ptp-config/PtpConfigDualCardGmWpc.yaml
    - optional/ptp-config/PtpConfigForHA.yaml
    - optional/ptp-config/PtpConfigMaster.yaml
    - optional/ptp-config/PtpConfigSlave.yaml
    - optional/ptp-config/PtpConfigSlaveForEvent.yaml
    - optional/ptp-config/PtpConfigForHAForEvent.yaml
    - optional/ptp-config/PtpConfigMasterForEvent.yaml
    - optional/ptp-config/PtpConfigBoundaryForEvent.yaml
  ptp-operator-config:
    One of the following is required:
    - optional/ptp-config/PtpOperatorConfig.yaml
    - optional/ptp-config/PtpOperatorConfigForEvent.yaml
optional-storage:
  storage:
    Missing CRs:
    - optional/local-storage-operator/StorageLV.yaml

...

No CRs are unmatched to reference CRs
Metadata Hash: 09650c31212be9a44b99315ec14d2e7715ee194a5d68fb6d24f65fd5ddbe3c3c
No patched CRs
```


Where: 

Cluster CR
     The CR under comparison. The plugin displays each CR with a difference from the corresponding template. 
Reference File
     The template matching with the CR for comparison. 
Diff Output
     The output in Linux diff format shows the difference between the template and the cluster CR. 
Summary
     After the plugin reports the line diffs for each CR, the summary of differences are reported. 
CRs with diffs
     The number of CRs in the comparison with differences from the corresponding templates. 
CRs in reference missing from the cluster
     The number of CRs represented in the reference configuration, but missing from the live cluster. 
Missing CRs
     The list of CRs represented in the reference configuration, but missing from the live cluster. 
No CRs are unmatched to reference CRs
     The CRs that did not match to a corresponding template in the reference configuration. 
Metadata Hash
     Identifies the reference configuration. 
No patched CRs
     The list of patched CRs. 




**Additional resources**

  * [Understanding the cluster-compare plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/comparing-cluster-configurations#understanding-the-cluster-compare-plugin "6.1. Understanding the cluster-compare plugin")
