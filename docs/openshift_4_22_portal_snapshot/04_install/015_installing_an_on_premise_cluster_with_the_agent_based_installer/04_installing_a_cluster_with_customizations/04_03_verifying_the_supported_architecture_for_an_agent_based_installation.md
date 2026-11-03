# 4.3. Verifying the supported architecture for an Agent-based installation

Before installing an OpenShift Container Platform cluster using the Agent-based Installer, you can optionally verify the supported architecture on which you can install the cluster. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You have downloaded the installation program. 



**Procedure**

  1. Log in to the OpenShift CLI (`oc`). 
  2. Check your release payload by running the following command: 

```shell-session
$ ./openshift-install version
```


**Example output**

```shell-session
./openshift-install 4.22.0
built from commit abc123def456
release image quay.io/openshift-release-dev/ocp-release@sha256:123abc456def789ghi012jkl345mno678pqr901stu234vwx567yz0
release architecture amd64
```


If you are using the release image with the `multi` payload, the `release architecture` displayed in the output of this command is the default architecture. 

  3. To check the architecture of the payload, run the following command: 

```shell-session
$ oc adm release info <release_image> -o jsonpath="{ .metadata.metadata}"
```


Replace `<release_image>` with the release image. For example: `quay.io/openshift-release-dev/ocp-release@sha256:123abc456def789ghi012jkl345mno678pqr901stu234vwx567yz0`. 

**Example output when the release image uses the`multi` payload**

```shell-session
{"release.openshift.io architecture":"multi"}
```


If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command.
