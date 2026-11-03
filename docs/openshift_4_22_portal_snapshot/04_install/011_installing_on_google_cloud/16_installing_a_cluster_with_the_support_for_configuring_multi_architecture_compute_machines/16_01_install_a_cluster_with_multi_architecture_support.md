# 16.1. Install a cluster with multi-architecture support

You can install a cluster with multi-architecture support to use compute machines with different Central Processing Unit (CPU) architectures. Modifying your configuration file helps ensure your control plane and worker nodes deploy with the correct architecture. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You have the OpenShift Container Platform installation program. 
  * You downloaded the pull secret for your cluster. 



**Procedure**

  1. Check that the `openshift-install` binary is using the `multi` payload by running the following command: 

```shell-session
$ ./openshift-install version
```


**Example output**

```shell-session
./openshift-install 4.22.0
built from commit abc123etc
release image quay.io/openshift-release-dev/ocp-release@sha256:abc123wxyzetc
release architecture multi
default architecture amd64
```


The output must contain `release architecture multi` to indicate that the `openshift-install` binary is using the `multi` payload. 

  2. Update the `install-config.yaml` file to configure the architecture for the nodes. 

**Sample`install-config.yaml` file with multi-architecture configuration**

```yaml
apiVersion: v1
baseDomain: example.openshift.com
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform: {}
  replicas: 3
controlPlane:
  architecture: arm64
  name: master
  platform: {}
  replicas: 3
# ...
```


where: 

`compute.architecture`
     Specifies the architecture of the worker node. You can set this field to either `arm64` or `amd64`. 
`controlPlane.architecture`
     Specifies the control plane node architecture. You can set this field to either `arm64` or `amd64`.
