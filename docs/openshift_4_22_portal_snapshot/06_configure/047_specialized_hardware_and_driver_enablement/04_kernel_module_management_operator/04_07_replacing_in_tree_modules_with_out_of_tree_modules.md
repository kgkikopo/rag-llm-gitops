# 4.7. Replacing in-tree modules with out-of-tree modules

You can use Kernel Module Management (KMM) to build kernel modules that can be loaded or unloaded into the kernel on demand. These modules extend the functionality of the kernel without the need to reboot the system. Modules can be configured as built-in or dynamically loaded. 

Dynamically loaded modules include in-tree modules and out-of-tree (OOT) modules. In-tree modules are internal to the Linux kernel tree, that is, they are already part of the kernel. Out-of-tree modules are external to the Linux kernel tree. They are generally written for development and testing purposes, such as testing the new version of a kernel module that is shipped in-tree, or to deal with incompatibilities. 

Some modules that are loaded by KMM could replace in-tree modules that are already loaded on the node. To unload in-tree modules before loading your module, set the value of the `.spec.moduleLoader.container.inTreeModulesToRemove` field to the modules that you want to unload. The following example demonstrates module replacement for all kernel mappings: 

```yaml
# ...
spec:
  moduleLoader:
    container:
      modprobe:
        moduleName: mod_a

      inTreeModulesToRemove: [mod_a, mod_b]
```


In this example, the `moduleLoader` pod uses `inTreeModulesToRemove` to unload the in-tree `mod_a` and `mod_b` before loading `mod_a` from the `moduleLoader` image. When the `moduleLoader`pod is terminated and `mod_a` is unloaded, `mod_b` is not loaded again. 

The following is an example for module replacement for specific kernel mappings: 

```yaml
# ...
spec:
  moduleLoader:
    container:
      kernelMappings:
        - literal: 6.0.15-300.fc37.x86_64
          containerImage: "some.registry/org/my-kmod:${KERNEL_FULL_VERSION}"
          inTreeModulesToRemove: [<module_name>, <module_name>]
```


**Additional resources**

  * [Building a linux kernel module](https://fastbitlab.com/building-a-linux-kernel-module/)



## 4.7.1. Example Module CR

Use this annotated `Module` custom resource example as a reference when you configure kernel module loading, device plugins, builds, and signing in OpenShift Container Platform. 

```yaml
apiVersion: kmm.sigs.x-k8s.io/v1beta1
kind: Module
metadata:
  name: <my_kmod>
spec:
  moduleLoader:
    container:
      modprobe:
        moduleName: <my_kmod>
        dirName: /opt
        firmwarePath: /firmware
        parameters:
          - param=1
      kernelMappings:
        - literal: 6.0.15-300.fc37.x86_64
          containerImage: some.registry/org/my-kmod:6.0.15-300.fc37.x86_64
        - regexp: '^.+\fc37\.x86_64$'
          containerImage: "some.other.registry/org/<my_kmod>:${KERNEL_FULL_VERSION}"
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
          sign:
            certSecret:
              name: <cert_secret>
            keySecret:
              name: <key_secret>
            filesToSign:
              - /opt/lib/modules/${KERNEL_FULL_VERSION}/<my_kmod>.ko
          registryTLS:
            insecure: false
            insecureSkipTLSVerify: false
    serviceAccountName: <sa_module_loader>
  devicePlugin:
    container:
      image: some.registry/org/device-plugin:latest
      env:
        - name: MY_DEVICE_PLUGIN_ENV_VAR
          value: SOME_VALUE
      volumeMounts:
        - mountPath: /some/mountPath
          name: <device_plugin_volume>
    volumes:
      - name: <device_plugin_volume>
        configMap:
          name: <some_configmap>
    serviceAccountName: <sa_device_plugin>
  imageRepoSecret:
    name: <secret_name>
  selector:
    node-role.kubernetes.io/worker: ""
```


where: 

`spec.moduleLoader.container.modprobe.moduleName`
     Specifies the name of the module to load. This parameter is required. 
`spec.moduleLoader.container.modprobe.dirName`
     Specifies the directory name to use for the module. This parameter is optional. 
`spec.moduleLoader.container.modprobe.firmwarePath`
     Specifies the path to the firmware to use for the module. This field is optional. Copies the contents of this path into the path specified in `worker.setFirmwareClassPath` (which is preset to `/var/lib/firmware`) of the `kmm-operator-manager-config` config map. This action occurs before `modprobe` is called to insert the kernel module. 
`spec.moduleLoader.container.modprobe.parameters`
     Specifies the parameters to pass to the module. This parameter is optional. 
`spec.moduleLoader.container.kernelMappings`
     Specifies at least one kernel item. This parameter is required. 
`spec.moduleLoader.container.kernelMappings.regexp`
     Specifies a tag or digest. Foreach node running a kernel matching the regular expression, KMM checks if you have included a tag or a digest. If you have not specified a tag or digest in the container image, then the validation webhook returns an error and does not apply the module. 
`spec.moduleLoader.container.kernelMappings.regexp`
     Specifies that for any other kernel, build the image using the Dockerfile in the `my-kmod` ConfigMap. 
`spec.moduleLoader.container.kernelMappings.containerImage`
     Specifies the container image that holds the customer’s kmods. This container should contain the `cp` binary. 
`spec.moduleLoader.container.kernelMappings.build.buildArgs`
     Specifies an optional field. 
`spec.moduleLoader.container.kernelMappings.build.secrets`
     Specifies that a value for `some-kubernetes-secret` can be obtained from the build environment at `/run/secrets/some-kubernetes-secret`. This field is optional. 
`spec.moduleLoader.container.kernelMappings.build.baseImageRegistryTLS`
     This fied has no effect. When building kmod images or signing kmods within a kmod image, you might sometimes need to pull base images from a registry that serves a certificate signed by an untrusted Certificate Authority (CA). In order for KMM to trust that CA, it must also trust the new CA by replacing the cluster’s CA bundle. See "Replacing the CA Bundle certificate" to learn how to replace the cluster’s CA bundle. 
`spec.moduleLoader.container.kernelMappings.build.baseImageRegistryTLS.insecureSkipTLSVerify`
     Specifies to an optional parameter; avoid using it. If set to `true`, the build skips any TLS server certificate validation when pulling the image in the Dockerfile `FROM` instruction using plain HTTP. This parameter is optional. 
`spec.moduleLoader.container.kernelMappings.build.dockerfileConfigMap`
     Specifies the `dockerfileConfigMap` parameter. This parameter is required. 
`spec.moduleLoader.container.kernelMappings.sign.certSecret`
     Specifies the `certSecret` parameter. This parameter is required. 
`spec.moduleLoader.container.kernelMappings.sign.keySecret`
     Specifies the `keySecret` parameter. This parameter is required. 
`spec.moduleLoader.container.kernelMappings.registryTLS`
     Specifies an optional parameter; avoid using it. If set to `true`, KMM is allowed to check if the container image already exists using plain HTTP. 
`spec.moduleLoader.container.kernelMappings.registryTLS.insecure`
     Specifies a optional parameter; avoid using it. If set to `true`, KMM skips any TLS server certificate validation when checking if the container image already exists. 
`spec.moduleLoader.serviceAccountName`
     Specifies the `serviceAccountName` parameter. This parameter is optional. 
`spec.devicePlugin`
     Specifies the `devicePlugin` parameter. This parameter is optional. 
`spec.devicePlugin.container.image`
     Specifies the `image` parameter. This parameter is required if the device plugin section is present. 
`spec.devicePlugin.container.volumeMounts`
     Specifies the `volumeMounts` parameter. This parameter is optional. 
`spec.devicePlugin.volumes`
     Specifies the `volumes` parameter. This parameter is optional. 
`spec.devicePlugin.serviceAccountName`
     Specifies the `serviceAccountName` parameter. This parameter is optional. 
`spec.imageRepoSecret`
     Specifies the `imageRepoSecret` parameter. This parameter is used to pull module loader and device plugin images. 

**Additional resources**

  * [Replacing the CA Bundle certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#ca-bundle-replacing_updating-ca-bundle)
