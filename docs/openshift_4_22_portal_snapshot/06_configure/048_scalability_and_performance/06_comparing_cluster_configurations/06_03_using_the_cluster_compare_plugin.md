# 6.3. Using the cluster-compare plugin

You can use the `cluster-compare` plugin to compare a reference configuration with a configuration from a live cluster or `must-gather` data. 

## 6.3.1. Using the cluster-compare plugin with a live cluster

You can use the `cluster-compare` plugin to compare a reference configuration with configuration custom resources (CRs) from a live cluster. 

Validate live cluster configurations to ensure compliance with reference configurations during design, development, or testing scenarios. 

Note

Use the `cluster-compare` plugin with live clusters in non-production environments only. For production environments, use the plugin with `must-gather` data. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You downloaded the `cluster-compare` plugin and include it in your `PATH` environment variable. 
  * You have access to a reference configuration. 



**Procedure**

  * Run the `cluster-compare` plugin by using the following command: 

```shell-session
$ oc cluster-compare -r <path_to_reference_config>/metadata.yaml
```


    * `-r` specifies a path to the `metadata.yaml` file of the reference configuration. You can specify a local directory or a URI. 

**Example output**

```shell-session
...

**********************************

Cluster CR: operator.openshift.io/v1_Console_cluster
Reference File: optional/console-disable/ConsoleOperatorDisable.yaml
Diff Output: diff -u -N /tmp/MERGED-622469311/operator-openshift-io-v1_console_cluster /tmp/LIVE-2358803347/operator-openshift-io-v1_console_cluster
/tmp/MERGED-622469311/operator-openshift-io-v1_console_cluster	2024-11-20 15:43:42.888633602 +0000
+++ /tmp/LIVE-2358803347/operator-openshift-io-v1_console_cluster	2024-11-20 15:43:42.888633602 +0000
@@ -4,5 +4,5 @@
   name: cluster
 spec:
   logLevel: Normal
-  managementState: Removed
+  managementState: Managed
   operatorLogLevel: Normal

**********************************

…

Summary
CRs with diffs: 5/49
CRs in reference missing from the cluster: 1
required-cluster-tuning:
  cluster-tuning:
    Missing CRs:
    - required/cluster-tuning/disabling-network-diagnostics/DisableSnoNetworkDiag.yaml
No CRs are unmatched to reference CRs
Metadata Hash: 512a9bf2e57fd5a5c44bbdea7abb3ffd7739d4a1f14ef9021f6793d5cdf868f0
No patched CRs
```


where: 

`Cluster CR`
     The CR under comparison. The plugin displays each CR with a difference from the corresponding template. 
`Reference File`
     The template matching with the CR for comparison. 
`Diff Output`
     The output in Linux diff format shows the difference between the template and the cluster CR. 
`Summary`
     After the plugin reports the line diffs for each CR, the summary of differences are reported. 
`CRs with diffs`
     The number of CRs in the comparison with differences from the corresponding templates. 
`CRs in reference missing from the cluster`
     The number of CRs represented in the reference configuration, but missing from the live cluster. 
`Missing CRs`
     The list of CRs represented in the reference configuration, but missing from the live cluster. 
`No CRs are unmatched to reference CRs`
     The CRs that did not match to a corresponding template in the reference configuration. 
`Metadata Hash`
     The metadata hash identifies the reference configuration. 
`No patched CRs`
    

The list of patched CRs. 

Note

Get the output in the `junit` format by adding `-o junit` to the command. For example: 

```shell-session
$ oc cluster-compare -r <path_to_reference_config>/metadata.yaml -o junit
```


The `junit` output includes the following result types: 

      * Passed results for each fully matched template. 
      * Failed results for differences found or missing required custom resources (CRs). 
      * Skipped results for differences patched using the user override mechanism. 




## 6.3.2. Using the cluster-compare plugin with must-gather data

You can use the `cluster-compare` plugin to compare a reference configuration with configuration custom resources (CRs) from `must-gather` data. 

Validate cluster configurations by using `must-gather` data to troubleshoot configuration issues in production environments. 

Note

For production environments, use the `cluster-compare` plugin with `must-gather` data only. 

  * You have access to `must-gather` data from a target cluster. 
  * You installed the OpenShift CLI (`oc`). 
  * You have downloaded the `cluster-compare` plugin and included it in your `PATH` environment variable. 
  * You have access to a reference configuration. 



**Procedure**

  * Compare the `must-gather` data to a reference configuration by running the following command: 

```shell-session
$ oc cluster-compare -r <path_to_reference_config>/metadata.yaml -f "must-gather*/*/cluster-scoped-resources","must-gather*/*/namespaces" -R
```


    * `-r` specifies a path to the `metadata.yaml` file of the reference configuration. You can specify a local directory or a URI. 
    * `-f` specifies the path to the `must-gather` data directory. You can specify a local directory or a URI. This example restricts the comparison to the relevant cluster configuration directories. 
    * `-R` searches the target directories recursively. 

The following is example output: 

```shell-session
...

**********************************

Cluster CR: operator.openshift.io/v1_Console_cluster
Reference File: optional/console-disable/ConsoleOperatorDisable.yaml
Diff Output: diff -u -N /tmp/MERGED-622469311/operator-openshift-io-v1_console_cluster /tmp/LIVE-2358803347/operator-openshift-io-v1_console_cluster
/tmp/MERGED-622469311/operator-openshift-io-v1_console_cluster	2024-11-20 15:43:42.888633602 +0000
+++ /tmp/LIVE-2358803347/operator-openshift-io-v1_console_cluster	2024-11-20 15:43:42.888633602 +0000
@@ -4,5 +4,5 @@
   name: cluster
 spec:
   logLevel: Normal
-  managementState: Removed
+  managementState: Managed
   operatorLogLevel: Normal

**********************************

…

Summary
CRs with diffs: 5/49
CRs in reference missing from the cluster: 1
required-cluster-tuning:
  cluster-tuning:
    Missing CRs:
    - required/cluster-tuning/disabling-network-diagnostics/DisableSnoNetworkDiag.yaml
No CRs are unmatched to reference CRs
Metadata Hash: 512a9bf2e57fd5a5c44bbdea7abb3ffd7739d4a1f14ef9021f6793d5cdf868f0
No patched CRs
```


where: 

`Cluster CR`
     The CR under comparison. The plugin displays each CR with a difference from the corresponding template. 
`Reference File`
     The template matching with the CR for comparison. 
`Diff Output`
     The output in Linux diff format shows the difference between the template and the cluster CR. 
`Summary`
     After the plugin reports the line diffs for each CR, the summary of differences are reported. 
`CRs with diffs`
     The number of CRs in the comparison with differences from the corresponding templates. 
`CRs in reference missing from the cluster`
     The number of CRs represented in the reference configuration, but missing from the live cluster. 
`Missing CRs`
     The list of CRs represented in the reference configuration, but missing from the live cluster. 
`No CRs are unmatched to reference CRs`
     The CRs that did not match to a corresponding template in the reference configuration. 
`Metadata Hash`
     The metadata hash identifies the reference configuration. 
`No patched CRs`
    

The list of patched CRs. 

Note

Get the output in the `junit` format by adding `-o junit` to the command. For example: 

```shell-session
$ oc cluster-compare -r <path_to_reference_config>/metadata.yaml -f "must-gather*/*/cluster-scoped-resources","must-gather*/*/namespaces" -R -o junit
```


The `junit` output includes the following result types: 

      * Passed results for each fully matched template. 
      * Failed results for differences found or missing required custom resources (CRs). 
      * Skipped results for differences patched using the user override mechanism. 




**Additional resources**

  * [Gathering data about your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#about-must-gather_gathering-cluster-data)



## 6.3.3. Reference cluster-compare plugin options

The following content describes the options for the `cluster-compare` plugin. 

Table 6.1. Cluster-compare plugin optionsOption| Description  
---|---  
`-A`, `--all-resources` |  When used with a live cluster, attempts to match all resources in the cluster that match a type in the reference configuration. When used with local files, attempts to match all resources in the local files that match a type in the reference configuration.   
`--concurrency` |  Specify an integer value for the number of templates to process in parallel when comparing with resources from the live version. A larger number increases speed but also memory, I/O, and CPU usage during that period. The default value is `4`.   
`-c`, `--diff-config` |  Specify the path to the user configuration file.   
`-f`, `--filename` |  Specify a filename, directory, or URL for the configuration custom resources that you want to use for a comparison with a reference configuration.   
`--generate-override-for` |  Specify the path for templates that requires a patch.   
`--show-template-functions` |  Displays the available template functions.  Note You must use a file path for the target template that is relative to the `metadata.yaml` file. For example, if the file path for the `metadata.yaml` file is `./compare/metadata.yaml`, a relative file path for the template might be `optional/my-template.yaml`.   
`-h`, `--help` |  Display help information.   
`-k`, `--kustomize` |  Specify a path to process the `kustomization` directory. This flag cannot be used together with `-f` or `-R`.   
`-o`, `--output` |  Specify the output format. Options include `json`, `yaml`, `junit`, or `generate-patches`.   
`--override-reason` |  Specify a reason for generating the override.   
`-p`, `--overrides` |  Specify a path to a patch override file for the reference configuration.   
`-R`, `--recursive` |  Processes the directory specified in `-f`, `--filename` recursively.   
`-r`, `--reference` |  Specify the path to the reference configuration `metadata.yaml` file.   
`--show-managed-fields` |  Specify `true` to include managed fields in the comparison.   
`-v`, `--verbose` |  Increases the verbosity of the plugin output.   
Show more

## 6.3.4. Example: Comparing a cluster with the telco core reference configuration

You can use the `cluster-compare` plugin to compare a reference configuration with a configuration from a live cluster or `must-gather` data. 

This example compares a configuration from a live cluster with the telco core reference configuration. The telco core reference configuration is derived from the telco core reference design specifications (RDS). The telco core RDS is designed for clusters to support large scale telco applications including control plane and some centralized data plane functions. 

The reference configuration is packaged in a container image with the telco core RDS. 

For further examples of using the `cluster-compare` plugin with the telco core and telco RAN distributed unit (DU) profiles, see the "Additional resources" section. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have credentials to access the `registry.redhat.io` container image registry. 
  * You installed the `cluster-compare` plugin. 



**Procedure**

  1. Log on to the container image registry with your credentials by running the following command: 

```shell-session
$ podman login registry.redhat.io
```


  2. Extract the content from the `telco-core-rds-rhel9` container image by running the following commands: 

```shell-session
$ mkdir -p ./out
```


```shell-session
$ podman run -it registry.redhat.io/openshift4/openshift-telco-core-rds-rhel9:v4.18 | base64 -d | tar xv -C out
```


You can view the reference configuration in the `reference-crs-kube-compare/` directory. 

```plaintext
out/telco-core-rds/configuration/reference-crs-kube-compare/
├── metadata.yaml
├── optional
│   ├── logging
│   ├── networking
│   ├── other
│   └── tuning
└── required
    ├── networking
    ├── other
    ├── performance
    ├── scheduling
    └── storage
```


where: 

`metadata.yaml`
     Configuration file for the reference configuration. 
`optional`
     Directory for optional templates. 
`required`
     Directory for required templates. 

  3. Compare the configuration for your cluster to the telco core reference configuration by running the following command: 

```shell-session
$ oc cluster-compare -r out/telco-core-rds/configuration/reference-crs-kube-compare/metadata.yaml
```


The following is example output: 

```shell-session
W1212 14:13:06.281590   36629 compare.go:425] Reference Contains Templates With Types (kind) Not Supported By Cluster: BFDProfile, BGPAdvertisement, BGPPeer, ClusterLogForwarder, Community, IPAddressPool, MetalLB, MultiNetworkPolicy, NMState, NUMAResourcesOperator, NUMAResourcesScheduler, NodeNetworkConfigurationPolicy, SriovNetwork, SriovNetworkNodePolicy, SriovOperatorConfig, StorageCluster

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
CRs with diffs: 3/4
CRs in reference missing from the cluster: 22
other:
  other:
    Missing CRs:
    - optional/other/control-plane-load-kernel-modules.yaml
    - optional/other/worker-load-kernel-modules.yaml
required-networking:
  networking-root:
    Missing CRs:
    - required/networking/nodeNetworkConfigurationPolicy.yaml
  networking-sriov:
    Missing CRs:
    - required/networking/sriov/sriovNetwork.yaml
    - required/networking/sriov/sriovNetworkNodePolicy.yaml
    - required/networking/sriov/SriovOperatorConfig.yaml
    - required/networking/sriov/SriovSubscription.yaml
    - required/networking/sriov/SriovSubscriptionNS.yaml
    - required/networking/sriov/SriovSubscriptionOperGroup.yaml
required-other:
  scheduling:
    Missing CRs:
    - required/other/catalog-source.yaml
    - required/other/icsp.yaml
required-performance:
  performance:
    Missing CRs:
    - required/performance/PerformanceProfile.yaml
required-scheduling:
  scheduling:
    Missing CRs:
    - required/scheduling/nrop.yaml
    - required/scheduling/NROPSubscription.yaml
    - required/scheduling/NROPSubscriptionNS.yaml
    - required/scheduling/NROPSubscriptionOperGroup.yaml
    - required/scheduling/sched.yaml
required-storage:
  storage-odf:
    Missing CRs:
    - required/storage/odf-external/01-rook-ceph-external-cluster-details.secret.yaml
    - required/storage/odf-external/02-ocs-external-storagecluster.yaml
    - required/storage/odf-external/odfNS.yaml
    - required/storage/odf-external/odfOperGroup.yaml
    - required/storage/odf-external/odfSubscription.yaml
No CRs are unmatched to reference CRs
Metadata Hash: fe41066bac56517be02053d436c815661c9fa35eec5922af25a1be359818f297
No patched CRs
```


where: 

`Cluster CR`
     The CR under comparison. The plugin displays each CR with a difference from the corresponding template. 
`Reference File`
     The template matching with the CR for comparison. 
`Diff Output`
     The output in Linux diff format shows the difference between the template and the cluster CR. 
`Summary`
     After the plugin reports the line diffs for each CR, the summary of differences are reported. 
`CRs with diffs`
     The number of CRs in the comparison with differences from the corresponding templates. 
`CRs in reference missing from the cluster`
     The number of CRs represented in the reference configuration, but missing from the live cluster. 
`Missing CRs`
     The list of CRs represented in the reference configuration, but missing from the live cluster. 
`No CRs are unmatched to reference CRs`
     The CRs that did not match to a corresponding template in the reference configuration. 
`Metadata Hash`
     The metadata hash identifies the reference configuration. 
`No patched CRs`
    

The list of patched CRs. 

Note

Get the output in the `junit` format by adding `-o junit` to the command. For example: 

```shell-session
$ oc cluster-compare -r out/telco-core-rds/configuration/reference-crs-kube-compare/metadata.yaml -o junit
```


The `junit` output includes the following result types: 

     * Passed results for each fully matched template. 
     * Failed results for differences found or missing required custom resources (CRs). 
     * Skipped results for differences patched using the user override mechanism. 




## 6.3.5. Additional resources

  * [Comparing a cluster with the telco RAN DU reference configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/telco-ran-du-ref-design-specs#using-cluster-compare-telco-ran_ran-ref-design-crs "4.9. Comparing a cluster with the telco RAN DU reference configuration")
  * [Comparing a cluster with the telco core reference configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/telco-core-ref-design-specs#using-cluster-compare-telco_core_telco-core "3.17.2. Compare a cluster with the telco core reference configuration")
