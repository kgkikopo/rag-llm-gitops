# 5.2. Reducing the size of must-gather output

The `oc adm must-gather` command collects comprehensive cluster information. However, a full data collection can result in a large file that is difficult to upload and analyze and could result in timeouts. 

To manage the output size and target your data collection for more effective troubleshooting, you can pass specific flags to the underlying `gather` script or scope the collection to particular resources. 

## 5.2.1. Gathering data for specific resources

Instead of collecting data for the entire cluster, you can direct the `must-gather` tool to inspect a specific resource. This method is highly effective for isolating issues within a single project, Operator, or application. 

The `must-gather` tool uses `oc adm inspect` internally. You can specify what to inspect by passing the `inspect` command and its arguments after the `--` separator. 

**Procedure**

  * To gather data for a specific namespace, such as `my-project`, run the following command: 

```shell-session
$ oc adm must-gather --dest-dir=my-project-must-gather -- oc adm inspect ns/my-project
```


  * This command collects all standard resources within the `my-project` namespace, including logs from pods in that namespace, but excludes cluster-scoped resources. 
  * To gather data related to a specific Cluster Operator, such as `openshift-apiserver`, run the following command: 

```shell-session
$ oc adm must-gather --dest-dir=apiserver-must-gather -- oc adm inspect clusteroperator/openshift-apiserver
```


  * To exclude rotated logs, such as `*.gz` or `*.1` files, from data collection, set the `REDUCE_LOGS` environment variable by running the following command: 

```shell-session
$ oc adm must-gather -- REDUCE_LOGS=skip_rotated_logs /usr/bin/gather
```


  * To exclude logs entirely and significantly reduce the size of the `must-gather` archive, add a double dash (`--`) after `oc adm must-gather` command and add the `--no-logs` argument: 

```shell-session
$ oc adm must-gather -- /usr/bin/gather --no-logs
```


## 5.2.2. Must-gather flags

The flags listed in the following table are available to use with the `oc adm must-gather` command. 

Table 5.1. OpenShift Container Platform flags for oc adm must-gatherFlag| Example command| Description  
---|---|---  
`--all-images` |  `oc adm must-gather --all-images=false` |  Collect `must-gather` data using the default image for all Operators on the cluster that are annotated with `operators.openshift.io/must-gather-image`.   
`--dest-dir` |  `oc adm must-gather --dest-dir='<directory_name>'` |  Set a specific directory on the local machine where the gathered data is written.   
`--host-network` |  `oc adm must-gather --host-network=false` |  Run `must-gather` pods as `hostNetwork: true`. Relevant if a specific command and image needs to capture host-level data.   
`--image` |  `oc adm must-gather --image=[<plugin_image>]` |  Specify a `must-gather` plugin image to run. If not specified, OpenShift Container Platform’s default `must-gather` image is used.   
`--image-stream` |  `oc adm must-gather --image-stream=[<image_stream>]` |  Specify an`<image_stream>` using a namespace or name:tag value containing a `must-gather` plugin image to run.   
`--node-name` |  `oc adm must-gather --node-name='<node>'` |  Set a specific node to use. If not specified, by default a random master is used.   
`--node-selector` |  `oc adm must-gather --node-selector='<node_selector_name>'` |  Set a specific node selector to use. Only relevant when specifying a command and image which needs to capture data on a set of cluster nodes simultaneously.   
`--run-namespace` |  `oc adm must-gather --run-namespace='<namespace>'` |  An existing privileged namespace where `must-gather` pods should run. If not specified, a temporary namespace is generated.   
`--since` |  `oc adm must-gather --since=<time>` |  Only return logs newer than the specified duration. Defaults to all logs. Plugins are encouraged but not required to support this. Only one `since-time` or `since` may be used.   
`--since-time` |  `oc adm must-gather --since-time='<date_and_time>'` |  Only return logs after a specific date and time, expressed in ([RFC3339](https://www.rfc-editor.org/rfc/rfc3339)) format. Defaults to all logs. Plugins are encouraged but not required to support this. Only one `since-time` or `since` may be used.   
`--source-dir` |  `oc adm must-gather --source-dir='/<directory_name>/'` |  Set the specific directory on the pod where you copy the gathered data from.   
`--timeout` |  `oc adm must-gather --timeout='<time>'` |  The length of time to gather data before timing out, expressed as seconds, minutes, or hours, for example, 3s, 5m, or 2h. Time specified must be higher than zero. Defaults to 10 minutes if not specified.   
`--volume-percentage` |  `oc adm must-gather --volume-percentage=<percent>` |  Specifies the maximum percentage of the allocated volume of a pod that can be used for `must-gather`. If this limit is exceeded, `must-gather` stops gathering, but still copies gathered data. Defaults to 70% if not specified.   
Show more

## 5.2.3. Gathering data about specific features

You can gather debugging information about specific features by using the `oc adm must-gather` CLI command with the `--image` or `--image-stream` argument. The `must-gather` tool supports multiple images, so you can gather data about more than one feature by running a single command. 

Table 5.2. Supported must-gather imagesImage| Purpose  
---|---  
`registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9` |  Data collection for OpenShift Virtualization.   
`registry.redhat.io/openshift-serverless-1/svls-must-gather-rhel8` |  Data collection for OpenShift Serverless.   
`registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:<installed_version_service_mesh>` |  Data collection for Red Hat OpenShift Service Mesh.   
`registry.redhat.io/multicluster-engine/must-gather-rhel8` |  Data collection for hosted control planes.   
`registry.redhat.io/odf4/odf-must-gather-rhel9:v<installed_version_ODF>` |  Data collection for Red Hat OpenShift Data Foundation.   
`registry.redhat.io/openshift-logging/cluster-logging-rhel9-operator:v<installed_version_logging>` |  Data collection for logging.   
`quay.io/netobserv/must-gather` |  Data collection for the Network Observability Operator.   
`registry.redhat.io/openshift4/ose-local-storage-mustgather-rhel9:v<installed_version_LSO>` |  Data collection for Local Storage Operator.   
`registry.redhat.io/openshift-sandboxed-containers/osc-must-gather-rhel8:v<installed_version_sandboxed_containers>` |  Data collection for OpenShift sandboxed containers.   
`registry.redhat.io/workload-availability/node-healthcheck-must-gather-rhel8:v<installed_version_NHC>` |  Data collection for the Red Hat Workload Availability Operators, including the Self Node Remediation (SNR) Operator, the Fence Agents Remediation (FAR) Operator, the Machine Deletion Remediation (MDR) Operator, the Node Health Check (NHC) Operator, and the Node Maintenance Operator (NMO).  Use this image if your NHC Operator version is **earlier than 0.9.0**.  For more information, see the "Gathering data" section for the specific Operator in [Remediation, fencing, and maintenance](https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/latest/html/remediation_fencing_and_maintenance/index) (Workload Availability for Red Hat OpenShift documentation).   
`registry.redhat.io/workload-availability/node-healthcheck-must-gather-rhel9:v<installed_version_NHC>` |  Data collection for the Red Hat Workload Availability Operators, including the Self Node Remediation (SNR) Operator, the Fence Agents Remediation (FAR) Operator, the Machine Deletion Remediation (MDR) Operator, the Node Health Check (NHC) Operator, and the Node Maintenance Operator (NMO).  Use this image if your NHC Operator version is **0.9.0. or later**.  For more information, see the "Gathering data" section for the specific Operator in [Remediation, fencing, and maintenance](https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/latest/html/remediation_fencing_and_maintenance/index) (Workload Availability for Red Hat OpenShift documentation).   
`registry.redhat.io/openshift4/numaresources-must-gather-rhel9:v<installed-version-nro>` |  Data collection for the NUMA Resources Operator (NRO).   
`registry.redhat.io/openshift4/ptp-must-gather-rhel8:v<installed-version-ptp>` |  Data collection for the PTP Operator.   
`registry.redhat.io/openshift-gitops-1/must-gather-rhel8:v<installed_version_GitOps>` |  Data collection for Red Hat OpenShift GitOps.   
`registry.redhat.io/openshift4/ose-secrets-store-csi-mustgather-rhel9:v<installed_version_secret_store>` |  Data collection for the Secrets Store CSI Driver Operator.   
`registry.redhat.io/lvms4/lvms-must-gather-rhel9:v<installed_version_LVMS>` |  Data collection for the LVM Operator.   
`registry.redhat.io/compliance/openshift-compliance-must-gather-rhel8:<digest-version>` |  Data collection for the Compliance Operator.   
Show more

Note

To determine the latest version for an OpenShift Container Platform component’s image, see the [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) web page on the Red Hat Customer Portal. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * The OpenShift Container Platform CLI (`oc`) is installed. 



**Procedure**

  1. Navigate to the directory where you want to store the `must-gather` data. 
  2. Run the `oc adm must-gather` command with one or more `--image` or `--image-stream` arguments. 

Note

     * To collect the default `must-gather` data in addition to specific feature data, add the `--image-stream=openshift/must-gather` argument. 
     * For information on gathering data about the Custom Metrics Autoscaler, see the Additional resources section that follows. 

For example, the following command gathers both the default cluster data and information specific to OpenShift Virtualization: 

```shell-session
$ oc adm must-gather \
  --image-stream=openshift/must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9
```


You can use the `must-gather` tool with additional arguments to gather data that is specifically related to OpenShift Logging and the Red Hat OpenShift Logging Operator in your cluster. For OpenShift Logging, run the following command: 

```shell-session
$ oc adm must-gather --image=$(oc -n openshift-logging get deployment.apps/cluster-logging-operator \
  -o jsonpath='{.spec.template.spec.containers[?(@.name == "cluster-logging-operator")].image}')
```


**Example`must-gather` output for OpenShift Logging**

```shell-session
├── cluster-logging
│  ├── clo
│  │  ├── cluster-logging-operator-74dd5994f-6ttgt
│  │  ├── clusterlogforwarder_cr
│  │  ├── cr
│  │  ├── csv
│  │  ├── deployment
│  │  └── logforwarding_cr
│  ├── collector
│  │  ├── fluentd-2tr64
│  ├── eo
│  │  ├── csv
│  │  ├── deployment
│  │  └── elasticsearch-operator-7dc7d97b9d-jb4r4
│  ├── es
│  │  ├── cluster-elasticsearch
│  │  │  ├── aliases
│  │  │  ├── health
│  │  │  ├── indices
│  │  │  ├── latest_documents.json
│  │  │  ├── nodes
│  │  │  ├── nodes_stats.json
│  │  │  └── thread_pool
│  │  ├── cr
│  │  ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
│  │  └── logs
│  │     ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
│  ├── install
│  │  ├── co_logs
│  │  ├── install_plan
│  │  ├── olmo_logs
│  │  └── subscription
│  └── kibana
│     ├── cr
│     ├── kibana-9d69668d4-2rkvz
├── cluster-scoped-resources
│  └── core
│     ├── nodes
│     │  ├── ip-10-0-146-180.eu-west-1.compute.internal.yaml
│     └── persistentvolumes
│        ├── pvc-0a8d65d9-54aa-4c44-9ecc-33d9381e41c1.yaml
├── event-filter.html
├── gather-debug.log
└── namespaces
   ├── openshift-logging
   │  ├── apps
   │  │  ├── daemonsets.yaml
   │  │  ├── deployments.yaml
   │  │  ├── replicasets.yaml
   │  │  └── statefulsets.yaml
   │  ├── batch
   │  │  ├── cronjobs.yaml
   │  │  └── jobs.yaml
   │  ├── core
   │  │  ├── configmaps.yaml
   │  │  ├── endpoints.yaml
   │  │  ├── events
   │  │  │  ├── elasticsearch-im-app-1596020400-gm6nl.1626341a296c16a1.yaml
   │  │  │  ├── elasticsearch-im-audit-1596020400-9l9n4.1626341a2af81bbd.yaml
   │  │  │  ├── elasticsearch-im-infra-1596020400-v98tk.1626341a2d821069.yaml
   │  │  │  ├── elasticsearch-im-app-1596020400-cc5vc.1626341a3019b238.yaml
   │  │  │  ├── elasticsearch-im-audit-1596020400-s8d5s.1626341a31f7b315.yaml
   │  │  │  ├── elasticsearch-im-infra-1596020400-7mgv8.1626341a35ea59ed.yaml
   │  │  ├── events.yaml
   │  │  ├── persistentvolumeclaims.yaml
   │  │  ├── pods.yaml
   │  │  ├── replicationcontrollers.yaml
   │  │  ├── secrets.yaml
   │  │  └── services.yaml
   │  ├── openshift-logging.yaml
   │  ├── pods
   │  │  ├── cluster-logging-operator-74dd5994f-6ttgt
   │  │  │  ├── cluster-logging-operator
   │  │  │  │  └── cluster-logging-operator
   │  │  │  │     └── logs
   │  │  │  │        ├── current.log
   │  │  │  │        ├── previous.insecure.log
   │  │  │  │        └── previous.log
   │  │  │  └── cluster-logging-operator-74dd5994f-6ttgt.yaml
   │  │  ├── cluster-logging-operator-registry-6df49d7d4-mxxff
   │  │  │  ├── cluster-logging-operator-registry
   │  │  │  │  └── cluster-logging-operator-registry
   │  │  │  │     └── logs
   │  │  │  │        ├── current.log
   │  │  │  │        ├── previous.insecure.log
   │  │  │  │        └── previous.log
   │  │  │  ├── cluster-logging-operator-registry-6df49d7d4-mxxff.yaml
   │  │  │  └── mutate-csv-and-generate-sqlite-db
   │  │  │     └── mutate-csv-and-generate-sqlite-db
   │  │  │        └── logs
   │  │  │           ├── current.log
   │  │  │           ├── previous.insecure.log
   │  │  │           └── previous.log
   │  │  ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
   │  │  ├── elasticsearch-im-app-1596030300-bpgcx
   │  │  │  ├── elasticsearch-im-app-1596030300-bpgcx.yaml
   │  │  │  └── indexmanagement
   │  │  │     └── indexmanagement
   │  │  │        └── logs
   │  │  │           ├── current.log
   │  │  │           ├── previous.insecure.log
   │  │  │           └── previous.log
   │  │  ├── fluentd-2tr64
   │  │  │  ├── fluentd
   │  │  │  │  └── fluentd
   │  │  │  │     └── logs
   │  │  │  │        ├── current.log
   │  │  │  │        ├── previous.insecure.log
   │  │  │  │        └── previous.log
   │  │  │  ├── fluentd-2tr64.yaml
   │  │  │  └── fluentd-init
   │  │  │     └── fluentd-init
   │  │  │        └── logs
   │  │  │           ├── current.log
   │  │  │           ├── previous.insecure.log
   │  │  │           └── previous.log
   │  │  ├── kibana-9d69668d4-2rkvz
   │  │  │  ├── kibana
   │  │  │  │  └── kibana
   │  │  │  │     └── logs
   │  │  │  │        ├── current.log
   │  │  │  │        ├── previous.insecure.log
   │  │  │  │        └── previous.log
   │  │  │  ├── kibana-9d69668d4-2rkvz.yaml
   │  │  │  └── kibana-proxy
   │  │  │     └── kibana-proxy
   │  │  │        └── logs
   │  │  │           ├── current.log
   │  │  │           ├── previous.insecure.log
   │  │  │           └── previous.log
   │  └── route.openshift.io
   │     └── routes.yaml
   └── openshift-operators-redhat
      ├── ...
```


  3. Run the `oc adm must-gather` command with one or more `--image` or `--image-stream` arguments. For example, the following command gathers both the default cluster data and information specific to KubeVirt: 

```shell-session
$ oc adm must-gather \
 --image-stream=openshift/must-gather \
 --image=quay.io/kubevirt/must-gather
```


  4. Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see [How to find the cluster-id or name on OpenShift cluster](https://access.redhat.com/solutions/5280291). For example, on a computer that uses a Linux operating system, run the following command: 

```shell-session
$ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
```


where: 

`<must_gather_local_dir>`
     Replace with the actual directory name. 

  5. Attach the compressed file to your support case on the [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal. 



**Additional resources**

  * [Gathering debugging data for the Custom Metrics Autoscaler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cma-autoscaling-custom-gather)
  * [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift)



## 5.2.4. Gathering network logs

You can gather network logs on all nodes in a cluster. 

**Procedure**

  1. Run the `oc adm must-gather` command with `-- gather_network_logs`: 

```shell-session
$ oc adm must-gather -- gather_network_logs
```


Note

By default, the `must-gather` tool collects the OVN `nbdb` and `sbdb` databases from all of the nodes in the cluster. Adding the `-- gather_network_logs` option to include additional logs that contain OVN-Kubernetes transactions for OVN `nbdb` database. 

  2. Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see [How to find the cluster-id or name on OpenShift cluster](https://access.redhat.com/solutions/5280291). For example, on a computer that uses a Linux operating system, run the following command: 

```shell-session
$ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
```


Replace the `<must_gather_local_dir>` placeholder with the actual directory name. 

  3. Attach the compressed file to your support case on the [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal. 



## 5.2.5. Changing the must-gather storage limit

When using the `oc adm must-gather` command to collect data the default maximum storage for the information is 30% of the storage capacity of the container. 

After the 30% limit is reached the container is killed and the gathering process stops. Information already gathered is downloaded to your local storage. To run the must-gather command again, you need either a container with more storage capacity or to adjust the maximum volume percentage. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * The OpenShift CLI (`oc`) is installed. 



**Procedure**

  * Run the `oc adm must-gather` command with the `volume-percentage` flag. The new value cannot exceed 100. 

```shell-session
$ oc adm must-gather --volume-percentage <storage_percentage>
```


If the container reaches the storage limit, an error message similar to the following example is generated: 

```shell-session
Disk usage exceeds the volume percentage of 30% for mounted directory. Exiting...
```
