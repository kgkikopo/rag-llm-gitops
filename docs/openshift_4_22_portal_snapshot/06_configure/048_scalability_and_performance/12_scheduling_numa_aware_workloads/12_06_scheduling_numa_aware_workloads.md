# 12.6. Scheduling NUMA-aware workloads

To process latency-sensitive and high-performance workloads efficiently, configure your OpenShift Container Platform cluster for NUMA-aware scheduling. This process aligns pods with specific NUMA zones to minimize network delays and maximize compute resource utilization. 

Clusters running latency-sensitive workloads typically feature performance profiles that help to minimize workload latency and optimize performance. The NUMA-aware scheduler deploys workloads based on available node NUMA resources and with respect to any performance profile settings applied to the node. The combination of NUMA-aware deployments, and the performance profile of the workload, ensures that workloads are scheduled in a way that maximizes performance. 

For the NUMA Resources Operator to be fully operational, you must deploy the `NUMAResourcesOperator` custom resource and the NUMA-aware secondary pod scheduler. 

## 12.6.1. Create the NUMAResourcesOperator custom resource

After you have installed the NUMA Resources Operator, you can create the `NUMAResourcesOperator` custom resource (CR). 

This CR instructs the NUMA Resources Operator to deploy the Resource Topology Exporter (RTE) as a daemon set on worker nodes and install all the cluster infrastructure that is needed to support the NUMA-aware scheduler. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 
  * You have installed the NUMA Resources Operator. 



Important

Only cluster administrators should create or modify `NUMAResourcesOperator` custom resources. The Resource Topology Exporter (RTE) runs as a daemon set on worker nodes with elevated read privileges that allow it to discover hardware topology information, observe node resources, and report NUMA zone details. 

The `spec.imageSpec` field in the `NUMAResourcesOperator` custom resource controls which container image runs with these RTE privileges on worker nodes. Granting non-admin users write access to the `NUMAResourcesOperator` resource creates a security risk. An attacker with write access could substitute a malicious container image and potentially access sensitive node information or cluster topology data. 

**Procedure**

  1. Create the `NUMAResourcesOperator` custom resource: 

     1. Save the following minimal required YAML file example as `nrop.yaml`: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesOperator
metadata:
  name: numaresourcesoperator
spec:
  nodeGroups:
  - machineConfigPoolSelector:
      matchLabels:
        pools.operator.machineconfiguration.openshift.io/worker: ""
# ...
```


`pools.operator.machineconfiguration.openshift.io/worker`: Specifies a value that must match the `MachineConfigPool` resource that you want to configure the NUMA Resources Operator on. For example, you might have created a `MachineConfigPool` resource named `worker-cnf` that designates a set of nodes expected to run telecommunications workloads. When configuring the `nodeGroups` spec, ensure that each `MachineConfigPool` resource you reference targets nodes with a unique `nodeSelector` label. This `nodeSelector` label should be applied exclusively to that specific node set. A node you want to manage with topology-aware scheduling must be associated with a single `MachineConfigPool` resource. Consequently, each `nodeGroup` should match exactly one `MachineConfigPool` resource, as configurations matching multiple pools are not supported. 

     2. Create the `NUMAResourcesOperator` CR by running the following command: 

```shell-session
$ oc create -f nrop.yaml
```


Note

Creating the `NUMAResourcesOperator` custom resource automatically deploys the Resource Topology Exporter (RTE) as a daemon set on the configured worker nodes. The RTE collects NUMA topology information and makes it available to the NUMA-aware scheduler. 

  2. Optional: To enable NUMA-aware scheduling for multiple machine config pools (MCPs), define a separate `NodeGroup` for each pool. For example, define three `NodeGroups` for `worker-cnf`, `worker-ht`, and `worker-other`, in the `NUMAResourcesOperator` CR as shown in the following example: 

**Example YAML definition for a`NUMAResourcesOperator` CR with multiple `NodeGroups`**

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesOperator
metadata:
  name: numaresourcesoperator
spec:
  logLevel: Normal
  nodeGroups:
    - machineConfigPoolSelector:
        matchLabels:
          machineconfiguration.openshift.io/role: worker-ht
    - machineConfigPoolSelector:
        matchLabels:
          machineconfiguration.openshift.io/role: worker-cnf
    - machineConfigPoolSelector:
        matchLabels:
          machineconfiguration.openshift.io/role: worker-other
# ...
```


  3. Optional: When you need to use a non-default Resource Topology Exporter (RTE) image, you can specify a custom image using the `spec.imageSpec` field: 

**Example YAML definition for a`NUMAResourcesOperator` CR with custom RTE image**

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesOperator
metadata:
  name: numaresourcesoperator
spec:
  imageSpec: "registry.example.com/openshift4/ose-numaresources-operator@sha256:abcd1234..."
  nodeGroups:
  - machineConfigPoolSelector:
      matchLabels:
        pools.operator.machineconfiguration.openshift.io/worker: ""
# ...
```


     * The `spec.imageSpec` field is optional. If not specified, the operator uses the default RTE image for your OpenShift Container Platform release. Custom operand image override is restricted by default. To enable custom image override, set `EXPORTER_IMAGE_RESTRICTION=false` in the Operator’s environment variables. 

Note

For standard deployments, including disconnected environments that use image mirroring (ICSP or IDMS), omit the `spec.imageSpec` field to use the default RTE image. The cluster’s image mirroring configuration automatically redirects the default image to your internal registry. Only specify `spec.imageSpec` when you need to override the default image with a different version or custom build. When specifying a custom image, use a digest-based reference (SHA256) rather than a tag for security and reproducibility. 




**Verification**

  1. Verify that the NUMA Resources Operator deployed successfully by running the following command: 

```shell-session
$ oc get numaresourcesoperators.nodetopology.openshift.io
```


**Example output**

```shell-session
NAME                    AGE
numaresourcesoperator   27s
```


  2. After a few minutes, run the following command to verify that the required resources deployed successfully: 

```shell-session
$ oc get all -n openshift-numaresources
```


**Example output**

```shell-session
NAME                                                    READY   STATUS    RESTARTS   AGE
pod/numaresources-controller-manager-7d9d84c58d-qk2mr   1/1     Running   0          12m
pod/numaresourcesoperator-worker-7d96r                  2/2     Running   0          97s
pod/numaresourcesoperator-worker-crsht                  2/2     Running   0          97s
pod/numaresourcesoperator-worker-jp9mw                  2/2     Running   0          97s
```


Note

The `numaresourcesoperator-worker-*` pods are the Resource Topology Exporter (RTE) daemon set instances running on each configured worker node. 




## 12.6.2. Create the NUMAResourcesOperator custom resource for hosted control planes

After you install the NUMA Resources Operator, create the `NUMAResourcesOperator` custom resource (CR). The CR instructs the NUMA Resources Operator to install all the cluster infrastructure that is needed to support the NUMA-aware scheduler on hosted control planes, including daemon sets and APIs. 

Important

Creating the NUMAResourcesOperator custom resource for hosted control planes is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Prerequisites**

  * Installed the OpenShift CLI (`oc`). 
  * Logged in as a user with `cluster-admin` privileges. 
  * Installed the NUMA Resources Operator. 



**Procedure**

  1. Export the management cluster kubeconfig file by running the following command: 

```shell-session
$ export KUBECONFIG=<path-to-management-cluster-kubeconfig>
```


  2. Find the `node-pool-name` for your cluster by running the following command: 

```shell-session
$ oc --kubeconfig="$MGMT_KUBECONFIG" get np -A
```


**Example output**

```shell-session
NAMESPACE   NAME                     CLUSTER       DESIRED NODES   CURRENT NODES   AUTOSCALING   AUTOREPAIR   VERSION   UPDATINGVERSION   UPDATINGCONFIG   MESSAGE
clusters    democluster-us-east-1a   democluster   1               1               False         False        4.22.0    False             False
```


The `node-pool-name` is the `NAME` field in the output. In this example, the `node-pool-name` is `democluster-us-east-1a`. 

  3. Create a YAML file named `nrop-hcp.yaml` with at least the following content: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesOperator
metadata:
  name: numaresourcesoperator
spec:
  nodeGroups:
  - poolName: democluster-us-east-1a
# ...
```


     * `spec.nodeGroups.poolName`: Specifies the `poolName`. The example shows the `node-pool-name` pool name that was retrieved from a previous step. 

  4. On the management cluster, run the following command to list the available secrets: 

```shell-session
$ oc get secrets -n clusters
```


**Example output**

```shell-session
NAME                              TYPE                      DATA   AGE
builder-dockercfg-25qpp           kubernetes.io/dockercfg   1      128m
default-dockercfg-mkvlz           kubernetes.io/dockercfg   1      128m
democluster-admin-kubeconfig      Opaque                    1      127m
democluster-etcd-encryption-key   Opaque                    1      128m
democluster-kubeadmin-password    Opaque                    1      126m
democluster-pull-secret           Opaque                    1      128m
deployer-dockercfg-8lfpd          kubernetes.io/dockercfg   1      128m
```


  5. Extract the `kubeconfig` file for the hosted cluster by running the following command: 

```shell-session
$ oc get secret <SECRET_NAME> -n clusters -o jsonpath='{.data.kubeconfig}' | base64 -d > hosted-cluster-kubeconfig
```


**Example**

```shell-session
$ oc get secret democluster-admin-kubeconfig -n clusters -o jsonpath='{.data.kubeconfig}' | base64 -d > hosted-cluster-kubeconfig
```


  6. Export the hosted cluster `kubeconfig` file by running the following command: 

```shell-session
$ export HC_KUBECONFIG=<path_to_hosted-cluster-kubeconfig>
```


  7. Create the `NUMAResourcesOperator` CR by running the following command on the hosted cluster: 

```shell-session
$ oc create -f nrop-hcp.yaml
```


**Verification**

  1. Verify that the NUMA Resources Operator deployed successfully by running the following command: 

```shell-session
$ oc get numaresourcesoperators.nodetopology.openshift.io
```


**Example output**

```shell-session
NAME                    AGE
numaresourcesoperator   27s
```


  2. After a few minutes, run the following command to verify that the required resources deployed successfully: 

```shell-session
$ oc get all -n openshift-numaresources
```


**Example output**

```shell-session
NAME                                                    READY   STATUS    RESTARTS   AGE
pod/numaresources-controller-manager-7d9d84c58d-qk2mr   1/1     Running   0          12m
pod/numaresourcesoperator-democluster-7d96r             2/2     Running   0          97s
pod/numaresourcesoperator-democluster-crsht             2/2     Running   0          97s
pod/numaresourcesoperator-democluster-jp9mw             2/2     Running   0          97s
```


**Additional resources**

  * [Creating a performance profile](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#cnf-create-performance-profiles_cnf-tuning-low-latency-nodes-with-perf-profile "17.1. Creating a performance profile")



## 12.6.3. Deploy the NUMA-aware secondary pod scheduler

To optimize the placement of high-performance workloads, deploy the NUMA-aware secondary pod scheduler. This component aligns pods with specific NUMA zones to ensure efficient resource utilization in your cluster. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 



Important

Only cluster administrators should create or modify `NUMAResourcesScheduler` custom resources. The NUMA Resources scheduler runs with elevated privileges that allow it to bind pods to nodes, observe all pods and nodes across the cluster, and make scheduling decisions that affect workload placement. 

The `spec.imageSpec` field in the `NUMAResourcesScheduler` custom resource controls which container image runs with these scheduler privileges. Granting non-admin users write access to the `NUMAResourcesScheduler` resource creates a privilege escalation risk. An attacker with write access could substitute a malicious container image and run arbitrary code with scheduler privileges. 

**Procedure**

  1. Create the `NUMAResourcesScheduler` custom resource that deploys the NUMA-aware custom pod scheduler: 

     1. Save the following minimal required YAML in the `nro-scheduler.yaml` file: 

```yaml
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesScheduler
metadata:
  name: numaresourcesscheduler
spec:
  imageSpec: "registry.redhat.io/openshift4/noderesourcetopology-scheduler-rhel9:v4.22"
# ...
```


        * `spec.imageSpec`: In a disconnected environment, make sure to configure the resolution of this image by either: 

          1. Create an `ImageTagMirrorSet` custom resource (CR). For more information, see "Configuring image registry repository mirroring" in the "Additional resources" section. 
          2. Set the URL to the disconnected registry. 
          3. Create the `NUMAResourcesScheduler` CR by running the following command: 

```shell-session
$ oc create -f nro-scheduler.yaml
```


Note

In a hosted control plane cluster, run this command on the hosted control plane node. 

  2. After a few seconds, run the following command to confirm the successful deployment of the required resources: 

```shell-session
$ oc get all -n openshift-numaresources
```


**Example output**

```shell-session
NAME                                                    READY   STATUS    RESTARTS   AGE
pod/numaresources-controller-manager-7d9d84c58d-qk2mr   1/1     Running   0          12m
pod/numaresourcesoperator-worker-7d96r                  2/2     Running   0          97s
pod/numaresourcesoperator-worker-crsht                  2/2     Running   0          97s
pod/numaresourcesoperator-worker-jp9mw                  2/2     Running   0          97s
pod/secondary-scheduler-847cb74f84-9whlm                1/1     Running   0          10m

NAME                                          DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR                     AGE
daemonset.apps/numaresourcesoperator-worker   3         3         3       3            3           node-role.kubernetes.io/worker=   98s

NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/numaresources-controller-manager   1/1     1            1           12m
deployment.apps/secondary-scheduler                1/1     1            1           10m

NAME                                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/numaresources-controller-manager-7d9d84c58d   1         1         1       12m
replicaset.apps/secondary-scheduler-847cb74f84                1         1         1       10m
```


## 12.6.4. Understanding NUMA image validation

The NUMA Resources Operator validates scheduler images against a trusted digest list. By default, the Operator rejects a custom Resource Topology Exporter (RTE) image so that only the default RTE image runs on worker nodes. 

### 12.6.4.1. Scheduler image validation

The NUMA Resources Operator validates scheduler images to ensure that only trusted images run with scheduler privileges. 

By default, the Operator enforces the following validation rules for images specified in the `NUMAResourcesScheduler` custom resource `spec.imageSpec` field: 

Digest-based references required
     The image reference must use a SHA-256 digest format. For example, `registry.redhat.io/openshift4/noderesourcetopology-scheduler-rhel9@sha256:abc123…​` is valid, but `registry.redhat.io/openshift4/noderesourcetopology-scheduler-rhel9:v5.0` is rejected. 
Trusted digest list
    

To be valid, the image digest must meet one of the following conditions: 

  * Included in the Operator’s trusted list of production scheduler images for the current release channel. 
  * The final digest released in the previous release channel. 
  * Added to the trusted list by setting the `SCHEDULER_IMAGE_DIGESTS` environment variable in the NUMA Resources Operator subscription. For more information, see "Extending the trusted scheduler image list". 



If you specify an image that does not meet these requirements, the Operator sets the `NUMAResourcesScheduler` resource status to `Degraded` with reason `InvalidSchedulerImage`, and the scheduler pods are not created. When validation fails, the `Degraded` condition reports the reason. For example: 

**Example output**

```shell-session
True - InvalidSchedulerImage: image "registry.example.com/custom-scheduler:v1.0" must be referenced by digest, not by tag
```


Note

The `spec.imageSpec` field is required. You must specify a scheduler image by using a digest-based reference. For standard deployments, use the production scheduler image for your OpenShift Container Platform release from `registry.redhat.io`. In disconnected environments, mirror this image to your registry and reference it by digest. If the digest changes from the original production digest, add the new digest to the trusted list by setting the `SCHEDULER_IMAGE_DIGESTS` environment variable in the NUMA Resources Operator subscription. 

### 12.6.4.2. RTE image validation

By default, the NUMA Resources Operator does not allow a custom Resource Topology Exporter (RTE) image. If you set the exporter image in the `NUMAResourcesOperator` custom resource `spec.imageSpec` field, the Operator sets the resource status to `Degraded` with reason `CustomUserImage` and does not reconcile the resource. When validation fails, the `Degraded` condition reports the reason. For example: 

**Example output**

```shell-session
True - CustomUserImage: custom operand image is not supported: registry.example.com/custom-rte:v1.0
```


Leave `spec.imageSpec` unset so that the Operator uses the default RTE image for your OpenShift Container Platform release. The default RTE image is the same image as the Operator container. In a disconnected environment, the image mirroring configuration for the Operator container redirects that image to your internal registry. 

A cluster administrator can temporarily restore the previous behavior, which allows a custom RTE image, by setting the `EXPORTER_IMAGE_RESTRICTION` environment variable to `false` in the NUMA Resources Operator subscription. 

Warning

Setting `EXPORTER_IMAGE_RESTRICTION` to `false` allows a custom RTE image to run with RTE privileges on worker nodes. Use this override only when you must run a non-default RTE image. 

## 12.6.5. Extending the trusted image list

You can add a custom scheduler image digest to the NUMA Resources Operator trusted list by setting the `SCHEDULER_IMAGE_DIGESTS` environment variable in the operator subscription. To use a custom Resource Topology Exporter (RTE) image, see "RTE image validation". 

Warning

Adding a custom scheduler image to the trusted list allows that image to run with scheduler privileges. Verify that you trust the source and integrity of the image before you add it. 

Add a custom scheduler image only when your environment requires it. 

### 12.6.5.1. Extending the trusted scheduler image list

You can extend the trusted scheduler image list by adding custom scheduler image digests to the `SCHEDULER_IMAGE_DIGESTS` environment variable. Supply a digest if your upgrade requires a scheduler image from another stream, or if the built-in list is missing the latest scheduler digest release. 

**Prerequisites**

  * You are logged in as a user with `cluster-admin` privileges. 
  * You have the SHA-256 digest of your custom scheduler image. 
  * You have verified the integrity and source of the custom scheduler image. 



**Procedure**

  1. Obtain the SHA-256 digest of your custom scheduler image by running the following command: 

```shell-session
$ oc image info <your_custom_scheduler_image> -o json | jq -r '.digest'
```


Below is an example of the output: 

```shell-session
sha256:819186877851017bb783d0c291fb990b7136c64a1fac7b031942e4ee1e0c3d53
```


  2. Add the digest to the NUMA Resources Operator subscription’s trusted list by running the following command: 

```shell-session
$ oc patch subscription numaresources-operator \
  -n openshift-numaresources \
  --type=merge \
  -p '{"spec":{"config":{"env":[{"name":"SCHEDULER_IMAGE_DIGESTS","value":"sha256:819186877851017bb783d0c291fb990b7136c64a1fac7b031942e4ee1e0c3d53"}]}}}'
```


Note

To add multiple custom digests, use a comma-separated list of digests in the `value` field. 

For example: 

```shell-session
$ oc patch subscription numaresources-operator \
  -n openshift-numaresources \
  --type=merge \
  -p '{"spec":{"config":{"env":[{"name":"SCHEDULER_IMAGE_DIGESTS","value":"sha256:<digest_1>,sha256:<digest_2>"}]}}}'
```


  3. Run the following command with the `-w` option to watch the NUMA Resources Operator pod restart with the new configuration: 

```shell-session
$ oc get pods -n openshift-numaresources -w
```


  4. Update the `NUMAResourcesScheduler` custom resource to use the digest-based image reference by running the following command: 

```shell-session
$ oc patch numaresourcesscheduler numaresourcesscheduler \
  --type=merge \
  -p '{"spec":{"imageSpec":"<your_registry>/<your_image>@sha256:819186877851017bb783d0c291fb990b7136c64a1fac7b031942e4ee1e0c3d53"}}'
```


**Verification**

  1. Verify that the NUMA Resources Operator deployment has the updated trusted image list by running the following command: 

```shell-session
$ oc get deployment numaresources-controller-manager \
  -n openshift-numaresources \
  -o jsonpath='{.spec.template.spec.containers[0].env[?(@.name=="SCHEDULER_IMAGE_DIGESTS")].value}{"\n"}'
```


**Example output**

```shell-session
sha256:819186877851017bb783d0c291fb990b7136c64a1fac7b031942e4ee1e0c3d53
```


  2. Verify that the scheduler is not in a degraded state by running the following command: 

```shell-session
$ oc get numaresourcesscheduler numaresourcesscheduler \
  -o jsonpath='{range .status.conditions[?(@.type=="Degraded")]}{.status}{" - "}{.reason}{": "}{.message}{"\n"}{end}'
```


**Example output**

```shell-session
False - Degraded:
```


A status of `False` means that the scheduler is not degraded. 

  3. Verify that the scheduler pods are running with your custom image by running the following command: 

```shell-session
$ oc get pods -n openshift-numaresources -l app=secondary-scheduler \
  -o jsonpath='{.items[0].spec.containers[0].image}{"\n"}'
```


## 12.6.6. Disabling image validation

You can disable scheduler or Resource Topology Exporter (RTE) image validation by setting the appropriate environment variables to `false` in the NUMA Resources Operator subscription. 

Warning

Disabling image validation removes important security controls. Any image that you set in the custom resource runs without filtering or validation. With validation disabled, users with write access to these custom resources can specify arbitrary container images that will run with elevated privileges. 

Only disable validation in exceptional circumstances. If you disable validation, ensure that only cluster administrators can change these resources, and implement additional security controls to verify image integrity. 

### 12.6.6.1. Disabling scheduler image validation

You can disable scheduler image validation by setting the `SCHEDULER_IMAGE_VALIDATION` environment variable to `false`. 

Warning

Disabling scheduler image validation creates a significant privilege escalation risk. A malicious scheduler image can: 

  * Access and manipulate all pods and nodes in the cluster 
  * Bind workloads to nodes in ways that compromise security or stability 
  * Observe sensitive cluster resource topology information 
  * Run arbitrary code with scheduler service account permissions 



**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 
  * You have installed the NUMA Resources Operator. 



**Procedure**

  1. Disable validation by running the following command: 

```shell-session
$ oc patch subscription numaresources-operator \
  -n openshift-numaresources \
  --type=merge \
  -p '{"spec":{"config":{"env":[{"name":"SCHEDULER_IMAGE_VALIDATION","value":"false"}]}}}'
```


  2. Run the following command with the `-w` option to watch the NUMA Resources Operator pod restart with the new configuration: 

```shell-session
$ oc get pods -n openshift-numaresources -w
```


**Verification**

  1. Verify that validation is disabled by running the following command: 

```shell-session
$ oc exec -n openshift-numaresources deploy/numaresources-controller-manager -- \
  printenv SCHEDULER_IMAGE_VALIDATION
```


**Example output**

```shell-session
false
```


### 12.6.6.2. Disabling RTE image validation

You can disable RTE image validation by setting the `EXPORTER_IMAGE_RESTRICTION` environment variable to `false`. 

Warning

Disabling RTE image validation creates a security risk. A malicious RTE image can: 

  * Access sensitive hardware topology information about worker nodes 
  * Observe node resource allocation and NUMA zone configurations 
  * Read detailed system information that could facilitate other attacks 
  * Run code with the RTE daemon set service account permissions 



**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 
  * You have installed the NUMA Resources Operator. 



**Procedure**

  1. Disable validation by running the following command: 

```shell-session
$ oc patch subscription numaresources-operator \
  -n openshift-numaresources \
  --type=merge \
  -p '{"spec":{"config":{"env":[{"name":"EXPORTER_IMAGE_RESTRICTION","value":"false"}]}}}'
```


  2. Run the following command with the `-w` option to watch the NUMA Resources Operator pod restart with the new configuration: 

```shell-session
$ oc get pods -n openshift-numaresources -w
```


**Verification**

  1. Verify that validation is disabled by running the following command: 

```shell-session
$ oc exec -n openshift-numaresources deploy/numaresources-controller-manager -- \
  printenv EXPORTER_IMAGE_RESTRICTION
```


**Example output**

```shell-session
false
```


  2. Verify that the NUMA Resources Operator is not degraded by running the following command: 

```shell-session
$ oc get numaresourcesoperator numaresourcesoperator \
  -o jsonpath='{range .status.conditions[?(@.type=="Degraded")]}{.status}{" - "}{.reason}{": "}{.message}{"\n"}{end}'
```


**Example output**

```shell-session
False - Degraded:
```


A status of `False` means that the Operator is not degraded. 




**Additional resources**

  * [Configuring image registry repository mirroring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#images-configuration-registry-mirror_updating-disconnected-cluster)



## 12.6.7. Schedule workloads with the NUMA-aware scheduler

To schedule workloads with the NUMA-aware scheduler, use deployment CRs that specify the minimum required resources. This ensures your cluster processes the workloads efficiently. 

Before you schedule workloads with the NUMA-aware scheduler, ensure that you previouslu installed the `topo-aware-scheduler`, you applied the `NUMAResourcesOperator` and `NUMAResourcesScheduler` CRs, and that your cluster has a matching performance profile or `kubeletconfig`. 

The example in the procedure uses NUMA-aware scheduling for a sample workload. 

**Prerequisites**

  * Installed the OpenShift CLI (`oc`). 
  * Logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Get the name of the NUMA-aware scheduler that is deployed in the cluster by running the following command: 

```shell-session
$ oc get numaresourcesschedulers.nodetopology.openshift.io numaresourcesscheduler -o json | jq '.status.schedulerName'
```


**Example output**

```shell-session
"topo-aware-scheduler"
```


  2. Create a `Deployment` CR that uses scheduler named `topo-aware-scheduler`, for example: 

     1. Save the following YAML in the `nro-deployment.yaml` file: 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: numa-deployment-1
  namespace: openshift-numaresources
spec:
  replicas: 1
  selector:
    matchLabels:
      app: test
  template:
    metadata:
      labels:
        app: test
    spec:
      schedulerName: topo-aware-scheduler
      containers:
      - name: ctnr
        image: quay.io/openshifttest/hello-openshift:openshift
        imagePullPolicy: IfNotPresent
        resources:
          limits:
            memory: "100Mi"
            cpu: "10"
          requests:
            memory: "100Mi"
            cpu: "10"
      - name: ctnr2
        image: registry.access.redhat.com/rhel:latest
        imagePullPolicy: IfNotPresent
        command: ["/bin/sh", "-c"]
        args: [ "while true; do sleep 1h; done;" ]
        resources:
          limits:
            memory: "100Mi"
            cpu: "8"
          requests:
            memory: "100Mi"
            cpu: "8"
```


`spec.schedulerName`: Specifies the scheduler name that must match the name of the NUMA-aware scheduler that is deployed in your cluster, such as `topo-aware-scheduler`. 

     2. Create the `Deployment` CR by running the following command: 

```shell-session
$ oc create -f nro-deployment.yaml
```


**Verification**

  1. Verify that the deployment was successful: 

```shell-session
$ oc get pods -n openshift-numaresources
```


**Example output**

```shell-session
NAME                                                READY   STATUS    RESTARTS   AGE
numa-deployment-1-6c4f5bdb84-wgn6g                  2/2     Running   0          5m2s
numaresources-controller-manager-7d9d84c58d-4v65j   1/1     Running   0          18m
numaresourcesoperator-worker-7d96r                  2/2     Running   4          43m
numaresourcesoperator-worker-crsht                  2/2     Running   2          43m
numaresourcesoperator-worker-jp9mw                  2/2     Running   2          43m
secondary-scheduler-847cb74f84-fpncj                1/1     Running   0          18m
```


  2. Verify that the `topo-aware-scheduler` is scheduling the deployed pod by running the following command: 

```shell-session
$ oc describe pod numa-deployment-1-6c4f5bdb84-wgn6g -n openshift-numaresources
```


**Example output**

```shell-session
Events:
  Type    Reason          Age    From                  Message
  ----    ------          ----   ----                  -------
  Normal  Scheduled       4m45s  topo-aware-scheduler  Successfully assigned openshift-numaresources/numa-deployment-1-6c4f5bdb84-wgn6g to worker-1
```


Note

Deployments that request more resources than is available for scheduling will fail with a `MinimumReplicasUnavailable` error. The deployment succeeds when the required resources become available. Pods remain in the `Pending` state until the required resources are available. 

  3. Verify that the expected allocated resources are listed for the node. 

     1. Identify the node that is running the deployment pod by running the following command: 

```shell-session
$ oc get pods -n openshift-numaresources -o wide
```


**Example output**

```shell-session
NAME                                 READY   STATUS    RESTARTS   AGE   IP            NODE     NOMINATED NODE   READINESS GATES
numa-deployment-1-6c4f5bdb84-wgn6g   0/2     Running   0          82m   10.128.2.50   worker-1   <none>  <none>
```


     2. Run the following command with the name of that node that is running the deployment pod. 

```shell-session
$ oc describe noderesourcetopologies.topology.node.k8s.io worker-1
```


**Example output**

```shell-session
...

Zones:
  Costs:
    Name:   node-0
    Value:  10
    Name:   node-1
    Value:  21
  Name:     node-0
  Resources:
    Allocatable:  39
    Available:    21
    Capacity:     40
    Name:         cpu
    Allocatable:  6442450944
    Available:    6442450944
    Capacity:     6442450944
    Name:         hugepages-1Gi
    Allocatable:  134217728
    Available:    134217728
    Capacity:     134217728
    Name:         hugepages-2Mi
    Allocatable:  262415904768
    Available:    262206189568
    Capacity:     270146007040
    Name:         memory
  Type:           Node
```


`Resources.Available`: Specifies the `Available` capacity that is reduced because of the resources that have been allocated to the guaranteed pod. Resources consumed by guaranteed pods are subtracted from the available node resources listed under `noderesourcetopologies.topology.node.k8s.io`. 

  4. Resource allocations for pods with a `Best-effort` or `Burstable` quality of service (`qosClass`) are not reflected in the NUMA node resources under `noderesourcetopologies.topology.node.k8s.io`. If a pod’s consumed resources are not reflected in the node resource calculation, verify that the pod has `qosClass` of `Guaranteed` and the CPU request is an integer value, not a decimal value. You can verify the that the pod has a `qosClass` of `Guaranteed` by running the following command: 

```shell-session
$ oc get pod numa-deployment-1-6c4f5bdb84-wgn6g -n openshift-numaresources -o jsonpath="{ .status.qosClass }"
```


**Example output**

```shell-session
Guaranteed
```
