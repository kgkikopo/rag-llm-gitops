# 11.5. Applying a custom layered image during OpenShift Container Platform installation

You can use the standard OpenShift Container Platform installation process to apply a custom layered image to your nodes by adding a `MachineOSConfig` custom resource (CR) YAML and a push secret YAML to the `<installation_directory>/manifests/` directory. 

This allows you to use image mode for OpenShift to apply additional functionality to specific nodes upon cluster installation. 

After the installation, if you modify a machine config pool or update the OpenShift Container Platform version, the Machine Config Operator (MCO) builds and applies a new custom layered image, and pushes the updated image to your repository. 

**Prerequisites**

  * You have a custom layered image in a repository that your cluster can access. 

**Example containerFile for a custom layered image**

```yaml
FROM quay.io/centos/centos:stream9 AS centos
RUN dnf install -y epel-release

FROM [rhel-coreos image] AS configs
COPY --from=centos /etc/yum.repos.d /etc/yum.repos.d
COPY --from=centos /etc/pki/rpm-gpg/RPM-GPG-KEY-* /etc/pki/rpm-gpg/
RUN sed -i 's/\$stream/9-stream/g' /etc/yum.repos.d/centos*.repo && \
    rpm-ostree install cowsay && \
    ostree container commit
```


  * You have a repository and any needed secret where the MCO can push any updated custom layered images. 



**Procedure**

  1. Create a YAML file for the `MachineOSConfig` object similar to the following: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  name: worker
  annotations:
    machineconfiguration.openshift.io/pre-built-image: "quay.io/myorg/custom-rhcos@sha256:abc123..."
spec:
  machineConfigPool:
    name: worker
  imageBuilder:
    imageBuilderType: Job
  renderedImagePushSpec: quay.io/your-registry/layered-rhcos:latest
  renderedImagePushSecret:
    name: push-secret
  containerFile:
  - containerfileArch: NoArch
    content: |
      FROM configs AS final
      RUN rpm-ostree install cowsay && \
        ostree container commit
```


where: 

`metadata.name`
     Specifies a name for the `MachineOSConfig` object. The name must match the name of the associated machine config pool. 
`metadata.annotations.machineconfiguration.openshift.io/pre-built-image`
     Specifies the digested image pull spec of your custom layered image. 
`spec.machineConfigPool`
     Specifies the name of the machine config pool associated with the nodes where you want to deploy the custom layered image. 
`spec.imageBuilder.imageBuilderType`
     Specifies the name of the image builder to use. This must be `Job`, which is a reference to the `job` object that is managing the image build. 
`spec.renderedImagePushSpec`
     Specifies an image registry to push any updated custom layered images to, if needed, after the installation process is complete. This can be any registry that your cluster has access to in the `host[:port][/namespace]/name` or `svc_name.namespace.svc[:port]/repository/name:<tag>` format. You can specify a mirror registry if you cluster is properly configured to use a mirror registry. 
`spec.renderedImagePushSecret.name`
     Specifies the name of the push secret needed by the MCO to push the updated custom layered image to that registry. 
`spec.containerFile`
     Specifies the containerFile that you used to create the custom layered image. 

  2. Create a YAML file for the push secret similar to the following: 

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: push-secret
  namespace: openshift-machine-config-operator
data:
  .dockerconfigjson: secret
type: kubernetes.io/dockerconfigjson
```


  3. When the `manifests` directory is available, add the `MachineOSConfig` YAML to the directory by using a command similar to the following: 

```shell-session
$ cp <file-name>.yaml manifests/
```


where: 

`file-name`
     Specifies the YAML file for the `MachineOSConfig` object. 

  4. Add the push secret YAML to the `manifests` directory by using a command similar to the following: 

```shell-session
$ cp <file-name>.yaml manifests/
```


where: 

`file-name`
     Specifies the YAML file for the push secret. 

  5. Continue with the installation process as usual. 



**Verification**

  * After the installation is complete, check that the `MachineOSConfig` object displays the `PreBuiltImageSeeded` status as `True` and contains a reference to the custom layered image by using the following command: 

```shell-session
$ oc get machineosconfigs.machineconfiguration.openshift.io -o yaml
```


**Example output**

```yaml
apiVersion: v1
items:
- apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineOSConfig
  metadata:
    annotations:
      machineconfiguration.openshift.io/current-machine-os-build: worker-4cedbc10da849ae7019288febc3a2d17
# ...
  status:
    conditions:
    - lastTransitionTime: "2025-11-19T13:32:17Z"
      message: MachineOSConfig seeded with pre-built image "quay.io/myorg/custom-rhcos@sha256:abc123..."
      reason: PreBuiltImageSeeded
      status: "True"
      type: Seeded
    currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/layered-rhcos@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
```


where: 

`items.status.conditions.reason.PreBuiltImageSeeded.True`
     Specifies that the associated nodes were created using your custom layered image. 
`items.status.currentImagePullSpec`
     Specifies the digested image pull spec for the new custom layered image.
