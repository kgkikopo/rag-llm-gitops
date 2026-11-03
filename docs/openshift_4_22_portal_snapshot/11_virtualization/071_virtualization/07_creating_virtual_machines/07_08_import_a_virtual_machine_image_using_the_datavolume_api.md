# 7.8. Import a virtual machine image using the DataVolume API

You can import a virtual machine (VM) image into your OpenShift Virtualization cluster by using the `DataVolume` API. A `DataVolume` automates PVC creation and image data transfer from an external source by using the Containerized Data Importer (CDI). 

## 7.8.1. Supported import sources

The `DataVolume` API supports importing VM images from several external sources. The Containerized Data Importer (CDI) detects the image format and converts it as needed. 

The following import sources are available: 

HTTP or HTTPS
     You specify the URL of the image file by using the `source.http` field. CDI downloads the image directly from the web server. You can optionally supply TLS certificates for custom certificate authorities and credentials for Basic authentication. 
Container registry
     You specify the image location by using the `source.registry` field with a `docker://` URL prefix. CDI pulls the image from the registry by using standard container image pull mechanisms. You can supply registry credentials in a `Secret` object if the registry requires authentication. 
S3 object storage
     You specify the object URL by using the `source.s3` field. CDI downloads the image from an S3-compatible storage service. You must supply access credentials in a `Secret` object. 
oVirt (ImageIO)
     You specify the connection details by using the `source.imageio` field. CDI connects to the oVirt ImageIO API to transfer disk images from a Red Hat Virtualization environment. 
VMware (VDDK)
     You specify the connection details by using the `source.vddk` field. CDI uses the VMware Virtual Disk Development Kit (VDDK) to transfer disk images from a VMware vSphere environment. 

Supported image formats include QCOW2, raw, ISO, and compressed archive files. 

## 7.8.2. Import a VM image from a container registry

You can import a virtual machine (VM) image from a container registry into a persistent volume claim (PVC) by using the `DataVolume` API. The Containerized Data Importer (CDI) creates a data volume and an associated PVC to store the imported image. 

**Prerequisites**

  * You have access to the container registry. 
  * If the registry is private, registry credentials are stored in a `Secret` object. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `DataVolume` object that specifies the container registry as the source: 

```yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: registry-image-datavolume
spec:
  source:
    registry:
      url: "docker://registry.example.com/my-vm-image:latest"
      pullMethod: node
      secretRef: <registry_secret>
      certConfigMap: <ca_certs_configmap>
  storage:
    resources:
      requests:
        storage: 20Gi
```


where: 

`url`
     Specifies the container registry URL with the `docker://` prefix. 
`pullMethod`
     Optional: Set to `node` to use the node container runtime cache and pull secrets. The default value is `pod`. 
`secretRef`
     Optional: Specifies the name of a `Secret` object that stores the registry credentials. 
`certConfigMap`
     Optional: Specifies the name of a `ConfigMap` object that stores custom CA certificates for the registry. 

  2. Create the data volume by running the following command: 

```shell-session
$ oc create -f <datavolume_manifest>.yaml
```


  3. Monitor the import progress by running the following command: 

```shell-session
$ oc get dv <datavolume_name>
```


**Verification**

  * Confirm that the data volume reaches the `Succeeded` phase by running the following command: 

```shell-session
$ oc get dv <datavolume_name>
```


Example output: 

```shell-session
NAME                        PHASE       PROGRESS
registry-image-datavolume   Succeeded   100.0%
```


  * Confirm that the PVC is created and bound by running the following command: 

```shell-session
$ oc get pvc
```


Example output: 

```shell-session
NAME                        STATUS   VOLUME     CAPACITY   ACCESS MODES
registry-image-datavolume   Bound    pv-name    20Gi       RWO
```


## 7.8.3. CPU architecture selection for DataVolume imports

You can target a specific CPU architecture when you import a virtual machine (VM) image from an Open Container Initiative (OCI) image index by setting the `platform.architecture` field in the `DataVolume` custom resource (CR). 

Important

Specifying CPU architecture for data volume imports is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

In heterogeneous clusters where nodes run different CPU architectures, importing the correct image variant is essential. Without specifying the target architecture, the imported image might not match the architecture of the node where the VM is scheduled to run. The `platform.architecture` field resolves this by selecting the appropriate variant from the image index. 

The following CPU architectures are supported: 

  * `amd64`
  * `arm64`
  * `s390x`



When you set the `platform.architecture` field in combination with `pullMethod: node`, OpenShift Virtualization adds a node selector to the importer pod. This node selector ensures that the importer pod runs on a node with the matching CPU architecture. The `node` pull method uses the container runtime cache of the node where the importer pod runs, so the pod must run on a node with the correct architecture. Without the node selector, the importer pod might run on a node with a different architecture, resulting in a mismatch between the pulled image and the target platform. 

Example `DataVolume` CR: 

```yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: my-vm-image
spec:
  source:
    registry:
      url: "docker://registry.example.com/my-multi-arch-image:latest"
      pullMethod: node
      platform:
        architecture: arm64
  storage:
    resources:
      requests:
        storage: 30Gi
```


## 7.8.4. Import a VM image from an HTTP or HTTPS source

You can import a virtual machine (VM) image from an HTTP or HTTPS source by creating a `DataVolume` object. The Containerized Data Importer (CDI) controller creates a data volume and an underlying persistent volume claim (PVC), then downloads the image from the specified URL into the PVC. 

**Prerequisites**

  * A VM image is accessible from an HTTP or HTTPS URL. 
  * Optional: Custom CA certificates for HTTPS connections are stored in a `ConfigMap` object. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `DataVolume` object that specifies the HTTP or HTTPS source of the VM image: 

```yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: http-image-datavolume
spec:
  source:
    http:
      url: "https://example.com/images/my-vm-image.qcow2"
      secretRef: <http_secret>
      certConfigMap: <ca_certs_configmap>
  storage:
    resources:
      requests:
        storage: 20Gi
```


where: 

`url`
     Specifies the HTTP or HTTPS URL of the VM image. 
`secretRef`
     Optional: Specifies the name of a `Secret` object that stores Basic authentication credentials. The `Secret` must contain `username` and `password` keys. 
`certConfigMap`
     Optional: Specifies the name of a `ConfigMap` object that stores custom CA certificates for HTTPS connections. 

  2. Create the data volume by running the following command: 

```shell-session
$ oc create -f <datavolume_manifest>.yaml
```


  3. Monitor the import progress by running the following command: 

```shell-session
$ oc get dv <datavolume_name>
```


**Verification**

  * Confirm that the data volume reaches the `Succeeded` phase by running the following command: 

```shell-session
$ oc get dv <datavolume_name>
```


Example output: 

```shell-session
NAME                     PHASE       PROGRESS
http-image-datavolume    Succeeded   100.0%
```


  * Confirm that the PVC is created and bound by running the following command: 

```shell-session
$ oc get pvc
```


Example output: 

```shell-session
NAME                     STATUS   VOLUME     CAPACITY   ACCESS MODES
http-image-datavolume    Bound    pv-name    20Gi       RWO
```


## 7.8.5. Import a VM image from S3 object storage

You can import a virtual machine (VM) image from an S3-compatible object storage bucket by using a `DataVolume` object. The Containerized Data Importer (CDI) pulls the image from the S3 endpoint and populates a persistent volume claim (PVC) that you can use to create a VM. 

**Prerequisites**

  * A VM image is stored in an S3-compatible bucket. 
  * You have S3 access credentials (access key ID and secret key) for your S3-compatible storage account. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `Secret` object for your S3 access credentials: 

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: s3-secret
type: Opaque
stringData:
  accessKeyId: "<access_key>"
  secretKey: "<secret_key>"
```


where: 

`<access_key>`
     Specifies the access key ID for your S3-compatible storage account. 
`<secret_key>`
     Specifies the secret key for your S3-compatible storage account. 

  2. Apply the `Secret` object: 

```shell-session
$ oc create -f <secret_manifest>.yaml
```


  3. Create a `DataVolume` object that specifies the S3 source URL and secret reference: 

```yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: s3-image-datavolume
spec:
  source:
    s3:
      url: "https://s3.example.com/my-bucket/my-vm-image.qcow2"
      secretRef: s3-secret
      certConfigMap: <ca_certs_configmap>
  storage:
    resources:
      requests:
        storage: 20Gi
```


where: 

`url`
     Specifies the S3 URL of the VM image. For non-AWS S3 services, specify the full endpoint URL. 
`secretRef`
     Specifies the name of the `Secret` with the S3 access credentials. 
`certConfigMap`
     Optional: Specifies the name of a `ConfigMap` object that stores custom CA certificates for the S3 endpoint. Required only if your endpoint uses a custom certificate authority. 

  4. Apply the `DataVolume` object by running the following command: 

```shell-session
$ oc create -f <datavolume_manifest>.yaml
```


  5. Monitor the import progress by running the following command: 

```shell-session
$ oc get dv <datavolume_name>
```


**Verification**

  * Confirm that the data volume reaches the `Succeeded` phase by running the following command: 

```shell-session
$ oc get dv <datavolume_name>
```


Example output: 

```shell-session
NAME                   PHASE       PROGRESS
s3-image-datavolume    Succeeded   100.0%
```


  * Confirm that the PVC is created and bound by running the following command: 

```shell-session
$ oc get pvc
```


Example output: 

```shell-session
NAME                   STATUS   VOLUME     CAPACITY   ACCESS MODES
s3-image-datavolume    Bound    pv-name    20Gi       RWO
```


## 7.8.6. DataVolume source fields

You can configure a `DataVolume` object to import a virtual machine (VM) image from several source types. Each source type has its own set of fields that control where and how the Containerized Data Importer (CDI) retrieves the image. 

### 7.8.6.1. Registry source fields

The `source.registry` source type imports a VM image from a container registry. 

Table 7.6. source.registry fieldsField| Type| Description  
---|---|---  
`url` |  String  |  Container registry URL of the image, specified with the `docker://` prefix. For example, `docker://registry.example.com/my-image:latest`.   
`pullMethod` |  String  |  Method for pulling the image. Specify `pod` to use the CDI importer pod or `node` to use the node’s container image cache. The default value is `pod`.   
`secretRef` |  String  |  Name of a `Secret` object that stores the credentials for the container registry.   
`certConfigMap` |  String  |  Name of a `ConfigMap` object that stores custom certificate authority (CA) certificates for the container registry.   
`platform.architecture` |  String  |  Target CPU architecture when importing from a multi-architecture image index. Supported values are `amd64`, `arm64`, and `s390x`. This field is a Technology Preview feature.   
Show more

### 7.8.6.2. HTTP source fields

The `source.http` source type imports a VM image from an HTTP or HTTPS URL. 

Table 7.7. source.http fieldsField| Type| Description  
---|---|---  
`url` |  String  |  HTTP or HTTPS URL of the VM image.   
`secretRef` |  String  |  Name of a `Secret` object that stores Basic authentication credentials for the HTTP server.   
`certConfigMap` |  String  |  Name of a `ConfigMap` object that stores custom certificate authority (CA) certificates for the HTTP server.   
`extraHeaders` |  List of strings  |  Additional HTTP headers to include in the image download request.   
`secretExtraHeaders` |  List of strings  |  Names of `Secret` objects that store additional HTTP headers to include in the image download request.   
Show more

### 7.8.6.3. S3 source fields

The `source.s3` source type imports a VM image from an S3-compatible object storage bucket. 

Table 7.8. source.s3 fieldsField| Type| Description  
---|---|---  
`url` |  String  |  S3 URL of the VM image.   
`secretRef` |  String  |  Name of a `Secret` object that stores the S3 access key ID and secret access key.   
`certConfigMap` |  String  |  Name of a `ConfigMap` object that stores custom certificate authority (CA) certificates for the S3 endpoint.   
Show more

### 7.8.6.4. ImageIO source fields

The `source.imageio` source type imports a disk image from a Red Hat Virtualization (oVirt) environment by using the ImageIO API. 

Table 7.9. source.imageio fieldsField| Type| Description  
---|---|---  
`url` |  String  |  URL of the oVirt Engine API endpoint. For example, `https://ovirt-engine.example.com/ovirt-engine/api`.   
`diskId` |  String  |  ID of the oVirt disk to import.   
`secretRef` |  String  |  Name of a `Secret` object that stores the credentials to access the oVirt Engine.   
`certConfigMap` |  String  |  Name of a `ConfigMap` object that stores CA certificates for the oVirt Engine.   
Show more

### 7.8.6.5. VDDK source fields

The `source.vddk` source type imports a disk image from a VMware vSphere environment by using the Virtual Disk Development Kit (VDDK). 

Table 7.10. source.vddk fieldsField| Type| Description  
---|---|---  
`url` |  String  |  URL of the vCenter or ESXi host.   
`uuid` |  String  |  UUID of the virtual machine in vCenter or ESXi.   
`backingFile` |  String  |  Path to the virtual hard drive to import from vCenter or ESXi.   
`thumbprint` |  String  |  TLS certificate thumbprint of the vCenter or ESXi host.   
`secretRef` |  String  |  Name of a `Secret` object that stores the username and password for the vCenter or ESXi host.   
`initImageURL` |  String  |  URL of a container image with an extracted VDDK library. Overrides the `v2v-vmware` config map.   
Show more

### 7.8.6.6. Blank source

The `source.blank` source type creates an empty disk with no data. This source type has no configurable fields. 

### 7.8.6.7. PVC source fields

The `source.pvc` source type clones the contents of an existing persistent volume claim (PVC). 

Table 7.11. source.pvc fieldsField| Type| Description  
---|---|---  
`namespace` |  String  |  Namespace of the source PVC.   
`name` |  String  |  Name of the source PVC.   
Show more

### 7.8.6.8. VolumeSnapshot source fields

The `source.snapshot` source type creates a volume from an existing `VolumeSnapshot` object. 

Table 7.12. source.snapshot fieldsField| Type| Description  
---|---|---  
`namespace` |  String  |  Namespace of the source `VolumeSnapshot` object.   
`name` |  String  |  Name of the source `VolumeSnapshot` object.   
Show more

### 7.8.6.9. Supported content types

The Containerized Data Importer (CDI) supports the following content types for VM image imports: 

  * QCOW2 
  * Raw 
  * ISO 
  * Archive (`tar.gz`) 



## 7.8.7. Data volume import troubleshooting

You can diagnose and resolve common issues with data volume imports by inspecting data volume conditions and events. Understanding these conditions helps you identify the root cause of failed or stalled imports. 

### 7.8.7.1. Data volume conditions

Each data volume reports three conditions that indicate its current state. You can view these conditions by running the `oc describe dv` command. 

`Bound`
     Indicates whether the persistent volume claim (PVC) has been created and bound to a persistent volume. `Status: True` means the PVC is bound. 
`Running`
     Indicates whether an import operation is actively running. `Status: True` means data is being imported. 
`Ready`
     Indicates whether the data volume is ready to use. `Status: True` means the import completed successfully. 

### 7.8.7.2. Diagnostic commands

You can use the following commands to gather information about a data volume import: 

`oc describe dv <datavolume_name>`
     Shows the data volume conditions, events, and status. Replace `<datavolume_name>` with the name of your data volume. 
`oc get events --field-selector involvedObject.name=<datavolume_name>`
     Shows events related to the data volume. Replace `<datavolume_name>` with the name of your data volume. 

### 7.8.7.3. Common failure scenarios

Table 7.13. Common data volume import failuresSymptom| Possible cause| Resolution  
---|---|---  
Import pod in `ErrImagePull` or `ImagePullBackOff` |  Wrong registry URL or missing credentials  |  Verify the registry URL and ensure the `secretRef` points to a valid `Secret`.   
Import pod in `CrashLoopBackOff` |  Invalid image format or corrupted image  |  Verify the image is in a supported format (QCOW2, raw, ISO, archive).   
Data volume stuck in `ImportScheduled` |  No available persistent volume matching the storage request  |  Verify available storage and storage class configuration.   
Data volume shows `Scratch space required` error  |  CDI requires scratch space for image conversion but none is available  |  Configure a scratch space storage class in the `CDI` object or ensure enough storage is available.   
TLS certificate errors  |  Custom CA not configured  |  Create a `ConfigMap` object with the CA certificate and reference it in the `certConfigMap` field.   
HTTP 401 or 403 errors  |  Missing or invalid authentication credentials  |  Verify the `Secret` referenced by `secretRef` has valid credentials.   
Show more

## 7.8.8. Additional resources

  * [Preparing CDI scratch space](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/storage#virt-preparing-cdi-scratch-space "10.9. Preparing CDI scratch space")
