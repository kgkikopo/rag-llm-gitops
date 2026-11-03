# 5.6. Mirror registry support for Windows containers

When using the Windows Machine Config Operator (WMCO), your Windows workloads can pull images from a registry mirror rather than from a public registry by using an `ImageDigestMirrorSet` (IDMS) or `ImageTagMirrorSet` (ITMS) object to configure your cluster to pull images from the mirror registry. 

A mirror registry has the following benefits: 

  * Avoids public registry outages 
  * Speeds up node and pod creation 
  * Pulls images from behind your organization’s firewall 



A mirror registry can also be used with a OpenShift Container Platform cluster in a disconnected, or air-gapped, network. A _disconnected network_ is a restricted network without direct internet connectivity. Because the cluster does not have access to the internet, any external container images cannot be referenced. 

Using a mirror registry requires the following general steps: 

  * Create the mirror registry, using a tool such as Red Hat Quay. 
  * Create a container image registry credentials file. 
  * Copy the images from your online image repository to your mirror registry. 



For information about these steps, see "About disconnected installation mirroring." 

After creating the mirror registry and mirroring the images, you can use an `ImageDigestMirrorSet` (IDMS) or `ImageTagMirrorSet` (ITMS) object to configure your cluster to pull images from the mirror registry without needing to update each of your pod specs. The IDMS and ITMS objects redirect requests to pull images from a repository on a source image registry and have it resolved by the mirror repository instead. 

If changes are made to the IDMS or ITMS object, the WMCO automatically updates the appropriate `hosts.toml` file on your Windows nodes with the new information. Note that the WMCO sequentially updates each Windows node when mirror settings are changed. As such, the time required for these updates increases with the number of Windows nodes in the cluster. 

Because Windows nodes configured by the WMCO rely on the containerd container runtime, the WMCO ensures that the containerd configuration files are up-to-date with the registry settings. For new nodes, these files are copied to the instances upon creation. For existing nodes, after activating the mirror registry, the registry controller uses SSH to access each node and copy the generated configuration files, replacing any existing files. 

You can use a mirror registry with machine set or Bring-Your-Own-Host (BYOH) Windows nodes. 

When using an IDMS or ITMS object to mirror container images on Windows nodes, take note of the following behaviors that differ from Linux nodes: 

  * Mirroring on Windows nodes works on the registry level, rather than on the image level used by Linux nodes. As such, Windows images mirrored by using IDMS or ITMS objects have specific naming requirements. 

The final portion of the namespace and the image name of the mirror image must match the image being mirrored. For example, when mirroring the `mcr.microsoft.com/oss/kubernetes/pause:3.9` image, the mirror must be in the `$mirrorRegistry/<organization>/oss/kubernetes/pause:3.9` format, where `$org` can be any organization name or namespace or excluded entirely. Some valid values are `$mirrorRegistry/oss/kubernetes/pause:3.9`, `$mirrorRegistry/custom/oss/kubernetes/pause:3.9`, and `$mirrorRegistry/x/y/z/oss/kubernetes/pause:3.9`. 

  * A Windows node takes the ITMS object and uses it to configure registry-wide mirrors. In the following example, configuring `quay.io/remote-org/image` to mirror to `quay.io/my-org/image` results in the Windows node using that mirror for all images from `quay.io/remote-org`. As such, `quay.io/remote-org/image:tag` uses the `quay.io/my-org/image:tag` image, as expected, but another container using `quay.io/remote-org/different-image:tag` would also try to use the `quay.io/remote-org/different-image:tag` mirror. This can cause unintended behavior if it is not accounted for. 

For this reason, specify container images using a digest by an IDMS object instead of an ITMS object. Using a digest can prevent the wrong container image from being used, by ensuring that the image the container specifies and the image being pulled have the same digest. 




## 5.6.1. Understanding image registry repository mirroring

You must mirror images to update clusters in disconnected environments. 

By setting up container registry repository mirroring, you can perform the following tasks: 

  * Configure your OpenShift Container Platform cluster to redirect requests to pull images from a repository on a source image registry and have it resolved by a repository on a mirrored image registry. 
  * Identify multiple mirrored repositories for each target repository, to make sure that if one mirror is down, another can be used. 



Repository mirroring in OpenShift Container Platform includes the following attributes: 

  * Image pulls are resilient to registry downtimes. 
  * Clusters in disconnected environments can pull images from critical locations, such as `quay.io`, and have registries behind a company firewall provide the requested images. 
  * A particular order of registries is tried when an image pull request is made, with the permanent registry typically being the last one tried. 
  * The mirror information you enter is added to the appropriate `hosts.toml` containerd configuration file(s) on every Windows node in the OpenShift Container Platform cluster. 
  * When a node makes a request for an image from the source repository, it tries each mirrored repository in turn until it finds the requested content. If all mirrors fail, the cluster tries the source repository. If successful, the image is pulled to the node. 



You can set up repository mirroring in the following ways: 

  * At OpenShift Container Platform installation: 

By pulling container images needed by OpenShift Container Platform and then bringing those images behind your company’s firewall, you can install OpenShift Container Platform into a data center that is in a disconnected environment. 

  * After OpenShift Container Platform installation: 

If you did not configure mirroring during OpenShift Container Platform installation, you can do so postinstallation by using any of the following custom resource (CR) objects: 

    * `ImageDigestMirrorSet` (IDMS). This object allows you to pull images from a mirrored registry by using digest specifications. The IDMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails. 
    * `ImageTagMirrorSet` (ITMS). This object allows you to pull images from a mirrored registry by using image tags. The ITMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails. 




Each of these custom resource objects identify the following information: 

  * The source of the container image repository you want to mirror. 
  * A separate entry for each mirror repository you want to offer the content 



Note the following actions and how they affect node drain behavior: 

  * If you create an IDMS or ICSP CR object, the MCO does not drain or reboot the node. 
  * If you create an ITMS CR object, the MCO drains and reboots the node. 
  * If you delete an ITMS or IDMS CR object, the MCO drains and reboots the node. 
  * If you modify an ITMS or IDMS CR object, the MCO drains and reboots the node. 



The Windows Machine Config Operator (WMCO) watches for changes to the IDMS and ITMS resources and generates a set of `hosts.toml` containerd configuration files, one file for each source registry, with those changes. The WMCO then updates any existing Windows nodes to use the new registry configuration. 

Note

The IDMS and ITMS objects must be created before you can add Windows nodes using a mirrored registry. 

## 5.6.2. Configure image registry repository mirroring

You can create postinstallation mirror configuration custom resources (CR) to redirect image pull requests from a source image registry to a mirrored image registry. 

Important

Windows images mirrored through `ImageDigestMirrorSet` and `ImageTagMirrorSet` objects have specific naming requirements as described in "Using Windows containers with a mirror registry". 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Configure mirrored repositories, by either: 

     * Setting up a mirrored repository with Red Hat Quay. You can copy images from one repository to another and also automatically sync those repositories repeatedly over time by using Red Hat Quay. 

       * [Red Hat Quay Repository Mirroring](https://docs.redhat.com/en/documentation/red_hat_quay/3/html/manage_red_hat_quay/arch-mirroring-intro#enabling-repository-mirroring-quay)

     * Using a tool such as `skopeo` to copy images manually from the source repository to the mirrored repository. 

For example, after installing the skopeo RPM package on a {op-system-base-full system}, use the `skopeo` command as shown in the following example: 

```shell-session
$ skopeo copy --all \
docker://registry.access.redhat.com/ubi9/ubi-minimal:latest@sha256:5cf... \
docker://example.io/example/ubi-minimal
```


In this example, you have a container image registry named `example.io` and image repository named `example`. You want to copy the `ubi9/ubi-minimal` image from `registry.access.redhat.com` to `example.io`. After you create the mirrored registry, you can configure your OpenShift Container Platform cluster to redirect requests made to the source repository to the mirrored repository. 

Important

You must mirror the `mcr.microsoft.com/oss/kubernetes/pause:3.9` image. For example, you could use the following `skopeo` command to mirror the image: 

```shell-session
$ skopeo copy \
docker://mcr.microsoft.com/oss/kubernetes/pause:3.9\
docker://example.io/oss/kubernetes/pause:3.9
```


  2. Log in to your OpenShift Container Platform cluster. 
  3. Create an `ImageDigestMirrorSet` or `ImageTagMirrorSet` CR, as needed, replacing the source and mirrors with your own registry and repository pairs and images: 

```yaml
apiVersion: config.openshift.io/v1
kind: ImageDigestMirrorSet
metadata:
  name: ubi9repo
spec:
  imageDigestMirrors:
  - mirrors:
    - example.io/example/ubi-minimal
    - example.com/example2/ubi-minimal
    source: registry.access.redhat.com/ubi9/ubi-minimal
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.com
    source: registry.redhat.io
    mirrorSourcePolicy: NeverContactSource
  - mirrors:
    - docker.io
    source: docker-mirror.internal
    mirrorSourcePolicy: AllowContactingSource
```


  4. Create the new object by running the following command: 

```shell-session
$ oc create -f registryrepomirror.yaml
```


  5. To check that the mirrored configuration settings are applied, do the following on one of the nodes. 

     1. List your nodes: 

```shell-session
$ oc get node
```


**Example output**

```shell-session
NAME                           STATUS                     ROLES    AGE  VERSION
worker-1.compute.local         Ready                      worker   7m   v1.35.4
master-1.compute.local         Ready                      master   11m  v1.35.4
master-2.compute.local         Ready                      master   11m  v1.35.4
worker-2.compute.local         Ready                      worker   7m   v1.35.4
worker-3.compute.local         Ready                      worker   7m   v1.35.4
master-3.compute.local         Ready                      master   11m  v1.35.4
```


     2. Start the debugging process to access the node: 

```shell-session
$ oc debug node/worker-1.compute.local
```


**Example output**

```shell-session
Starting pod/worker-1.compute.local-debug ...
To use host binaries, run `chroot /host`
```


     3. Change your root directory to `/host`: 

```shell-session
sh-4.2# chroot /host
```


     4. Check that the WMCO generated a `hosts.toml` file for each registry on each Windows instance. For the previous example IDMS object, there should be three files in the following file structure: 

```shell-session
$ tree $config_path
```


**Example output**

```shell-session
C:/k/containerd/registries/
|── registry.access.redhat.com
|   └── hosts.toml
|── mirror.example.com
|   └── hosts.toml
└── docker.io
    └── hosts.toml:
```


The following output represents a `hosts.toml` containerd configuration file where the previous example IDMS object was applied. 

**Example host.toml files**

```shell-session
$ cat "$config_path"/registry.access.redhat.com/host.toml
server = "https://registry.access.redhat.com" # default fallback server since "AllowContactingSource" mirrorSourcePolicy is set

[host."https://example.io/example/ubi-minimal"]
 capabilities = ["pull"]

[host."https://example.com/example2/ubi-minimal"] # secondary mirror
 capabilities = ["pull"]


$ cat "$config_path"/registry.redhat.io/host.toml
# "server" omitted since "NeverContactSource" mirrorSourcePolicy is set

[host."https://mirror.example.com"]
 capabilities = ["pull"]


$ cat "$config_path"/docker.io/host.toml
server = "https://docker.io"

[host."https://docker-mirror.internal"]
 capabilities = ["pull", "resolve"] # resolve tags
```


     5. Pull an image to the node from the source and check if it is resolved by the mirror. 

```shell-session
sh-4.2# podman pull --log-level=debug registry.access.redhat.com/ubi9/ubi-minimal@sha256:5cf...
```


**Troubleshooting**

If the repository mirroring procedure does not work as described, use the following information about how repository mirroring works to help troubleshoot the problem: 

  * The first working mirror is used to supply the pulled image. 
  * The main registry is only used if no other mirror works. 
  * From the system context, the `Insecure` flags are used as fallback.
