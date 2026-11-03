# 3.5. Volume Attributes Classes

Volume Attributes Classes enable dynamic modification of storage performance, such as IOPS and throughput, on persistent volume claims without re-provisioning or downtime. Administrators define classes representing quality-of-service levels, and users apply them for on-demand performance tuning. 

## 3.5.1. Volume Attributes Classes Limitations

Volume Attributes Classes have the following limitations: 

  * Only supported with AWS Elastic Block Storage (EBS) and Google Cloud Platform (GCP) persistent disk (PD) Container Storage Interface (CSI). 
  * With GCP PD, volume modification using Volume Attributes Classes is only possible for hyperdisk-balanced disk types. 
  * No more than 512 parameters can be defined for a `VolumeAttributesClass`. 
  * The total length of the parameter’s object, including its keys and values, cannot exceed 256 KiB. 
  * If you apply a Volume Attributes Class to a PVC, you can change the applied Volume Attributes Class for that PVC, but you cannot delete it from the PVC. To delete the Volume Attributes Class from the PVC, you must delete the PVC, and then re-create the PVC. 
  * Volume Attributes Class parameters cannot be edited. If you need to change Volume Attributes Class parameters, create a new Volume Attributes Class with the desired parameters, and then apply it to a PVC. 



## 3.5.2. Defining Volume Attributes Classes

When defining Volume Attributes Classes, you must verify supported parameters with your storage provider and explicitly declare all parameters in every Volume Attributes Classes definition. 

If there are multiple Volume Attributes Classes on one driver with different parameters sets, and you change from one Volume Attributes Classes to another, you might expect every non-defined parameter to be set back to the default. However, that does not occur. The non-defined parameters stay the same. 

For example, if you have: 

  * Volume Attributes Class A defines throughput `125` and iops `300`. 
  * Volume Attributes Class B only defines iops to `400`. 



If a persistent volume claim (PVC) changes its Volume Attributes Class from A to B, the resulting volume’s parameters are changed to throughput `125` and iops `400`. 

The metric, `openshift_cluster_storage_vac_mismatch_parameters`, helps identify mismatched parameters that might lead to the persistence issues: 

  * `0`: All Volume Attributes Classes define the same set of parameters. 
  * `1`: Mismatch detected. At least one Volume Attributes Class defines a different set of parameters than the others. 



You can modify a Volume Attributes Class on a PVC at any time. However, if a Volume Attributes Class is changed multiple times in a short time period, the underlying storage provider might enforce a delay of several hours before the most recent change is fully reconciled on the disk. 

The following is an example Volume Attributes Class YAML file for AWS EBS. 

**Example`VolumeAttributesClass` AWS EBS definition**

```yaml
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: silver
driverName: ebs.csi.aws.com
parameters:
  iops: "300"
  throughput: "125"
  type: io2
  ...
```


  * `kind`: Defines object as Volumes Attributes Classes. 
  * `metadata.Name`: Specifies the name of the `VolumeAttributesClass`. In this example, it is `silver`. 
  * `driverName`: Specifies the provisioner that determines what volume plugin is used for provisioning persistent volumes (PVs). In this example, it is `ebs.csi.aws.com` for AWS EBS. 
  * `parameters.type`: Defines the disk type. 



The following is an example Volume Attributes Class YAML file for GPC PD. 

**Example`VolumeAttributesClass` GPC PD definition**

```yaml
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: silver
driverName: pd.csi.storage.gke.io
parameters:
  iops: "3000"
  throughput: "150Mi"
  ...
```


  * `kind`: Defines object as Volumes Attributes Classes. 
  * `metadata.Name`: Specifies the name of the `VolumeAttributesClass`. In this example, it is `silver`. 
  * `driverName`: Specifies the provisioner that determines what volume plugin is used for provisioning persistent volumes (PVs). In this example, it is "pd.csi.storage.gke.io" for GPC PD. 



## 3.5.3. Applying a Volume Attributes Class to a PVC

Apply a Volume Attributes Class to a new or existing persistent volume claim (PVC) by setting the `volumeAttributesClassName` parameter to dynamically configure storage attributes, such as performance tiers without recreating the volume. 

**Procedure**

  * Set the PVC’s `volumeAttributesClassName` parameter to the Volume Attributes Class’s name: 

**Example**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pv-claim
spec:
  …
  volumeAttributesClassName: silver
```


Where `spec.volumeAttributesClassName` specifies using the Volume Attributes Class `silver` for this PVC. 




## 3.5.4. Deleting Volume Attributes Classes

Delete a Volume Attributes Class that is no longer needed by first removing or reassigning all persistent volume claims (PVCs) that reference it, since a Volume Attributes Class cannot be deleted while it is still in use. 

If you try to delete a Volume Attributes Class while it is still being used by a PVC, the command does not complete until all resources that use the Volume Attributes Class are updated to not use it. 

**Procedure**

  1. Search for PVCs that are using Volume Attributes Classes by running the following command: 

```shell-session
$ oc get pvc -A -o jsonpath='{range .items[?(@.spec.volumeAttributesClassName=="<vac-name>")]}{.metadata.name}{"\n"}{end}'
```


Where `<vac-name>` is the Volume Attributes Class name. 

**Example command output**

```shell-session
$ mypvc
```


  2. Complete one of the following steps: 

     * Specify a different Volume Attributes Class name in the PVC’s `volumeAttributesClassName` parameter: 

**Example PVC definition specifying a Volume Attributes Class**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: mypvc
spec:
…
volumeAttributesClassName: silver
```


Where `spec.volumeAttributesClassName` specifies a different Volume Attributes Class. In this example, `silver`. 

     * Delete all PVCs that specify the Volume Attributes Class by running the following command: 

```shell-session
$ oc delete pvc <pvc-name>
```


Where `<pvc-name>` is the name of the PVC that you want to delete. 

  3. Now that the Volume Attributes Class is no longer being used by any PVC, delete the Volume Attributes Class by running the following command: 

```shell-session
$ oc delete vac <vac-name>
```


Where `<pvc-name>` is the name of the Volume Attributes Class that you want to delete.
