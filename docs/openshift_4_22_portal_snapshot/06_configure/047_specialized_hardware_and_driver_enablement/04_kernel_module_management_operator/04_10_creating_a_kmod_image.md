# 4.10. Creating a kmod image

A kmod image is a standard OCI container image that holds `.ko` kernel module files for use with Kernel Module Management (KMM) on OpenShift Container Platform. You must place `.ko` files under a path that matches `<prefix>/lib/modules/[kernel-version]/`. 

Keep the following in mind when working with the `.ko` files: 

  * In most cases, `<prefix>` should be equal to `/opt`. This is the `Module` CRD’s default value. 
  * `kernel-version` must not be empty and must be equal to the kernel version the kernel modules were built for. 



In addition to the `.ko` files, the kmod image also requires the `cp` binary to be present because the `.ko` files are copied from this image to the image-loader worker pod created by the Operator. This is a minimal requirement and no other binary tool is required in the image. 

## 4.10.1. Running depmod

Run the `depmod` utlity at the end of the build process to generate `modules.dep` and `.map` files. This is especially useful if your kmod image contains several kernel modules and if one of the modules depends on another module. 

If you are building your image on OpenShift Container Platform, consider using the Driver Toolkit (DTK). For further information, see [How to use entitled image builds to build DriverContainers with UBI on OpenShift](https://cloud.redhat.com/blog/how-to-use-entitled-image-builds-to-build-drivercontainers-with-ubi-on-openshift). 

Note

You must have a Red Hat subscription to download the `kernel-devel` package. 

**Procedure**

  * Generate `modules.dep` and `.map` files for a specific kernel version by running the following command: 

```shell-session
$ depmod -b /opt ${KERNEL_FULL_VERSION}+`.
```


The following example Dockerfile shows how to run `depmod` at the end of the build: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kmm-ci-dockerfile
data:
  dockerfile: |
    ARG DTK_AUTO
    FROM ${DTK_AUTO} as builder
    ARG KERNEL_FULL_VERSION
    WORKDIR /usr/src
    RUN ["git", "clone", "https://github.com/rh-ecosystem-edge/kernel-module-management.git"]
    WORKDIR /usr/src/kernel-module-management/ci/kmm-kmod
    RUN KERNEL_SRC_DIR=/lib/modules/${KERNEL_FULL_VERSION}/build make all
    FROM registry.redhat.io/ubi9/ubi-minimal
    ARG KERNEL_FULL_VERSION
    RUN microdnf install kmod
    COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_a.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
    COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_b.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
    RUN depmod -b /opt ${KERNEL_FULL_VERSION}
```


**Additional resources**

  * [Driver Toolkit](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/driver-toolkit "Chapter 2. Driver Toolkit")



## 4.10.2. Building in the cluster

Kernel Module Management (KMM) can build kmod container images in the cluster on OpenShift Container Platform when the image does not already exist in the registry. You configure in-cluster builds through the `build` section of a kernel mapping in the `Module` CR. 

  * Provide build instructions using the `build` section of a kernel mapping. 
  * Copy the Dockerfile for your container image into a `ConfigMap` resource, under the `dockerfile` key. 
  * Ensure that the `ConfigMap` is located in the same namespace as the `Module`. 



KMM checks if the image name specified in the `containerImage` field exists. If it does, the build is skipped. 

Otherwise, KMM creates a `Build` resource to build your image. After the image is built, KMM proceeds with the `Module` reconciliation. See the following example. 

```yaml
# ...
- regexp: '^.+$'
  containerImage: "some.registry/org/<my_kmod>:${KERNEL_FULL_VERSION}"
  build:
    buildArgs:
      - name: ARG_NAME
        value: <some_value>
    secrets:
      - name: <some_kubernetes_secret>
    baseImageRegistryTLS:
      insecure: false
      insecureSkipTLSVerify: false
    dockerfileConfigMap:
      name: <my_kmod_dockerfile>
  registryTLS:
    insecure: false
    insecureSkipTLSVerify: false
```


where: 

`spec.moduleLoader.container.kernelMappings.build.buildArgs`
     Specifies build arguments. This field is optional. 
`spec.moduleLoader.container.kernelMappings.build.secrets`
     Specifies secrets. This field is optional. 
`spec.moduleLoader.container.kernelMappings.build.secrets.name`
     Specifies that the secret will be mounted in the file path of the build pod as `/run/secrets/some-kubernetes-secret`. 
`spec.moduleLoader.container.kernelMappings.build.baseImageRegistryTLS.insecure`
     Specifies an optional parameter; avoid using this parameter. If set to `true`, the build will be allowed to pull the image in the Dockerfile `FROM` instruction using plain HTTP. 
`spec.moduleLoader.container.kernelMappings.build.baseImageRegistryTLS.insecureSkipTLSVerify`
     Specifies an optional parameter; avoid using this parameter. If set to `true`, the build will skip any TLS server certificate validation when pulling the image in the Dockerfile `FROM` instruction using plain HTTP. 
`spec.moduleLoader.container.kernelMappings.build.dockerfileConfigMap`
     Specifies the Dockerfile ConfigMap. This field is required. 
`spec.moduleLoader.container.kernelMappings.registryTLS.insecure`
     Specifies an optional parameter; avoid using this parameter. If set to `true`, KMM will be allowed to check if the container image already exists using plain HTTP. 
`spec.moduleLoader.container.kernelMappings.registryTLS.insecureSkipTLSVerify`
     Specifies an optional parameter; avoid using this parameter. If set to `true`, KMM will skip any TLS server certificate validation when checking if the container image already exists. 

Successful build pods are garbage collected immediately, unless the `job.gcDelay` parameter is set in the Operator configuration. Failed build pods are always preserved and must be deleted manually by the administrator for the build to be restarted. 

**Additional resources**

  * [Build configuration resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/builds_using_buildconfig/#build-configuration)
  * [Preflight validation for Kernel Module Management (KMM) Modules](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#preflight-validation-for-kernel-module-management-kmm-modules)



## 4.10.3. Using the Driver Toolkit

To build kernel module loader images in OpenShift Container Platform, you can use the Driver Toolkit (DTK) as the first stage of a multi-stage Dockerfile. DTK provides kernel headers and build tools matched to the cluster OpenShift Container Platform version. 

**Procedure**

  1. Build the kernel modules. 
  2. Copy the `.ko` files into a smaller end-user image such as [`ubi-minimal`](https://catalog.redhat.com/software/containers/ubi9/ubi-minimal). 
  3. To leverage DTK in your in-cluster build, use the `DTK_AUTO` build argument. The value is automatically set by KMM when creating the `Build` resource. See the following example. 

```plaintext
ARG DTK_AUTO
FROM ${DTK_AUTO} as builder
ARG KERNEL_FULL_VERSION
WORKDIR /usr/src
RUN ["git", "clone", "https://github.com/rh-ecosystem-edge/kernel-module-management.git"]
WORKDIR /usr/src/kernel-module-management/ci/kmm-kmod
RUN KERNEL_SRC_DIR=/lib/modules/${KERNEL_FULL_VERSION}/build make all
FROM ubi9/ubi-minimal
ARG KERNEL_FULL_VERSION
RUN microdnf install kmod
COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_a.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_b.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
RUN depmod -b /opt ${KERNEL_FULL_VERSION}
```


**Additional resources**

  * [Driver Toolkit](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/driver-toolkit "Chapter 2. Driver Toolkit")
