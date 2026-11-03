# 3.1. Configuring the registry for AWS user-provisioned infrastructure

Save your container images to a durable storage location by configuring the built-in image registry to use dedicated AWS storage. This setup provides persistent scalable storage for your registry, separate from ephemeral cluster storage. 

## 3.1.1. Configuring a secret for the Image Registry Operator

In addition to the `configs.imageregistry.operator.openshift.io` and ConfigMap resources, configuration is provided to the Operator by a separate secret resource located within the `openshift-image-registry` namespace. 

The `image-registry-private-configuration-user` secret provides credentials needed for storage access and management. It overrides the default credentials used by the Operator, if default credentials were found. 

For S3 on AWS storage, the secret is expected to contain two keys: 

  * `REGISTRY_STORAGE_S3_ACCESSKEY`
  * `REGISTRY_STORAGE_S3_SECRETKEY`



**Procedure**

  * Create an OpenShift Container Platform secret that contains the required keys. 

```shell-session
$ oc create secret generic image-registry-private-configuration-user --from-literal=REGISTRY_STORAGE_S3_ACCESSKEY=myaccesskey --from-literal=REGISTRY_STORAGE_S3_SECRETKEY=mysecretkey --namespace openshift-image-registry
```


## 3.1.2. Configuring registry storage for AWS with user-provisioned infrastructure

If the Registry Operator cannot automatically create and configure an Amazon S3 bucket during installation, you must manually configure registry storage for your cluster. 

Warning

To secure your registry images in Amazon Web Services (AWS), [block public access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html) to the S3 bucket. 

**Prerequisites**

  * You have a cluster on AWS with user-provisioned infrastructure. 
  * For Amazon S3 storage, the secret must contain two keys: 

    * `REGISTRY_STORAGE_S3_ACCESSKEY`
    * `REGISTRY_STORAGE_S3_SECRETKEY`




**Procedure**

  1. Set up a [Bucket Lifecycle Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config) to cancel incomplete multipart uploads that are one day old. 
  2. Enter the storage configuration in `configs.imageregistry.operator.openshift.io/cluster`: 

```shell-session
$ oc edit configs.imageregistry.operator.openshift.io/cluster
```


**Example configuration**

```yaml
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  storage:
    s3:
      bucket: <bucket_name>
      region: <region_name>
```


## 3.1.3. Image Registry Operator configuration parameters for AWS S3

The following configuration parameters are available for AWS S3 registry storage. 

The image registry `spec.storage.s3` configuration parameter holds the information to configure the registry to use the AWS S3 service for back-end storage. See the [S3 storage driver documentation](https://docs.docker.com/registry/storage-drivers/s3/) for more information. 

Parameter| Description  
---|---  
`bucket` |  Bucket is the bucket name in which you want to store the registry’s data. It is optional and is generated if not provided.   
`chunkSizeMiB` |  ChunkSizeMiB is the size of the multipart upload chunks of the S3 API. The default is `10` MiB with a minimum of `5` MiB.   
`region` |  Region is the AWS region in which your bucket exists. It is optional and is set based on the installed AWS Region.   
`regionEndpoint` |  RegionEndpoint is the endpoint for S3 compatible storage services. It is optional and defaults based on the Region that is provided.   
`virtualHostedStyle` |  VirtualHostedStyle enables using S3 virtual hosted style bucket paths with a custom RegionEndpoint. It is optional and defaults to false.  Set this parameter to deploy OpenShift Container Platform to hidden regions.   
`encrypt` |  Encrypt specifies whether or not the registry stores the image in encrypted format. It is optional and defaults to false.   
`keyID` |  KeyID is the KMS key ID to use for encryption. It is optional. Encrypt must be true, or this parameter is ignored.   
`cloudFront` |  CloudFront configures Amazon Cloudfront as the storage middleware in a registry. It is optional.   
`trustedCA` |  The namespace for the config map referenced by `trustedCA` is `openshift-config`. The key for the bundle in the config map is `ca-bundle.crt`. It is optional.   
Show more

Note

When the value of the `regionEndpoint` parameter is configured to a URL of a Rados Gateway, an explicit port must not be specified. For example: 

```yaml
regionEndpoint: http://rook-ceph-rgw-ocs-storagecluster-cephobjectstore.openshift-storage.svc.cluster.local
```
