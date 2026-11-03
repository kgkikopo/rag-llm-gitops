# 9.5. Understanding image registry repository mirroring

You must mirror images to update clusters in disconnected environments. 

By setting up container registry repository mirroring, you can perform the following tasks: 

  * Configure your OpenShift Container Platform cluster to redirect requests to pull images from a repository on a source image registry and have it resolved by a repository on a mirrored image registry. 
  * Identify multiple mirrored repositories for each target repository, to make sure that if one mirror is down, another can be used. 



Repository mirroring in OpenShift Container Platform includes the following attributes: 

  * Image pulls are resilient to registry downtimes. 
  * Clusters in disconnected environments can pull images from critical locations, such as `quay.io`, and have registries behind a company firewall provide the requested images. 
  * A particular order of registries is tried when an image pull request is made, with the permanent registry typically being the last one tried. 
  * The mirror information you enter is added to the `/etc/containers/registries.conf` file on every node in the OpenShift Container Platform cluster. 
  * When a node makes a request for an image from the source repository, it tries each mirrored repository in turn until it finds the requested content. If all mirrors fail, the cluster tries the source repository. If successful, the image is pulled to the node. 



You can set up repository mirroring in the following ways: 

  * At OpenShift Container Platform installation: 

By pulling container images needed by OpenShift Container Platform and then bringing those images behind your company’s firewall, you can install OpenShift Container Platform into a data center that is in a disconnected environment. 

  * After OpenShift Container Platform installation: 

If you did not configure mirroring during OpenShift Container Platform installation, you can do so postinstallation by using any of the following custom resource (CR) objects: 

    * `ImageDigestMirrorSet` (IDMS). This object allows you to pull images from a mirrored registry by using digest specifications. The IDMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails. 
    * `ImageTagMirrorSet` (ITMS). This object allows you to pull images from a mirrored registry by using image tags. The ITMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails. 
    * `ImageContentSourcePolicy` (ICSP). This object allows you to pull images from a mirrored registry by using digest specifications. The ICSP CR always falls back to the source registry if the mirrors do not work. 

Important

Using an `ImageContentSourcePolicy` (ICSP) object to configure repository mirroring is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported. It will be removed in a future release and is not recommended for new deployments. 

If you have existing YAML files that you used to create `ImageContentSourcePolicy` objects, you can use the `oc adm migrate icsp` command to convert those files to a `ImageDigestMirrorSet` YAML files. For more information, see "Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring". 




Each of these custom resource objects identify the following information: 

  * The source of the container image repository you want to mirror. 
  * A separate entry for each mirror repository you want to offer the content 



Note the following actions and how they affect node drain behavior: 

  * If you create an IDMS or ICSP CR object, the MCO does not drain or reboot the node. 
  * If you create an ITMS CR object, the MCO drains and reboots the node. 
  * If you delete an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node. 
  * If you modify an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node. 

Important

    * When the MCO detects any of the following changes, it applies the update without draining or rebooting the node: 

      * Changes to the SSH key in the `spec.config.passwd.users.sshAuthorizedKeys` parameter of a machine config. 
      * Changes to the global pull secret or pull secret in the `openshift-config` namespace. 
      * Automatic rotation of the `/etc/kubernetes/kubelet-ca.crt` certificate authority (CA) by the Kubernetes API Server Operator. 

    * When the MCO detects changes to the `/etc/containers/registries.conf` file, such as editing an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object, it drains the corresponding nodes, applies the changes, and uncordons the nodes. The node drain does not happen for the following changes: 

      * The addition of a registry with the `pull-from-mirror = "digest-only"` parameter set for each mirror. 
      * The addition of a mirror with the `pull-from-mirror = "digest-only"` parameter set in a registry. 
      * The addition of items to the `unqualified-search-registries` list. 




For new clusters, you can use IDMS, ITMS, and ICSP CRs objects as needed. However, using IDMS and ITMS is recommended. 

If you upgraded a cluster, any existing ICSP objects remain stable, and both IDMS and ICSP objects are supported. Workloads that use ICSP objects continue to function as expected. However, if you want to take advantage of the fallback policies introduced in the IDMS CRs, you can migrate current workloads to IDMS objects by using the `oc adm migrate icsp` command as shown in the **Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring** section that follows. Migrating to IDMS objects does not require a cluster reboot. 

Note

By default, if your cluster uses an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object to configure repository mirroring, you must use a global pull secret for mirrored registries. You cannot add an image pull secret to a project. 

However, you can configure a cluster-wide `CRIOCredentialProviderConfig` object to enable project-scoped image pull secrets that you can use with mirrored repositories. For more information, see "Configuring project-scoped image pull secrets for mirrored registries". 

## 9.5.1. Configuring project-scoped image pull secrets for mirrored registries

As a cluster administrator, you can edit the cluster-wide `CRIOCredentialProviderConfig` object, named `cluster`, to enable project-scoped image pull secrets that you can use with mirrored repositories. 

By using project-scoped secrets, you can maintain security isolation between projects without exposing credentials in a global pull secret. 

By default, if your cluster uses an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object to configure repository mirroring, you must use a global pull secret for mirrored registries. You cannot add an image pull secret to a project. However, you can use the cluster-wide `CRIOCredentialProviderConfig` object to configure the kubelet to trigger the CRI-O credential provider, which enables project-scoped image pull secrets. 

Important

Project-scoped image pull secrets for mirrored registries is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

An administrator edits the `CRIOCredentialProviderConfig` object named `cluster`, to list the registries that a developer can pull from by using a project-scoped secret. The administrator then creates an image pull secret in each namespace where it is needed and configures role-based access control (RBAC) permissions that allow the pod’s service account within that namespace to access the secret. The admin can create a different pull secret with different credentials for each namespace or use the same pull secret in multiple namespaces. 

When a developer uses a pod spec in one of those namespaces to pull an image from a listed registry, the `CRIOCredentialProviderConfig` object triggers the CRI-O credential provider. The credential provider resolves mirror configurations, discovers namespace-scoped secrets, and generates short-lived authentication files for CRI-O consumption. This process maintains credential isolation between namespaces while preserving existing mirror configuration methods. 

The following is an example `CRIOCredentialProviderConfig` object: 

```shell-session
apiVersion: config.openshift.io/v1alpha1
kind: CRIOCredentialProviderConfig
metadata:
  name: cluster
spec:
  matchImages:
    - "docker.io"
    - "*.example.io"
    - "quay.io"
    - "registry.example.com:5000"
```


where: 

`spec.matchImages`
     Specifies the registries available for pulling by using project-scoped secrets. The items in this list trigger the CRI-O credential provider. 

Editing this object updates the `CredentialProviderConfig` object on the nodes. 

The following is an example `CredentialProviderConfig` object: 

```shell-session
apiVersion: kubelet.config.k8s.io/v1
kind: CredentialProviderConfig
providers:
- apiVersion: credentialprovider.kubelet.k8s.io/v1
  args:
  - get-credentials
  - --v=3
  defaultCacheDuration: 1m0s
  matchImages:
  - gcr.io
  - '*.gcr.io'
  - '*.pkg.dev'
  - container.cloud.google.com
  name: gcr-credential-provider
- apiVersion: credentialprovider.kubelet.k8s.io/v1
  defaultCacheDuration: 1s
  matchImages:
  - '*.example.io'
  - docker.io
  - quay.io
  - registry.example.com:5000
  name: crio-credential-provider
  tokenAttributes:
    cacheType: Token
    requireServiceAccount: false
    serviceAccountTokenAudience: https://kubernetes.default.svc
```


where: 

`providers.matchImages`
     Specifies the registries you listed in the `CRIOCredentialProviderConfig` object. 
`providers.tokenAttributes`
     Specifies the configuration of the service account token that is passed to the CRI-O credential provider. 

Only the `matchImages` parameter is configurable by using the `CRIOCredentialProviderConfig` object. All other parameters are immutable. 

In this example, the `crio-credential-provider` configuration was generated from the `CRIOCredentialProviderConfig` object. The `gcr-credential-provider` configuration is a default configuration. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have enabled the `TechPreviewNoUpgrade` feature set in your cluster’s `FeatureGate` custom resource (CR). For more information, see "Understanding feature gates". 



**Procedure**

  1. Create a namespace for the pod by running the following command: 

```shell-session
$ oc create namespace <namespace_name>
```


Replace `<namespace_name>` with a name for your namespace. 

  2. Create a secret in that namespace from an existing authentication file: 

     1. For Docker clients using `.docker/config.json`, run the following command: 

```shell-session
$ oc create secret generic <pull_secret_name> \
    --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson
```


Replace `<pull_secret_name>` with a name for your secret and `<path/to/.docker/config.json>` with the path to your Docker `config.json` file. 

     2. For Podman clients using `.config/containers/auth.json`, run the following command: 

```shell-session
$ oc create secret generic <pull_secret_name> \
     --from-file=<path/to/.config/containers/auth.json> \
     --type=kubernetes.io/podmanconfigjson
```


Replace `<pull_secret_name>` with a name for your secret and `<path/to/.config/containers/auth.json>` with the path to your Podman `auth.json` file. 

  3. Create a `Role` and a `RoleBinding` object in the namespace to grant service account access to image pull secrets: 

     1. Create a YAML file similar to the following example: 

**Example`Role` and `RoleBinding` objects**

```shell-session
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: <role_name>
  namespace: <namespace_name>
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: credential-provider-secret-access-binding
  namespace: <namespace_name>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: <role_name>
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: system:serviceaccount:<namespace_name>:default
```


Replace `<namespace_name>` with a name for your namespace and `<role_name>` with a name for the role. 

     2. Create the `Role` and `RoleBinding` objects: 

```shell-session
$ oc create -f <file_name>.yaml
```


     3. Edit the `CRIOCredentialProviderConfig` object: 

```shell-session
$ oc edit criocredentialproviderconfig cluster
```


     4. Add the `spec.matchImages` stanza with a list of registries similar to the following example: 

```shell-session
apiVersion: config.openshift.io/v1alpha1
kind: CRIOCredentialProviderConfig
metadata:
  name: cluster
spec:
  matchImages:
    - "docker.io"
    - "*.example.io"
    - "quay.io"
    - "registry.example.com:5000"
```


where: 

`spec.matchImages`
     Specifies the registries that you want pods to pull from by using a project-scoped secret. Each entry in the list must be a valid fully-qualified domain name with an optional wildcard, port, and path. The maximum length is 512 characters. Wildcards ('*') are supported for full-subdomain labels and top-level domains. Wildcards are not allowed in the port or path portions. The items in this list trigger the CRI-O credential provider. 

After you save the changes, OpenShift Container Platform updates the `CredentialProviderConfig` object on the nodes. 




**Verification**

  1. Verify that the `CredentialProviderConfig` object contains the registries from the `matchImages` list: 

     1. Start a debug session as root for a control plane node by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


     2. Set `/host` as the root directory within the debug shell: 

```shell-session
sh-5.1# chroot /host
```


     3. View the `/etc/kubernetes/credential-providers/<platform>-credential-provider.yaml` file: 

```shell-session
sh-5.1# cat /etc/kubernetes/credential-providers/<platform>-credential-provider.yaml
```


Replace `<platform>` with one of the following options: 

        * Use `ecr` for an AWS cluster. 
        * Use `gcr` for a Google Cloud cluster. 
        * Use `acr` for an Azure cluster. 
        * Use `generic` for non-cloud platforms. 

The output should include the repositories you added to the `CRIOCredentialProviderConfig` object. 

```shell-session
apiVersion: kubelet.config.k8s.io/v1
kind: CredentialProviderConfig
providers:
# ...
- apiVersion: credentialprovider.kubelet.k8s.io/v1
  defaultCacheDuration: 1s
  matchImages:
  - '*.example.io'
  - docker.io
  - quay.io
  - registry.example.com:5000
# ...
```


## 9.5.2. Configure image registry repository mirroring

You can create postinstallation mirror configuration custom resources (CR) to redirect image pull requests from a source image registry to a mirrored image registry. 

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

  2. Create a postinstallation mirror configuration custom resource (CR), by using one of the following examples: 

     * Create an `ImageDigestMirrorSet` or `ImageTagMirrorSet` CR, as needed, replacing the source and mirrors with your own registry and repository pairs and images: 

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
    - mirror.example.com/redhat
    source: registry.example.com/redhat
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.com
    source: registry.example.com
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.net/image
    source: registry.example.com/example/myimage
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.net
    source: registry.example.com/example
    mirrorSourcePolicy: AllowContactingSource
  - mirrors:
    - mirror.example.net/registry-example-com
    source: registry.example.com
    mirrorSourcePolicy: AllowContactingSource
```


     * Create an `ImageContentSourcePolicy` custom resource, replacing the source and mirrors with your own registry and repository pairs and images: 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: ImageContentSourcePolicy
metadata:
  name: mirror-ocp
spec:
  repositoryDigestMirrors:
  - mirrors:
    - mirror.registry.com:443/ocp/release
    source: quay.io/openshift-release-dev/ocp-release
  - mirrors:
    - mirror.registry.com:443/ocp/release
    source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
```


where: 

`- mirror.registry.com:443/ocp/release`
     Specifies the name of the mirror image registry and repository. 
`source: quay.io/openshift-release-dev/ocp-release`
     Specifies the online registry and repository containing the content that is mirrored. 

  3. Create the new object by running the following command: 

```shell-session
$ oc create -f registryrepomirror.yaml
```


After the object is created, the Machine Config Operator (MCO) drains the nodes for `ImageTagMirrorSet` objects only. The MCO does not drain the nodes for `ImageDigestMirrorSet` and `ImageContentSourcePolicy` objects. 

  4. To check that the mirrored configuration settings are applied, do the following on one of the nodes. 

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


     4. Check the `/etc/containers/registries.conf` file to make sure the changes were made: 

```shell-session
sh-4.2# cat /etc/containers/registries.conf
```


The following output represents a `registries.conf` file where postinstallation mirror configuration CRs are applied. 

**Example output**

```shell-session
unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]
short-name-mode = ""

[[registry]]
  prefix = ""
  location = "registry.access.redhat.com/ubi9/ubi-minimal"

  [[registry.mirror]]
    location = "example.io/example/ubi-minimal"
    pull-from-mirror = "digest-only"

  [[registry.mirror]]
    location = "example.com/example/ubi-minimal"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com"

  [[registry.mirror]]
    location = "mirror.example.net/registry-example-com"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com/example"

  [[registry.mirror]]
    location = "mirror.example.net"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com/example/myimage"

  [[registry.mirror]]
    location = "mirror.example.net/image"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com"

  [[registry.mirror]]
    location = "mirror.example.com"
    pull-from-mirror = "digest-only"

[[registry]]
  prefix = ""
  location = "registry.example.com/redhat"

  [[registry.mirror]]
    location = "mirror.example.com/redhat"
    pull-from-mirror = "digest-only"
[[registry]]
  prefix = ""
  location = "registry.access.redhat.com/ubi9/ubi-minimal"
  blocked = true

  [[registry.mirror]]
    location = "example.io/example/ubi-minimal-tag"
    pull-from-mirror = "tag-only"
```


where: 

`[[registry]].location = "registry.access.redhat.com/ubi9/ubi-minimal"`
     The repository listed in a pull spec. 
`[[registry.mirror]].location = "example.io/example/ubi-minimal"`
     Indicates the mirror for that repository. 
`[[registry.mirror]].pull-from-mirror = "digest-only"`
     Means that the image pull from the mirror is a digest reference image. 
`[[registry]].blocked = true`
     Indicates that the `NeverContactSource` parameter is set for this repository. 
`[[registry.mirror]].pull-from-mirror = "tag-only"`
     Indicates that the image pull from the mirror is a tag reference image. 

     5. Pull an image to the node from the source and check if it is resolved by the mirror. 

```shell-session
sh-4.2# podman pull --log-level=debug registry.access.redhat.com/ubi9/ubi-minimal@sha256:5cf...
```


**Troubleshooting**

If the repository mirroring procedure does not work as described, use the following information about how repository mirroring works to help troubleshoot the problem: 

  * The first working mirror is used to supply the pulled image. 
  * The main registry is only used if no other mirror works. 
  * From the system context, the `Insecure` flags are used as fallback. 
  * The format of the `/etc/containers/registries.conf` file has changed recently. It is now version 2 and in TOML format. 



## 9.5.3. Image registry repository mirroring configuration parameters

You can use the following table for information about parameters when configuring your image repository for mirroring. 

**Parameter**| **Values and Information**  
---|---  
`apiVersion:` |  Required. The value must be `config.openshift.io/v1` API.   
`kind:` |  The kind of object according to the pull type. The `ImageDigestMirrorSet` type pulls a digest reference image The `ImageTagMirrorSet` type pulls a tag reference image.   
`spec: imageDigestMirrors:` |  The type of image pull method. Use `imageDigestMirrors` for an `ImageDigestMirrorSet` CR. Use `imageTagMirrors` for an `ImageTagMirrorSet` CR.   
`- mirrors: - example.io/example/ubi-minimal` |  The name of the mirrored image registry and repository.   
`- mirrors: -example.com/example2/ubi-minimal` |  The value of this parameter is the name of a secondary mirror repository for each target repository. If one mirror is down the target repository can use the secondary mirror.   
`source: registry.access.redhat.com/ubi9/ubi-minimal` |  The registry and repository source. The source is the repository that is listed in an image pull specification.   
`mirrorSourcePolicy: AllowContactingSource` |  Optional parameter that indicates the fallback policy if the image pull fails. The `AllowContactingSource` value allows continued attempts to pull the image from the source repository. Default value. `NeverContactSource` prevents continued attempts to pull the image from the source repository.   
`source: registry.example.com/redhat` |  An optional parameter that indicates a namespace inside a registry. Setting a namespace inside a registry allows use of any image in that namespace. If you use a registry domain as a source, the object applies to all of the repositories from the registry.   
`source: registry.example.com` |  Optional parameter that indicates a registry. Allows us of any image in that registry. If you specify a registry name, the object applies to all repositories from a source registry to a mirror registry.   
`source: registry.example.com/example/myimage` |  Pulls the image `registry.example.com/example/myimage@sha256:…​` from the mirror `mirror.example.net/image@sha256:..`.   
`source: registry.example.com/example` |  Pulls the image `registry.example.com/example/image@sha256:…​` in the source registry namespace from the mirror `mirror.example.net/image@sha256:…​`.   
`source: registry.example.com` |  Pulls the image `registry.example.com/myimage@sha256` from the mirror registry `example.net/registry-example-com/myimage@sha256:…​`.   
Show more

## 9.5.4. Convert ImageContentSourcePolicy (ICSP) files for image registry repository mirroring

You can convert existing `ImageContentSourcePolicy` (ICSP) files to `ImageDigestMirrorSet` files to configure image registry repository mirroring. 

Using an `ImageContentSourcePolicy` (ICSP) object to configure repository mirroring is a deprecated feature. 

This functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments. 

ICSP objects are being replaced by `ImageDigestMirrorSet` and `ImageTagMirrorSet` objects to configure repository mirroring. If you have existing YAML files that you used to create `ImageContentSourcePolicy` objects, you can use the `oc adm migrate icsp` command to convert those files to an `ImageDigestMirrorSet` YAML file. The command updates the API to the current version, changes the `kind` value to `ImageDigestMirrorSet`, and changes `spec.repositoryDigestMirrors` to `spec.imageDigestMirrors`. The rest of the file is not changed. 

Because the migration does not change the `registries.conf` file, the cluster does not need to reboot. 

For more information about `ImageDigestMirrorSet` or `ImageTagMirrorSet` objects, see "Configuring image registry repository mirroring" in the previous section. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * Ensure that you have `ImageContentSourcePolicy` objects on your cluster. 



**Procedure**

  1. Use the following command to convert one or more `ImageContentSourcePolicy` YAML files to an `ImageDigestMirrorSet` YAML file: 

```shell-session
$ oc adm migrate icsp <file_name>.yaml <file_name>.yaml <file_name>.yaml --dest-dir <path_to_the_directory>
```


where: 

`<file_name>`
     Specifies the name of the source `ImageContentSourcePolicy` YAML. You can list multiple file names. 
`--dest-dir`
    

Optional: Specifies a directory for the output `ImageDigestMirrorSet` YAML. If unset, the file is written to the current directory. 

For example, the following command converts the `icsp.yaml` and `icsp-2.yaml` file and saves the new YAML files to the `idms-files` directory. 

```shell-session
$ oc adm migrate icsp icsp.yaml icsp-2.yaml --dest-dir idms-files
```


**Example output**

```shell-session
wrote ImageDigestMirrorSet to idms-files/imagedigestmirrorset_ubi8repo.5911620242173376087.yaml
wrote ImageDigestMirrorSet to idms-files/imagedigestmirrorset_ubi9repo.6456931852378115011.yaml
```


  2. Create the CR object by running the following command: 

```shell-session
$ oc create -f <path_to_the_directory>/<file-name>.yaml
```


where: 

`<path_to_the_directory>`
     Specifies the path to the directory, if you used the `--dest-dir` flag. 
`<file_name>`
     Specifies the name of the `ImageDigestMirrorSet` YAML. 

  3. Remove the ICSP objects after the IDMS objects are rolled out.
