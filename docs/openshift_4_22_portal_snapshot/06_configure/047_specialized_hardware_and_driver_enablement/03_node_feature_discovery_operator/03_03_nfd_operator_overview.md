# 3.3. NFD Operator overview

The Node Feature Discovery (NFD) Operator orchestrates all resources needed to run the NFD daemon set. You create a `NodeFeatureDiscovery` custom resource (CR), and the Operator creates the operand components in the selected namespace. 

As a cluster administrator, you can create a `NodeFeatureDiscovery` CR by using the OpenShift CLI (`oc`) or the web console. 

Note

Starting with version 4.12, the `operand.image` field in the `NodeFeatureDiscovery` CR is mandatory. If the NFD Operator is deployed by using Operator Lifecycle Manager (OLM), OLM automatically sets the `operand.image` field. If you create the `NodeFeatureDiscovery` CR by using the OpenShift Container Platform CLI or the OpenShift Container Platform web console, you must set the `operand.image` field explicitly. 

## 3.3.1. Create a NodeFeatureDiscovery CR by using the CLI

Create a `NodeFeatureDiscovery` CR instance by using the OpenShift CLI (`oc`) to deploy the NFD operand and enable hardware feature detection on your cluster nodes. 

Note

The `spec.operand.image` setting requires a `-rhel9` image to be defined for use with OpenShift Container Platform releases 4.13 and later. 

The following example shows the use of `-rhel9` to acquire the correct image. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster. 
  * You installed the OpenShift CLI (`oc`). 
  * You logged in as a user with `cluster-admin` privileges. 
  * You installed the NFD Operator. 



**Procedure**

  1. Create a `NodeFeatureDiscovery` CR: 

**Example`NodeFeatureDiscovery` CR**

```yaml
apiVersion: nfd.openshift.io/v1
kind: NodeFeatureDiscovery
metadata:
  name: nfd-instance
  namespace: openshift-nfd
spec:
  instance: "" # instance is empty by default
  topologyupdater: false # False by default
  operand:
    image: registry.redhat.io/openshift4/ose-node-feature-discovery-rhel9:v4.22
    imagePullPolicy: Always
  workerConfig:
    configData: |
      core:
      #  labelWhiteList:
      #  noPublish: false
        sleepInterval: 60s
      #  sources: [all]
      #  klog:
      #    addDirHeader: false
      #    alsologtostderr: false
      #    logBacktraceAt:
      #    logtostderr: true
      #    skipHeaders: false
      #    stderrthreshold: 2
      #    v: 0
      #    vmodule:
      ##   NOTE: the following options are not dynamically run-time configurable
      ##         and require a nfd-worker restart to take effect after being changed
      #    logDir:
      #    logFile:
      #    logFileMaxSize: 1800
      #    skipLogHeaders: false
      sources:
        cpu:
          cpuid:
      #     NOTE: whitelist has priority over blacklist
            attributeBlacklist:
              - "BMI1"
              - "BMI2"
              - "CLMUL"
              - "CMOV"
              - "CX16"
              - "ERMS"
              - "F16C"
              - "HTT"
              - "LZCNT"
              - "MMX"
              - "MMXEXT"
              - "NX"
              - "POPCNT"
              - "RDRAND"
              - "RDSEED"
              - "RDTSCP"
              - "SGX"
              - "SSE"
              - "SSE2"
              - "SSE3"
              - "SSE4.1"
              - "SSE4.2"
              - "SSSE3"
            attributeWhitelist:
        kernel:
          kconfigFile: "/path/to/kconfig"
          configOpts:
            - "NO_HZ"
            - "X86"
            - "DMI"
        pci:
          deviceClassWhitelist:
            - "0200"
            - "03"
            - "12"
          deviceLabelFields:
            - "class"
  customConfig:
    configData: |
          - name: "more.kernel.features"
            matchOn:
            - loadedKMod: ["example_kmod3"]
```


where: 

`operand.image`
     Specifies the required operand image. 

  2. Create the `NodeFeatureDiscovery` CR by running the following command: 

```shell-session
$ oc apply -f <filename>
```


**Verification**

  1. Check that the `NodeFeatureDiscovery` CR was created by running the following command: 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME                                      READY   STATUS    RESTARTS   AGE
nfd-controller-manager-7f86ccfb58-vgr4x   2/2     Running   0          11m
nfd-master-hcn64                          1/1     Running   0          60s
nfd-master-lnnxx                          1/1     Running   0          60s
nfd-master-mp6hr                          1/1     Running   0          60s
nfd-worker-vgcz9                          1/1     Running   0          60s
nfd-worker-xqbws                          1/1     Running   0          60s
```


A successful deployment shows a `Running` status. 




## 3.3.2. Creating a NodeFeatureDiscovery CR by using the CLI in a disconnected environment

Create a `NodeFeatureDiscovery` CR instance in a disconnected environment by using the OpenShift CLI (`oc`) and a mirror registry to deploy the NFD operand without direct internet access. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster. 
  * You installed the OpenShift CLI (`oc`). 
  * You logged in as a user with `cluster-admin` privileges. 
  * You installed the NFD Operator. 
  * You have access to a mirror registry with the required images. 
  * You installed the `skopeo` CLI tool. 



**Procedure**

  1. Determine the digest of the registry image: 

     1. Run the following command: 

```shell-session
$ skopeo inspect docker://registry.redhat.io/openshift4/ose-node-feature-discovery:<openshift_version>
```


**Example command**

```shell-session
$ skopeo inspect docker://registry.redhat.io/openshift4/ose-node-feature-discovery:v4.12
```


     2. Inspect the output to identify the image digest: 

**Example output**

```shell-session
{
  ...
  "Digest": "sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
  ...
}
```


  2. Use the `skopeo` CLI tool to copy the image from `registry.redhat.io` to your mirror registry, by running the following command: 

```shell-session
$ skopeo copy docker://registry.redhat.io/openshift4/ose-node-feature-discovery@<image_digest> docker://<mirror_registry>/openshift4/ose-node-feature-discovery@<image_digest>
```


**Example command**

```shell-session
$ skopeo copy docker://registry.redhat.io/openshift4/ose-node-feature-discovery@sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef docker://<your_mirror_registry>/openshift4/ose-node-feature-discovery@sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```


  3. Create a `NodeFeatureDiscovery` CR: 

**Example`NodeFeatureDiscovery` CR**

```yaml
apiVersion: nfd.openshift.io/v1
kind: NodeFeatureDiscovery
metadata:
  name: nfd-instance
spec:
  operand:
    image: <mirror_registry>/openshift4/ose-node-feature-discovery@<image_digest>
    imagePullPolicy: Always
  workerConfig:
    configData: |
      core:
      #  labelWhiteList:
      #  noPublish: false
        sleepInterval: 60s
      #  sources: [all]
      #  klog:
      #    addDirHeader: false
      #    alsologtostderr: false
      #    logBacktraceAt:
      #    logtostderr: true
      #    skipHeaders: false
      #    stderrthreshold: 2
      #    v: 0
      #    vmodule:
      ##   NOTE: the following options are not dynamically run-time configurable
      ##         and require a nfd-worker restart to take effect after being changed
      #    logDir:
      #    logFile:
      #    logFileMaxSize: 1800
      #    skipLogHeaders: false
      sources:
        cpu:
          cpuid:
      #     NOTE: whitelist has priority over blacklist
            attributeBlacklist:
              - "BMI1"
              - "BMI2"
              - "CLMUL"
              - "CMOV"
              - "CX16"
              - "ERMS"
              - "F16C"
              - "HTT"
              - "LZCNT"
              - "MMX"
              - "MMXEXT"
              - "NX"
              - "POPCNT"
              - "RDRAND"
              - "RDSEED"
              - "RDTSCP"
              - "SGX"
              - "SSE"
              - "SSE2"
              - "SSE3"
              - "SSE4.1"
              - "SSE4.2"
              - "SSSE3"
            attributeWhitelist:
        kernel:
          kconfigFile: "/path/to/kconfig"
          configOpts:
            - "NO_HZ"
            - "X86"
            - "DMI"
        pci:
          deviceClassWhitelist:
            - "0200"
            - "03"
            - "12"
          deviceLabelFields:
            - "class"
  customConfig:
    configData: |
          - name: "more.kernel.features"
            matchOn:
            - loadedKMod: ["example_kmod3"]
```


where: 

`operand.image`
     Specifies the required operand image. 

  4. Create the `NodeFeatureDiscovery` CR by running the following command: 

```shell-session
$ oc apply -f <filename>
```


**Verification**

  1. Check the status of the `NodeFeatureDiscovery` CR by running the following command: 

```shell-session
$ oc get nodefeaturediscovery nfd-instance -o yaml
```


  2. Check that the pods are running without `ImagePullBackOff` errors by running the following command: 

```shell-session
$ oc get pods -n <nfd_namespace>
```


## 3.3.3. Create a NodeFeatureDiscovery CR by using the web console

Create a `NodeFeatureDiscovery` CR by using the OpenShift Container Platform web console to deploy the NFD operand and enable hardware feature detection on your cluster nodes. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster. 
  * You logged in as a user with `cluster-admin` privileges. 
  * You installed the NFD Operator. 



**Procedure**

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. In the **Node Feature Discovery** section, under **Provided APIs** , click **Create instance**. 
  3. Edit the values of the `NodeFeatureDiscovery` CR. 
  4. Click **Create**. 

Note

Starting with version 4.12, the `operand.image` field in the `NodeFeatureDiscovery` CR is mandatory. If the NFD Operator is deployed by using Operator Lifecycle Manager (OLM), OLM automatically sets the `operand.image` field. If you create the `NodeFeatureDiscovery` CR by using the OpenShift Container Platform CLI or the OpenShift Container Platform web console, you must set the `operand.image` field explicitly.
