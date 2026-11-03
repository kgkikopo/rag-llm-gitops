# 8.2. Prepare an Agent-based cluster deployment for the multicluster engine for Kubernetes Operator while disconnected

You can mirror the required OpenShift Container Platform container images, the multicluster engine Operator, and the Local Storage Operator (LSO) into your local mirror registry in a disconnected environment. Ensure that you note the local DNS hostname and port of your mirror registry. 

Note

To mirror your OpenShift Container Platform image repository to your mirror registry, you can use either the `oc adm release image` or `oc mirror` command. In this procedure, the `oc mirror` command is used as an example. 

**Procedure**

  1. Create an `<assets_directory>` folder to contain valid `install-config.yaml` and `agent-config.yaml` files. This directory is used to store all the assets. 
  2. To mirror an OpenShift Container Platform image repository, the multicluster engine, and the LSO, create a `ImageSetConfiguration.yaml` file with the following settings: 

**Example`ImageSetConfiguration.yaml`**

```yaml
  kind: ImageSetConfiguration
  apiVersion: mirror.openshift.io/v1alpha2
  archiveSize: 4
  storageConfig:
    imageURL: <your-local-registry-dns-name>:<your-local-registry-port>/mirror/oc-mirror-metadata
    skipTLS: true
  mirror:
    platform:
      architectures:
        - "amd64"
      channels:
        - name: stable-4.22
          type: ocp
    additionalImages:
      - name: registry.redhat.io/ubi9/ubi:latest
    operators:
      - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.22
        packages:
          - name: multicluster-engine
          - name: local-storage-operator
```


where: 

`archiveSize`
     Specifies the maximum size, in GiB, of each file within the image set. 
`storageConfig`
     Specifies the back-end location to receive the image set metadata. This location can be a registry or local directory. It is required to specify `storageConfig` values. 
`storageConfig.imageURL`
     Specifies the registry URL for the storage backend. 
`channels.name`
     Specifies the channel that contains the OpenShift Container Platform images for the version you are installing. 
`operators.catalog`
     Specifies the Operator catalog that contains the OpenShift Container Platform images that you are installing. 
`packages`
    

Specifies only certain Operator packages and channels to include in the image set. Remove this field to retrieve all packages in the catalog. In this example, a `package.name` value of `multicluster-engine` includes the multicluster engine packages and channels, and `local-storage-operator` includes the LSO packages and channels. 

Note

This file is required by the `oc mirror` command when mirroring content. 

  3. To mirror a specific OpenShift Container Platform image repository, the multicluster engine, and the LSO, run the following command: 

```shell-session
$ oc mirror --dest-skip-tls --config ocp-mce-imageset.yaml docker://<your-local-registry-dns-name>:<your-local-registry-port>
```


  4. Update the registry and certificate in the `install-config.yaml` file: 

**Example`imageContentSources.yaml`**

```yaml
  imageContentSources:
    - source: "quay.io/openshift-release-dev/ocp-release"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/openshift/release-images"
    - source: "quay.io/openshift-release-dev/ocp-v4.0-art-dev"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/openshift/release"
    - source: "registry.redhat.io/ubi9"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/ubi9"
    - source: "registry.redhat.io/multicluster-engine"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/multicluster-engine"
    - source: "registry.redhat.io/rhel8"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/rhel8"
    - source: "registry.redhat.io/redhat"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/redhat"
```


Additionally, ensure your certificate is present in the `additionalTrustBundle` field of the `install-config.yaml`. 

**Example`install-config.yaml`**

```yaml
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  zzzzzzzzzzz
  -----END CERTIFICATE-------
```


Important

The `oc mirror` command creates a folder called `oc-mirror-workspace` with several outputs. This includes the `imageContentSourcePolicy.yaml` file that identifies all the mirrors you need for OpenShift Container Platform and your selected Operators. 

  5. Generate the cluster manifests by running the following command: 

```shell-session
$ openshift-install agent create cluster-manifests
```


This command updates the cluster manifests folder to include a `mirror` folder that contains your mirror configuration.
