# 11.4. Using Out-of-cluster image mode to apply a custom layered image

You can use the image mode for OpenShift out-of-cluster build process to apply a custom layered image to your nodes by creating a `MachineOSConfig` custom resource (CR). 

When you create the object, the Machine Config Operator (MCO) reboots those nodes with the new custom layered image, overriding the base Red Hat Enterprise Linux CoreOS (RHCOS) image. 

To apply a custom layered image to your cluster, you must have the custom layered image in a repository that your cluster can access. Then, create a `MachineConfig` object that points to the custom layered image. You need a separate `MachineConfig` object for each machine config pool that you want to configure. 

Important

As soon as you apply an out-of-cluster custom image to your cluster, you effectively _take ownership_ of your custom layered images and those nodes. OpenShift Container Platform no longer automatically updates any node that uses the custom layered image. You become responsible for maintaining and updating your nodes as appropriate. If you roll back the custom layer, OpenShift Container Platform resumes automatically updating the node. See the "Updating with a RHCOS custom layered image" for important information about updating nodes that use a custom layered image. 

**Prerequisites**

  * You must create a custom layered image that is based on an OpenShift Container Platform image digest, not a tag. 

Note

You should use the same base RHCOS image that is installed on the rest of your cluster. Use the `oc adm release info --image-for rhel-coreos` command to obtain the base image being used in your cluster. 

For example, the following Containerfile creates a custom layered image from an OpenShift Container Platform 4.22 image and overrides the kernel package with one from CentOS 9 Stream: 

**Example Containerfile for a custom layer image**

```yaml
# Using a 4.22.0 image
FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...
#Install hotfix rpm
RUN rpm-ostree override replace http://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os/Packages/kernel-{,core-,modules-,modules-core-,modules-extra-}5.14.0-295.el9.x86_64.rpm && \
    rpm-ostree cleanup -m && \
    bootc container lint
```


where: 

`FROM`
     Specifies the RHCOS base image of your cluster. 
`RUN`
     Replaces the kernel packages. 

Note

Instructions on how to create a Containerfile are beyond the scope of this documentation. 

  * Because the process for building a custom layered image is performed outside of the cluster, you must use the `--authfile /path/to/pull-secret` option with Podman or Buildah. Alternatively, to have the pull secret read by these tools automatically, you can add it to one of the default file locations: `~/.docker/config.json`, `$XDG_RUNTIME_DIR/containers/auth.json`, `~/.docker/config.json`, or `~/.dockercfg`. Refer to the `containers-auth.json` man page for more information. 
  * You must push the custom layered image to a repository that your cluster can access. 



**Procedure**

  1. Create a machine config file. 

     1. Create a YAML file similar to the following: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: os-layer-custom
spec:
  osImageURL: quay.io/my-registry/custom-image@sha256...
```


where: 

`metadata.labels`
     Specifies the machine config pool to deploy the custom layered image. 
`spec.osImageURL`
     Specifies the path to the custom layered image in the repository. 

     2. Create the `MachineConfig` object: 

```shell-session
$ oc create -f <file_name>.yaml
```


Important

It is strongly recommended that you test your images outside of your production environment before rolling out to your cluster. 




**Verification**

You can verify that the custom layered image is applied by performing any of the following checks: 

  1. Check that the worker machine config pool has rolled out with the new machine config: 

     1. Check that the new machine config is created: 

```shell-session
$ oc get mc
```


**Sample output**

```shell-session
NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
00-master                                          5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
00-worker                                          5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
01-master-container-runtime                        5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
01-master-kubelet                                  5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
01-worker-container-runtime                        5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
01-worker-kubelet                                  5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
99-master-generated-registries                     5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
99-master-ssh                                                                                 3.2.0             98m
99-worker-generated-registries                     5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
99-worker-ssh                                                                                 3.2.0             98m
os-layer-custom                                                                                                 10s
rendered-master-15961f1da260f7be141006404d17d39b   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
rendered-worker-5aff604cb1381a4fe07feaf1595a797e   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
rendered-worker-5de4837625b1cbc237de6b22bc0bc873   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             4s
```


The `os-layer-custom` object is the newly created machine config. The `rendered-worker-5de4837625b1cbc237de6b22bc0bc873` object is the newly created rendered machine config. 

     2. Check that the `osImageURL` value in the new machine config points to the expected image: 

```shell-session
$ oc describe mc rendered-worker-5de4837625b1cbc237de6b22bc0bc873
```


**Example output**

```shell-session
Name:         rendered-worker-5de4837625b1cbc237de6b22bc0bc873
Namespace:
Labels:       <none>
Annotations:  machineconfiguration.openshift.io/generated-by-controller-version: 5bdb57489b720096ef912f738b46330a8f577803
              machineconfiguration.openshift.io/release-image-version: 4.22.0-ec.3
API Version:  machineconfiguration.openshift.io/v1
Kind:         MachineConfig
...
  Os Image URL: quay.io/my-registry/custom-image@sha256...
```


     3. Check that the associated machine config pool is updated with the new machine config: 

```shell-session
$ oc get mcp
```


**Sample output**

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-15961f1da260f7be141006404d17d39b   True      False      False      3              3                   3                     0                      39m
worker   rendered-worker-5de4837625b1cbc237de6b22bc0bc873   True      False      False      3              0                   0                     0                      39m
```


When the `UPDATING` field is `True`, the machine config pool is updating with the new machine config. In this case, you will not see the new machine config listed in the output. When the field becomes `False`, the worker machine config pool has rolled out to the new machine config. 

     4. Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied: 

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


  2. When the node is back in the `Ready` state, check that the node is using the custom layered image: 

     1. Open an `oc debug` session to the node. For example: 

```shell-session
$ oc debug node/ip-10-0-155-125.us-west-1.compute.internal
```


     2. Set `/host` as the root directory within the debug shell: 

```shell-session
sh-4.4# chroot /host
```


     3. Run the `rpm-ostree status` command to view that the custom layered image is in use: 

```shell-session
sh-4.4# sudo rpm-ostree status
```


**Example output**

```plaintext
State: idle
Deployments:
* ostree-unverified-registry:quay.io/my-registry/...
                   Digest: sha256:...
```


## 11.4.1. Reverting an out-of-cluster node

You can revert an out-of-cluster custom layered image from the nodes in specific machine config pools. The Machine Config Operator (MCO) reboots those nodes with the cluster base Red Hat Enterprise Linux CoreOS (RHCOS) image, overriding the custom layered image. 

To remove a Red Hat Enterprise Linux CoreOS (RHCOS) custom layered image from your cluster, you need to delete the machine config that applied the image. 

**Procedure**

  * Delete the machine config that applied the custom layered image. 

```shell-session
$ oc delete mc os-layer-custom
```


After deleting the machine config, the nodes reboot. 




**Verification**

You can verify that the custom layered image is removed by performing any of the following checks: 

  1. Check that the worker machine config pool is updating with the previous machine config: 

```shell-session
$ oc get mcp
```


**Sample output**

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-6faecdfa1b25c114a58cf178fbaa45e2   True      False      False      3              3                   3                     0                      39m
worker   rendered-worker-6b000dbc31aaee63c6a2d56d04cd4c1b   False     True       False      3              0                   0                     0                      39m
```


When the `UPDATING` field is `True`, the machine config pool is updating with the previous machine config. When the field becomes `False`, the worker machine config pool has rolled out to the previous machine config. 

  2. Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied: 

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


  3. When the node is back in the `Ready` state, check that the node is using the base image: 

     1. Open an `oc debug` session to the node by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


     2. Set `/host` as the root directory within the debug shell by running the following command: 

```shell-session
sh-5.1# chroot /host
```


     3. Run the `rpm-ostree status` command to view that the custom layered image is in use: 

```shell-session
sh-5.1# sudo rpm-ostree status
```


**Example output**

```plaintext
State: idle
Deployments:
* ostree-unverified-registry:podman pull quay.io/openshift-release-dev/ocp-release@sha256:e2044c3cfebe0ff3a99fc207ac5efe6e07878ad59fd4ad5e41f88cb016dacd73
                   Digest: sha256:e2044c3cfebe0ff3a99fc207ac5efe6e07878ad59fd4ad5e41f88cb016dacd73
```
