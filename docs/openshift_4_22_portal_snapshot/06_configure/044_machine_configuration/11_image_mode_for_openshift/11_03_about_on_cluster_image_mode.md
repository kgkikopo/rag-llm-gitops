# 11.3. About on-cluster image mode

You can use the image mode for OpenShift on-cluster build process to apply a custom layered image to your nodes by creating a `MachineOSConfig` custom resource (CR). 

When you create the object, the Machine Config Operator (MCO) creates a `MachineOSBuild` object and a builder pod. The process also creates transient objects, such as config maps, which are cleaned up after the build is complete. The `MachineOSBuild` object and the associated `builder-*` pod use the same naming scheme, `<MachineOSConfig_CR_name>-<hash>`, for example: 

**Example`MachineOSBuild` object**

```shell-session
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED
layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae   False      False      True        False         False
```


**Example builder pod**

```shell-session
NAME                                                      READY   STATUS      RESTARTS        AGE
build-layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae      2/2     Running     0               11m
```


You should not need to interact with these new objects or the `machine-os-builder` pod. However, you can use all of these resources for troubleshooting, if necessary. 

When the build is complete, the MCO pushes the new custom layered image to your repository and rolls the image out to the nodes in the associated machine config pool. You can see the digested image pull spec for the new custom layered image in the `MachineOSConfig` object. This is now the active image pull spec for this `MachineOSConfig`. 

**Example digested image pull spec**

```shell-session
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layered-9a8f89455246fa0c42ecee6ff1fa1a45
  labels:
    machineconfiguration.openshift.io/createdByOnClusterBuildsHelper: ""
  name: layered-image
# ...
status:
  currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-image@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
```


Tip

You can test a `MachineOSBuild` object to make sure it builds correctly without rolling out the custom layered image to active nodes by using a custom machine config pool that contains non-production nodes. Alternatively, you can use a custom machine config pool that has no nodes. The `MachineOSBuild` object builds even if there are no nodes for the MCO to deploy the custom layered image onto. 

You can apply a custom layered image to any machine config pool in your cluster, including the control plane, worker, or custom pools. 

Note

For single-node OpenShift clusters, you can apply a custom layered image to the control plane node only. 

Making certain changes to a `MachineOSConfig` object triggers an automatic rebuild of the associated custom layered image. You can mitigate the effects of the rebuild by pausing the machine config pool where the custom layered image is applied as described in "Pausing the machine config pools". While the pools are paused, the MCO does not roll out the newly built image to the nodes after the build is complete. However, the build runs regardless of whether the pool is paused or not. For example, if you want to remove and replace a `MachineOSCOnfig` object, pausing the machine config pools before making the change prevents the MCO from reverting the associated nodes to the base image, reducing the number of reboots needed. 

When a machine config pool is paused, the `oc get machineconfigpools` reports the following status: 

**Example output**

```shell-session
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master    rendered-master-a0b404d061a6183cc36d302363422aba    True      False      False      3              3                   3                     0                      4h14m
worker    rendered-worker-221507009cbcdec0eec8ab3ccd789d18    False     False      False      2              2                   2                     0                      4h14m
```


The `worker` machine config pool is paused, as indicated by the three `False` statuses and the `READYMACHINECOUNT` at `0`. 

After the changes have been rolled out, you can unpause the machine config pool. 

In the case of a build failure, for example due to network issues or an invalid secret, the MCO retries the build three additional times before the job fails. The MCO creates a different build pod for each build attempt. Note that the MCO automatically removes these build pods after a short period of time. Also, the affected machine config pool reports a build failure through the `ImageBuildDegraded` status condition. You can use the build pod logs to troubleshoot any build failures. 

**Example failed`MachineOSBuild` object**

```shell-session
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae   False      False      False        False        True     12m
```


You can manually rebuild your custom layered image by either modifying your `MachineOSConfig` object or applying an annotation to the `MachineOSConfig` object. For more information, see "Rebuilding an on-cluster custom layered image". 

If you used a custom machine config pool to apply an on-cluster layered image to a node, you can remove the custom layered image from the node and revert to the base image. For more information, see "Reverting an on-cluster layered node". 

You can modify an on-custom layered image as needed, to install additional packages, remove existing packages, change repositories, update secrets, or other similar changes, by editing the MachineOSConfig object. For more information, see "Modifying a custom layered image". 

## 11.3.1. On-cluster image mode known limitations

Note the following limitations when working with the on-cluster layering feature: 

  * On-cluster image mode is not supported on multi-architecture compute machines. 
  * Using multiple `MachineOSConfig` objects on the same machine config pool is not supported. You need a separate `MachineOSConfig` CR for each machine config pool where you want to use a distinct custom layered image. 
  * If you scale up a machine set that uses a custom layered image, the nodes reboot two times. The first, when the node is initially created with the base image and a second time when the custom layered image is applied. 
  * Node disruption policies are not supported on nodes with a custom layered image. However, the following machine configuration changes do not cause a new image build or the reboot of a node with an on-cluster custom layered image: 

    * Modifying the configuration files in the `/var` or `/etc` directory 
    * Adding or modifying a systemd service 
    * Changing SSH keys 
    * Removing mirroring rules from `ICSP`, `ITMS`, and `IDMS` objects 
    * Changing the trusted CA, by updating the `user-ca-bundle` configmap in the `openshift-config` namespace 

  * The following machine configuration changes do cause a new image build and a node reboot: 

    * Changing the kernel arguments 
    * Changing the `OSImageURL` parameter 
    * Adding or removing extensions 

  * The images used in creating custom layered images take up space in your push registry. Always be aware of the free space in your registry and prune the images as needed. You can automatically remove an on-cluster custom layered image from the repository by deleting the `MachineOSBuild` object that created the image. Note that the credentials provided by the registry push secret must also grant permission to delete an image from the registry. For more information, see "Removing an on-cluster custom layered image". 



## 11.3.2. Using the on-cluster image mode to apply a custom layered image

You can use the on-cluster build process to apply a custom layered image to your cluster by creating a `MachineOSConfig` custom resource (CR). 

The `MachineOSConfig` CR specifies the following parameters: 

  * the Containerfile to build 
  * the machine config pool to associate the build 
  * where the final image should be pushed and pulled from 
  * the push and pull secrets to use 



You can create only one `MachineOSConfig` CR for each machine config pool. 

**Prerequisites**

  * You have the pull secret in the `openshift-machine-config-operator` namespace that the Machine Config Operator (MCO) needs in order to pull the base operating system image from your repository. By default, the MCO uses the cluster global pull secret, which it synchronizes into the `openshift-machine-config-operator` namespace. You can add your pull secret to the OpenShift Container Platform global pull secret or you can use a different pull secret. For information on modifying the global pull secret, see "Updating the global cluster pull secret". 
  * You have the push secret of the registry that the MCO needs to push the new custom layered image to. The credentials provided by the secret must also grant permission to delete an image from the registry. 

Note

In a disconnected environment, ensure that the disconnected cluster can access the registry where you want to push the image. Image mirroring applies only to pulling images. 

  * You have the pull secret that your nodes need to pull the new custom layered image from your registry. This should be a different secret than the one used to push the image to the repository. 
  * You are familiar with how to configure a Containerfile. Instructions on how to create a Containerfile are beyond the scope of this documentation. 
  * Optional: You have a separate machine config pool for the nodes where you want to apply the custom layered image. One benefit to having a custom machine config pool for the nodes it that you can easily revert to the base image, if needed. For more information, see "Reverting an on-cluster layered node". 



**Procedure**

  1. Create a `MachineOSconfig` object: 

     1. Create a YAML file similar to the following: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  name: layered-image
spec:
  machineConfigPool:
    name: layered-image
  containerFile:
  - containerfileArch: NoArch
    content: |-
      FROM configs AS final
      RUN dnf install -y cowsay && \
        dnf clean all && \
        bootc container lint
  imageBuilder:
    imageBuilderType: Job
  baseImagePullSecret:
    name: global-pull-secret-copy
  renderedImagePushSpec: image-registry.openshift-image-registry.svc:5000/openshift/os-image:latest
  renderedImagePushSecret:
    name: builder-dockercfg-mtcl23
```


where: 

`apiVersion`
     Specifies the `machineconfiguration.openshift.io/v1` API that is required for `MachineConfig` CRs. 
`metadata.name`
     Specifies a name for the `MachineOSConfig` object. The name must match the name of the associated machine config pool. This name is used with other on-cluster image mode resources. The examples in this documentation use the name `layered-image`. 
`spec.machineConfigPool.name`
     Specifies the name of the machine config pool associated with the nodes where you want to deploy the custom layered image. The examples in this documentation use the `layered-image` machine config pool. 
`spec.containerFile`
     Specifies the Containerfile to configure the custom layered image. 
`spec.containerFile.containerfileArch`
     Specifies the architecture this containerfile is to be built for: `ARM64`, `AMD64`, `PPC64LE`, `S390X`, or `NoArch`. The default is `NoArch`, which defines a Containerfile that can be applied to any architecture. 
`spec.imageBuilder`
     Specifies the name of the image builder to use. This must be `Job`, which is a reference to the `job` object that is managing the image build. 
`spec.baseImagePullSecret`
     Specifies the name of the pull secret that the MCO needs to pull the base operating system image from the registry. By default, the global pull secret is used. This parameter is optional. 
`spec.renderedImagePushSpec`
     Specifies the image registry to push the newly-built custom layered image to. This can be any registry that your cluster has access to in the `host[:port][/namespace]/name` or `svc_name.namespace.svc[:port]/repository/name:<tag>` format. This example uses the internal OpenShift Container Platform registry. You can specify a mirror registry if you cluster is properly configured to use a mirror registry. 
`spec.renderedImagePushSecret`
     Specifies the name of the push secret that the MCO needs to push the newly-built custom layered image to that registry. 

     2. Create the `MachineOSConfig` object: 

```shell-session
$ oc create -f <filename>.yaml
```


  2. If necessary, when the `MachineOSBuild` object has been created and is in the `READY` state, modify the node spec for the nodes where you want to use the new custom layered image: 

     1. Check that the `MachineOSBuild` object is ready, by running the following command: 

```shell-session
$ oc get machineosbuild
```


When the `SUCCEEDED` value is `True`, the build is complete: 

**Example output showing that the`MachineOSBuild` object is ready**

```shell-session
NAME                                                     PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-ad5a3cad36303c363cf458ab0524e7c0-builder   False      False      True        False         False    43s
```


     2. Edit the nodes where you want to deploy the custom layered image by adding a label for the machine config pool you specified in the `MachineOSConfig` object: 

```shell-session
$ oc label node <node_name> 'node-role.kubernetes.io/<mcp_name>='
```


where: 

node-role.kubernetes.io/<mcp_name>=
     Specifies a node selector that identifies the nodes to deploy the custom layered image. 

When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the new custom layered image. 




**Verification**

  1. Verify that the new pods are ready by running the following command: 

```shell-session
$ oc get pods -n openshift-machine-config-operator
```


**Example output**

```shell-session
NAME                                                                    READY   STATUS    RESTARTS   AGE
build-layered-image-ad5a3cad36303c363cf458ab0524e7c0-hxrws              2/2     Running   0          2m40s
# ...
machine-os-builder-6fb66cfb99-zcpvq                                     1/1     Running   0          2m42s
```


The build pod where the custom layered image is building is named in the `build-<MachineOSConfig_CR_name>-<hash>` format. The `machine-os-builder-*` pod can be used for troubleshooting. 

  2. Verify the custom layered image build by running a command similar to the following: 

```shell-session
$ oc get machineconfigpool <mcp_name> -o yaml
```


**Example output**

```shell-session
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  labels:
    machineconfiguration.openshift.io/mco-built-in: ""
    pools.operator.machineconfiguration.openshift.io/layered: ""
  name: layered
# ...
status:
# ...
  conditions
# ...
  - lastTransitionTime: "2025-09-09T13:43:35Z"
    message: 'Failed to build OS image for pool worker (MachineOSBuild: worker-2d03dc921ff0c242c5892a3ef1ed1608):
      Failed: Build Failed'
    reason: BuildFailed
    status: "True"
    type: ImageBuildDegraded
```


The `reason: BuildFailed` status indicates whether the custom layered image build failed. If `False`, the build succeeded. If `True`, the build failed. You can use the build pod logs to troubleshoot any build failures. 

  3. Verify the current stage of your layered build by running the following command: 

```shell-session
$ oc get machineosbuilds
```


**Example output**

```shell-session
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-ad5a3cad36303c363cf458ab0524e7c0   False      True       False       False         False    12m
```


The `MachineOSBuild` object is named in the `<MachineOSConfig_CR_name>-<hash>` format. 

The build is complete when `BUILDING` is `False` and `SUCCEEDED` is `True`. 

  4. When the build is complete, verify that the image has been applied to the nodes in the affected pool by running a command similar to the following: 

```shell-session
$ oc describe machineconfignode/<machine_config_node_name>
```


**Example machine config node output**

```shell-session
Name:         ip-10-0-14-86.us-west-1.compute.internal
API Version:  machineconfiguration.openshift.io/v1
Kind:         MachineConfigNode
# ...
Spec:
  Config Image:
    Desired Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
  Config Version:
    Desired:  rendered-worker-d63c7736923b60b8b82492ae9a1eef40
  Node:
    Name:  ip-10-0-14-86.us-west-1.compute.internal
  Pool:
    Name:  worker
# ...
Status:
  Conditions:
# ...
    Message:               Action during update to image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3: Successfully pulled OS image image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3 from registry
    Reason:                ImagePulledFromRegistry
    Status:                False
    Type:                  ImagePulledFromRegistry
# ...
  Config Image:
    Current Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
    Desired Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
# ...
```


The digested image pull spec for the new custom layered image is in the `Spec.Config Image.Desired Image` parameter. 

Important

The `ImagePulledFromRegistry` condition is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

  5. Verify that the `MachineOSConfig` object contains a reference to the new custom layered image by running the following command: 

```shell-session
$ oc describe machineosconfig <object_name>
```


**Example digested image pull spec**

```shell-session
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layered-9a8f89455246fa0c42ecee6ff1fa1a45
  labels:
    machineconfiguration.openshift.io/createdByOnClusterBuildsHelper: ""
  name: layered-image
# ...
status:
  currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-image@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
```


where: 

`status.currentImagePullSpec`
     Specifies the digested image pull spec for the new custom layered image. 

  6. Verify that the appropriate nodes are using the new custom layered image: 

     1. Start a debug session as root for a control plane node by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


     2. Set `/host` as the root directory within the debug shell: 

```shell-session
sh-4.4# chroot /host
```


     3. Run the `rpm-ostree status` command to view that the custom layered image is in use: 

```shell-session
sh-5.1# rpm-ostree status
```


**Example output**

```shell-session
# ...
Deployments:
* ostree-unverified-registry:image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-images@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
                   Digest: sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
                  Version: 419.94.202502100215-0 (2025-02-12T19:20:44Z)
```


The `Deployments` stanza includes the digested image pull spec for the new custom layered image. 




## 11.3.3. Modify an on-cluster custom layered image

You can modify an on-cluster custom layered image, as needed, to install additional packages, remove existing packages, change the pull or push repositories, update secrets, or other similar changes. 

You can edit the `MachineOSConfig` object, apply changes to the YAML file that created the `MachineOSConfig` object, or create a new YAML file for that purpose. 

If you modify and apply the `MachineOSConfig` object YAML or create a new YAML file, the YAML overwrites any changes you made directly to the `MachineOSConfig` object itself. 

Making certain changes to a `MachineOSConfig` object triggers an automatic rebuild of the associated custom layered image. You can mitigate the effects of the rebuild by pausing the machine config pool where the custom layered image is applied as described in "Pausing the machine config pools". While the pools are paused, the MCO does not roll out the newly built image to the nodes after the build is complete. However, the build runs regardless of whether the pool is paused or not. For example, if you want to remove and replace a `MachineOSCOnfig` object, pausing the machine config pools before making the change prevents the MCO from reverting the associated nodes to the base image, reducing the number of reboots needed. 

When a machine config pool is paused, the `oc get machineconfigpools` reports the following status: 

**Example output**

```shell-session
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master    rendered-master-a0b404d061a6183cc36d302363422aba    True      False      False      3              3                   3                     0                      4h14m
worker    rendered-worker-221507009cbcdec0eec8ab3ccd789d18    False     False      False      2              2                   2                     0                      4h14m
```


The `worker` machine config pool is paused, as indicated by the three `False` statuses and the `READYMACHINECOUNT` at `0`. 

After the changes have been rolled out, you can unpause the machine config pool. 

**Prerequisites**

  * You have opted in to on-cluster image mode by creating a `MachineOSConfig` object. 



**Procedure**

  * Modify an object to update the associated custom layered image: 

    1. Edit the `MachineOSConfig` object to modify the custom layered image. The following example adds the `rngd` daemon to nodes that already have the tree package that was installed using a custom layered image. 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  name: layered-image
spec:
  machineConfigPool:
    name: layered-image
  containerFile:
  - containerfileArch: noarch
    content: |-
      FROM configs AS final

      RUN rpm-ostree install rng-tools && \
          systemctl enable rngd && \
          rpm-ostree cleanup -m && \
          bootc container lint

      RUN rpm-ostree install tree && \
          bootc container lint
  imageBuilder:
    imageBuilderType: PodImageBuilder
  baseImagePullSecret:
    name: global-pull-secret-copy
  renderedImagePushspec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-images:latest
  renderedImagePushSecret:
    name: new-secret-name
```


where: 

`spec:containerFile.content`
     Modify the Containerfile, for example to add or remove packages. This parameter is optional. 
`spec.baseImagePullSecret`
     Update the secret needed to pull the base operating system image from the registry. This parameter is optional. 
`spec.renderedImagePushspec`
     Modify the image registry to push the newly built custom layered image to. This parameter is optional. 
`spec.renderedImagePushSecret`
     Update the secret needed to push the newly built custom layered image to the registry. This parameter is optional. 

When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the cluster base Red Hat Enterprise Linux CoreOS (RHCOS) image. If your changes modify a secret only, no new build is triggered and no reboot is performed. 




**Verification**

  1. Verify that the new `MachineOSBuild` object was created by using the following command: 

```shell-session
$ oc get machineosbuild
```


**Example output**

```shell-session
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-a5457b883f5239cdcb71b57e1a30b6ef   False      False      True        False         False    4d17h
layered-image-f91f0f5593dd337d89bf4d38c877590b   False      True       False       False         False    2m41s
```


The value `True` in the `BUILDING` column indicates that the `MachineOSBuild` object is building. When the `SUCCEEDED` column reports `True`, the build is complete. 

  2. You can watch as the new machine config is rolled out to the nodes by using the following command: 

```shell-session
$ oc get machineconfigpools
```


**Example output**

```shell-session
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master    rendered-master-a0b404d061a6183cc36d302363422aba    True      False      False      3              3                   3                     0                      3h38m
worker    rendered-worker-221507009cbcdec0eec8ab3ccd789d18    False     True       False      2              2                   2                     0                      3h38m
```


The value `FALSE` in the `UPDATED` column indicates that the `MachineOSBuild` object is building. When the `UPDATED` column reports `FALSE`, the new custom layered image has rolled out to the nodes. 

  3. When the node is back in the `Ready` state, check that the changes were applied: 

     1. Open an `oc debug` session to the node by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


     2. Set `/host` as the root directory within the debug shell by running the following command: 

```shell-session
sh-5.1# chroot /host
```


     3. Use an appropriate command to verify that change was applied. The following examples shows that the `rngd` daemon was installed: 

```shell-session
sh-5.1# rpm -qa |grep rng-tools
```


**Example output**

```shell-session
rng-tools-6.17-3.fc41.x86_64
```


```shell-session
sh-5.1# rngd -v
```


**Example output**

```shell-session
rngd 6.16
```


## 11.3.4. Rebuild an on-cluster custom layered image

You can rebuild an on-cluster custom layered image by either modifying your `MachineOSConfig` object or adding an annotation to the `MachineOSConfig` object. Both of these actions trigger an automatic rebuild of the object. 

For example, you could perform a rebuild if the you change the Containerfile or need to update the `osimageurl` location in a machine config. 

After you add the annotation, the Machine Config Operator (MCO) deletes the current `MachineOSBuild` object and creates a new one in its place. When the build process is complete, the MCO automatically removes the annotation. 

**Prerequisites**

  * You have opted-in to on-cluster image mode by creating a `MachineOSConfig` object. 



**Procedure**

  * Edit the `MachineOSConfig` object to add the `machineconfiguration.openshift.io/rebuild` annotation by using the following command: 

```shell-session
$ oc edit MachineOSConfig <object_name>
```


**Example`MachineOSConfig` object**

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layering-c26d4a003432df70ee66c83981144cfa
    machineconfiguration.openshift.io/rebuild: ""
# ...
  name: layered-image
# ...
```


Add the `machineconfiguration.openshift.io/rebuild: ""` annotation to trigger a rebuild of the custom layered image. 




**Verification**

  * Check that the `MachineOSBuild` object is building by using the following command: 

```shell-session
$ oc get machineosbuild
```


**Example output**

```shell-session
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-d6b929a29c6dbfa8e4007c8069a2fd08   False      True       False       False         False    2m41s
```


The value `True` in the `BUILDING` column indicates that the `MachineOSBuild` object is building. 

  * Edit the `MachineOSConfig` object to verify that the MCO removed the `machineconfiguration.openshift.io/rebuild` annotation by using the following command: 

```shell-session
$ oc edit MachineOSConfig <object_name>
```


**Example`MachineOSConfig` object**

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layering-c26d4a003432df70ee66c83981144cfa
# ...
  name: layered-image
# ...
```


## 11.3.5. Reverting an on-cluster custom layered image

If you applied an on-cluster layered image to a node in a custom machine config pool (MCP), you can remove the custom layered image from the node and revert to the base image. 

To revert the node, remove the node from the custom MCP by removing the custom machine config pool label from the node. After you remove the label, the Machine Config Operator (MCO) reboots the node with the cluster base Red Hat Enterprise Linux CoreOS (RHCOS) image, overriding the custom layered image. 

Important

Before you remove the label, make sure the node is associated with another MCP. 

**Prerequisites**

  * You have opted-in to On-cluster image mode by creating a `MachineOSConfig` object. 
  * You have applied a `MachineOSConfig` object to a node in a custom machine config pool. 



**Procedure**

  * Remove the label from the node by using the following command: 

```shell-session
$ oc label node/<node_name> node-role.kubernetes.io/<mcp_name>-
```


When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the cluster base Red Hat Enterprise Linux CoreOS (RHCOS) image. 




**Verification**

  * Verify that the custom layered image is removed by performing any of the following checks: 

    * Check that the worker machine config pool is updating with the previous machine config: 

```shell-session
$ oc get mcp
```


**Sample output**

```shell-session
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
layered   rendered-layered-e8c8bc1de69777325003e80bc0c04b82   True      False      False      0              0                   0                     0                      4h20m
master    rendered-master-50d7bc27ee8b9ca2250383f0647ade7f    True      False      False      3              3                   3                     0                      5h39m
worker    rendered-worker-e8c8bc1de69777325003e80bc0c04b82    True      False      False      3              3                   3                     0                      5h39m
```


The custom machine config pool, named `layered`, no longer has any nodes. When the `UPDATING` field is `True`, the machine config pool is updating with the previous machine config. When the field becomes `False`, the worker machine config pool has rolled out to the previous machine config. 

    * Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME                                         STATUS                     ROLES                  AGE   VERSION
ip-10-0-148-79.us-west-1.compute.internal    Ready                      worker                 32m   v1.35.4
ip-10-0-155-125.us-west-1.compute.internal   Ready,SchedulingDisabled   worker                 35m   v1.35.4
ip-10-0-170-47.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-174-77.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-211-49.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
ip-10-0-218-151.us-west-1.compute.internal   Ready                      worker                 31m   v1.35.4
```


    * When the node is back in the `Ready` state, check that the node is using the base image: 

      1. Open an `oc debug` session to the node. For example: 

```shell-session
$ oc debug node/ip-10-0-155-125.us-west-1.compute.internal
```


      2. Set `/host` as the root directory within the debug shell: 

```shell-session
sh-4.4# chroot /host
```


      3. Run the `rpm-ostree status` command to view that the base image is in use: 

```shell-session
sh-4.4# rpm-ostree status
```


**Example output**

```plaintext
State: idle
Deployments:
* ostree-unverified-registry:registry.build05.ci.openshift.org/ci-ln-qd0hmqk/stable@sha256:a8bd32573f787f6d1c23e1d669abbefd1e31339826d06e750c0ca632ad6c414f
                   Digest: sha256:a8bd32573f787f6d1c23e1d669abbefd1e31339826d06e750c0ca632ad6c414f
                  Version: 419.96.202501202201-0 (2025-01-20T22:06:13Z)
```


## 11.3.6. Removal of an on-cluster custom layered image

You can remove an on-cluster custom layered image from the repository by deleting the `MachineOSBuild` object that created the image. Removing unneeded custom layered images prevents the images from taking up excessive space in your registry. 

The credentials provided by the registry push secret that you added to the `MachineOSBuild` object must grant the permission for deleting an image from the registry. If the delete permission is not provided, the image is not removed when you delete the `MachineOSBuild` object. 

The custom layered image is not deleted if the image is either currently in use on a node or is desired by the nodes, as indicated by the `machineconfiguration.openshift.io/currentImage` or `machineconfiguration.openshift.io/desiredImage` annotations on the node, which are added to the node when you create the `MachineOSConfig` object.
