# 4.25. Troubleshooting KMM

When troubleshooting KMM on OpenShift Container Platform, you can monitor Operator logs to identify the failure stage and gather diagnostic data for that stage. 

## 4.25.1. Reading Operator logs

KMM and KMM-Hub Operator logs on OpenShift Container Platform provide diagnostic information for troubleshooting installation and runtime issues. You can read them with the `oc logs` command against the controller and webhook server deployments. 

Example command for KMM controller
    

```shell-session
$ oc logs -fn openshift-kmm deployments/kmm-operator-controller
```


Example command for KMM webhook server
    

```shell-session
$ oc logs -fn openshift-kmm deployments/kmm-operator-webhook-server
```


Example command for KMM-Hub controller
    

```shell-session
$ oc logs -fn openshift-kmm-hub deployments/kmm-operator-hub-controller
```


Example command for KMM-Hub webhook server
    

```shell-session
$ oc logs -fn openshift-kmm deployments/kmm-operator-hub-webhook-server
```


## 4.25.2. Observing events

You can observe Kernel Module Management (KMM) events on OpenShift Container Platform to monitor kmod image builds, signing, and module load or unload operations. Events attach to `Module` and `Node` objects and appear in `oc describe` output. 

### 4.25.2.1. Build & sign

KMM publishes events whenever it starts a kmod image build or observes its outcome. These events are attached to `Module` objects and are available at the end of the output of `oc describe module` command, as in the following example: 

```shell-session
$ oc describe modules.kmm.sigs.x-k8s.io kmm-ci-a
[...]
Events:
  Type    Reason          Age                From  Message
  ----    ------          ----               ----  -------
  Normal  BuildCreated    2m29s              kmm   Build created for kernel 6.6.2-201.fc39.x86_64
  Normal  BuildSucceeded  63s                kmm   Build job succeeded for kernel 6.6.2-201.fc39.x86_64
  Normal  SignCreated     64s (x2 over 64s)  kmm   Sign created for kernel 6.6.2-201.fc39.x86_64
  Normal  SignSucceeded   57s                kmm   Sign job succeeded for kernel 6.6.2-201.fc39.x86_64
```


### 4.25.2.2. Module load or unload

KMM publishes events whenever it successfully loads or unloads a kernel module on a node. These events are attached to `Node` objects and are available at the end of the output of `oc describe node` command, as in the following example: 

```shell-session
$ oc describe node my-node
[...]
Events:
  Type    Reason          Age    From  Message
  ----    ------          ----   ----  -------
[...]
  Normal  ModuleLoaded    4m17s  kmm   Module default/kmm-ci-a loaded into the kernel
  Normal  ModuleUnloaded  2s     kmm   Module default/kmm-ci-a unloaded from the kernel
```


## 4.25.3. Using the must-gather tool

To collect Kernel Module Management debugging data for Red Hat Support on OpenShift Container Platform, you can run the `oc adm must-gather` command with KMM-specific arguments. 

**Additional resources**

  * [About the must-gather tool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#about-must-gather_gathering-cluster-data)



### 4.25.3.1. Gathering data for KMM

To troubleshoot Kernel Module Management (KMM) on OpenShift Container Platform, you can gather Operator data with the `must-gather` tool and review controller manager logs. 

**Procedure**

  1. Gather the data for the KMM Operator controller manager: 

     1. Set the `MUST_GATHER_IMAGE` variable: 

```shell-session
$ export MUST_GATHER_IMAGE=$(oc get deployment -n openshift-kmm kmm-operator-controller -ojsonpath='{.spec.template.spec.containers[?(@.name=="manager")].env[?(@.name=="RELATED_IMAGE_MUST_GATHER")].value}')
```


```shell-session
$ oc adm must-gather --image="${MUST_GATHER_IMAGE}" -- /usr/bin/gather
```


Note

Use the `-n <namespace>` switch to specify a namespace if you installed KMM in a custom namespace. 

     2. Run the `must-gather` tool: 

```shell-session
$ oc adm must-gather --image="${MUST_GATHER_IMAGE}" -- /usr/bin/gather
```


  2. View the Operator logs: 

```shell-session
$ oc logs -fn openshift-kmm deployments/kmm-operator-controller
```


Example output: 

```shell-session
I0228 09:36:37.352405       1 request.go:682] Waited for 1.001998746s due to client-side throttling, not priority and fairness, request: GET:https://172.30.0.1:443/apis/machine.openshift.io/v1beta1?timeout=32s
I0228 09:36:40.767060       1 listener.go:44] kmm/controller-runtime/metrics "msg"="Metrics server is starting to listen" "addr"="127.0.0.1:8080"
I0228 09:36:40.769483       1 main.go:234] kmm/setup "msg"="starting manager"
I0228 09:36:40.769907       1 internal.go:366] kmm "msg"="Starting server" "addr"={"IP":"127.0.0.1","Port":8080,"Zone":""} "kind"="metrics" "path"="/metrics"
I0228 09:36:40.770025       1 internal.go:366] kmm "msg"="Starting server" "addr"={"IP":"::","Port":8081,"Zone":""} "kind"="health probe"
I0228 09:36:40.770128       1 leaderelection.go:248] attempting to acquire leader lease openshift-kmm/kmm.sigs.x-k8s.io...
I0228 09:36:40.784396       1 leaderelection.go:258] successfully acquired lease openshift-kmm/kmm.sigs.x-k8s.io
I0228 09:36:40.784876       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1beta1.Module"
I0228 09:36:40.784925       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1.DaemonSet"
I0228 09:36:40.784968       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1.Build"
I0228 09:36:40.785001       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1.Job"
I0228 09:36:40.785025       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1.Node"
I0228 09:36:40.785039       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module"
I0228 09:36:40.785458       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PodNodeModule" "controllerGroup"="" "controllerKind"="Pod" "source"="kind source: *v1.Pod"
I0228 09:36:40.786947       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation" "source"="kind source: *v1beta1.PreflightValidation"
I0228 09:36:40.787406       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation" "source"="kind source: *v1.Build"
I0228 09:36:40.787474       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation" "source"="kind source: *v1.Job"
I0228 09:36:40.787488       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation" "source"="kind source: *v1beta1.Module"
I0228 09:36:40.787603       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="NodeKernel" "controllerGroup"="" "controllerKind"="Node" "source"="kind source: *v1.Node"
I0228 09:36:40.787634       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="NodeKernel" "controllerGroup"="" "controllerKind"="Node"
I0228 09:36:40.787680       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation"
I0228 09:36:40.785607       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream" "source"="kind source: *v1.ImageStream"
I0228 09:36:40.787822       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="preflightvalidationocp" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidationOCP" "source"="kind source: *v1beta1.PreflightValidationOCP"
I0228 09:36:40.787853       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream"
I0228 09:36:40.787879       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="preflightvalidationocp" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidationOCP" "source"="kind source: *v1beta1.PreflightValidation"
I0228 09:36:40.787905       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="preflightvalidationocp" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidationOCP"
I0228 09:36:40.786489       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="PodNodeModule" "controllerGroup"="" "controllerKind"="Pod"
```


### 4.25.3.2. Gathering data for KMM-Hub

To collect diagnostic data for the KMM-Hub Operator on OpenShift Container Platform, you can run the `must-gather` tool with the hub controller image and review Operator logs. 

**Procedure**

  1. Gather the data for the KMM Operator hub controller manager: 

     1. Set the `MUST_GATHER_IMAGE` variable: 

```shell-session
$ export MUST_GATHER_IMAGE=$(oc get deployment -n openshift-kmm-hub kmm-operator-hub-controller -ojsonpath='{.spec.template.spec.containers[?(@.name=="manager")].env[?(@.name=="RELATED_IMAGE_MUST_GATHER")].value}')
```


```shell-session
$ oc adm must-gather --image="${MUST_GATHER_IMAGE}" -- /usr/bin/gather -u
```


Note

Use the `-n <namespace>` switch to specify a namespace if you installed KMM in a custom namespace. 

     2. Run the `must-gather` tool: 

```shell-session
$ oc adm must-gather --image="${MUST_GATHER_IMAGE}" -- /usr/bin/gather -u
```


  2. View the Operator logs: 

```shell-session
$ oc logs -fn openshift-kmm-hub deployments/kmm-operator-hub-controller
```


Example output: 

```shell-session
I0417 11:34:08.807472       1 request.go:682] Waited for 1.023403273s due to client-side throttling, not priority and fairness, request: GET:https://172.30.0.1:443/apis/tuned.openshift.io/v1?timeout=32s
I0417 11:34:12.373413       1 listener.go:44] kmm-hub/controller-runtime/metrics "msg"="Metrics server is starting to listen" "addr"="127.0.0.1:8080"
I0417 11:34:12.376253       1 main.go:150] kmm-hub/setup "msg"="Adding controller" "name"="ManagedClusterModule"
I0417 11:34:12.376621       1 main.go:186] kmm-hub/setup "msg"="starting manager"
I0417 11:34:12.377690       1 leaderelection.go:248] attempting to acquire leader lease openshift-kmm-hub/kmm-hub.sigs.x-k8s.io...
I0417 11:34:12.378078       1 internal.go:366] kmm-hub "msg"="Starting server" "addr"={"IP":"127.0.0.1","Port":8080,"Zone":""} "kind"="metrics" "path"="/metrics"
I0417 11:34:12.378222       1 internal.go:366] kmm-hub "msg"="Starting server" "addr"={"IP":"::","Port":8081,"Zone":""} "kind"="health probe"
I0417 11:34:12.395703       1 leaderelection.go:258] successfully acquired lease openshift-kmm-hub/kmm-hub.sigs.x-k8s.io
I0417 11:34:12.396334       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1beta1.ManagedClusterModule"
I0417 11:34:12.396403       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1.ManifestWork"
I0417 11:34:12.396430       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1.Build"
I0417 11:34:12.396469       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1.Job"
I0417 11:34:12.396522       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1.ManagedCluster"
I0417 11:34:12.396543       1 controller.go:193] kmm-hub "msg"="Starting Controller" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule"
I0417 11:34:12.397175       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream" "source"="kind source: *v1.ImageStream"
I0417 11:34:12.397221       1 controller.go:193] kmm-hub "msg"="Starting Controller" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream"
I0417 11:34:12.498335       1 filter.go:196] kmm-hub "msg"="Listing all ManagedClusterModules" "managedcluster"="local-cluster"
I0417 11:34:12.498570       1 filter.go:205] kmm-hub "msg"="Listed ManagedClusterModules" "count"=0 "managedcluster"="local-cluster"
I0417 11:34:12.498629       1 filter.go:238] kmm-hub "msg"="Adding reconciliation requests" "count"=0 "managedcluster"="local-cluster"
I0417 11:34:12.498687       1 filter.go:196] kmm-hub "msg"="Listing all ManagedClusterModules" "managedcluster"="sno1-0"
I0417 11:34:12.498750       1 filter.go:205] kmm-hub "msg"="Listed ManagedClusterModules" "count"=0 "managedcluster"="sno1-0"
I0417 11:34:12.498801       1 filter.go:238] kmm-hub "msg"="Adding reconciliation requests" "count"=0 "managedcluster"="sno1-0"
I0417 11:34:12.501947       1 controller.go:227] kmm-hub "msg"="Starting workers" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream" "worker count"=1
I0417 11:34:12.501948       1 controller.go:227] kmm-hub "msg"="Starting workers" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "worker count"=1
I0417 11:34:12.502285       1 imagestream_reconciler.go:50] kmm-hub "msg"="registered imagestream info mapping" "ImageStream"={"name":"driver-toolkit","namespace":"openshift"} "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream" "dtkImage"="quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:df42b4785a7a662b30da53bdb0d206120cf4d24b45674227b16051ba4b7c3934" "name"="driver-toolkit" "namespace"="openshift" "osImageVersion"="412.86.202302211547-0" "reconcileID"="e709ff0a-5664-4007-8270-49b5dff8bae9"
```
